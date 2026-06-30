# [Environment: Python Virtual Environment]
import socket
import time
import random
import sys

# Simulated External C2 Server (Cloudflare DNS for reliable socket testing)
TARGET_IP = "1.1.1.1"
TARGET_PORT = 80

def execute_beacon(strict_mode=True):
    """
    Simulates malware command and control (C2) polling.
    strict_mode=True: Simulates basic malware (rigid intervals, caught by our IDS).
    strict_mode=False: Simulates advanced malware (high jitter, evades our IDS).
    """
    print(f"[*] Initializing Synthetic C2 Beacon...")
    print(f"[*] Target Vector: {TARGET_IP}:{TARGET_PORT}")
    print(f"[*] Mode: {'Rigid (Basic)' if strict_mode else 'Randomized (Advanced)'}")
    
    polling_interval = 2.0  # Base interval of 2 seconds
    
    try:
        while True:
            # 1. Calculate Jitter (Evasion Mechanics)
            if strict_mode:
                # Basic malware: Near-zero jitter to simulate a naive sleep() loop
                sleep_time = polling_interval + random.uniform(-0.1, 0.1)
            else:
                # Advanced malware: 50% jitter randomization to blend with organic traffic
                jitter_variance = polling_interval * 0.5
                sleep_time = polling_interval + random.uniform(-jitter_variance, jitter_variance)
            
            # 2. Execute Polling Connection
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1.0)
                    s.connect((TARGET_IP, TARGET_PORT))
                    # Connection established, silently drop to simulate a zero-byte ping
            except Exception:
                pass # Suppress connection errors to keep the beacon quiet
            
            print(f"[*] Beacon dispatched. Sleeping for {sleep_time:.4f}s...")
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\n[*] Synthetic beacon terminated by Operator.")
        sys.exit(0)

if __name__ == "__main__":
    # Run in strict mode to trigger the analyze_beacon_jitter() logic in passive_ids_sensor.py
    execute_beacon(strict_mode=True)