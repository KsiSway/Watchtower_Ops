# [Environment: Python Virtual Environment]
import subprocess
import sys

def enforce_encrypted_management(target_ip):
    print(f"[*] Initiating secure shell connection to {target_ip}...")
    print("[*] Pushing UCI network-layer configuration (Drop Port 80)...")
    
    # Native SSH command to implement a strict firewall drop rule, bypassing nginx
    ssh_cmd = [
        "ssh", 
        f"root@{target_ip}", 
        "uci add firewall rule && uci set firewall.@rule[-1].name='Drop-Cleartext-HTTP' && uci set firewall.@rule[-1].src='lan' && uci set firewall.@rule[-1].dest_port='80' && uci set firewall.@rule[-1].proto='tcp' && uci set firewall.@rule[-1].target='DROP' && uci commit firewall && /etc/init.d/firewall restart"
    ]
    
    try:
        # Assuming SSH keys are configured for passwordless entry
        result = subprocess.run(ssh_cmd, text=True, capture_output=True)
        
        if result.returncode == 0:
            print("[*] Configuration committed successfully. Port 80 cleartext traffic is now dropped at the network layer.")
        else:
            print(f"[!] EXECUTION FAILURE: SSH command returned exit code {result.returncode}.\n{result.stderr}")
    except FileNotFoundError:
        print("[!] CRITICAL: Native SSH binary not found in host PATH.")
        sys.exit(1)

if __name__ == "__main__":
    enforce_encrypted_management("192.168.68.128")
