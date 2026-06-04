import socket
import sys
import concurrent.futures

def check_port(ip, port, timeout=0.5):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return port, True
        except:
            return port, False

def interrogate(ip):
    print(f"--- INTERROGATING TARGET: {ip} ---")
    
    # Tactical Port Selection
    ports = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        445: "SMB (EXPOSURE)",
        1900: "UPNP",
        5555: "ADB (ANDROID ROOT)",
        8001: "SAMSUNG CONTROL (UNSECURE)",
        8002: "SAMSUNG CONTROL (SECURE)",
        8008: "CHROMECAST REST",
        8009: "CHROMECAST SIGNALING",
        8291: "MIKROTIK WINBOX"
    }
    
    open_services = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(ports)) as executor:
        future_to_port = {executor.submit(check_port, ip, port): port for port in ports}
        for future in concurrent.futures.as_completed(future_to_port):
            port, is_open = future.result()
            if is_open:
                service_name = ports[port]
                open_services.append(f"PORT {port}: {service_name}")
                print(f"[+] {port} ({service_name}) is OPEN")
                
    if not open_services:
        print("[-] NO TACTICAL SERVICES DETECTED ON COMMON PORTS.")
    else:
        print(f"--- SCAN COMPLETE: {len(open_services)} VECTORS IDENTIFIED ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python mesh_interrogate.py [IP]")
    else:
        interrogate(sys.argv[1])
