#!/usr/bin/env bash
set -euo pipefail

# Watchtower Mango Recovery: Cryptographic Trust & Sensor Reconfiguration
# Target: 192.168.8.1 (Factory Default) -> 192.168.68.200 (Tactical IP)

readonly FACTORY_IP="192.168.8.1"
readonly TACTICAL_IP="192.168.68.200"
readonly CENTRAL_HOST="192.168.68.110"
readonly DEFAULT_PASS="goodlife"
readonly KEY_PATH="$HOME/.ssh/id_ed25519"

echo "[*] Phase 1: Validating Cryptographic Pair..."
if [ ! -f "$KEY_PATH" ]; then
    echo "[*] No ED25519 key found. Generating for OptiPlex..."
    ssh-keygen -t ed25519 -f "$KEY_PATH" -N "" -q
else
    echo "[+] Cryptographic pair verified: $KEY_PATH"
fi

echo "[*] Phase 2: Bridging to Factory Subnet..."
# Set static IP on Ethernet to talk to 192.168.8.1
netsh.exe interface ipv4 set address name="Ethernet" static 192.168.8.50 255.255.255.0 || echo "[-] Warning: netsh failed. Run as Admin."

echo "[!] ACTION: Press and hold Mango Reset button for 10 seconds NOW."
echo "[*] Waiting for heartbeat from ${FACTORY_IP}..."
until ping.exe -n 1 "$FACTORY_IP" > /dev/null 2>&1; do
    sleep 5
done
echo "[+] Target responsive. Waiting for SSH daemon (45s)..."
sleep 45

echo "[*] Phase 3: Planting Host Key in Dropbear Vault..."
# Attempt automated injection; if sshpass fails, manual password 'goodlife' required.
if command -v sshpass >/dev/null 2>&1; then
    sshpass -p "$DEFAULT_PASS" ssh-copy-id -i "${KEY_PATH}.pub" -o StrictHostKeyChecking=no "root@${FACTORY_IP}" || true
else
    echo "[!] sshpass not found. Prepare to enter password: ${DEFAULT_PASS}"
    ssh-copy-id -i "${KEY_PATH}.pub" -o StrictHostKeyChecking=no "root@${FACTORY_IP}"
fi

echo "[*] Phase 4: Pushing Hardened Sensor Payload..."
# Sanitized UCI configuration (Removed notebook path artifacts)
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

ssh -o BatchMode=yes -o StrictHostKeyChecking=no "root@${FACTORY_IP}" "${MASTER_PAYLOAD}" || echo "[-] Payload transmission failed. Verify Phase 3."

echo "[*] Phase 5: Restoring Host Environment..."
netsh.exe interface ipv4 set address name="Ethernet" source=dhcp || true

echo "[+] Sequence Complete. Mango is migrating to ${TACTICAL_IP}."
echo "[+] Verify connectivity via: ping ${TACTICAL_IP}"
