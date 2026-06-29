# [Environment: Python Virtual Environment]
import subprocess
import sys

def extract_active_uplinks(target_ip):
    print(f"[*] Initiating diagnostic connection to {target_ip}...")
    print("[*] Extracting active TCP states from nf_conntrack...")
    
    # Native SSH command to parse the connection tracking table for established TCP states
    ssh_cmd = [
        "ssh", 
        f"root@{target_ip}", 
        "cat /proc/net/nf_conntrack | grep 'tcp' | grep 'ESTABLISHED'"
    ]
    
    try:
        result = subprocess.run(ssh_cmd, text=True, capture_output=True)
        
        if result.returncode == 0:
            print("[*] Connection telemetry extracted successfully:\n")
            lines = result.stdout.strip().split('\n')
            
            for line in lines:
                if not line: continue
                # Parse standard conntrack output for source, destination, and port
                parts = line.split()
                src = next((p for p in parts if p.startswith('src=')), None)
                dst = next((p for p in parts if p.startswith('dst=')), None)
                dport = next((p for p in parts if p.startswith('dport=')), None)
                
                if src and dst and dport:
                    print(f"    -> {src} | {dst} | {dport}")
            
            if not lines or (len(lines) == 1 and not lines[0]):
                print("    [!] No active ESTABLISHED TCP connections found.")
        else:
            # Silently handle grep exit code 1 (no lines matched) as a clean output
            if result.returncode == 1:
                print("    [!] No active ESTABLISHED TCP connections found.")
            else:
                print(f"[!] EXECUTION FAILURE: SSH command returned exit code {result.returncode}.\n{result.stderr}")
                
    except FileNotFoundError:
        print("[!] CRITICAL: Native SSH binary not found in host PATH.")
        sys.exit(1)

if __name__ == "__main__":
    extract_active_uplinks("192.168.68.128")
