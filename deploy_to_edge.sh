#!/bin/bash
set -euo pipefail

# Configuration
ADB_PATH="C:/adb/platform-tools/adb.exe"
REMOTE_DIR="/data/local/tmp/"

# Array of target ADB nodes
TARGETS=("adb-R5CY53NEAAY-IYwX0h._adb-tls-connect._tcp" "adb-R8YW40WRQLA-xrOfga._adb-tls-connect._tcp")

for TARGET in "${TARGETS[@]}"; do
    echo "Pushing to $TARGET..."
    "$ADB_PATH" -s "$TARGET" push "run_inference.py" "$REMOTE_DIR"
    "$ADB_PATH" -s "$TARGET" push "run_inference.sh" "$REMOTE_DIR"
    "$ADB_PATH" -s "$TARGET" shell "chmod +x ${REMOTE_DIR}run_inference.py"
    "$ADB_PATH" -s "$TARGET" shell "chmod +x ${REMOTE_DIR}run_inference.sh"
done

echo "Deployment complete."