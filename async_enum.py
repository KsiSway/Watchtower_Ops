import asyncio
import re
from pathlib import Path

# Paths configured for Windows environment
LEDGER_PATH = Path(r"C:\Users\Lance\Watchtower_Ops\raw_scan.txt")
OUTPUT_DIR = Path(r"C:\Users\Lance\Watchtower_Ops\Enum_Results")

async def scan_host(ip: str):
    """Executes asynchronous Nmap service detection on a single IP."""
    print(f"[*] Enumerating target: {ip}")
    output_file = OUTPUT_DIR / f"{ip}_services.txt"
    
    # Internal subnet scan. -sV for service version detection, -T4 for aggressive timing
    cmd = f"nmap -sV -T4 --open -oN {output_file} {ip}"
    
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    
    await process.communicate()
    print(f"[+] Scan logged: {output_file}")

async def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    if not LEDGER_PATH.exists():
        print(f"[-] CRITICAL: Ledger not found at {LEDGER_PATH}")
        return

    with open(LEDGER_PATH, 'r') as file:
        raw_data = file.read()

    # Extract valid internal IPv4 addresses
    ipv4_pattern = r'\b(?:192\.168\.68\.(?:[1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-4]))\b'
    target_ips = list(set(re.findall(ipv4_pattern, raw_data)))

    if not target_ips:
        print("[-] No valid 192.168.68.x IPs extracted from ledger.")
        return

    print(f"[*] Parsed {len(target_ips)} targets. Initiating asynchronous Layer 4/7 enumeration...")
    
    # Semaphore to prevent network congestion/router lockup
    sem = asyncio.Semaphore(5)
    
    async def bounded_scan(ip):
        async with sem:
            await scan_host(ip)

    tasks = [bounded_scan(ip) for ip in target_ips]
    await asyncio.gather(*tasks)
    
    print("[*] ENUMERATION DIRECTIVE COMPLETE.")

if __name__ == "__main__":
    asyncio.run(main())