import re
import requests
import datetime
import os
import sys

# Project Watchtower Integration
C2_LOG = "C2_Activity.log"
INTEL_LOG = "intelligence_log.csv"

def log_c2(module, target, status, details):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{module}] TARGET: {target} | STATUS: {status} | DETAILS: {details}\n"
    with open(C2_LOG, "a") as f:
        f.write(log_entry)

def log_intel(category, source, status):
    timestamp = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    log_entry = f"{timestamp},{category},{source},{status}\n"
    with open(INTEL_LOG, "a") as f:
        f.write(log_entry)

def extract_mega_links(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        log_c2("MEGA_SCAN", url, "STARTING", "Initiating link extraction")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        pattern = r'https://mega\.nz/(?:file|folder)/[a-zA-Z0-9_-]+#[a-zA-Z0-9_-]+'
        links = re.findall(pattern, response.text)
        unique_links = list(set(links))
        
        count = len(unique_links)
        log_c2("MEGA_SCAN", url, "SUCCESS", f"Found {count} unique MEGA links")
        
        for link in unique_links:
            log_intel("OSINT_MEGA", link, "FOUND")
            print(f"[+] {link}")
            
        return unique_links

    except Exception as e:
        log_c2("MEGA_SCAN", url, "FAILURE", str(e))
        print(f"[-] Error: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python osint_mega_scan.py <URL>")
        sys.exit(1)
        
    target = sys.argv[1]
    extract_mega_links(target)
