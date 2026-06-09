import asyncio

async def check_node_state(ip: str, port: int, hostname: str):
    """
    Executes an asynchronous TCP connection test to verify node availability.
    """
    try:
        conn = asyncio.open_connection(ip, port)
        reader, writer = await asyncio.wait_for(conn, timeout=3.0)
        print(f"[+] {hostname} ({ip}:{port}) - ONLINE")
        writer.close()
        await writer.wait_closed()
    except Exception:
        print(f"[-] {hostname} ({ip}:{port}) - OFFLINE/UNREACHABLE")

async def execute_infrastructure_sync():
    print("[*] Initiating internal subnet roll call...")
    
    # Target definitions mapped to verified active mesh IPs
    nodes = [
        ("192.168.68.110", 445, "OptiPlex 3050 (x64 Server)"),
        ("192.168.68.120", 8022, "S25 Edge (ARM64 Main)"),
        ("192.168.68.112", 8022, "Tab A8 (ARM64 Rooted Node)"),
        ("192.168.68.1", 80, "Deco XE75-PRO (Primary Gateway)")
    ]
    
    tasks = [check_node_state(ip, port, name) for ip, port, name in nodes]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(execute_infrastructure_sync())
