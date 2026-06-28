# [Environment: Python Virtual Environment]
import csv
from pathlib import Path

def decode_telemetry(file_path):
    csv_path = Path(file_path)
    if not csv_path.exists():
        print(f"[!] CRITICAL: Baseline file missing at {csv_path}")
        return

    print(f"[*] Decoding Mesh Topology Telemetry from: {csv_path.name}")
    
    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = list(csv.DictReader(file))
        
        # Actively quantify anomalies for the Cognitive Analyst engine
        unknown_nodes = [row for row in reader if row.get('Hostname') == 'UNKNOWN']
        
        print(f"[*] Total Nodes Discovered: {len(reader)}")
        print(f"[*] Anomalous/Unknown Nodes: {len(unknown_nodes)}\n")
        
        print(f"{'IP ADDRESS':<18} | {'HOSTNAME':<25} | {'STATUS'}")
        print("-" * 60)
        
        for row in reader:
            ip = row.get('IP', 'N/A')
            host = row.get('Hostname', 'UNKNOWN')
            status = row.get('Status', 'N/A')
            print(f"{ip:<18} | {host:<25} | {status}")

if __name__ == "__main__":
    decode_telemetry(r"D:\Watchtower_Ops\Watchtower_Final_Baseline.csv")
