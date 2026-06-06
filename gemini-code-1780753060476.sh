#!/usr/bin/env bash
set -euo pipefail

# Target Profiling: GL-MT300N-V2
readonly TARGET_SN="28fd19b83b24eca1"
readonly TARGET_MAC="94:83:C4:43:49:77"
readonly TARGET_IP="192.168.8.1"

echo "[*] Target Registered. S/N: ${TARGET_SN} | MAC: ${TARGET_MAC}"