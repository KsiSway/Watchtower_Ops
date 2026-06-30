# [Environment: Python Virtual Environment]
import socket
import time
import random
import sys

# Simulated External Endpoint (Cloudflare DNS for reliable socket testing)
TARGET_IP = "1.1.1.1"
TARGET_PORT = 80

def execute_telemetry(strict_mode=True):
    """
    Simulates automated network telemetry polling.
    strict_mode=True: Simulates basic routines (rigid intervals).
    strict_mode=False: Simulates advanced routines (high variance, organic traffic blending).
    """
    print(f"[*] Initializing Synthetic Network Telemetry...")
    print(f"[*] Execution Zone: Isolated Python Virtual Environment")
    print(f"[*] Target Vector: {TARGET_IP}:{TARGET_PORT}")
    print(f"[*] Mode: {'Rigid (Basic)' if strict_mode else 'Randomized (Advanced)'}")
    
    polling_interval = 2.0  # Base interval of 2 seconds
    
    try:
        while True:
            # 1. Calculate Variance 
            if strict_mode:
                # Low-entropy routine: Near-zero variance
                sleep_time = polling_interval + random.uniform(-0.1, 0.1)
            else:
                # High-entropy routine: 50% variance randomization
                jitter_variance = polling_interval * 0.5
                sleep_time = polling_interval + random.uniform(-jitter_variance, jitter_variance)
            
            # 2. Execute Polling Connection
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1.0)
                    s.connect((TARGET_IP, TARGET_PORT))
                    # Connection established, silently drop to simulate a zero-byte ping
            except Exception:
                pass # Suppress connection errors to keep the telemetry quiet
            
            print(f"[*] Telemetry dispatched. Sleeping for {sleep_time:.4f}s...")
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        print("\n[*] Synthetic telemetry terminated by Operator.")
        sys.exit(0)

if __name__ == "__main__":
    # Run in advanced mode to validate statistical variance mechanics
    # This will mathematically blind the Jitter engine but trigger Destination Persistence
    execute_telemetry(strict_mode=False)