import asyncio
import sys

# Authorized Mesh Targets
TARGET_NODE = "192.168.68.100"
EDGE_COMMANDER = "192.168.68.109"
AWS_UPLINK = "3.234.129.4:8000"

def parse_hex_ip(hex_str: str) -> str:
    """Translates little-endian hex from /proc/net/tcp to IPv4."""
    try:
        ip_hex, port_hex = hex_str.split(':')
        ip = ".".join(str(int(ip_hex[i:i+2], 16)) for i in [6, 4, 2, 0])
        port = int(port_hex, 16)
        return f"{ip}:{port}"
    except Exception:
        return "UNKNOWN_IP"

async def run_async_subprocess(name: str, *args) -> str:
    process = await asyncio.create_subprocess_exec(
        name, *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    if process.returncode != 0:
        print(f"[-] FAULT: {name} execution failed (Code: {process.returncode})\n    [STDERR]: {stderr.decode().strip()}")
        return ""
    return stdout.decode().strip()

async def deep_service_interrogation():
    print("=== Tactical Reconnaissance: Unidentified Node ===")
    print(f"[*] Initiating deep service interrogation (-sV -p-) on {TARGET_NODE}...")
    # Authorized local subnet scope: 192.168.68.x
    output = await run_async_subprocess("nmap", "-sV", "-p-", TARGET_NODE)
    print(output)
    print("==================================================\n")

async def verify_aws_uplink():
    print("=== S25 Edge Commander Telemetry ===")
    print(f"[*] Extracting TCP state table via ADB ({EDGE_COMMANDER})...")
    
    output = await run_async_subprocess("adb", "-s", EDGE_COMMANDER, "shell", "cat", "/proc/net/tcp")
    if not output:
        return
        
    print("[*] Performing Hex-to-IP Translation...")
    lines = output.strip().split('\n')[1:] # Skip header
    uplink_verified = False
    
    for line in lines:
        parts = line.split()
        if len(parts) >= 4:
            local_addr = parse_hex_ip(parts[1])
            remote_addr = parse_hex_ip(parts[2])
            state = parts[3]
            
            # TCP State 01 = ESTABLISHED
            if state == "01":
                if remote_addr == AWS_UPLINK:
                    uplink_verified = True
                    print(f"[+] AWS UPLINK VERIFIED ACTIVE: {local_addr} -> {remote_addr}")
                elif remote_addr != "0.0.0.0:0":
                    print(f"[!] ANOMALOUS OUTBOUND CONNECTION: {local_addr} -> {remote_addr}")
                    
    if not uplink_verified:
        print(f"[-] WARNING: AWS Uplink ({AWS_UPLINK}) not detected in established TCP states.")

async def main():
    await deep_service_interrogation()
    await verify_aws_uplink()

if __name__ == "__main__":
    asyncio.run(main())