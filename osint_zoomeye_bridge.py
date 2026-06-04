# DEPLOYMENT: Watchtower_Ops/osint_zoomeye_bridge.py
# Interrogates ZoomEye v2 for target intelligence.

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
ZOOMEYE_KEY = os.getenv("ZOOMEYE_API_KEY")

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_zoomeye_v2_data(target: str):
    """Polls ZoomEye v2 API for asset search."""
    if not ZOOMEYE_KEY:
        return {"status": "error", "message": "ZOOMEYE_API_KEY missing from environment."}

    url = "https://api.zoomeye.ai/v2/search"
    headers = {"API-KEY": ZOOMEYE_KEY}
    
    # Encode target in base64 as required by v2 API
    qbase64 = base64.b64encode(target.encode('utf-8')).decode('utf-8')
    payload = {
        "qbase64": qbase64, 
        "fields": "ip,port,domain,os,ssl.jarm,ssl.ja3s"
    }
    
    async with aiohttp.ClientSession() as session:
        try:
            # ZoomEye v2 uses POST for searches with qbase64
            async with session.post(url, headers=headers, json=payload, timeout=20) as response:
                if response.status == 200:
                    return await response.json()
                elif response.status == 429:
                    return {"status": "error", "message": "Rate limited by ZoomEye v2."}
                else:
                    return {"status": "error", "message": f"HTTP {response.status}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

async def execute_zoomeye_sweep(target: str):
    """Executes ZoomEye v2 sweep and integrates with Watchtower Brain."""
    data = await fetch_zoomeye_v2_data(target)
    
    if isinstance(data, dict) and data.get("status") == "error":
        return data

    # Summarize results for brain
    total = data.get("total", 0)
    list_data = data.get("list", []) # v2 returns results in 'list'
    summary_matches = []
    for m in list_data[:5]:
        summary_matches.append({
            "ip": m.get("ip"),
            "port": m.get("port"),
            "os": m.get("os"),
            "jarm": m.get("ssl", {}).get("jarm")
        })
    
    dossier = f"ZOOMEYE V2 RESULTS FOR {target}:\nTOTAL: {total}\nTOP MATCHES: {summary_matches}"

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

        if brain_proc.returncode == 0:
            return {
                "status": "success",
                "raw_data": summary_matches,
                "analysis": json.loads(b_stdout.decode().strip())
            }
        else:
             return {"status": "success", "raw_data": summary_matches, "analysis": "Brain pipeline unavailable."}
    except Exception as e:
        return {"status": "success", "raw_data": summary_matches, "analysis": f"Integration error: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_zoomeye_bridge.py '<query>'" }))
        sys.exit(1)
        
    print(json.dumps(asyncio.run(execute_zoomeye_sweep(sys.argv[1])), indent=2))
