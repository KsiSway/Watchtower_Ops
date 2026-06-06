# DEPLOYMENT: Watchtower_Ops/osint_passive_orchestrator.py
# Unified Orchestrator for Passive Reconnaissance with Local Fallback

import json
import sys
import asyncio
import os
import logging
import subprocess
from recon_datastore import ReconDatastore

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def run_bridge(script_name: str, target: str):
    """Executes a bridge script and returns its output."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(script_dir, script_name)
    
    if not os.path.exists(script_path):
        return {"status": "error", "message": f"Bridge {script_name} not found."}

    try:
        proc = await asyncio.create_subprocess_exec(
            "python", script_path, target,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()

        if proc.returncode == 0:
            return json.loads(stdout.decode().strip())
        else:
            return {"status": "error", "message": stderr.decode().strip()}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def execute_local_fallback(target: str):
    """Local nmap fallback for targets within the authorized subnet."""
    if target.startswith("192.168.68."):
        logging.info(f"INITIATING LOCAL FOOTPRINTING for {target}...")
        try:
            result = subprocess.run(["nmap", "-sn", target], capture_output=True, text=True, check=True)
            return {"status": "success", "type": "local_nmap", "output": result.stdout}
        except Exception as e:
            return {"status": "error", "message": f"Local nmap failed: {str(e)}"}
    else:
        return {"status": "skipped", "message": "Target outside authorized local subnet."}

import ipaddress

async def run_passive_recon(target: str):
    """Orchestrates passive recon via multiple bridges with local fallback."""
    logging.info(f"Starting Unified Passive Recon for: {target}")
    db = ReconDatastore()
    
    internal_aliases = ["watchtower_influxdb", "optiplex-local", "host.docker.internal"]
    try:
        ipaddress.ip_address(target)
    except ValueError:
        if target.endswith(".local") or target in internal_aliases:
            logging.warning(f"[!] INTERNAL HOSTNAME DETECTED: {target}. Bypassing external OSINT APIs.")
            return {"status": "skipped", "message": "Target is an internal node. External queries aborted."}

    
    # Run bridges in parallel
    tasks = [
        run_bridge("osint_shodan_bridge.py", target),
        run_bridge("osint_crtsh_bridge.py", target),
        run_bridge("osint_zoomeye_bridge.py", target),
        run_bridge("osint_wayback_bridge.py", target),
        run_bridge("osint_urlscan_bridge.py", target),
        run_bridge("osint_leakcheck_bridge.py", target),
        run_bridge("osint_wigle_bridge.py", target),
        run_bridge("osint_brave_bridge.py", target)
    ]
    
    results = await asyncio.gather(*tasks)
    
    recon_data = {
        "shodan": results[0],
        "crtsh": results[1],
        "zoomeye": results[2],
        "wayback": results[3],
        "urlscan": results[4],
        "leakcheck": results[5],
        "wigle": results[6],
        "brave": results[7]
    }
    
    # Log bridge results to datastore
    db.log_sweep(target, "shodan", results[0])
    db.log_sweep(target, "crtsh", results[1])
    db.log_sweep(target, "zoomeye", results[2])
    db.log_sweep(target, "wayback", results[3])
    db.log_sweep(target, "urlscan", results[4])
    db.log_sweep(target, "leakcheck", results[5])
    db.log_sweep(target, "wigle", results[6])
    db.log_sweep(target, "brave", results[7])
    
    # Evaluate if external recon failed or was insufficient
    external_failed = all(r.get("status") == "error" for r in results)
    
    if external_failed:
        logging.warning("External APIs failed or returned errors. Checking local fallback...")
        fallback_data = execute_local_fallback(target)
        recon_data["local_fallback"] = fallback_data
        db.log_sweep(target, "local_fallback", fallback_data)
    
    # TRIGGER: Automated Brain Analysis Pipeline
    logging.info("INITIATING ZERO-CLICK BRAIN ANALYSIS...")
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        brain_path = os.path.join(script_dir, "osint_brain.py")
        
        # Compile all successful results into a unified dossier
        unified_dossier = json.dumps(recon_data, indent=2)
        
        brain_proc = await asyncio.create_subprocess_exec(
            "python", brain_path, "telemetry", unified_dossier,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        b_stdout, b_stderr = await brain_proc.communicate()
        
        if brain_proc.returncode == 0:
            recon_data["brain_analysis"] = json.loads(b_stdout.decode().strip())
        else:
            recon_data["brain_analysis"] = {"error": b_stderr.decode().strip()}
            
    except Exception as e:
        logging.error(f"Brain trigger failed: {str(e)}")
        recon_data["brain_analysis"] = {"error": str(e)}

    return recon_data

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_passive_orchestrator.py '<target>'" }))
        sys.exit(1)
        
    target = sys.argv[1]
    final_report = asyncio.run(run_passive_recon(target))
    print(json.dumps(final_report, indent=2))
