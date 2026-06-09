import os
from samsungtvws import SamsungTVWS
import json

TARGET_IP = "192.168.68.101"
TOKEN = "54873798"

print(f"[*] Connecting to {TARGET_IP} via Secure Port 8002...")
try:
    tv = SamsungTVWS(host=TARGET_IP, port=8002, token=TOKEN, name='Watchtower Interrogator')
    apps = tv.app_list()
    print("[+] Application Enumeration Successful:")
    print(json.dumps(apps, indent=4))
except Exception as e:
    print(f"[-] Interrogation Failed: {e}")
