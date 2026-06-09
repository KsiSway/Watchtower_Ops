#!/usr/bin/env python3
"""
Watchtower Telemetry Sync: UDP 514 Syslog to JSON Line Protocol
Target: 192.168.68.110 (OptiPlex 3050 Central Host)
Standards: Python 3.11+, Synchronous Sockets, Zero External Dependencies
"""

import socket
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

SYSLOG_REGEX = re.compile(
    r'<(?P<pri>\d+)>(?P<timestamp>[A-Z][a-z]{2}\s+\d+\s+\d+:\d+:\d+)\s+'
    r'(?P<host>\S+)\s+(?P<app>[a-zA-Z0-9_\-]+)(?:\[(?P<pid>\d+)\])?:\s+(?P<msg>.*)'
)

readonly_STAGING_PATH = Path("D:/OSINT_Staging/mango_telemetry.jsonl")

def process_telemetry(raw_log: str, addr: tuple):
    match = SYSLOG_REGEX.match(raw_log)
    
    if not match:
        payload = {
            "measurement": "raw_syslog",
            "tags": {"source_ip": addr[0]},
            "fields": {"message": raw_log},
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    else:
        parsed = match.groupdict()
        payload = {
            "measurement": "openwrt_telemetry",
            "tags": {
                "source_ip": addr[0],
                "hostname": parsed.get("host", "unknown"),
                "daemon": parsed.get("app", "unknown")
            },
            "fields": {
                "message": parsed.get("msg", ""),
                "priority": int(parsed.get("pri", 0)),
                "pid": int(parsed.get("pid", 0)) if parsed.get("pid") else 0
            },
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    
    json_line = json.dumps(payload)
    print(f"[+] {addr[0]} -> {json_line}", flush=True)
    
    try:
        readonly_STAGING_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(readonly_STAGING_PATH, "a") as f:
            f.write(json_line + "\n")
    except IOError as e:
        print(f"[-] CRITICAL: I/O write failure to staging volume: {e}", flush=True)

def sync_daemon():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 514))
    print("[*] SYNC ENGAGED: Listening for OpenWrt telemetry on 127.0.0.1:514 (UDP)", flush=True)
    
    try:
        while True:
            data, addr = sock.recvfrom(4096)
            print(f"[DEBUG] Received from {addr}: {data}", flush=True)
            raw_log = data.decode('utf-8', errors='replace').strip()
            process_telemetry(raw_log, addr)
    except KeyboardInterrupt:
        print("\n[*] SYNC TERMINATED BY OPERATOR.", flush=True)
    finally:
        sock.close()

if __name__ == "__main__":
    sync_daemon()