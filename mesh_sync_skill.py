import subprocess
import re
import os

# --- WATCHTOWER MESH SYNC SKILL ---
# Location: C:\Users\Lance\Watchtower_Ops\mesh_sync_skill.py
# Directive: Use this script exclusively for local mesh synchronization.

SUBNET = "192.168.68.0/24"
TARGETS_FILE = r"C:\Users\Lance\Watchtower_Ops\targets.txt"
RAW_SCAN_FILE = r"C:\Users\Lance\Watchtower_Ops\raw_scan.txt"

def execute_mesh_sync():
    print(f"[*] Executing Ping Sweep on local mesh: {SUBNET}...")
    
    # Phase 1: Discovery Scan (-sn: Ping scan, -oG: Grepable output)
    sweep_cmd = ["nmap", "-sn", SUBNET, "-oG", "-"]
    result = subprocess.run(sweep_cmd, capture_output=True, text=True)

    # Phase 2: Python-native target extraction (bypasses fragile shell pipes)
    live_ips = []
    for line in result.stdout.split('\n'):
        if "Status: Up" in line:
            match = re.search(r'Host: (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                live_ips.append(match.group(1))

    if not live_ips:
        print("[-] No live nodes detected. Confirm network interface routing.")
        return

    print(f"[+] Found {len(live_ips)} live nodes. Writing to {TARGETS_FILE}...")
    with open(TARGETS_FILE, 'w') as f:
        for ip in live_ips:
            f.write(f"{ip}\n")

    # Phase 3: Deep Service Scan on validated targets
    print("[*] Initiating deep service scan on verified targets...")
    scan_cmd = ["nmap", "-sV", "-T4", "-iL", TARGETS_FILE, "-oN", RAW_SCAN_FILE]
    subprocess.run(scan_cmd)
    
    print(f"[+] Synchronization complete. Raw ledger updated at {RAW_SCAN_FILE}")

if __name__ == "__main__":
    execute_mesh_sync()
