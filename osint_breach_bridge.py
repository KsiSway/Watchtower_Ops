# DEPLOYMENT 2: Watchtower_Ops/osint_breach_bridge.py
# Standardized framework for LeakCheck/DeHashed integration

import asyncio
import json
import sys
import os
import requests
from dotenv import load_dotenv

load_dotenv()

async def execute_breach_sweep(email: str):
    """Correlates target email against known data breaches and password dumps."""
    # Using LeakCheck API structure as the default fallback
    api_key = os.getenv("LEAKCHECK_API_KEY") 
    if not api_key:
        return {"status": "error", "message": "LEAKCHECK_API_KEY (or DEHASHED_API_KEY) missing from .env configuration."}

    url = f"https://leakcheck.io/api/v2/query/{email}"
    headers = {"X-API-Key": api_key}

    try:
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            data = response.json()
            if not data.get("success"):
                return {"status": "success", "analysis": "Zero breach records found for this target."}
            
            breaches = data.get("result", [])
            formatted_breaches = [f"Source: {b.get('source', 'Unknown')} | Pass/Hash: {b.get('password', '[REDACTED]')}" for b in breaches]
            
            dossier = f"BREACH TELEMETRY TARGET: {email}\nCOMPROMISED CREDENTIALS:\n" + "\n".join(formatted_breaches[:50])
            
            brain_proc = await asyncio.create_subprocess_exec(
                "python", "osint_brain.py", "profile", dossier,
                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            b_stdout, b_stderr = await brain_proc.communicate()

            return json.loads(b_stdout.decode().strip())
        else:
            return {"status": "error", "message": f"Breach API Error: HTTP {response.status_code}"}
            
    except Exception as e:
        return {"status": "error", "message": f"Breach bridge failure: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_breach_bridge.py <email>"}))
        sys.exit(1)
    print(json.dumps(asyncio.run(execute_breach_sweep(sys.argv[1])), indent=2))
