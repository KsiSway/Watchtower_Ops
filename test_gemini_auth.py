import os
import urllib.request
import json

def test_gemini_auth():
    """
    Pulls the local environment variable and tests authentication against the API.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        try:
            with open(".env", "r") as f:
                for line in f:
                    if line.startswith("GEMINI_API_KEY="):
                        api_key = line.strip().split("=", 1)[1]
                        break
        except FileNotFoundError:
            pass
            
    if not api_key:
        print("[-] GEMINI_API_KEY environment variable not found. Deployment failed or shell needs restarting.")
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    
    print("[*] Testing API authentication...")
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print("[+] Authentication SUCCESS. API key is active and routing correctly.")
    except urllib.error.HTTPError as e:
        print(f"[-] Authentication FAILED. HTTP Error: {e.code}")
    except Exception as e:
        print(f"[-] Network FAILED. Check VPN state. Error: {e}")

if __name__ == "__main__":
    test_gemini_auth()
