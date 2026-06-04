# DEPLOYMENT 1: Watchtower_Ops/osint_maigret_bridge.py
# Dependency: pip install maigret

import asyncio
import json
import sys
import os
import logging

logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

async def execute_maigret_sweep(target_alias: str):
    """Deep biographical extraction and profiling via Maigret."""
    try:
        # Maigret is heavy; timeout set to 15s per request.
        # Ensure we run from the script directory for brain resolution
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        try:
            proc = await asyncio.create_subprocess_exec(
                "maigret", target_alias, "--timeout", "15", "-a", 
                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=30)
        except asyncio.TimeoutError:
            proc.kill()
            return {"status": "error", "message": "Maigret process timeout (30s limit exceeded)"}
        
        if proc.returncode != 0 and not stdout:
            return {"status": "error", "message": f"Maigret execution failed: {stderr.decode().strip()}"}

        # Parse and validate Maigret output before truncation
        try:
            maigret_output = stdout.decode()
            # Truncate for context window while preserving line integrity
            dossier = f"MAIGRET DEEP SCAN: {target_alias}\nRAW DATA:\n{maigret_output[:3000]}"
        except Exception as e:
            logger.error(f"Failed to process Maigret output: {e}")
            dossier = f"MAIGRET DEEP SCAN: {target_alias}\nRAW DATA: [Output processing error]"
        
        try:
            brain_proc = await asyncio.create_subprocess_exec(
                "python", os.path.join(script_dir, "osint_brain.py"), "profile", dossier,
                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            b_stdout, b_stderr = await asyncio.wait_for(brain_proc.communicate(), timeout=60)
        except asyncio.TimeoutError:
            brain_proc.kill()
            return {"status": "error", "message": "Brain process timeout (60s limit exceeded)"}

        if brain_proc.returncode != 0:
            return {"status": "error", "message": f"Brain pipeline failed: {b_stderr.decode().strip()}"}

        try:
            result = json.loads(b_stdout.decode().strip())
            return result
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse brain output as JSON: {e}")
            return {"status": "error", "message": f"Invalid JSON from brain process: {str(e)}"}

    except Exception as e:
        logger.error(f"Unexpected error in execute_maigret_sweep: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python3 osint_maigret_bridge.py <target_alias>"}))
        sys.exit(1)
    print(json.dumps(asyncio.run(execute_maigret_sweep(sys.argv[1])), indent=2))
