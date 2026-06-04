import asyncio
import socket
import subprocess
import sys

async def get_free_port(starting_port: int = 8081) -> int:
    port = starting_port
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
        port += 1

ADB_PATH = r"C:\adb\platform-tools\adb.exe"

async def deploy_mesh_node(target_ip: str, target_port: int, script_name: str):
    print(f"[*] Targeting node {target_ip} on port {target_port}")
    
    # Push payload
    # Using shell execution for ADB compatibility in this environment
    process = await asyncio.create_subprocess_exec(
        ADB_PATH, "-s", target_ip, "push", script_name, "/data/local/tmp/",
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    
    if process.returncode != 0:
        print(f"[!] Push failed: {stderr.decode().strip()}")
        sys.exit(1)
        
    print(f"[*] Payload {script_name} delivered to {target_ip}. Ready for inference execution.")

async def main():
    target_device = "adb-R5CY53NEAAY-IYwX0h._adb-tls-connect._tcp"
    # We will push the inference script, as the orchestrator stays on the host
    payload = "run_inference.py"
    
    safe_port = await get_free_port(8081)
    print(f"[*] System assigned clean port: {safe_port}")
    
    await deploy_mesh_node(target_device, safe_port, payload)

if __name__ == "__main__":
    asyncio.run(main())
