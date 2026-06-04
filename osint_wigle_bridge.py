# DEPLOYMENT: Watchtower_Ops/osint_wigle_bridge.py
# Interrogates WiGLE.net for geospatial RF intelligence.

import json
import sys
import aiohttp
import asyncio
import os
import logging
import base64
from dotenv import load_dotenv

# Initialize Exocortex Environment
load_dotenv()
WIGLE_NAME = os.getenv("WIGLE_API_NAME")
WIGLE_TOKEN = os.getenv("WIGLE_API_TOKEN")

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_wigle_data(ssid: str = None, bssid: str = None):
    """Polls WiGLE.net API for network search."""
    if not WIGLE_NAME or not WIGLE_TOKEN:
        return {"status": "error", "message": "WiGLE credentials missing from environment."}

    url = "https://api.wigle.net/api/v2/network/search"
    auth_str = f"{WIGLE_NAME}:{WIGLE_TOKEN}"
    encoded_auth = base64.b64encode(auth_str.encode()).decode()
    headers = {"Authorization": f"Basic {encoded_auth}"}
    
    params = {}
    if ssid: params['ssid'] = ssid
    if bssid: params['netid'] = bssid
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers, params=params, timeout=20) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    return {"status": "error", "message": f"HTTP {response.status}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

async def execute_wigle_sweep(target: str):
    """Executes WiGLE sweep (assuming target is SSID or BSSID) and integrates with Watchtower Brain."""
    # Simple heuristic: if it looks like a MAC, use bssid
    is_bssid = ":" in target or "-" in target
    data = await fetch_wigle_data(ssid=None if is_bssid else target, bssid=target if is_bssid else None)
    
    if data.get("status") == "error":
        return data

    # Summarize results
    results = data.get("results", [])
    summary = []
    for r in results[:5]:
        summary.append({
            "ssid": r.get("ssid"),
            "bssid": r.get("netid"),
            "lat": r.get("trilat"),
            "lon": r.get("trilon"),
            "vendor": r.get("housenumber") # Housenumber field often repurposed in some contexts or check other fields
        })
    
    dossier = f"WIGLE GEOSPATIAL RESULTS FOR {target}:\nFOUND: {len(results)}\nTOP MATCHES: {summary}"

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
            "networks_found": len(results),
            "raw_summary": summary,
            "analysis": json.loads(b_stdout.decode().strip()) if brain_proc.returncode == 0 else "Brain pipeline unavailable."
        }
    except Exception as e:
        return {"status": "success", "networks_found": len(results), "analysis": f"Integration error: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_wigle_bridge.py '<SSID_or_BSSID>'" }))
        sys.exit(1)
        
    print(json.dumps(asyncio.run(execute_wigle_sweep(sys.argv[1])), indent=2))
