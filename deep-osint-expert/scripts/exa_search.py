import requests
import json
import os

API_KEY = "a6c3db49-66df-4608-8b10-db1a6df71fc0"

def search(query, num_results=5):
    url = "https://api.exa.ai/search"
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "query": query,
        "useAutoprompt": True,
        "numResults": num_results
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    import sys
    q = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Project Watchtower OSINT"
    results = search(q)
    print(json.dumps(results, indent=2))
