import subprocess
import platform
import datetime
import socket
import json
import re
import os
import asyncio


PORTS_TO_CHECK = {
    "Grafana": 8501,
    "SMB": 445
}

def log_activity(module, target, status, details=""):
    """Logs tactical activity to a local file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{module}] TARGET: {target} | STATUS: {status} | DETAILS: {details}\n"
    with open("C2_Activity.log", "a") as f:
        f.write(log_entry)

async def ping_host(host):
    """Returns True if host responds to a ping request."""
    param = '-n' if platform.system().lower() == 'Windows' else '-c'
    proc = await asyncio.create_subprocess_exec(
        'ping', param, '1', host,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.STDOUT
    )
    await proc.wait()
    return proc.returncode == 0

async def check_port(ip, port, timeout=1.0):
    """Returns True if the specified port is open on the target IP."""
    try:
        fut = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(fut, timeout=timeout)
        writer.close()
        await writer.wait_closed()
        return True
    except Exception:
        return False

def load_nodes_from_memory(filepath="/D/Watchtower_Ops/Gemini_Memory_Extraction.json"):
    """Parses the JSON memory file to dynamically extract mesh nodes."""
    nodes = {}
    if not os.path.exists(filepath):
        print(f"[-] Memory file not found: {filepath}")
        return nodes
        
    with open(filepath, "r", encoding="utf-8") as f:
        logs = json.load(f)
        
    base_ip = "192.168.68"
    
    for entry in logs:
        content = entry.get("content", "")
        
        # Extract devices matching recognized memory footprint signatures
        if "OptiPlex 3050" in content:
            match = re.search(r"OptiPlex 3050.*?\((192\.168\.68\.\d+)\)", content)
            if match: nodes["Primary C2 (OptiPlex 3050)"] = match.group(1)
        if "S25 Edge" in content:
            match = re.search(r"S25 Edge \(\.(\d+)\)", content)
            if match: nodes["Secondary Node (S25 Edge)"] = f"{base_ip}.{match.group(1)}"
        if "Hikvision Camera" in content:
            match = re.search(r"Hikvision Camera \(\.(\d+)\)", content)
            if match: nodes["Secondary Node (Hikvision Camera)"] = f"{base_ip}.{match.group(1)}"
        if "Tab A8" in content:
            match = re.search(r"Tab A8 \((192\.168\.68\.\d+)\)", content)
            if match: nodes["Tab A8 (ADB Target)"] = match.group(1)
        if "Samsung Monitor" in content:
            match = re.search(r"Samsung Monitor \(\.(\d+)\)", content)
            if match: nodes["Samsung Monitor"] = f"{base_ip}.{match.group(1)}"
            
    return nodes

async def scan_node(name, ip):
    is_up = await ping_host(ip)
    status = "[ONLINE]" if is_up else "[OFFLINE]"
    output = [f" {status} - {name} ({ip})"]
    details_list = []
    
    if is_up:
        for service, port in PORTS_TO_CHECK.items():
            is_open = await check_port(ip, port)
            port_status = "OPEN" if is_open else "BLOCKED/CLOSED"
            output.append(f"    -> {service} (Port {port}): {port_status}")
            details_list.append(f"{service}:{port_status}")
            
    log_status = "SUCCESS" if is_up else "FAILURE"
    details = ", ".join(details_list) if is_up else "Unreachable"
    return name, ip, is_up, "\n".join(output), log_status, details

async def run_sync_async():
    nodes = load_nodes_from_memory()
    if not nodes:
        print("[-] No nodes dynamically extracted from memory. Aborting.")
        return
        
    print(f"[*] Initiating System Sync and Health Check at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    tasks = [scan_node(name, ip) for name, ip in nodes.items()]
    results = await asyncio.gather(*tasks)
    
    all_operational = True
    for name, ip, is_up, output, log_status, details in results:
        print(output)
        log_activity("MESH_SYNC", ip, log_status, details)
        if not is_up:
            all_operational = False
            
    print("-" * 50)
    if all_operational:
        print("[+] System is 100% operational. All instances synchronized.")
    else:
        print("[-] Warning: One or more mesh nodes are unreachable or unresponsive.")

def run_sync():
    asyncio.run(run_sync_async())

if __name__ == "__main__":
    run_sync()
