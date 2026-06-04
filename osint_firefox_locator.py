import os
import glob

def locate_firefox_vault():
    appdata = os.getenv('APPDATA')
    if not appdata:
        print("[-] APPDATA not found. Ensure execution environment is standard Windows.")
        return

    profile_path = os.path.join(appdata, 'Mozilla', 'Firefox', 'Profiles')
    if not os.path.exists(profile_path):
        print(f"[-] No Firefox profiles located at {profile_path}")
        return

    print("[+] Scanning for synced credential vaults...")
    search_pattern = os.path.join(profile_path, '**', 'logins.json')
    vault_files = glob.glob(search_pattern, recursive=True)

    for vault in vault_files:
        db_path = vault.replace('logins.json', 'key4.db')
        print(f"[!] Target Vault Identified:\n    -> Data: {vault}\n    -> Keys: {db_path}")

if __name__ == '__main__':
    locate_firefox_vault()
