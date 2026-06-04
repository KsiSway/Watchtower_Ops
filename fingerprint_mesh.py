import pandas as pd
import socket
import sys
import concurrent.futures
import os

def check_port(ip, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return port, True
        except:
            return port, False

def fingerprint_node(ip):
    # Mapping ports to likely device identities
    signatures = {
        8002: "SAMSUNG-SMART-TV",
        8001: "SAMSUNG-SMART-TV-UNSEC",
        5555: "ADB-ENABLED-ANDROID",
        8008: "CHROMECAST-DEVICE",
        8291: "MIKROTIK-ROUTER",
        22: "SSH-LINUX-NODE",
        445: "WINDOWS-SMB-NODE",
        80: "HTTP-WEB-INTERFACE"
    }
    
    found_services = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(signatures)) as executor:
        future_to_port = {executor.submit(check_port, ip, port): port for port in signatures}
        for future in concurrent.futures.as_completed(future_to_port):
            port, is_open = future.result()
            if is_open:
                found_services.append(signatures[port])
    
    if found_services:
        # Return the most specific signature found
        return "|".join(list(set(found_services)))
    return None

def execute_fingerprint_sweep():
    csv_file = "Watchtower_Final_Baseline.csv"
    if not os.path.exists(csv_file):
        print("[-] Error: Baseline CSV not found.")
        return

    df = pd.read_csv(csv_file)
    print(f"[*] Initiating Fingerprint Sweep for 'RESOLVE_FAIL' nodes...")

    for index, row in df.iterrows():
        if row['Hostname'] == "RESOLVE_FAIL":
            ip = row['IP']
            print(f"[*] Probing {ip}...", end="\r")
            identity = fingerprint_node(ip)
            if identity:
                df.at[index, 'Hostname'] = identity
                print(f"[+] Identified {ip} as {identity}        ")
    
    df.to_csv(csv_file, index=False)
    print("=== Fingerprint Sweep Complete. Baseline Updated. ===")

if __name__ == "__main__":
    execute_fingerprint_sweep()
