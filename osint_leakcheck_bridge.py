# DEPLOYMENT: Watchtower_Ops/osint_leakcheck_bridge.py
# Interrogates LeakCheck.io for breach intelligence.

import json
import sys
import aiohttp
import asyncio
import os
import logging
from dotenv import load_dotenv

# Initialize Exocortex Environment
load_dotenv()
LEAKCHECK_KEY = os.getenv("LEAKCHECK_API_KEY")

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_leakcheck_data(query: str, search_type: str = "auto"):
    """Polls LeakCheck.io API for breach data."""
    if not LEAKCHECK_KEY:
        return {"status": "error", "message": "LEAKCHECK_API_KEY missing from environment."}

    # API v2 endpoint
    url = f"https://leakcheck.io/api/v2/query/{query}"
    params = {
        "key": LEAKCHECK_KEY,
        "type": search_type
    }
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, params=params, timeout=20) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {"status": "error", "message": f"HTTP {response.status}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

async def execute_leakcheck_sweep(target: str):
    """Executes LeakCheck sweep and integrates with Watchtower Brain."""
    # Attempt to auto-detect type or default to email/domain
    data = await fetch_leakcheck_data(target)
    
    if data.get("success") is False or data.get("status") == "error":
        return {"status": "error", "message": data.get("message", "LeakCheck query failed.")}

    # Summarize results for brain
    found = data.get("found", 0)
    result_list = data.get("result", [])
    
    # Grab a sample of sources
    sources = list(set([r.get("source", "Unknown") for r in result_list]))
    
    dossier = f"LEAKCHECK BREACH RESULTS FOR {target}:\nTOTAL FOUND: {found}\nSOURCES: {sources[:10]}"

    # Resolve brain script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    brain_path = os.path.join(script_dir, "osint_brain.py")

    # Send to brain for tactical context
    try:
        brain_proc = await asyncio.create_subprocess_exec(
            "python", brain_path, "telemetry", dossier,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        b_stdout, b_stderr = await brain_proc.communicate()

        return {
            "status": "success",
            "breach_count": found,
            "sources": sources,
            "analysis": json.loads(b_stdout.decode().strip()) if brain_proc.returncode == 0 else "Brain pipeline unavailable."
        }
    except Exception as e:
        return {"status": "success", "breach_count": found, "analysis": f"Integration error: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_leakcheck_bridge.py '<email_or_domain>'" }))
        sys.exit(1)
        
    print(json.dumps(asyncio.run(execute_leakcheck_sweep(sys.argv[1])), indent=2))
