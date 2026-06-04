import paramiko
import requests
import sys

TARGET_IP = "192.168.68.110"
# Standard default credential matrix for infrastructure
CREDS = [
    ("admin", "admin"), 
    ("root", "root"), 
    ("admin", "password"), 
    ("pi", "raspberry"),
    ("Lance", "password"),
    ("Lance", "123456"),
    ("Lance", "lance")
]

def check_ssh(ip, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, port=22, username=user, password=pwd, timeout=3)
        print(f"[!] CRITICAL: SSH VULNERABLE -> {user}:{pwd}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[-] SSH Secured against: {user}:{pwd}")
    except Exception as e:
        print(f"[-] SSH Error: {e}")
    return False

def check_grafana(ip, user, pwd):
    url = f"http://{ip}:3000/api/user"
    try:
        r = requests.get(url, auth=(user, pwd), timeout=3)
        if r.status_code == 200:
            print(f"[!] CRITICAL: GRAFANA VULNERABLE -> {user}:{pwd}")
            return True
        else:
            print(f"[-] Grafana Secured against: {user}:{pwd}")
    except Exception as e:
         print(f"[-] Grafana Connection Error: {e}")
    return False

if __name__ == "__main__":
    print(f"[*] Commencing Credential Audit on {TARGET_IP}...")
    hits = 0
    for u, p in CREDS:
        if check_ssh(TARGET_IP, u, p): hits += 1
        if check_grafana(TARGET_IP, u, p): hits += 1
    
    print(f"\n[*] Phase 1 Audit Complete. Hits detected: {hits}")
    if hits > 0:
        print("[!] IMMEDIATE ACTION REQUIRED: REMEDIATE VULNERABLE ACCOUNTS")
    else:
        print("[+] Primary management services secured against default matrix.")
