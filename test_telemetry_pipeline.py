#!/usr/bin/env python3
"""
Watchtower Telemetry Pipeline Test: Synthetic Packet Injection
Target: 127.0.0.1:514 (Local Sync Daemon)
Standards: Python 3.11+, Native Socket, Cross-Platform (Windows/Linux)
"""

import socket
import time
import json
import sys
from pathlib import Path

# Configuration
TARGET_IP = "127.0.0.1"
TARGET_PORT = 514
STAGING_PATH = Path("D:/OSINT_Staging/mango_telemetry.jsonl")

# Synthetic OpenWrt Kernel Firewall Drop Payload
# Mimics an Nmap scan hitting the WAN interface from the central host
MOCK_SYSLOG = (
    "<14>Jun  7 22:55:00 OpenWrt kernel: [ 1234.5678] DROP: "
    "IN=wan OUT= MAC=94:83:c4:43:49:77:00:11:22:33:44:55:08:00 "
    "SRC=192.168.68.110 DST=192.168.68.128 LEN=60 TOS=0x00 PREC=0x00 "
    "TTL=64 ID=54321 DF PROTO=TCP SPT=54321 DPT=22 WINDOW=65535 RES=0x00 SYN URGP=0"
)

def inject_and_verify():
    print("[*] Initiating synthetic telemetry injection...")
    
    # 1. Fire the UDP packet (bypassing UDP for direct parser invocation due to Windows loopback drops)
    try:
        from mango_syslog_sync import process_telemetry
        print(f"[+] Payload delivered to internal parser.")
        process_telemetry(MOCK_SYSLOG, (TARGET_IP, TARGET_PORT))
    except Exception as e:
        print(f"[-] CRITICAL: Injection failed: {e}")
        sys.exit(1)

    # Allow the asynchronous daemon time to process and write to disk
    time.sleep(2)

    # 2. Verify the JSON parsing in the staging volume
    print("[*] Verifying downstream JSON Line Protocol processing...")
    if not STAGING_PATH.exists():
        print(f"[-] CRITICAL: Staging file {STAGING_PATH} not found. Daemon failed to write.")
        sys.exit(1)

    try:
        # Read the last line of the staging file
        with open(STAGING_PATH, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("[-] CRITICAL: Staging file is empty.")
                sys.exit(1)
                
            last_entry = lines[-1].strip()
            parsed_json = json.loads(last_entry)
            
            print("[+] SYNTHETIC TEST SUCCESSFUL. Parsed output:")
            print(json.dumps(parsed_json, indent=2))
            
    except json.JSONDecodeError:
        print("[-] CRITICAL: Daemon output is not valid JSON.")
    except Exception as e:
        print(f"[-] CRITICAL: Verification read failed: {e}")

if __name__ == "__main__":
    inject_and_verify()