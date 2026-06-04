# DEPLOYMENT: Watchtower_Ops/osint_spiderfoot_bridge.py
# Integration Bridge for SpiderFoot API

import json
import sys
import os
import requests

def fetch_spiderfoot_results(target: str):
    """Fetches deep scan results for the target via the local SpiderFoot REST API."""
    sf_host = "spiderfoot" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
    base_url = f"http://{sf_host}:5001"
    
    try:
        # 1. Fetch all scans from the ledger
        res = requests.get(f"{base_url}/scanlist", timeout=5)
        if res.status_code != 200:
            return {"status": "error", "message": f"SpiderFoot API error: HTTP {res.status_code}"}
            
        scans = res.json()
        
        # 2. Filter for the specific target
        # SpiderFoot /scanlist typically returns: [ID, Name, Target, Status, Started, Finished]
        target_scans = [s for s in scans if isinstance(s, list) and len(s) > 3 and target in s[2]]
        
        if not target_scans:
            return {
                "status": "success", 
                "analysis": f"No historical scan data found for '{target}'. Use the API Controls to start a deep scan first.",
                "intel": {}
            }
            
        # 3. Pull the most recent scan ID
        latest_scan = target_scans[0]
        scan_id = latest_scan[0]
        scan_status = latest_scan[3]
        
        # 4. Fetch the intelligence summary for this scan
        sum_res = requests.get(f"{base_url}/scansummary?id={scan_id}&by=type", timeout=5)
        summary_data = sum_res.json() if sum_res.status_code == 200 else []
        
        intel = {"target": target, "scan_id": scan_id, "status": scan_status, "findings": {}}
        total_events = 0
        
        for item in summary_data:
            # item format: [EventType, Description, Count]
            if isinstance(item, list) and len(item) >= 3:
                intel["findings"][item[1]] = item[2]
                total_events += int(item[2])
                
        dossier = f"SPIDERFOOT DEEP SCAN [{scan_status}]: Extracted {total_events} intelligence data points across {len(intel['findings'])} vectors."
        
        return {"status": "success", "analysis": dossier, "intel": intel}
        
    except Exception as e:
        return {"status": "error", "message": f"SpiderFoot bridge failed: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_spiderfoot_bridge.py '<target>'" }))
        sys.exit(1)
        
    target = sys.argv[1]
    print(json.dumps(fetch_spiderfoot_results(target), indent=2))
