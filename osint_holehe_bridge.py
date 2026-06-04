# DEPLOYMENT 2: Watchtower_Ops/osint_holehe_bridge.py
# Dependency: pip install holehe

import asyncio
import json
import sys
import os

async def execute_holehe_sweep(target_email: str):
    """Email registration verification via forgotten password endpoints."""
    try:
        proc = await asyncio.create_subprocess_exec(
            "holehe", target_email, "--only-used",
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        
        raw_output = stdout.decode()
        # Filter for verified hits (Holehe uses [+] for positive hits)
        verified_services = [line.strip().replace('[+]', '').strip() for line in raw_output.split('\n') if "[+]" in line]
        
        if not verified_services:
            return {"status": "success", "analysis": "Zero linked services detected for this email address."}

        dossier = f"TARGET EMAIL: {target_email}\nVERIFIED REGISTERED PLATFORMS:\n" + "\n".join(verified_services)
        
        # Resolve brain script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        brain_path = os.path.join(script_dir, "osint_brain.py")
        if not os.path.exists(brain_path):
            # Try fallback to skill scripts directory
            brain_path = os.path.join(script_dir, "cognitive-analyst", "scripts", "osint_brain.py")

        brain_proc = await asyncio.create_subprocess_exec(
            "python", brain_path, "profile", dossier,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        b_stdout, b_stderr = await brain_proc.communicate()

        if brain_proc.returncode != 0:
            return {"status": "error", "message": f"Brain pipeline failed: {b_stderr.decode().strip()}"}

        return json.loads(b_stdout.decode().strip())

    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python3 osint_holehe_bridge.py <target_email>"}))
        sys.exit(1)
    print(json.dumps(asyncio.run(execute_holehe_sweep(sys.argv[1])), indent=2))
