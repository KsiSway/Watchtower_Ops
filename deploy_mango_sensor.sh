#!/usr/bin/env bash
set -euo pipefail

# Watchtower Edge Sensor Deployment
# Target: 192.168.68.200 (Accessed via direct LAN wiretap)
# Note: Requires VPN status check only if executing external recon. This is local mesh manipulation.

readonly TARGET_LAN_IP="192.168.68.200"
readonly CENTRAL_HOST="192.168.68.110"

echo "[*] Initiating Max Info Protocol: Converting Mango into a transparent edge sensor..."

# UCI Payload: Merges firewall zones, maxes out log verbosity, sets UDP 514 target
readonly SENSOR_PAYLOAD="
uci set firewall.@zone[1].input='ACCEPT'
uci set firewall.@zone[1].forward='ACCEPT'
uci set system.@system[0].log_ip='${CENTRAL_HOST}'
uci set system.@system[0].log_port='514'
uci set system.@system[0].conloglevel='8'
uci commit firewall
uci commit system
/etc/init.d/firewall restart &
/etc/init.d/log restart &
exit
"

echo "[*] Pushing structural override to ${TARGET_LAN_IP}..."

ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no "root@${TARGET_LAN_IP}" "${SENSOR_PAYLOAD}" || true

echo "[+] Execution complete. WAN isolation dropped."
echo "[+] Verify your D:\OSINT_Staging\mango_telemetry.jsonl file in 60 seconds."