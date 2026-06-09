# DEPLOYMENT: Watchtower_Ops/osint_wayback_bridge.py
# Finds hidden, historical, and deleted URLs via Web Archive.

import json
import sys
import aiohttp
import asyncio
import os
import logging
from recon_datastore import ReconDatastore

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_wayback_cdx(target: str):
    """Query Wayback CDX for target domain."""
    url = "http://web.archive.org/cdx/search/cdx"
    params = {
        'url': f"*.{target}/*",
        'output': 'json',
        'collapse': 'urlkey',
        'limit': 500 
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, headers=headers, params=params, timeout=30) as response:
                if response.status == 200:
                    data = await response.json()
                    if data and len(data) > 1:
                        urls = [row[2] for row in data[1:]]
                        return {"status": "success", "count": len(urls), "sample": urls[:20]}
                    return {"status": "success", "count": 0, "sample": []}
                else:
                    return {"status": "error", "message": f"HTTP {response.status}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

async def execute_wayback_sweep(target: str):
    """Executes Wayback sweep and integrates with Watchtower Brain."""
    data = await fetch_wayback_cdx(target)
    
    if data.get("status") == "error":
        return data

    dossier = f"WAYBACK CDX ENDPOINTS FOR {target}:\nFOUND: {data['count']}\nSAMPLES: {data['sample']}"

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
            "endpoints_found": data['count'],
            "sample_urls": data['sample'],
            "analysis": json.loads(b_stdout.decode().strip()) if brain_proc.returncode == 0 else "Brain pipeline unavailable."
        }
        return result
    except Exception as e:
        return {"status": "success", "endpoints_found": data['count'], "analysis": f"Integration error: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_wayback_bridge.py '<target_domain>'" }))
        sys.exit(1)
        
    print(json.dumps(asyncio.run(execute_wayback_sweep(sys.argv[1])), indent=2))
