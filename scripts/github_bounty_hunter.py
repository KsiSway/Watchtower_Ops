import urllib.request
import json
import urllib.parse
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

def hunt_bounties(limit=10):
    try:
        print("[*] Initiating Watchtower Bounty Hunt...")
        print("[*] Target Parameter: 'good first issue'")
        print("[*] State: OPEN\n")
        
        # Fallback to REST API since GitHub CLI 'gh' is missing from host PATH
        query = urllib.parse.quote('label:"good first issue" state:open type:issue')
        url = f"https://api.github.com/search/issues?q={query}&per_page={limit}"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Watchtower-Exocortex/1.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
        issues = data.get("items", [])
        
        print(f"[*] Extracted {len(issues)} active baseline targets:")
        print("="*60)
        for issue in issues:
            repo_url = issue.get("repository_url", "")
            repo_name = repo_url.replace("https://api.github.com/repos/", "") if repo_url else "Unknown"
            title = issue.get("title", "No Title")
            html_url = issue.get("html_url", "No URL")
            print(f"TARGET : {repo_name}")
            print(f"ISSUE  : {title}")
            print(f"UPLINK : {html_url}")
            print("-" * 60)
            
    except Exception as e:
        print(f"[!] CRITICAL: Bounty Hunt REST API execution failed.\n{e}")

if __name__ == "__main__":
    hunt_bounties()
