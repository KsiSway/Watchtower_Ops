# [Environment: Python Virtual Environment]
import urllib.request
import urllib.error
import socket

def verify_firewall_drop(target_ip):
    print(f"[*] Verifying network-layer DROP rule on {target_ip}:80...")
    
    try:
        # A 3-second timeout is sufficient to detect a dropped packet
        req = urllib.request.Request(f"http://{target_ip}", method="HEAD")
        response = urllib.request.urlopen(req, timeout=3)
        print(f"[!] VULNERABILITY ACTIVE: Port 80 is still accessible (HTTP {response.status}). Firewall rule failed.")
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print("[*] SECURE: Connection timed out. Firewall DROP rule is actively discarding Port 80 traffic.")
        elif isinstance(e.reason, ConnectionRefusedError):
            print("[*] SECURE: Connection refused. Port 80 is effectively closed at the network layer.")
        else:
            print(f"[*] SECURE: Connection blocked by network layer ({e.reason}).")
    except socket.timeout:
        print("[*] SECURE: Connection timed out. Firewall DROP rule is actively discarding Port 80 traffic.")

if __name__ == "__main__":
    verify_firewall_drop("192.168.68.128")
