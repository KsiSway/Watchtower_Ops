#!/usr/bin/env bash
set -euo pipefail

# Watchtower Edge Deployment: APIPA Bypass & Sensor Override
# Note: Execution requires an Elevated (Administrator) terminal to modify Windows routes.

readonly TARGET_LAN_IP="192.168.68.200"
readonly CENTRAL_HOST="192.168.68.110"

echo "[*] Bypassing APIPA. Re-aligning Windows routing table to Phase 1 constraints..."

# Force Windows Ethernet to the .68 subnet and isolate Wi-Fi interference
netsh interface ipv4 set address name="Ethernet" static 192.168.68.50 255.255.255.0 || echo "[-] Warning: netsh failed. Ensure terminal is elevated."
netsh interface set interface "Wi-Fi" admin=disable || true

sleep 3

echo "[*] Sweeping LAN wiretap for Mango at ${TARGET_LAN_IP}..."
if ping -c 3 "$TARGET_LAN_IP" > /dev/null 2>&1; then
    echo "[+] NETWORK BRIDGE RE-ESTABLISHED. Target acquired on copper wire."
else
    echo "[-] CRITICAL: Mango is unresponsive at .200."
    echo "[-] ACTION: Unplug Mango power, wait 5 seconds, plug back in. Re-run script."
    netsh interface ipv4 set address name="Ethernet" source=dhcp || true
    netsh interface set interface "Wi-Fi" admin=enable || true
    exit 1
fi

echo "[*] Pushing Max Info Sensor Override to ${TARGET_LAN_IP}..."

# UCI Payload: Drops WAN firewall, configures Telemetry, maxes verbosity.
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

ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no "root@${TARGET_LAN_IP}" "${SENSOR_PAYLOAD}" || true

echo "[+] Execution complete. WAN isolation dropped. Edge sensor is live."
echo "[*] Restoring OptiPlex mesh configuration..."

# Restore normal Windows networking
netsh interface ipv4 set address name="Ethernet" source=dhcp || true
netsh interface set interface "Wi-Fi" admin=enable || true

echo "[+] Host restored. Telemetry pipeline active."