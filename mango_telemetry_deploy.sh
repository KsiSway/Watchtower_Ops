#!/usr/bin/env bash
set -euo pipefail

# Watchtower Operations: Mango (GL-MT300N-V2) Telemetry Deployment
# Target: GL-MT300N-V2 (Mango Router) at 192.168.68.200
# Execution: Local terminal -> SSH into Mango

TARGET_IP="${1:-192.168.68.200}"
TARGET_USER="root"
WATCHTOWER_SYSLOG_IP="192.168.68.10" # Placeholder for Watchtower Brain IP
WATCHTOWER_SYSLOG_PORT="514"

echo "[*] Initiating OpenWrt UCI telemetry payload deployment to Mango router at $TARGET_IP"

ssh "$TARGET_USER@$TARGET_IP" << EOF
echo "[+] Connected to Mango device."

# 1. Configure Remote Syslog for Watchtower
echo "[*] Reconfiguring system logging to forward to Watchtower Brain ($WATCHTOWER_SYSLOG_IP)..."
uci set system.@system[0].log_ip='$WATCHTOWER_SYSLOG_IP'
uci set system.@system[0].log_port='$WATCHTOWER_SYSLOG_PORT'
uci set system.@system[0].log_remote='1'
uci commit system

# 2. Enable Firewall Drop Logging
echo "[*] Enabling telemetry for rejected/dropped packets on the firewall..."
uci set firewall.@defaults[0].drop_invalid='1'
uci set firewall.@defaults[0].log='1'
uci commit firewall

# 3. Enable Network Traffic Monitoring (nlbwmon if available)
echo "[*] Enabling nlbwmon traffic telemetry..."
if uci show nlbwmon >/dev/null 2>&1; then
    uci set nlbwmon.@nlbwmon[0].enable='1'
    uci set nlbwmon.@nlbwmon[0].commit_interval='1h'
    uci commit nlbwmon
    /etc/init.d/nlbwmon restart
else
    echo "[-] nlbwmon not found. Skipping traffic telemetry."
fi

echo "[+] Telemetry configuration committed successfully. Restarting services..."
/etc/init.d/log restart
/etc/init.d/firewall restart

echo "[+] Telemetry payload delivered. Mango metrics are now routing to Watchtower."
EOF
