# DEPLOYMENT: Watchtower_Ops/osint_cert_bridge.py
# Passive Subdomain Extraction Bridge (v1.1 - Resilient)

import requests
import json
import sys
import asyncio
import time
import socket

async def execute_local_dns_fallback(domain: str) -> list:
    """Alternative fallback logic: Local DNS dictionary sweep."""
    # High-probability tactical subdomains
    common_subs = ["www", "mail", "remote", "vpn", "api", "dev", "staging", "portal", "admin", "secure", "smtp", "git"]
    found_nodes = []
    
    # Resolving locally; bypasses external API reliance
    for sub in common_subs:
        target = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(target)
            found_nodes.append(f"RESOLVED SUBDOMAIN: {target} -> {ip}")
        except Exception:
            pass
    return found_nodes

async def fetch_certificate_logs(domain: str, max_retries: int = 3):
    """Extracts subdomains with exponential backoff and automated local fallback."""
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    headers = {"User-Agent": "WatchtowerC2/1.1"}
    base_delay = 3

    for attempt in range(max_retries):
        try:
            # Extended timeout for massive corporate domains
            response = requests.get(url, headers=headers, timeout=45)
            
            if response.status_code == 200:
                data = response.json()
                subdomains = sorted(list(set([entry['name_value'].lower() for entry in data])))
                
                if not subdomains:
                    return {"status": "success", "analysis": "Zero certificate logs found for this domain."}

                dossier = f"CERTIFICATE TRANSPARENCY LOGS: {domain}\nDISCOVERED SUBDOMAINS:\n" + "\n".join(subdomains[:100])
                
                brain_proc = await asyncio.create_subprocess_exec(
                    "python", "osint_brain.py", "telemetry", dossier,
                    stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                )
                b_stdout, b_stderr = await brain_proc.communicate()

                if brain_proc.returncode == 0:
                    return json.loads(b_stdout.decode().strip())
                else:
                     return {"status": "success", "analysis": f"Found {len(subdomains)} subdomains. Brain pipeline offline."}
                     
            elif response.status_code in [429, 502, 503, 504]:
                # Force backoff on server overloads
                raise requests.exceptions.ConnectionError(f"HTTP {response.status_code} - Server Overload")
            else:
                return {"status": "error", "message": f"crt.sh API Error: {response.status_code}"}
                
        except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
            if attempt < max_retries - 1:
                time.sleep(base_delay * (2 ** attempt))
            else:
                # Primary external API vector failed. Deploying local fallback per directive.
                fallback_nodes = await execute_local_dns_fallback(domain)
                if fallback_nodes:
                    return {"status": "success", "analysis": f"crt.sh API failed ({str(e)}). LOCAL FALLBACK ENGAGED:\n" + "\n".join(fallback_nodes)}
                else:
                    return {"status": "error", "message": f"crt.sh API and local DNS fallback both failed. Target may be offline."}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_cert_bridge.py <domain>"}))
        sys.exit(1)
    print(json.dumps(asyncio.run(fetch_certificate_logs(sys.argv[1])), indent=2))
