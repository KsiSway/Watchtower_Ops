import asyncio
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

GRAFANA_URL = "http://127.0.0.1:3000"
AUTH = aiohttp.BasicAuth(os.getenv("GRAFANA_USER"), os.getenv("GRAFANA_PASS"))

async def provision_dashboard():
    # Watchtower Time Series Dashboard JSON Model
    dashboard_payload = {
        "dashboard": {
            "id": None,
            "title": "Watchtower Mesh Performance",
            "tags": ["tactical", "inference"],
            "timezone": "browser",
            "panels": [
                {
                    "type": "timeseries",
                    "title": "Inference Latency by Node",
                    "gridPos": {"h": 10, "w": 24, "x": 0, "y": 0},
                    "targets": [
                        {
                            "datasource": {"type": "influxdb", "uid": "InfluxDB"},
                            "query": 'from(bucket: "telemetry") |> range(start: v.timeRangeStart) |> filter(fn: (r) => r["_measurement"] == "inference_metrics") |> group(columns: ["node"])'
                        }
                    ]
                }
            ],
            "schemaVersion": 36
        },
        "overwrite": True
    }

    print("[*] Pushing dashboard JSON to Grafana API...")
    async with aiohttp.ClientSession(auth=AUTH) as session:
        async with session.post(f"{GRAFANA_URL}/api/dashboards/db", json=dashboard_payload) as resp:
            if resp.status == 200:
                print("[*] SUCCESS | Dashboard provisioned.")
            else:
                error_data = await resp.text()
                print(f"[!] FAILED | HTTP {resp.status}: {error_data}")

if __name__ == "__main__":
    asyncio.run(provision_dashboard())
