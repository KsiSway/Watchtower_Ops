import asyncio
import aiohttp
import os

# Watchtower Credentials & Routing
GRAFANA_URL = "http://localhost:3000"
GRAFANA_USER = "KsiSway"
GRAFANA_PASS = "DOCnomore1!"
INFLUX_TOKEN = os.getenv("INFLUXDB_TOKEN", "LANCE-1985-SECURE")

DATASOURCE_PAYLOAD = {
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

# Flux Telemetry Queries
latency_query = 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "inference_metrics") |> filter(fn: (r) => r["_field"] == "latency") |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false) |> yield(name: "mean")'
hw_query = 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "hardware") |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false) |> yield(name: "mean")'
pingmesh_query = 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "pingmesh") |> filter(fn: (r) => r["_field"] == "p10_latency") |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false) |> yield(name: "mean")'
container_health_query = 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "docker_health") |> aggregateWindow(every: v.windowPeriod, fn: last, createEmpty: false) |> yield(name: "last")'
ollama_query = 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "ollama_inference") |> filter(fn: (r) => r["_field"] == "load") |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false) |> yield(name: "mean")'

DASHBOARD_PAYLOAD = {
    "dashboard": {
        "id": None,
        "title": "Watchtower Mesh Performance",
        "panels": [
            {
                "type": "timeseries",
                "title": "Inference Latency by Node",
                "gridPos": {"h": 8, "w": 24, "x": 0, "y": 0},
                "targets": [{"query": latency_query, "refId": "A", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}]
            },
            {
                "type": "timeseries",
                "title": "OptiPlex Hardware (CPU/Memory/Disk)",
                "gridPos": {"h": 8, "w": 12, "x": 0, "y": 8},
                "targets": [{"query": hw_query, "refId": "B", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}]
            },
            {
                "type": "timeseries",
                "title": "Pingmesh p10 Latency",
                "gridPos": {"h": 8, "w": 12, "x": 12, "y": 8},
                "targets": [{"query": pingmesh_query, "refId": "C", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}]
            },
            {
                "type": "stat",
                "title": "Docker Container Health",
                "gridPos": {"h": 8, "w": 12, "x": 0, "y": 16},
                "targets": [{"query": container_health_query, "refId": "D", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}]
            },
            {
                "type": "timeseries",
                "title": "Ollama Inference Load",
                "gridPos": {"h": 8, "w": 12, "x": 12, "y": 16},
                "targets": [{"query": ollama_query, "refId": "E", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}]
            }
        ],
        "schemaVersion": 36,
        "refresh": "5s"
    },
    "overwrite": True
}

async def execute_provisioning_sequence():
    auth = aiohttp.BasicAuth(GRAFANA_USER, GRAFANA_PASS)
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    async with aiohttp.ClientSession(auth=auth, headers=headers) as session:
        print("[*] Initiating Asynchronous Data Source Provisioning...")
        async with session.post(f"{GRAFANA_URL}/api/datasources", json=DATASOURCE_PAYLOAD) as ds_resp:
            if ds_resp.status in (200, 201):
                print("[+] SUCCESS: InfluxDB Data Source mapped.")
            elif ds_resp.status == 409:
                print("[+] Data Source already exists (409 Conflict handled).")
            else:
                error_msg = await ds_resp.text()
                print(f"[!] CRITICAL: Data Source mapping failed. HTTP {ds_resp.status}. Diagnostics: {error_msg}")
                return

        # Asynchronous sequential gating
        await asyncio.sleep(1)

        print("[*] Deploying Expanded Watchtower Performance Dashboard...")
        async with session.post(f"{GRAFANA_URL}/api/dashboards/db", json=DASHBOARD_PAYLOAD) as dash_resp:
            if dash_resp.status == 200:
                data = await dash_resp.json()
                print(f"[+] SUCCESS: Command Center HUD is live. Access at: {GRAFANA_URL}{data.get('url', '')}")
            else:
                error_msg = await dash_resp.text()
                print(f"[!] CRITICAL: Dashboard injection failed. HTTP {dash_resp.status}. Diagnostics: {error_msg}")

if __name__ == "__main__":
    asyncio.run(execute_provisioning_sequence())
