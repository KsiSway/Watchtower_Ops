#!/bin/bash
set -euo pipefail

cd "/D/Watchtower_Ops"

echo "[*] INITIATING PHASE 1: Scanning scripts/ for legacy hardcoded root paths..."
# Expanded regex to capture D:\, D:/, /D/, and /d/ path variants
grep -rnE '(D:\\[Ww]atchtower_Ops|D:/[Ww]atchtower_Ops|/[Dd]/[Ww]atchtower_Ops)' "scripts/" || echo "[+] No internal script path anomalies detected."

echo -e "\n[*] INITIATING PHASE 2: Validating active Docker volume bridges..."
# Captures all volume mount definitions across all services in the compose file
grep -n -E "^\s+-\s+.*:" "docker-compose.yml" || echo "[-] WARNING: docker-compose.yml not found or contains no mounts."