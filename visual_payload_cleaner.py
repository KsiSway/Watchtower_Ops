#!/usr/bin/env python3
# PROJECT WATCHTOWER: Tactical Storage Scrubber
# Architecture: OptiPlex x64 Host -> Background Daemon

import os
import time
import logging

# --- TACTICAL CONFIGURATION ---
ARCHIVE_DIR = "D:/Watchtower_Ops/Payloads/Visual_Intel_Analyzed"
RETENTION_HOURS = 24
POLL_INTERVAL_SECONDS = 3600 # Sweep every 60 minutes
LOG_FILE = "D:/Watchtower_Ops/C2_Activity.log"

# Append to master C2 audit trail
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='[%(asctime)s] [STORAGE_PURGE] %(message)s')

def enforce_retention_policy():
    print(f"[*] INITIALIZING STORAGE RETENTION DAEMON (Limit: {RETENTION_HOURS} hours)")
    
    if not os.path.exists(ARCHIVE_DIR):
        print(f"[!] Target directory offline or unmounted: {ARCHIVE_DIR}")
        return

    while True:
        current_time = time.time()
        purged_count = 0
        
        for filename in os.listdir(ARCHIVE_DIR):
            filepath = os.path.join(ARCHIVE_DIR, filename)
            
            if os.path.isfile(filepath):
                # Calculate age in hours
                file_age_hours = (current_time - os.path.getmtime(filepath)) / 3600
                
                if file_age_hours > RETENTION_HOURS:
                    try:
                        os.remove(filepath)
                        purged_count += 1
                    except Exception as e:
                        logging.error(f"Failed to purge target {filename}: {e}")
        
        if purged_count > 0:
            msg = f"ACTION: PURGED {purged_count} STALE VISUAL PAYLOADS | REASON: EXCEEDED {RETENTION_HOURS}H CAP"
            logging.info(msg)
            print(f"[+] {msg}")
            
        # Hibernate thread until next cycle
        time.sleep(POLL_INTERVAL_SECONDS)

if __name__ == '__main__':
    try:
        enforce_retention_policy()
    except KeyboardInterrupt:
        print("\n[*] STORAGE SCRUBBER OFFLINE.")
