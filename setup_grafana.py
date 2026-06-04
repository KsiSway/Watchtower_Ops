import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

GRAFANA_URL = "http://localhost:3000"
GRAFANA_USER = os.getenv("GRAFANA_USER")
GRAFANA_PASS = os.getenv("GRAFANA_PASS")
INFLUX_TOKEN = os.getenv("INFLUXDB_TOKEN")

auth = (GRAFANA_USER, GRAFANA_PASS)

def setup_datasource():
    print("[*] Adding InfluxDB Data Source...")
    ds_url = f"{GRAFANA_URL}/api/datasources"
    payload = {
        "name": "InfluxDB",
        "type": "influxdb",
        "access": "proxy",
        "url": "http://watchtower_influxdb:8086",
        "jsonData": {
            "version": "Flux",
            "organization": "watchtower",
            "defaultBucket": "telemetry"
        },
        "secureJsonData": {
            "token": INFLUX_TOKEN
        },
        "isDefault": True
    }
    
    response = requests.post(ds_url, json=payload, auth=auth)
    if response.status_code in [200, 409]:
        print(f"[+] Data Source initialized: {response.status_code}")
    else:
        print(f"[!] Error adding data source: {response.text}")

def setup_dashboard():
    print("[*] Deploying Watchtower Performance Dashboard...")
    dash_url = f"{GRAFANA_URL}/api/dashboards/db"
    
    # Simple Flux query for the panel
    flux_query = 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "inference_metrics") |> filter(fn: (r) => r["_field"] == "latency") |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false) |> yield(name: "mean")'

    dashboard_json = {
        "dashboard": {
            "id": None,
            "title": "Watchtower Mesh Performance",
            "panels": [
                {
                    "type": "timeseries",
                    "title": "Inference Latency by Node",
                    "gridPos": {"h": 8, "w": 24, "x": 0, "y": 0},
                    "targets": [
                        {
                            "query": flux_query,
                            "refId": "A",
                            "datasource": {"type": "influxdb", "uid": "InfluxDB"}
                        }
                    ],
                    "fieldConfig": {
                        "defaults": {
                            "unit": "s",
                            "custom": {
                                "drawStyle": "line",
                                "lineInterpolation": "smooth",
                                "showPoints": "always"
                            }
                        }
                    }
                }
            ],
            "schemaVersion": 36,
            "refresh": "5s"
        },
        "overwrite": True
    }
    
    response = requests.post(dash_url, json=dashboard_json, auth=auth)
    if response.status_code == 200:
        print(f"[+] Dashboard deployed: {response.json()['url']}")
    else:
        print(f"[!] Error deploying dashboard: {response.text}")

if __name__ == "__main__":
    setup_datasource()
    setup_dashboard()
