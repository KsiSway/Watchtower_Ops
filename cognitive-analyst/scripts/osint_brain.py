#!/usr/bin/env python3
# Minimum Requirement: Python 3.11+
# Dependencies: pip install aiohttp
# Prerequisite: Local LLM running an OpenAI-compatible API (e.g., Ollama at localhost:11434)

import asyncio
import aiohttp
import json
import sys
import logging

logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Configuration for local, offline LLM
# Adjust the URL and Model Name based on your specific deployment (e.g., llama3, mistral, dolphin)
LLM_API_URL = "http://127.0.0.1:11434/api/generate" 
MODEL_NAME = "dolphin-llama3:latest" # Known for uncensored operational capability

async def query_local_brain(system_prompt: str, raw_data: str) -> dict:
    """Sends unstructured OSINT data to the local LLM for tactical analysis."""
    
    # Construct the operational prompt
    full_prompt = f"""[SYSTEM DIRECTIVE]: {system_prompt}
    
[RAW INTELLIGENCE DATA]:
{raw_data}

[OUTPUT FORMAT]: Provide a concise, tactical summary. Do not include conversational filler."""

    payload = {
        "model": MODEL_NAME,
        "prompt": full_prompt,
        "stream": False,
        "options": {
            "temperature": 0.2 # Low temperature for factual, analytical output
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
    except asyncio.TimeoutError:
        return {"status": "error", "message": "Local LLM connection timeout (300s limit exceeded)"}
    except aiohttp.ClientError as e:
        logger.error(f"HTTP client error: {e}")
        return {"status": "error", "message": f"Local LLM connection failed: {str(e)}"}
    except Exception as e:
        logger.error(f"Unexpected error in query_local_brain: {e}")
        return {"status": "error", "message": f"Local LLM connection failed: {str(e)}"}

async def main(task_type: str, data_payload: str):
    """Execution orchestrator for different cognitive tasks."""
    
    prompts = {
        "profile": "Analyze the provided digital dossier (usernames, platforms). Deduce the target's technical background, primary language, and operational habits.",
        "darkweb": "Analyze the provided dark web HTML snippet. Identify the primary illicit service or product being offered and any OPSEC failures by the host.",
        "telemetry": "Analyze the provided network ARP logs. Identify any anomalous device behavior, potential spoofing, or unauthorized hardware."
    }
    
    sys_prompt = prompts.get(task_type)
    if not sys_prompt:
        error_output = {"error": f"Unknown task type. Valid options: {list(prompts.keys())}"}
        print(json.dumps(error_output))
        sys.exit(1)
        
    result = await query_local_brain(sys_prompt, data_payload)
    
    # Validate result before JSON serialization
    if not isinstance(result, dict):
        result = {"error": "Invalid result type from query_local_brain"}
    
    try:
        print(json.dumps(result, indent=2))
    except (TypeError, ValueError) as e:
        logger.error(f"JSON serialization error: {e}")
        print(json.dumps({"error": f"Failed to serialize result: {str(e)}"}))

if __name__ == "__main__":
    if len(sys.argv) != 3:
         error_output = {"error": "Usage: python3 osint_brain.py <task_type> <raw_data_string>"}
         print(json.dumps(error_output))
         sys.exit(1)
         
    task = sys.argv[1]
    data = sys.argv[2]
    asyncio.run(main(task, data))
