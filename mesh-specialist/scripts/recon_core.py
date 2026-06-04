import os
import sys
import json
import time
import requests
import shodan
import re
import csv
from dotenv import load_dotenv

# Initialize Exocortex Environment
load_dotenv()
SHODAN_KEY = os.getenv("SHODAN_API_KEY")
CENSYS_TOKEN = os.getenv("CENSYS_PERSONAL_ACCESS_TOKEN")
ABUSE_KEY = os.getenv("ABUSEIPDB_API_KEY")
ALIEN_KEY = os.getenv("ALIENVAULT_API_KEY")
ABSTRACT_KEY = os.getenv("ABSTRACT_API_KEY")
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

HIGH_RISK_PORTS = [22, 23, 3389, 445, 20, 21]

def alert_discord(ip, ports, abuse_score, country):
    if not WEBHOOK_URL: return
    payload = {
        "content": f"🚨 **WATCHTOWER CRITICAL ALERT** 🚨\n**Target IP:** `{ip}` ({country})\n**Exposed Ports:** `{ports}`\n**Abuse Confidence:** `{abuse_score}%`\n*Immediate review required.*"
    }
    try:
        requests.post(WEBHOOK_URL, json=payload, timeout=5)
    except: pass

def shodan_scan(ip):
    try:
        api = shodan.Shodan(SHODAN_KEY)
        host = api.host(ip)
        return {"hostnames": host.get("hostnames", []), "ports": host.get("ports", []), "os": host.get("os", "Unknown")}
    except Exception as e: return {"error": str(e)}

def censys_scan(ip):
    headers = {"Accept": "application/json", "Authorization": f"Bearer {CENSYS_TOKEN}"}
    try:
        res = requests.get(f"https://api.platform.censys.io/v3/global/asset/host/{ip}", headers=headers, timeout=10)
        if res.status_code == 200:
            return [s.get("port") for s in res.json().get("result", {}).get("services", [])]
        return {"error": f"HTTP {res.status_code}"}
    except Exception as e: return {"error": str(e)}

def abuseipdb_scan(ip):
    headers = {"Accept": "application/json", "Key": ABUSE_KEY}
    try:
        res = requests.get("https://api.abuseipdb.com/api/v2/check", headers=headers, params={"ipAddress": ip, "maxAgeInDays": 90}, timeout=10)
        if res.status_code == 200:
            data = res.json().get("data", {})
            return {"abuseConfidenceScore": data.get("abuseConfidenceScore", 0), "totalReports": data.get("totalReports", 0)}
        return {"error": f"HTTP {res.status_code}"}
    except Exception as e: return {"error": str(e)}

def alienvault_scan(ip):
    headers = {"X-OTX-API-KEY": ALIEN_KEY}
    try:
        res = requests.get(f"https://otx.alienvault.com/api/v1/indicators/IPv4/{ip}/general", headers=headers, timeout=10)
        if res.status_code == 200:
            return {"pulse_count": res.json().get("pulse_info", {}).get("count", 0)}
        return {"error": f"HTTP {res.status_code}"}
    except Exception as e: return {"error": str(e)}

def abstractapi_scan(ip):
    try:
        res = requests.get(f"https://ipgeolocation.abstractapi.com/v1/?api_key={ABSTRACT_KEY}&ip_address={ip}", timeout=10)
        if res.status_code == 200:
            data = res.json()
            return {"country": data.get("country"), "city": data.get("city"), "is_vpn": data.get("security", {}).get("is_vpn")}
        return {"error": f"HTTP {res.status_code}"}
    except Exception as e: return {"error": str(e)}

def parse_nmap_to_csv(nmap_output, output_file="C:\\Users\\Lance\\Watchtower_Ops\\Watchtower_Final_Baseline.csv"):
    hosts = []
    current_ip = None
    
    # Regex extraction for IP, MAC, and Vendor
    for line in nmap_output.split('\n'):
        ip_match = re.search(r'Nmap scan report for .*?(\d+\.\d+\.\d+\.\d+)', line)
        mac_match = re.search(r'MAC Address: ([0-9A-F:]+) \((.*?)\)', line)
        
        if ip_match:
            current_ip = ip_match.group(1)
        elif mac_match and current_ip:
            hosts.append({
                "IP": current_ip,
                "MAC": mac_match.group(1).replace(':', '-'),
                "Vendor": mac_match.group(2)
            })
            current_ip = None
            
    # Write structured data to the C2 baseline ledger
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["IP", "MAC", "Vendor"])
        writer.writeheader()
        writer.writerows(hosts)
    return f"[+] Baseline ledger updated: {len(hosts)} nodes documented."

def main():
    print("=== Project Watchtower: Multi-Engine v5 Initiated ===")
    if not os.path.exists("targets.txt"): sys.exit("[-] Fatal: targets.txt missing.")
    with open("targets.txt", "r") as f:
        targets = [line.strip() for line in f if line.strip()]
    if not targets: sys.exit("[-] Target queue empty.")

    log_file = "Watchtower_Log.json"
    log_data = []
    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f: log_data = json.load(f)
        except ValueError: pass

    for ip in targets:
        print(f"\n[*] Sweeping {ip} (Multi-Spectrum)...")
        
        # Parallel Execution Simulation
        shodan_data = shodan_scan(ip)
        censys_data = censys_scan(ip)
        abuse_data = abuseipdb_scan(ip)
        alien_data = alienvault_scan(ip)
        abstract_data = abstractapi_scan(ip)
        
        record = {
            "ip": ip,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "geo_intel": abstract_data,
            "shodan": shodan_data,
            "censys_ports": censys_data,
            "abuse_intel": abuse_data,
            "otx_intel": alien_data
        }
        log_data.append(record)
        
        # Evaluation Matrix
        s_ports = shodan_data.get("ports") if isinstance(shodan_data, dict) and "ports" in shodan_data else []
        exposed = [p for p in s_ports if p in HIGH_RISK_PORTS]
        abuse_score = abuse_data.get("abuseConfidenceScore", 0) if isinstance(abuse_data, dict) else 0
        country = abstract_data.get("country", "Unknown") if isinstance(abstract_data, dict) else "Unknown"
        
        if exposed or abuse_score > 0:
            print(f"[!] THREAT DETECTED: {ip} | Ports: {exposed} | Abuse Score: {abuse_score}%")
            alert_discord(ip, exposed, abuse_score, country)
        else:
            print(f"[+] {ip} : Clear.")
            
        with open(log_file, "w") as f:
            json.dump(log_data, f, indent=4)
            
        time.sleep(3) # Increased throttling for 5-engine array
        
    print("\n=== Sweep Complete. Ledger Updated. ===")

if __name__ == "__main__":
    main()
