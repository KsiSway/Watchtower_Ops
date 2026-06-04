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
    target_ip = "192.168.68.107"
    ports_to_check = [80, 443, 3000, 3001, 8080, 8082, 8086, 25417]
    
    print(f":: SURGICAL INTERROGATION OF {target_ip}...")
    for port in ports_to_check:
        is_open = check_port(target_ip, port)
        status = "OPEN" if is_open else "CLOSED/FILTERED"
        print(f"[#] Port {port}: {status}")

if __name__ == "__main__":
    main()
