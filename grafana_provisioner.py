import aiohttp
import asyncio
import os
import json
from dotenv import load_dotenv

load_dotenv()

GRAFANA_URL = "http://localhost:3000"
GRAFANA_USER = os.getenv("GRAFANA_USER", "admin")
GRAFANA_PASS = os.getenv("GRAFANA_PASS", "admin")
INFLUX_TOKEN = os.getenv("INFLUXDB_TOKEN")

auth = aiohttp.BasicAuth(GRAFANA_USER, GRAFANA_PASS)

async def setup_datasource(session):
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
        "secureJsonData": { "token": INFLUX_TOKEN },
        "isDefault": True
    }
    async with session.post(ds_url, json=payload, auth=auth) as response:
        if response.status == 200:
            print(f"[+] Data Source created: {response.status}")
        elif response.status == 409:
            print("[+] Data Source already exists (409 Conflict handled).")

async def setup_dashboard(session):
    print("[*] Deploying Watchtower Performance Dashboard...")
    dash_url = f"{GRAFANA_URL}/api/dashboards/db"

    queries = {
        "latency": 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "inference_metrics") |> filter(fn: (r) => r["_field"] == "latency") |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false) |> yield(name: "mean")',
        "hw": 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "hardware") |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false) |> yield(name: "mean")',
        "pingmesh": 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "pingmesh") |> filter(fn: (r) => r["_field"] == "p10_latency") |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false) |> yield(name: "mean")',
        "docker": 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "docker_health") |> aggregateWindow(every: v.windowPeriod, fn: last, createEmpty: false) |> yield(name: "last")',
        "ollama": 'from(bucket: "telemetry") |> range(start: v.timeRangeStart, stop: v.timeRangeStop) |> filter(fn: (r) => r["_measurement"] == "ollama_inference") |> filter(fn: (r) => r["_field"] == "load") |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false) |> yield(name: "mean")'
    }

    dashboard_json = {
        "dashboard": {
            "title": "Watchtower Mesh Performance",
            "panels": [
                { "type": "timeseries", "title": "Inference Latency", "gridPos": {"h": 8, "w": 24, "x": 0, "y": 0}, "targets": [{"query": queries["latency"], "refId": "A", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}] },
                { "type": "timeseries", "title": "OptiPlex Hardware", "gridPos": {"h": 8, "w": 12, "x": 0, "y": 8}, "targets": [{"query": queries["hw"], "refId": "B", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}] },
                { "type": "timeseries", "title": "Pingmesh p10", "gridPos": {"h": 8, "w": 12, "x": 12, "y": 8}, "targets": [{"query": queries["pingmesh"], "refId": "C", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}] },
                { "type": "stat", "title": "Docker Health", "gridPos": {"h": 8, "w": 12, "x": 0, "y": 16}, "targets": [{"query": queries["docker"], "refId": "D", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}] },
                { "type": "timeseries", "title": "Ollama Load", "gridPos": {"h": 8, "w": 12, "x": 12, "y": 16}, "targets": [{"query": queries["ollama"], "refId": "E", "datasource": {"type": "influxdb", "uid": "InfluxDB"}}] }
            ],
            "schemaVersion": 36, "refresh": "5s"
        },
        "overwrite": True
    }

    async with session.post(dash_url, json=dashboard_json, auth=auth) as response:
        if response.status == 200:
            data = await response.json()
            print(f"[+] Dashboard deployed: {data.get('url', '')}")

async def main():
    async with aiohttp.ClientSession() as session:
        await setup_datasource(session)
        await asyncio.sleep(1)
        await setup_dashboard(session)

if __name__ == "__main__":
    asyncio.run(main())
