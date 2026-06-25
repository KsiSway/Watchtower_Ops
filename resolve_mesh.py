import socket
import os

BASELINE = r"D:\Watchtower_Ops\Watchtower_Final_Baseline.csv"

KNOWN_MESH = {
    "192.168.68.1": "Deco_XE75_Gateway",
    "192.168.68.52": "Tab_A8_Mobile_Node",
    "192.168.68.65": "BLU_Burner",
    "192.168.68.104": "Xbox_Series_S",
    "192.168.68.109": "S25_Edge_Commander",
    "192.168.68.110": "OptiPlex_Watchtower_C2",
    "192.168.68.113": "Samsung_SmartMonitor",
    "192.168.68.114": "Samsung_SmartTV"
}

def heal_mesh():
    if not os.path.exists(BASELINE):
        print("[-] FAULT: Ledger missing. Skipping hostname resolution.")
        return

    with open(BASELINE, mode="r", encoding="utf-8") as f:
        lines = f.readlines()

    healed_lines = []
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) >= 5 and parts[0] != "IP":
            ip = parts[0]
            hostname = parts[1]
            
            # 1. Hardware Matrix Override
            if ip in KNOWN_MESH:
                hostname = KNOWN_MESH[ip]
            # 2. mDNS / Socket Fallback
            elif hostname == "UNKNOWN" or not hostname:
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except socket.herror:
                    hostname = "UNKNOWN"
            
            parts[1] = hostname
        
        healed_lines.append(",".join(parts) + "\n")

    with open(BASELINE, mode="w", encoding="utf-8") as f:
        f.writelines(healed_lines)
        
    print(f"[+] Mesh healed. {len(healed_lines)} ledger entries processed.")

if __name__ == "__main__":
    heal_mesh()
