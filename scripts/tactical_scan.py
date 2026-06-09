import socket
import sys
import concurrent.futures

def check_port(ip, port, timeout=0.1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return port, True
        except:
            return port, False

def main():
    target_ips = ["192.168.68.107", "192.168.68.110", "192.168.68.123"]
    # Scan tactical ranges: 3000-3010, 8000-8100, 25000-25500
    port_ranges = list(range(3000, 3011)) + list(range(8000, 8101)) + list(range(25400, 25430))
    
    for ip in target_ips:
        print(f":: SCANNING {ip} FOR TACTICAL WEBSOCKET CANDIDATES...")
        open_ports = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            future_to_port = {executor.submit(check_port, ip, port): port for port in port_ranges}
            for future in concurrent.futures.as_completed(future_to_port):
                port, is_open = future.result()
                if is_open:
                    open_ports.append(port)
        
        if open_ports:
            print(f"[+] Node {ip} OPEN ports: {sorted(open_ports)}")
        else:
            print(f"[-] Node {ip} No tactical ports identified in range.")

if __name__ == "__main__":
    main()
