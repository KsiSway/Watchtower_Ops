import sqlite3
import os
import json

def extract_cookies(profile_path):
    print(f"[*] Extracting cookies from: {profile_path}")
    cookie_db = os.path.join(profile_path, 'cookies.sqlite')
    if not os.path.exists(cookie_db):
        print("[-] cookies.sqlite not found.")
        return

    try:
        conn = sqlite3.connect(cookie_db)
        cursor = conn.cursor()
        cursor.execute("SELECT host, name, value, path, expiry FROM moz_cookies")
        
        cookies = []
        for row in cursor.fetchall():
            cookies.append({
                "host": row[0],
                "name": row[1],
                "value": row[2],
                "path": row[3],
                "expiry": row[4]
            })
        
        output_file = os.path.join(r'C:\Users\Lance\Watchtower_Ops', f"cookies_{os.path.basename(profile_path)}.json")
        with open(output_file, 'w') as f:
            json.dump(cookies, f, indent=4)
        
        print(f"[+] Successfully extracted {len(cookies)} cookies to {output_file}")
        conn.close()
    except Exception as e:
        print(f"[-] Cookie extraction failed: {e}")

if __name__ == '__main__':
    profiles = [
        r'C:\Users\Lance\AppData\Roaming\Mozilla\Firefox\Profiles\mutcsx0v.default-release',
        r'C:\Users\Lance\AppData\Roaming\Mozilla\Firefox\Profiles\44PP2Dju.Profile 1'
    ]
    for p in profiles:
        extract_cookies(p)
