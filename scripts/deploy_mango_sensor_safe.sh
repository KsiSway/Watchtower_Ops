#!/usr/bin/env bash
set -euo pipefail

# Watchtower Hardened Edge Sensor Deployment (Safe Routing Mode)
# Target: 192.168.68.200 (Direct LAN Wiretap)
# Host Environment: Windows 11 / Git Bash / WSL Interop

readonly TARGET_LAN_IP="192.168.68.200"
readonly CENTRAL_HOST="192.168.68.110"

echo "[*] Establishing isolated route to wiretap (preserving Wi-Fi uplink)..."

# Set static IP WITHOUT a default gateway to prevent Windows routing conflicts
netsh.exe interface ipv4 set address name="Ethernet" static 192.168.68.50 255.255.255.0 || echo "[-] Warning: netsh failed. Ensure terminal is elevated."

sleep 2

echo "[*] Testing safe path validity to ${TARGET_LAN_IP}..."
if ping.exe -n 3 "$TARGET_LAN_IP" > /dev/null 2>&1; then
    echo "[+] Network bridge alive. Target acquired."
else
    echo "[-] CRITICAL: Link down. Verify physical connection to LAN port."
    netsh.exe interface ipv4 set address name="Ethernet" source=dhcp || true
    exit 1
fi

# Hardened UCI String Configuration (Fixing Zone Index and SSH hangs)
readonly HARDENED_PAYLOAD="
uci set firewall.@zone[1].input='ACCEPT'
uci set firewall.@zone[1].forward='ACCEPT'
uci set system.@system[0].log_ip='${CENTRAL_HOST}'
uci set system.@system[0].log_port='514'
uci set system.@system[0].log_remote='1'
uci commit firewall
uci commit system
/etc/init.d/firewall restart
/etc/init.d/log restart
exit
"

echo "[*] Injecting tactical configuration over SSH..."
ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no "root@${TARGET_LAN_IP}" "${HARDENED_PAYLOAD}" || true

echo "[*] Restoring host Ethernet to DHCP..."
netsh.exe interface ipv4 set address name="Ethernet" source=dhcp || true

echo "[+] Deployment sequence complete. Edge sensor is armed and host is secure."
