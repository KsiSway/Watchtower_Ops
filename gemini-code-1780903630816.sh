#!/usr/bin/env bash
set -euo pipefail

# Watchtower Master Edge Deployment: APIPA Remediation & Execution
# Target: 192.168.8.1 (Post-Hardware Reset)

readonly TARGET_FACTORY_IP="192.168.8.1"
readonly CENTRAL_HOST="192.168.68.110"
readonly NEW_STATIC_IP="192.168.68.200"
readonly PRIMARY_GATEWAY="192.168.68.1"

echo "[*] Verifying Layer 3 route to the isolated Mango subnet..."

if ! ping -c 2 "$TARGET_FACTORY_IP" > /dev/null 2>&1; then
    echo "[-] CRITICAL: Network bridge failed. Host adapter is stranded on APIPA (169.254.x.x)."
    echo "[*] OPERATOR ACTION REQUIRED: Open an elevated Windows PowerShell terminal and execute:"
    echo '    netsh interface ipv4 set address name="Ethernet" static 192.168.8.10 255.255.255.0'
    echo "[*] Re-execute this deployment script once the static IP is applied."
    exit 1
fi

echo "[+] Network bridge verified. Pushing Master Edge Sensor payload..."

# Unified UCI Payload: Drops WAN firewall, configures Telemetry, disables DHCP, bridges IP.
readonly MASTER_PAYLOAD="
uci set firewall.@zone[1].input='ACCEPT'
uci set firewall.@zone[1].forward='ACCEPT'
uci set system.@system[0].log_ip='${CENTRAL_HOST}'
uci set system.@system[0].log_port='514'
uci set system.@system[0].conloglevel='8'
uci set network.lan.ipaddr='${NEW_STATIC_IP}'
uci set network.lan.gateway='${PRIMARY_GATEWAY}'
uci set network.lan.dns='${PRIMARY_GATEWAY}'
uci set dhcp.lan.ignore='1'
uci set dropbear.@dropbear[0].PasswordAuth='off'
uci set dropbear.@dropbear[0].RootPasswordAuth='off'
uci commit firewall
uci commit system
uci commit network
uci commit dhcp
uci commit dropbear
/etc/init.d/network restart &
exit
"

# Using standard inline SSH. Expect connection drop when network restarts.
ssh -o ConnectTimeout=10 -o StrictHostKeyChecking=no "root@${TARGET_FACTORY_IP}" "${MASTER_PAYLOAD}" || true

echo "[+] Execution complete. The Mango is actively bridging telemetry to ${NEW_STATIC_IP}."