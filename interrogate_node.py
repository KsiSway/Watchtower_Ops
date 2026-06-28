# [Environment: Python Virtual Environment]
import subprocess
import sys

def interrogate_node(target_ip):
    print(f"[*] Initiating Layer 4/7 Interrogation on Ghost Node: {target_ip}")
    print("[*] Deploying Nmap (Service Enumeration, OS Fingerprinting, Aggressive Timing)...")
    
    # Nmap flags: -sV (Service versions), -O (OS fingerprinting), -T4 (Aggressive), -Pn (Assume online)
    nmap_cmd = ["nmap", "-sV", "-O", "-T4", "-Pn", target_ip]
    
    try:
        result = subprocess.run(nmap_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("[*] Interrogation Complete. Raw Telemetry:")
            print("-" * 60)
            print(result.stdout)
            print("-" * 60)
        else:
            print(f"[!] EXECUTION FAILURE: Nmap returned a non-zero exit code.\n{result.stderr}")
    except FileNotFoundError:
        print("[!] CRITICAL: Nmap binary not found in system PATH. Ensure local OptiPlex dependencies are met.")
        sys.exit(1)

if __name__ == "__main__":
    interrogate_node("192.168.68.128")
