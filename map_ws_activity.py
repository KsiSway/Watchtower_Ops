import socket
import sys
import concurrent.futures

def check_port(ip, port, timeout=0.2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return ip, True
        except:
            return ip, False

def main():
    port = 3001
    subnet = "192.168.68."
    print(f":: MAPPING WEBSOCKET ACTIVITY ON PORT {port}...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_port, f"{subnet}{i}", port) for i in range(1, 255)]
        for future in concurrent.futures.as_completed(futures):
            ip, is_open = future.result()
            if is_open:
                print(f"[!] ALERT: Node {ip} is LISTENING on port {port}")

if __name__ == "__main__":
    main()
