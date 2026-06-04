import subprocess
import json
import sys
import argparse
import os

TERMUX_BASH = "/data/data/com.termux/files/usr/bin/bash"

def execute_termux_command(device_id, command, background=False):
    """Executes a command inside the Termux environment on a mobile node."""
    # Pattern: adb -s <serial> shell "/data/data/com.termux/files/usr/bin/bash -c '<cmd>'"
    # If background is True, we might use 'nohup' and '&' inside the shell
    
    inner_cmd = command
    if background:
        inner_cmd = f"nohup {command} > /data/data/com.termux/files/home/c2_output.log 2>&1 &"
        
    adb_cmd = ["adb", "-s", device_id, "shell", f"{TERMUX_BASH} -c \"{inner_cmd}\""]
    
    print(f"[*] Dispatching to Termux on {device_id}: {command}")
    
    try:
        process = subprocess.Popen(adb_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            return {"status": "SUCCESS", "details": stdout.strip() or "Command dispatched successfully."}
        else:
            return {"status": "FAILURE", "details": stderr.strip()}
    except Exception as e:
        return {"status": "FAILURE", "details": str(e)}

def upload_and_run_script(device_id, local_script_path, remote_name):
    """Uploads a local bash script to Termux and executes it."""
    remote_path = f"/data/data/com.termux/files/home/{remote_name}"
    
    # 1. Push to a temporary location (usually /data/local/tmp)
    # 2. Move to Termux home (requires Termux app to be accessible or adb to have permissions)
    # 3. Chmod and execute
    
    push_cmd = ["adb", "-s", device_id, "push", local_script_path, "/data/local/tmp/temp_script.sh"]
    move_cmd = ["adb", "-s", device_id, "shell", f"cp /data/local/tmp/temp_script.sh {remote_path} && chmod +x {remote_path}"]
    run_cmd = ["adb", "-s", device_id, "shell", f"{TERMUX_BASH} {remote_path}"]
    
    try:
        subprocess.run(push_cmd, check=True, capture_output=True)
        subprocess.run(move_cmd, check=True, capture_output=True, shell=True) # shell=True for &&
        process = subprocess.run(run_cmd, capture_output=True, text=True)
        
        if process.returncode == 0:
            return {"status": "SUCCESS", "details": process.stdout.strip()}
        else:
            return {"status": "FAILURE", "details": process.stderr.strip()}
    except Exception as e:
        return {"status": "FAILURE", "details": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Watchtower Termux C2 Wrapper")
    parser.add_argument("--device", required=True, help="ADB Device Serial/ID")
    parser.add_argument("--cmd", help="Bash command to execute")
    parser.add_argument("--script", help="Path to local script to upload and run")
    parser.add_argument("--bg", action="store_true", help="Run in background")
    
    args = parser.parse_args()
    
    if args.script:
        result = upload_and_run_script(args.device, args.script, os.path.basename(args.script))
    elif args.cmd:
        result = execute_termux_command(args.device, args.cmd, args.bg)
    else:
        result = {"status": "FAILURE", "details": "Either --cmd or --script required."}
        
    print(json.dumps(result))
