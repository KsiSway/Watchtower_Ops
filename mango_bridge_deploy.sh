#!/usr/bin/env bash
set -euo pipefail

# Watchtower Operations: Mango (GL-MT300N-V2) Network Bridge Deployment
# Target: GL-MT300N-V2 (Mango Router)
# Execution: Local terminal -> SSH into Mango

# Configure the target IP address of the unconfigured Mango router
TARGET_IP="${1:-192.168.8.1}" # 192.168.8.1 is the default IP for GL.iNet routers
TARGET_USER="root"

echo "[*] Initiating OpenWrt UCI payload deployment to Mango router at $TARGET_IP"

ssh "$TARGET_USER@$TARGET_IP" << 'EOF'
echo "[+] Connected to Mango device."

# 1. Migrate GL-MT300N-V2 to 192.168.68.200
echo "[*] Reconfiguring LAN IP address..."
uci set network.lan.ipaddr='192.168.68.200'
uci commit network

# 2. Disable DHCP
echo "[*] Disabling DHCP server on LAN interface..."
uci set dhcp.lan.ignore='1'
uci commit dhcp

# 3. Enforce Dropbear SSH hardening
echo "[*] Enforcing Dropbear SSH key-only authentication..."
uci set dropbear.@dropbear[0].PasswordAuth='off'
uci set dropbear.@dropbear[0].RootPasswordAuth='off'
uci commit dropbear

echo "[+] Configuration committed successfully. Restarting services..."
/etc/init.d/dnsmasq restart
/etc/init.d/dropbear restart

# Restarting the network will drop the connection
echo "[!] Applying network changes. Connection will be severed."
/etc/init.d/network restart >/dev/null 2>&1 &
exit
EOF

echo "[+] Bridge deployment payload delivered."
echo "[-] Access the Mango router at its new address: 192.168.68.200"
