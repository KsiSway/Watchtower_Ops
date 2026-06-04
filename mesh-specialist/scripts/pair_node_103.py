import sys
import os
import time
from samsungtvws import SamsungTVWS

target_ip = '192.168.68.103'
port = 8080
token_file = 'tizen_token_192_168_68_103.txt'

print(f":: INITIATING SECURE UPLINK TO {target_ip} ON PORT {port}...")

try:
    # Initialize connection on port 8080
    tv = SamsungTVWS(host=target_ip, port=port, name='Watchtower C2')
    
    print(":: PAIRING REQUEST SENT. CHECK TV SCREEN FOR A PIN OR 'ALLOW' PROMPT...")
    
    # Send a benign key to trigger the handshake
    # Note: On some 8080 devices, this triggers a 4-digit PIN on the screen.
    tv.send_key("KEY_VOLDOWN") 
    
    # The .token attribute is populated after the handshake is accepted on screen
    # We loop for a bit to wait for the user to interact with the TV
    for i in range(30):
        if tv.token:
            with open(token_file, 'w') as f:
                f.write(str(tv.token))
            print(f"\n:: NEW CRYPTOGRAPHIC TOKEN GENERATED AND SAVED: {tv.token}")
            sys.exit(0)
        print(".", end="", flush=True)
        time.sleep(2)

    print("\n:: WARNING: TIMEOUT. NO TOKEN CAPTURED.")

except Exception as e:
    print(f"\n:: UPLINK FAILED: {e}")
