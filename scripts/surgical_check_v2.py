import socket
import sys

def check_port(ip, port, timeout=1.0):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return True
        except Exception as e:
            return False

def main():
    target_ips = ["192.168.68.107", "192.168.68.113", "192.168.68.110", "192.168.68.123"]
    ports_to_check = [3001, 8082, 8086, 25417]
    
    for ip in target_ips:
        print(f":: SURGICAL INTERROGATION OF {ip}...")
        for port in ports_to_check:
            is_open = check_port(ip, port)
            status = "OPEN" if is_open else "CLOSED/FILTERED"
            print(f"[#] {ip}:{port}: {status}")

if __name__ == "__main__":
    main()
