import socket
import requests

TARGET_IP = "192.168.68.109"
PORT = 8000

def grab_banner(ip, port):
    print(f"[*] Attempting raw TCP socket connection to {ip}:{port}...")
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((ip, port))
        # Sending a basic HTTP-like request to provoke a response
        s.send(b"OPTIONS / HTTP/1.1\r\nHost: target\r\n\r\n")
        banner = s.recv(1024)
        print("[+] Raw TCP Response:")
        print(banner.decode('utf-8', errors='ignore').strip())
        s.close()
    except Exception as e:
        print(f"[-] TCP Socket Error: {e}")

def check_http(ip, port):
    print(f"\n[*] Attempting HTTP GET request to http://{ip}:{port}...")
    try:
        # Note: Nmap detected SSL on this port, so we try http first but keep https in mind
        r = requests.get(f"http://{ip}:{port}", timeout=3, verify=False)
        print(f"[+] HTTP Status Code: {r.status_code}")
        print("[+] HTTP Server Headers:")
        for header, value in r.headers.items():
            print(f"    {header}: {value}")
        
        if 'text' in r.headers.get('Content-Type', ''):
            print("\n[+] Response Body Snippet:")
            print(r.text[:500].strip())
            
    except requests.exceptions.RequestException as e:
        print(f"[-] HTTP Connection Error: {e}")
        print("[*] Attempting HTTPS connection...")
        try:
            r = requests.get(f"https://{ip}:{port}", timeout=3, verify=False)
            print(f"[+] HTTPS Status Code: {r.status_code}")
            print("[+] HTTPS Server Headers:")
            for header, value in r.headers.items():
                print(f"    {header}: {value}")
        except Exception as e2:
            print(f"[-] HTTPS Connection Error: {e2}")

if __name__ == "__main__":
    grab_banner(TARGET_IP, PORT)
    check_http(TARGET_IP, PORT)
