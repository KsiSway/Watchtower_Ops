# DEPLOYMENT: Watchtower_Ops/osint_crtsh_bridge.py
# Passive Subdomain Enumeration via crt.sh

import json
import sys
import aiohttp
import asyncio
import os
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_crtsh_data(target: str):
    """Polls crt.sh for subdomain enumeration."""
    url = f"https://crt.sh/?q={target}&output=json"
    max_retries = 3
    async with aiohttp.ClientSession() as session:
        for attempt in range(max_retries):
            try:
                async with session.get(url, timeout=20) as response:
                    if response.status == 200:
                        return await response.json()
                    elif response.status in [429, 502, 503]:
                        wait = 2 ** attempt
                        logging.warning(f"crt.sh error {response.status}. Retrying in {wait}s...")
                        await asyncio.sleep(wait)
                    else:
                        return {"status": "error", "message": f"HTTP {response.status}"}
            except Exception as e:
                logging.error(f"crt.sh connection error: {str(e)}")
                await asyncio.sleep(1)
    return {"status": "error", "message": "Max retries exceeded for crt.sh"}

async def execute_crtsh_sweep(target: str):
    """Executes crt.sh sweep and integrates with Watchtower Brain."""
    data = await fetch_crtsh_data(target)
    
    if isinstance(data, dict) and data.get("status") == "error":
        return data

    # Process results: extract unique names
    subdomains = set()
    if isinstance(data, list):
        for entry in data:
            name_value = entry.get("name_value", "")
            for name in name_value.split("\n"):
                subdomains.add(name.strip().replace("*.", ""))
    
    intel_list = sorted(list(subdomains))
    dossier = f"CRT.SH SUBDOMAINS FOR {target}:\n" + "\n".join(intel_list[:20])
    if len(intel_list) > 20:
        dossier += f"\n... and {len(intel_list) - 20} more."

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
                "target": target,
                "subdomains": intel_list,
                "analysis": json.loads(b_stdout.decode().strip())
            }
        else:
             return {"status": "success", "target": target, "subdomains": intel_list, "analysis": "Brain pipeline unavailable."}
    except Exception as e:
        return {"status": "success", "target": target, "subdomains": intel_list, "analysis": f"Integration error: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_crtsh_bridge.py '<target_domain>'" }))
        sys.exit(1)
        
    print(json.dumps(asyncio.run(execute_crtsh_sweep(sys.argv[1])), indent=2))
