# DEPLOYMENT 1: Watchtower_Ops/osint_maigret_bridge.py
# Dependency: pip install maigret

import asyncio
import json
import sys
import os

async def execute_maigret_sweep(target_alias: str):
    """Deep biographical extraction and profiling via Maigret."""
    try:
        # Maigret is heavy; timeout set to 15s per request.
        proc = await asyncio.create_subprocess_exec(
            "maigret", target_alias, "--timeout", "15", "-a", 
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        
        if proc.returncode != 0 and not stdout:
            return {"status": "error", "message": f"Maigret execution failed: {stderr.decode().strip()}"}

        # Pipe raw Maigret output directly to the Cognitive Brain
        dossier = f"MAIGRET DEEP SCAN: {target_alias}\nRAW DATA:\n{stdout.decode()[:3000]}" # Truncated for context window
        
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
        print(json.dumps({"error": "Usage: python3 osint_maigret_bridge.py <target_alias>"}))
        sys.exit(1)
    print(json.dumps(asyncio.run(execute_maigret_sweep(sys.argv[1])), indent=2))
