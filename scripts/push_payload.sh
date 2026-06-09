#!/usr/bin/env bash
set -euo pipefail

readonly FACTORY_IP="192.168.8.1"
readonly TACTICAL_IP="192.168.68.200"
readonly CENTRAL_HOST="192.168.68.110"

echo "[*] Phase 4: Pushing Hardened Sensor Payload..."
# Sanitized UCI configuration
readonly MASTER_PAYLOAD="
uci set firewall.@zone[1].input='ACCEPT'
uci set firewall.@zone[1].forward='ACCEPT'
uci set system.@system[0].log_ip='${CENTRAL_HOST}'
uci set system.@system[0].log_port='514'
uci set system.@system[0].log_remote='1'
uci set network.lan.ipaddr='${TACTICAL_IP}'
uci set network.lan.gateway='192.168.68.1'
uci set network.lan.dns='192.168.68.1'
uci set dhcp.lan.ignore='1'
uci set dropbear.@dropbear[0].PasswordAuth='off'
uci set dropbear.@dropbear[0].RootPasswordAuth='off'
uci commit firewall
uci commit system
uci commit network
uci commit dhcp
uci commit dropbear
/etc/init.d/network restart
exit
"

ssh -o BatchMode=yes -o StrictHostKeyChecking=no "root@${FACTORY_IP}" "${MASTER_PAYLOAD}" || echo "[-] Payload transmission failed."

echo "[*] Phase 5: Restoring Host Environment..."
netsh.exe interface ipv4 set address name="Ethernet" source=dhcp || true

echo "[+] Sequence Complete. Mango is migrating to ${TACTICAL_IP}."
echo "[+] Verify connectivity via: ping ${TACTICAL_IP}"
