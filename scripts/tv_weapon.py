import argparse
import sys
import os
import subprocess
from samsungtvws import SamsungTVWS

def main():
    parser = argparse.ArgumentParser(description="Watchtower TV Weapon - Multimedia C2 & Diagnostic")
    parser.add_argument("--target", required=True, help="Target IP address")
    parser.add_argument("--port", type=int, default=8002, help="WebSocket port (default: 8002)")
    parser.add_argument("--token", help="Auth token for secure connection")
    parser.add_argument("--execute", help="Local command to execute upon successful uplink")
    
    args = parser.parse_args()
    
    print(f":: INITIATING SECURE UPLINK TO {args.target}:{args.port}...")
    
    try:
        # Initialize connection
        # The library handles the handshake and token validation
        tv = SamsungTVWS(host=args.target, port=args.port, token=args.token, name='Watchtower C2')
        
        # Verify connection by sending a benign key (Mute)
        # This confirms the WebSocket channel is active and authenticated
        tv.shortcuts().mute()
        print(":: UPLINK SECURED. DIAGNOSTIC PACKET DELIVERED.")
        
        if args.execute:
            print(f":: EXECUTING TACTICAL PAYLOAD: {args.execute}")
            # Execute the provided shell command locally as a beacon/mapping event
            result = subprocess.run(args.execute, shell=True, capture_output=True, text=True)
            print(f":: STDOUT:\n{result.stdout}")
            if result.stderr:
                print(f":: STDERR:\n{result.stderr}")
                
    except Exception as e:
        print(f":: UPLINK FAILED: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
