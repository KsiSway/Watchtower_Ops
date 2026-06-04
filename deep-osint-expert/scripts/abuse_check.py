import requests
import sys
import json
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    print("[-] Error: ABUSEIPDB_API_KEY not found in .env file")
    sys.exit(1)

def check_ip_reputation(ip_address):
    url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    querystring = {'ipAddress': ip_address, 'maxAgeInDays': '90'}

    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        
        if response.status_code == 200:
            return json.dumps(response.json()['data'], indent=4)
        elif response.status_code == 401 or response.status_code == 403:
            return f"[-] Auth Error {response.status_code}: Key rejected. Check account status."
        elif response.status_code == 429:
            return "[-] Quota Error 429: Daily limit reached."
        else:
            return f"[-] API Error: {response.status_code}"
            
    except requests.exceptions.Timeout:
        return "[-] Request Timeout: API did not respond within 10 seconds"
    except requests.exceptions.RequestException as e:
        return f"[-] Request Error: {e}"
    except Exception as e:
        return f"[-] Critical Backend Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(check_ip_reputation(sys.argv[1]))
    else:
        print("[-] Target IP Required.")
