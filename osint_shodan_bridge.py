# DEPLOYMENT: Watchtower_Ops/osint_shodan_bridge.py
# Dependency: python -m pip install shodan

import json
import sys
import shodan
import asyncio
import os
from dotenv import load_dotenv

# Initialize Exocortex Environment
load_dotenv()
SHODAN_KEY = os.getenv("SHODAN_API_KEY")

async def execute_shodan_sweep(target: str):
    """Interrogates Shodan for a target IP or domain."""
    try:
        api = shodan.Shodan(SHODAN_KEY)
        
        # Determine if target is IP or query
        if any(char.isdigit() for char in target) and target.count('.') >= 2:
            # Assume IP scan
            host = api.host(target)
            intel = {
                "ip": host.get("ip_str"),
                "hostnames": host.get("hostnames", []),
                "ports": host.get("ports", []),
                "os": host.get("os", "Unknown"),
                "org": host.get("org", "Unknown"),
                "isp": host.get("isp", "Unknown"),
                "country": host.get("country_name", "Unknown"),
                "city": host.get("city", "Unknown")
            }
            dossier = f"SHODAN TARGET: {target}\nPORTS: {intel['ports']}\nOS: {intel['os']}\nORG: {intel['org']}\nLOCATION: {intel['city']}, {intel['country']}"
        else:
            # Assume general query
            results = api.search(target)
            intel = {
                "total": results.get("total", 0),
                "matches": [{"ip": r.get("ip_str"), "port": r.get("port"), "org": r.get("org")} for r in results.get("matches", [])[:5]]
            }
            dossier = f"SHODAN SEARCH: {target}\nTOTAL_RESULTS: {intel['total']}\nTOP_MATCHES: {intel['matches']}"

        # Resolve brain script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        brain_path = os.path.join(script_dir, "osint_brain.py")

        # Send to brain for tactical context
        brain_proc = await asyncio.create_subprocess_exec(
            "python", brain_path, "telemetry", dossier,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        b_stdout, b_stderr = await brain_proc.communicate()

        if brain_proc.returncode == 0:
            return json.loads(b_stdout.decode().strip())
        else:
             return {"status": "success", "analysis": f"Shodan Data: {dossier}. Brain pipeline unavailable."}

    except shodan.APIError as e:
        return {"status": "error", "message": f"Shodan API Error: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"Shodan sweep failed: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_shodan_bridge.py '<target_ip_or_query>'" }))
        sys.exit(1)
        
    print(json.dumps(asyncio.run(execute_shodan_sweep(sys.argv[1])), indent=2))
