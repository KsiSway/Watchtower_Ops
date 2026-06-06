import asyncio
import aiohttp
import os
import time
from dotenv import load_dotenv

load_dotenv()

# Configuration
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUX_ORG = "watchtower"
INFLUX_BUCKET = "telemetry"

async def push_to_influx(session, measurement, fields, tags=None):
    url = f"{INFLUX_URL}/api/v2/write?org={INFLUX_ORG}&bucket={INFLUX_BUCKET}&precision=s"
    tag_str = "," + ",".join([f"{k}={v}" for k, v in tags.items()]) if tags else ""
    
    field_parts = []
    for k, v in fields.items():
        if isinstance(v, str):
            field_parts.append(f'{k}="{v}"')
        else:
            field_parts.append(f"{k}={v}")
    
    field_str = ",".join(field_parts)
    line = f"{measurement}{tag_str} {field_str} {int(time.time())}"
    
    headers = {"Authorization": f"Token {INFLUX_TOKEN}", "Content-Type": "text/plain; charset=utf-8"}
    try:
        async with session.post(url, data=line, headers=headers) as resp:
            if resp.status not in [200, 204]:
                print(f"[!] InfluxDB Error: {resp.status} - {await resp.text()}")
            else:
                print(f"[+] Pushed {measurement} to InfluxDB.")
    except Exception as e:
        print(f"[!] Connection Error: {e}")

async def collect_telemetry(session):
    # 1. Hardware
    await push_to_influx(session, "hardware", {"cpu": 15.5, "memory": 40.2}, {"node": "optiplex_3050"})
    
    # 2. Pingmesh
    await push_to_influx(session, "pingmesh", {"p10_latency": 0.042}, {"target": "gateway"})
    
    # 3. Docker Health
    await push_to_influx(session, "docker_health", {"running": 1}, {"container": "watchtower_c2"})
    
    # 4. Ollama Load
    await push_to_influx(session, "ollama_inference", {"load": 10.0}, {"node": "optiplex_3050"})

async def main():
    async with aiohttp.ClientSession() as session:
        print("[*] Watchtower Telemetry Daemon v1.1 Active.")
        while True:
            await collect_telemetry(session)
            await asyncio.sleep(5)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("[*] Daemon Terminated.")
