import pandas as pd
import socket
from zeroconf import Zeroconf, ServiceBrowser
import time
import os

class NameCollector:
    def __init__(self):
        self.found_names = {}

    def remove_service(self, zeroconf, service_type, name):
        pass

    def add_service(self, zeroconf, service_type, name):
        self.update_service(zeroconf, service_type, name)

    def update_service(self, zeroconf, service_type, name):
        try:
            info = zeroconf.get_service_info(service_type, name)
            if info:
                for addr in info.addresses:
                    ip = socket.inet_ntoa(addr)
                    # Strip .local and extract clean name
                    clean_name = info.server.split('.')[0]
                    self.found_names[ip] = clean_name
        except Exception:
            pass

def resolve_internal_mesh():
    csv_file = "Watchtower_Final_Baseline.csv"
    if not os.path.exists(csv_file):
        print("[-] Error: Baseline CSV not found.")
        return

    df = pd.read_csv(csv_file)
    print(f"[*] Initializing mDNS sweep for {len(df)} nodes...")

    # Vector 1: mDNS Passive Listen
    collector = NameCollector()
    zeroconf = Zeroconf()
    services = ["_http._tcp.local.", "_googlecast._tcp.local.", "_workstation._tcp.local.", "_smb._tcp.local."]
    browsers = [ServiceBrowser(zeroconf, s, collector) for s in services]
    
    print("[*] Listening for broadcast callsigns (5s)...")
    time.sleep(5)
    zeroconf.close()

    # Vector 2: Active Correction Loop
    for index, row in df.iterrows():
        ip = row['IP']
        current_hostname = row['Hostname']

        if current_hostname == "RESOLVE_FAIL":
            # Check mDNS results first
            if ip in collector.found_names:
                df.at[index, 'Hostname'] = collector.found_names[ip]
                print(f"[+] Reacquired via mDNS: {ip} -> {collector.found_names[ip]}")
            else:
                try:
                    # Final attempt: Standard Socket with timeout
                    socket.setdefaulttimeout(1)
                    name = socket.gethostbyaddr(ip)[0]
                    df.at[index, 'Hostname'] = name
                    print(f"[+] Reacquired via Socket: {ip} -> {name}")
                except:
                    pass

    # Commit to disk
    df.to_csv(csv_file, index=False)
    print("=== Mesh Baseline Healed. Dashboard update pending. ===")

if __name__ == "__main__":
    resolve_internal_mesh()
