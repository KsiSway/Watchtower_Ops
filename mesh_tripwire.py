# DEPLOYMENT: Watchtower_Ops/mesh_tripwire.py
# Passive Mesh Defense / ARP Tripwire (v1.0 - Tactical)

import sys
import json
import subprocess
import os

ADB_PATH = r"C:\adb\platform-tools\adb.exe"

def run_tripwire(device_id):
    """Executes a passive ARP sniff on the target node via su-wrapped tcpdump."""
    
    # Tactical Command: Capture 10 ARP packets on wlan0 interface
    # -i wlan0: interface
    # -c 10: count
    # -n: no DNS resolution
    # arp: filter
    sniff_cmd = [ADB_PATH, "-s", device_id, "shell", "su -c 'tcpdump -i wlan0 -c 10 -n arp'"]
    
    try:
        process = subprocess.Popen(sniff_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(timeout=30)
        
        if process.returncode == 0:
            lines = stdout.strip().split('\n')
            telemetry = []
            for line in lines:
                if "ARP" in line:
                    telemetry.append({"packet": line.strip()})
            
            # Fallback: If tcpdump produced no ARP packets, check the static ARP table
            if not telemetry:
                arp_table_cmd = [ADB_PATH, "-s", device_id, "shell", "su -c 'cat /proc/net/arp'"]
                arp_res = subprocess.run(arp_table_cmd, capture_output=True, text=True)
                if arp_res.returncode == 0:
                    arp_lines = arp_res.stdout.strip().split('\n')[1:] # Skip header
                    for line in arp_lines:
                        telemetry.append({"packet": f"STATIC CACHE: {line.strip()}"})

            return {
                "status": "success",
                "telemetry": telemetry
            }
        else:
            return {"status": "error", "message": f"Sniff Failure: {stderr.strip()}"}
            
    except subprocess.TimeoutExpired:
        return {"status": "error", "message": "Sniffing timed out. Interface may be dormant."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "message": "Usage: python mesh_tripwire.py <device_id>"}))
        sys.exit(1)
    
    target_id = sys.argv[1]
    # Set working directory to file location
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(json.dumps(run_tripwire(target_id)))
