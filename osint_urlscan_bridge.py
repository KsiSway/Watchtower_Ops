# DEPLOYMENT: Watchtower_Ops/osint_urlscan_bridge.py
# Searches URLScan index for passive DOM and network request data.

import json
import sys
import aiohttp
import asyncio
import os
import logging
from dotenv import load_dotenv

# Initialize Exocortex Environment
load_dotenv()
URLSCAN_KEY = os.getenv("URLSCAN_API_KEY")

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_urlscan_data(target: str):
    """Query URLScan Index for target domain."""
    url = "https://urlscan.io/api/v1/search/"
    params = {'q': f"domain:{target}"}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    if URLSCAN_KEY:
        headers['API-Key'] = URLSCAN_KEY

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers, params=params, timeout=20) as response:
                if response.status == 200:
                    data = await response.json()
                    if data and data.get('results'):
                        results = []
                        for res in data['results'][:10]:
                            page = res.get('page', {})
                            results.append({
                                "url": page.get('url'),
                                "ip": page.get('ip'),
                                "server": page.get('server'),
                                "scan_id": res.get('_id')
                            })
                        return {"status": "success", "records": results}
                    return {"status": "success", "records": []}
                else:
                    return {"status": "error", "message": f"HTTP {response.status}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

async def execute_urlscan_sweep(target: str):
    """Executes URLScan sweep and integrates with Watchtower Brain."""
    data = await fetch_urlscan_data(target)
    
    if data.get("status") == "error":
        return data

    dossier = f"URLSCAN HISTORICAL RECORDS FOR {target}:\n{json.dumps(data['records'], indent=2)}"

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

        result = {
            "status": "success",
            "records": data['records'],
            "analysis": json.loads(b_stdout.decode().strip()) if brain_proc.returncode == 0 else "Brain pipeline unavailable."
        }
        return result
    except Exception as e:
        return {"status": "success", "records": data['records'], "analysis": f"Integration error: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_urlscan_bridge.py '<target_domain>'" }))
        sys.exit(1)
        
    print(json.dumps(asyncio.run(execute_urlscan_sweep(sys.argv[1])), indent=2))
