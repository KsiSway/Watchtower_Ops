import os
import json
import base64
import sqlite3
from hashlib import sha1
try:
    from pyDes import triple_des, CBC, PAD_PKCS5
except ImportError:
    print("[-] pyDes not found. Run: pip install pyDes")

# NOTE: This is a simplified extraction logic. 
# Firefox decryption typically requires the NSS library (nss3.dll) or a complex pure-python implementation of Mozilla's encryption.

def extract_credentials(profile_path):
    print(f"[*] Processing profile: {profile_path}")
    logins_json_path = os.path.join(profile_path, 'logins.json')
    key_db_path = os.path.join(profile_path, 'key4.db')

    if not os.path.exists(logins_json_path) or not os.path.exists(key_db_path):
        print("[-] Missing logins.json or key4.db in this profile.")
        return

    with open(logins_json_path, 'r') as f:
        logins_data = json.load(f)

    # Firefox uses key4.db (SQLite) to store the master key which decrypts logins.json
    # This script prints the ENCRYPTED blobs. Decryption requires proper NSS context.
    
    print(f"[+] Found {len(logins_data.get('logins', []))} stored credentials.")
    
    for login in logins_data.get('logins', []):
        url = login.get('hostname')
        user_enc = login.get('encryptedUsername')
        pass_enc = login.get('encryptedPassword')
        
        print(f"\n[!] Entry for: {url}")
        print(f"    -> Encrypted User: {user_enc}")
        print(f"    -> Encrypted Pass: {pass_enc}")

if __name__ == '__main__':
    profiles = [
        r'C:\Users\Lance\AppData\Roaming\Mozilla\Firefox\Profiles\44PP2Dju.Profile 1',
        r'C:\Users\Lance\AppData\Roaming\Mozilla\Firefox\Profiles\mutcsx0v.default-release'
    ]
    for p in profiles:
        extract_credentials(p)
