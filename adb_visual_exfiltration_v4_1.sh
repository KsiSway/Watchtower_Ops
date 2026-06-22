#!/bin/bash
set -euo pipefail

# PROJECT WATCHTOWER: Asynchronous Optical Exfiltration (V4.1 - Topology Corrected)
# Architecture: OptiPlex x64 Host -> Android Edge Nodes
# Target Subnet: 192.168.68.x

PAYLOAD_DIR="D:/Watchtower_Ops/Payloads/Visual_Intel"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# True Edge Nodes
S25_EDGE="192.168.68.109:5555"
TAB_A8="192.168.68.112:5555"

mkdir -p "$PAYLOAD_DIR"
echo "[*] INITIATING CONCURRENT OPTICAL EXFILTRATION ON 192.168.68.x MESH..."

# 1. Extraction Function with Root Toggle
extract_frame() {
    local NODE=$1
    local IS_ROOT=$2
    
    echo "[*] Bridging socket to $NODE..."
    adb connect "$NODE" > /dev/null
    
    if adb devices | grep -q "${NODE}.*device"; then
        SAFE_NODE_NAME="${NODE//:/_}"
        FILE_PATH="${PAYLOAD_DIR}/optical_tap_${SAFE_NODE_NAME}_${TIMESTAMP}.png"
        
        # 2. Prevent CRLF corruption while elevating privileges
        if [[ "$IS_ROOT" == "true" ]]; then
            adb -s "$NODE" exec-out su -c 'screencap -p' > "$FILE_PATH"
        else
            adb -s "$NODE" exec-out screencap -p > "$FILE_PATH"
        fi
        
        echo "[+] Frame extracted: $FILE_PATH"
    else
        echo "[!] WARNING: Connection to $NODE failed."
    fi
}

# 3. Execute concurrently and synchronize
extract_frame "$S25_EDGE" "false" &
extract_frame "$TAB_A8" "true" &

wait

echo "[*] EXFILTRATION CYCLE COMPLETE. Severing bridges."
adb disconnect "$S25_EDGE" > /dev/null
adb disconnect "$TAB_A8" > /dev/null
