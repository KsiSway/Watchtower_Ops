#!/usr/bin/env python3
import sys
import json
import subprocess
import time

def deploy_tripwire(adb_id):
    """Deploys a zero-footprint ARP sniffer using tcpdump if available on rooted node."""
    try:
        # Check for tcpdump presence (common in rooted/Magisk environments)
        check_tcpdump = subprocess.run(
            ["adb", "-s", adb_id, "shell", "which tcpdump"],
            capture_output=True, text=True
        )
        
        if "/system/bin/tcpdump" not in check_tcpdump.stdout and "tcpdump" not in check_tcpdump.stdout:
            return {"status": "error", "message": "tcpdump binary not found on target. Ensure root/Magisk installation."}

        # Sniff wlan0 for 5 seconds for ARP broadcasts (0x0806)
        # Using -c 10 to capture up to 10 packets or timeout
        sniff_cmd = "su -c 'tcpdump -i wlan0 -c 10 -n arp'"
        
        # Run the capture
        capture = subprocess.run(
            ["adb", "-s", adb_id, "shell", sniff_cmd],
            capture_output=True, text=True, timeout=10
        )
        
        if capture.returncode != 0:
            return {"status": "error", "message": capture.stderr.strip()}

        # Parse the raw output into structured telemetry
        lines = capture.stdout.strip().split('\n')
        telemetry = []
        for line in lines:
            if "ARP" in line:
                telemetry.append({"packet": line.strip()})
        
        return {"status": "success", "telemetry": telemetry}

    except subprocess.TimeoutExpired:
        return {"status": "error", "message": "Capture timed out. No ARP traffic detected."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Usage: python mesh_tripwire.py <adb_id>"}))
        sys.exit(1)
        
    target_id = sys.argv[1]
    result = deploy_tripwire(target_id)
    print(json.dumps(result))
