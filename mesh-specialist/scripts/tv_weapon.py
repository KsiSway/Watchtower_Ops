import sys
import os
import time
from samsungtvws import SamsungTVWS

# Ensure the script uses the directory it resides in for token storage
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) < 3:
    print(":: ERROR: INSUFFICIENT PARAMETERS.")
    print(":: USAGE: py tv_weapon.py [KEY_CODE] [TARGET_IP]")
    sys.exit()

command = sys.argv[1].upper()
target_ip = sys.argv[2]

# Dynamically generate token filenames based on the target IP
safe_ip = target_ip.replace('.', '_')
token_file = os.path.join(BASE_DIR, f"tizen_token_{safe_ip}.txt")

# Load existing token if available
token = None
if os.path.exists(token_file) and os.path.getsize(token_file) > 0:
    with open(token_file, 'r') as f:
        token = f.read().strip()

print(f":: INITIATING SECURE UPLINK TO {target_ip}...")

try:
    # Initialize connection. 
    # The library will attempt to use the token if provided.
    tv = SamsungTVWS(host=target_ip, port=8002, token=token, name='Watchtower C2')
    
    # Force a connection check/pairing trigger
    # The .token attribute is populated after the handshake
    if not token:
        print(":: PAIRING REQUIRED. CHECK TV SCREEN AND SELECT 'ALLOW'...")
        # Try to send a benign key to trigger the prompt
        tv.send_key("KEY_VOLDOWN") 
        time.sleep(1) # Wait for handshake to complete
        
        if tv.token:
            with open(token_file, 'w') as f:
                f.write(str(tv.token))
            print(f":: NEW CRYPTOGRAPHIC TOKEN GENERATED AND SAVED: {tv.token}")
        else:
            print(":: WARNING: NO TOKEN CAPTURED. RE-RUN AFTER ALLOWING ON SCREEN.")

    # Execute the actual command
    tv.send_key(command)
    print(f":: PAYLOAD '{command}' DELIVERED.")

except Exception as e:
    print(f":: UPLINK FAILED: {e}")
