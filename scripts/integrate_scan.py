import re
import csv
import sys

def parse_nmap_to_ledger(scan_file, ledger_file):
    try:
        with open(scan_file, 'r', encoding='utf-8') as f:
            raw_data = f.read()
    except FileNotFoundError:
        print(f"Error: {scan_file} not found.")
        sys.exit(1)

    # Split the raw output into individual host blocks
    host_blocks = re.split(r'Nmap scan report for ', raw_data)[1:]
    
    updates = 0
    with open(ledger_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        for block in host_blocks:
            # Extract IP
            ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', block)
            # Extract MAC and Vendor
            mac_match = re.search(r'MAC Address: ([A-F0-9:]+) \((.*?)\)', block)
            
            if ip_match:
                ip = ip_match.group(1)
                mac = mac_match.group(1) if mac_match else "UNKNOWN/LOCAL"
                vendor = mac_match.group(2) if mac_match else "UNKNOWN"
                
                writer.writerow([ip, mac, vendor, 'UP', 'Auto-Parsed'])
                print(f"Appended: {ip} | {mac} | {vendor}")
                updates += 1

    print(f"\nTask Complete. {updates} nodes integrated into {ledger_file}.")

if __name__ == "__main__":
    # Save your raw Nmap paste to 'raw_scan.txt' in the same directory before running
    if len(sys.argv) > 1:
        parse_nmap_to_ledger(sys.argv[1], "Watchtower_Final_Baseline.csv")
    else:
        parse_nmap_to_ledger("raw_scan.txt", "Watchtower_Final_Baseline.csv")
