# DEPLOYMENT: Watchtower_Ops/osint_brave_bridge.py
# Interrogates Brave Search API for web intelligence.

import json
import sys
import aiohttp
import asyncio
import os
import logging
from dotenv import load_dotenv

# Initialize Exocortex Environment
load_dotenv()
BRAVE_KEY = os.getenv("BRAVE_SEARCH_API_KEY")

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_brave_data(query: str):
    """Polls Brave Search API for web results."""
    if not BRAVE_KEY:
        return {"status": "error", "message": "BRAVE_SEARCH_API_KEY missing from environment."}

    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": BRAVE_KEY
    }
    params = {"q": query}
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers, params=params, timeout=20) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {"status": "error", "message": f"HTTP {response.status}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

async def execute_brave_sweep(target: str):
    """Executes Brave Search sweep and integrates with Watchtower Brain."""
    data = await fetch_brave_data(target)
    
    if data.get("status") == "error":
        return data

    # Summarize web results
    web_results = data.get("web", {}).get("results", [])
    summary = [{"title": r.get("title"), "url": r.get("url"), "description": r.get("description")} for r in web_results[:5]]
    
    dossier = f"BRAVE SEARCH RESULTS FOR {target}:\n{json.dumps(summary, indent=2)}"

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
            "results_count": len(web_results),
            "top_hits": summary,
            "analysis": json.loads(b_stdout.decode().strip()) if brain_proc.returncode == 0 else "Brain pipeline unavailable."
        }
    except Exception as e:
        return {"status": "success", "results_count": len(web_results), "analysis": f"Integration error: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_brave_bridge.py '<query>'" }))
        sys.exit(1)
        
    print(json.dumps(asyncio.run(execute_brave_sweep(sys.argv[1])), indent=2))
