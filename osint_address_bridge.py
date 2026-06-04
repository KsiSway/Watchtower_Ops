# DEPLOYMENT: Watchtower_Ops/osint_address_bridge.py
# Dependency: pip install aiohttp

import asyncio
import json
import sys
import aiohttp
import urllib.parse
import os

async def execute_address_sweep(address: str):
    """Geocodes a physical address using OpenStreetMap Nominatim."""
    encoded_address = urllib.parse.quote(address)
    url = f"https://nominatim.openstreetmap.org/search?q={encoded_address}&format=json&addressdetails=1"
    headers = {"User-Agent": "WatchtowerC2/1.0"}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as response:
                if response.status == 200:
                    data = await response.json()
                    if data:
                        # Grab the best match
                        best_match = data[0]
                        lat = best_match.get("lat")
                        lon = best_match.get("lon")
                        formatted_address = best_match.get("display_name")
                        
                        dossier = f"ADDRESS SEARCH: {address}\nMATCH: {formatted_address}\nCOORDINATES: {lat}, {lon}"
                        
                        # Resolve brain script location
                        script_dir = os.path.dirname(os.path.abspath(__file__))
                        brain_path = os.path.join(script_dir, "osint_brain.py")

                        # Send to brain for context
                        brain_proc = await asyncio.create_subprocess_exec(
                            "python", brain_path, "telemetry", dossier,
                            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                        )
                        b_stdout, b_stderr = await brain_proc.communicate()
                        
                        if brain_proc.returncode == 0:
                            return json.loads(b_stdout.decode().strip())
                        else:
                             return {"status": "success", "analysis": f"Address resolved to: {formatted_address} (Lat: {lat}, Lon: {lon}). Brain pipeline unavailable."}

                    else:
                        return {"status": "success", "analysis": "Zero results found for this address."}
                else:
                    return {"status": "error", "message": f"Nominatim API Error: {response.status}"}
    except Exception as e:
        return {"status": "error", "message": f"Address lookup failed: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_address_bridge.py '<address>'"}))
        sys.exit(1)
    print(json.dumps(asyncio.run(execute_address_sweep(sys.argv[1])), indent=2))
