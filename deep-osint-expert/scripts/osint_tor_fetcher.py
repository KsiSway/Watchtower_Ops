#!/usr/bin/env python3
# Minimum Requirement: Python 3.11+
# Dependencies: pip install aiohttp aiohttp-socks
# Prerequisite: Tor daemon running locally on port 9050

import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector, ProxyType
import logging
import json
import sys
import re
import time
import os

# Add parent directory to path to import hybrid_inference
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
try:
    from hybrid_inference import log_telemetry
except ImportError:
    # Fallback if execution context differs
    def log_telemetry(*args, **kwargs): pass

# Suppress standard output to enforce JSON purity for Watchtower dashboard
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

def extract_tactical_intel(html_content: str) -> dict:
    """Regex hunting engine for dark web IOCs."""
    intel = {
        "bitcoin_addresses": [],
        "monero_addresses": [],
        "pgp_keys_found": False,
        "emails": []
    }
    
    # Bitcoin: Matches legacy (1), script (3), and native segwit (bc1)
    btc_pattern = re.compile(r'\b(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-zA-HJ-NP-Z0-9]{39,59})\b')
    intel["bitcoin_addresses"] = list(set(re.findall(btc_pattern, html_content)))
    
    # Monero: Standard addresses starting with 4, integrated starting with 8
    xmr_pattern = re.compile(r'\b([48][0-9a-zA-Z]{94})\b')
    intel["monero_addresses"] = list(set(re.findall(xmr_pattern, html_content)))
    
    # PGP Public Key Block Detection
    if "-----BEGIN PGP PUBLIC KEY BLOCK-----" in html_content:
        intel["pgp_keys_found"] = True
        
    # Standard Email Extraction (Basic)
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    intel["emails"] = list(set(re.findall(email_pattern, html_content)))
    
    return intel

async def fetch_onion_data(onion_url: str) -> dict:
    """Routes async HTTP GET request through local Tor SOCKS5 proxy and extracts IOCs."""
    start_time = time.time()
    connector = ProxyConnector(proxy_type=ProxyType.SOCKS5, host='127.0.0.1', port=9050, rdns=True)
    
    async with aiohttp.ClientSession(connector=connector) as session:
        try:
            # High timeout recommended for Tor latency
            async with session.get(onion_url, timeout=30) as response:
                latency = time.time() - start_time
                if response.status == 200:
                    html_content = await response.text()
                    tactical_data = extract_tactical_intel(html_content)
                    
                    # Log telemetry to InfluxDB
                    log_telemetry(node="OPTIPLEX-LOCAL", transport="TOR-SOCKS5", latency=latency)
                    
                    return {
                        "status": "success", 
                        "length": len(html_content), 
                        "latency": round(latency, 3),
                        "intel": tactical_data,
                        "data": html_content[:500] # Snippet for UI display
                    }
                else:
                    return {"status": "error", "message": f"HTTP {response.status}", "latency": round(latency, 3)}
        except Exception as e:
             latency = time.time() - start_time
             return {"status": "error", "message": str(e), "latency": round(latency, 3)}

async def main(target_url: str):
    """Execution orchestrator."""
    result = await fetch_onion_data(target_url)
    
    # Output strict JSON for Watchtower UI dashboard ingestion
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python3 osint_tor_fetcher.py <onion_url>"}))
        sys.exit(1)
        
    target = sys.argv[1]
    asyncio.run(main(target))
