#!/usr/bin/env python3
# Minimum Requirement: Python 3.11+
# Dependencies: pip install aiohttp
# Prerequisite: Local LLM running an OpenAI-compatible API (e.g., Ollama at localhost:11434)

import asyncio
import aiohttp
import json
import sys
import logging
import os
from recon_parser import ReconParser

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

# Configuration for local, offline LLM
# Inside Docker container: use service name 'ollama' on Docker network
# Outside Docker: use 127.0.0.1:11434
# Auto-detect based on DOCKER_ENV environment variable
if os.environ.get("DOCKER_ENV") == "true":
    LLM_API_URL = "http://ollama:11434/api/generate"
else:
    LLM_API_URL = "http://127.0.0.1:11434/api/generate"

MODEL_NAME = "dolphin-llama3:latest"

async def query_local_brain(system_prompt: str, raw_data: str) -> dict:
    """Sends unstructured OSINT data to the local LLM for tactical analysis."""
    
    # Pre-process with ReconParser to identify high-value indicators
    parser = ReconParser()
    extracted = parser.extract_indicators(raw_data)
    
    # Construct the operational prompt with extracted indicators
    full_prompt = f"""[SYSTEM DIRECTIVE]: {system_prompt}
    
[EXTRACTED INDICATORS]:
{json.dumps(extracted, indent=2)}

[RAW INTELLIGENCE DATA]:
{raw_data}

[OUTPUT FORMAT]: Provide a concise, tactical summary. Focus on the correlation between extracted indicators and the raw data. Do not include conversational filler."""

    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,  # Low temperature for factual, analytical output
            "num_predict": 500   # Limit output length for tactical brevity
        }
    }
    
    try:
        timeout = aiohttp.ClientTimeout(total=300)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(LLM_API_URL, json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    return {"status": "success", "analysis": result.get("response", "").strip()}
                else:
                    return {"status": "error", "message": f"LLM API Error: HTTP {response.status}"}
    except Exception as e:
        return {"status": "error", "message": f"Local LLM connection failed: {str(e)}. Attempting endpoint: {LLM_API_URL}"}

async def main(task_type: str, data_payload: str):
    """Execution orchestrator for different cognitive tasks."""
    
    prompts = {
        "profile": "Analyze the provided digital dossier (usernames, platforms). Deduce the target's technical background, primary language, and operational habits.",
        "darkweb": "Analyze the provided dark web HTML snippet. Identify the primary illicit service or product being offered and any OPSEC failures by the host.",
        "telemetry": "Analyze the provided network ARP logs. Identify any anomalous device behavior, potential spoofing, or unauthorized hardware."
    }
    
    sys_prompt = prompts.get(task_type)
    if not sys_prompt:
        print(json.dumps({"error": f"Unknown task type. Valid options: {list(prompts.keys())}"}))
        sys.exit(1)
        
    result = await query_local_brain(sys_prompt, data_payload)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(json.dumps({"error": "Usage: python3 osint_brain.py <task_type> <raw_data_string>"}))
        sys.exit(1)
         
    task = sys.argv[1]
    data = sys.argv[2]
    asyncio.run(main(task, data))
