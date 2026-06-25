import os
import re
import csv

WATCHTOWER_DIR = r"D:\Watchtower_Ops"
NMAP_FILE = os.path.join(WATCHTOWER_DIR, "live_nodes.txt")
LEDGER_FILE = os.path.join(WATCHTOWER_DIR, "Watchtower_Final_Baseline.csv")

def ingest_scan():
    if not os.path.exists(NMAP_FILE):
        print("[-] FAULT: live_nodes.txt not found. Nmap sweep phase failed.")
        return

    live_hosts = []
    with open(NMAP_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if "Status: Up" in line:
                match = re.search(r'Host: (\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    # Enforce strict 5-column Watchtower schema
                    live_hosts.append([match.group(1), "UNKNOWN", "UNKNOWN", "UNKNOWN", "Clear"])

    print(f"[*] Found {len(live_hosts)} active nodes. Writing 5-column ledger...")
    with open(LEDGER_FILE, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP", "Hostname", "MAC", "Vendor", "Status"])
        writer.writerows(live_hosts)

if __name__ == "__main__":
    ingest_scan()
