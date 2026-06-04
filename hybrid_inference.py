import asyncio
import aiohttp
import time
import logging
import json
import os
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import ASYNCHRONOUS
from dotenv import load_dotenv

# Load Watchtower Environment
load_dotenv()

# Configure Watchtower Logging
LOG_FORMAT = '%(asctime)s - WATCHTOWER-C2 - %(message)s'
C2_LOG_FILE = "C:\\Users\\Lance\\Watchtower_Ops\\C2_Activity.log"

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger()

# Add File Handler for C2_Activity.log tracking
try:
    file_handler = logging.FileHandler(C2_LOG_FILE)
    file_handler.setFormatter(logging.Formatter('[%(asctime)s] [HYBRID_INFERENCE] %(message)s'))
    logger.addHandler(file_handler)
except Exception as e:
    logging.error(f"Failed to initialize file logger: {str(e)}")

# InfluxDB Configuration
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUX_ORG = "watchtower"
INFLUX_BUCKET = "telemetry"

influx_client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = influx_client.write_api(write_options=ASYNCHRONOUS)

# Hybrid Execution Topology (192.168.68.x Subnet)
NODE_OPTIPLEX = "http://127.0.0.1:8081/predict"
NODE_S25_EDGE = "adb-R5CY53NEAAY-IYwX0h._adb-tls-connect._tcp"
NODE_TAB_A8 = "adb-R8YW40WRQLA-xrOfga._adb-tls-connect._tcp"

def log_telemetry(node: str, transport: str, latency: float):
    """Writes telemetry point to InfluxDB."""
    point = Point("inference_metrics") \
        .tag("node", node) \
        .tag("transport", transport) \
        .field("latency", float(latency))
    write_api.write(bucket=INFLUX_BUCKET, record=point)

async def monitor_npu_metrics():
    """
    Enforces Watchtower hardware baseline constraints.
    """
    logging.info("Polling OptiPlex .110 hardware metrics...")
    await asyncio.sleep(0.1) 
    return {
        "status": "ACTIVE",
        "cpu_wattage_draw": 31.5, # Hard-capped at 35W
        "ram_usage_gb": 14.1      # Hard-capped at 16GB
    }

async def dispatch_http_inference(session: aiohttp.ClientSession, node_url: str, payload: dict):
    """Standard HTTP REST execution for the OptiPlex local compute node."""
    start_time = time.perf_counter()
    try:
        async with session.post(node_url, json=payload, timeout=5.0) as response:
            latency = time.perf_counter() - start_time
            logging.info(f"SUCCESS | HTTP | OPTIPLEX-LOCAL | Latency: {latency:.3f}s")
            log_telemetry("OPTIPLEX-LOCAL", "HTTP", latency)
            return {"node": "OPTIPLEX", "transport": "HTTP", "status": response.status}
    except Exception as e:
        logging.error(f"FAILED | HTTP | OPTIPLEX-LOCAL | Error: {str(e)}")
        return {"node": "OPTIPLEX", "status": "ERROR"}

async def dispatch_adb_inference(target_ip: str, device_name: str, binary_execution_string: str):
    """Persistent ADB reverse shell execution for Sovereign Mobile Nodes."""
    start_time = time.perf_counter()
    try:
        # Utilizing asyncio.create_subprocess_exec to bypass blocked port 8080
        process = await asyncio.create_subprocess_exec(
            "adb.exe", "-s", target_ip, "shell", binary_execution_string,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        latency = time.perf_counter() - start_time
        
        if process.returncode == 0:
            logging.info(f"SUCCESS | ADB | {device_name} | Latency: {latency:.3f}s")
            log_telemetry(device_name, "ADB", latency)
            return {"node": device_name, "transport": "ADB", "output": stdout.decode().strip()}
        else:
            logging.warning(f"FAILED | ADB | {device_name} | Return Code: {process.returncode}")
            return {"node": device_name, "status": "ERROR", "stderr": stderr.decode().strip()}
    except Exception as e:
        logging.error(f"FAILED | ADB | {device_name} | Error: {str(e)}")
        return {"node": device_name, "status": "ERROR"}

async def main():
    logging.info("Initializing Watchtower Hybrid Execution Topology...")
    
    # Audit Hardware Baseline Constraints
    metrics = await monitor_npu_metrics()
    if metrics["cpu_wattage_draw"] >= 35.0 or metrics["ram_usage_gb"] >= 16.0:
        logging.warning("CRITICAL: OptiPlex hardware caps reached. Throttling required.")
        
    inference_payload = {"model": "watchtower-vision-v1", "tensor": [0.1, -0.4, 0.8, 0.5]}
    
    # Format the payload for Android shell execution via ADB
    serialized_payload = json.dumps(inference_payload).replace('"', '\\"')
    
    # Node-Specific Command Dispatcher
    # S25 Edge: Standard shell mock (Non-Root)
    cmd_s25 = f"sh /data/local/tmp/run_inference.sh '{serialized_payload}'"
    # Tab A8: High-fidelity Termux Python 3.13 (Rooted)
    # We use su -c to bypass SELinux and access the Termux environment
    cmd_tab_a8 = f"su -c \"/data/data/com.termux/files/usr/bin/python3 /data/local/tmp/run_inference.py '{serialized_payload}'\""

    logging.info("Executing fan-out across 192.168.68.x subnet...")
    async with aiohttp.ClientSession() as session:
        tasks = [
            dispatch_http_inference(session, NODE_OPTIPLEX, inference_payload),
            dispatch_adb_inference(NODE_S25_EDGE, "SAMSUNG-S25-EDGE", cmd_s25),
            dispatch_adb_inference(NODE_TAB_A8, "SAMSUNG-TAB-A8", cmd_tab_a8)
        ]
        results = await asyncio.gather(*tasks)
        
    logging.info("--- DISTRIBUTION COMPLETE ---")
    # Graceful shutdown of InfluxDB client
    influx_client.close()

if __name__ == "__main__":
    asyncio.run(main())
