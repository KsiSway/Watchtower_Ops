# [Environment: Python Virtual Environment]
import json
import time
from pathlib import Path

def dispatch_event(node_ip, variance_pct, confidence):
    print(f"[*] Formatting network variance event for central dashboard ingestion...")
    alert_path = Path(r"D:\Watchtower_Ops\active_alerts.json")
    
    event_payload = {
        "timestamp": int(time.time()),
        "source_node": node_ip,
        "event_type": "baseline_variance_event",
        "metrics": {"variance_percent": variance_pct},
        "confidence": confidence,
        "status": "pending_analysis"
    }
    
    # Load existing ledger or create a new one
    if alert_path.exists():
        with open(alert_path, "r", encoding="utf-8") as f:
            try:
                alerts = json.load(f)
            except json.JSONDecodeError:
                alerts = []
    else:
        alerts = []
        
    alerts.append(event_payload)
    
    with open(alert_path, "w", encoding="utf-8") as f:
        json.dump(alerts, f, indent=4)
        
    print(f"[*] Event committed to {alert_path.name}. Ready for watchtower_gui.py and osint_brain.py ingestion.")

if __name__ == "__main__":
    # Simulating the automated handoff from the latency diagnostic
    dispatch_event("192.168.68.128", 3.60, "HIGH")
