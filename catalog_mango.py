# [Environment: Python Virtual Environment]
import csv
import urllib.request
from pathlib import Path

def catalog_and_verify():
    csv_path = Path(r"D:\Watchtower_Ops\Watchtower_Final_Baseline.csv")
    temp_path = Path(r"D:\Watchtower_Ops\Watchtower_Final_Baseline_tmp.csv")
    target_ip = "192.168.68.128"

    print(f"[*] Cataloging {target_ip} as Mango_Router in baseline...")
    
    with open(csv_path, 'r', encoding='utf-8') as infile, open(temp_path, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        
        for row in reader:
            if row.get('IP') == target_ip:
                row['Hostname'] = 'Mango_Router'
                row['Vendor'] = 'GL.iNet'
                row['Status'] = 'Authorized'
            writer.writerow(row)

    temp_path.replace(csv_path)
    print("[*] Baseline updated successfully.\n")

    print("[*] Verifying encrypted administrative management on Port 80...")
    try:
        req = urllib.request.Request(f"http://{target_ip}", method="HEAD")
        response = urllib.request.urlopen(req, timeout=5)
        print(f"[!] VULNERABILITY DETECTED: Port 80 is serving unencrypted content (HTTP {response.status}).")
    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 308):
            print(f"[*] SECURE: Port 80 successfully redirects to HTTPS (HTTP {e.code}).")
        else:
            print(f"[*] Unexpected HTTP Response: {e.code}")
    except Exception as e:
        print(f"[*] Port 80 connection result: {e}")

if __name__ == "__main__":
    catalog_and_verify()
