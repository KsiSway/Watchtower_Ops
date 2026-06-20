#!/bin/bash
set -euo pipefail

echo "STATUS: PURGING ISOLATED SPIDERFOOT CONTAINER"
docker rm -f spiderfoot || true

echo "STATUS: REBUILDING C2 MESH WITH PERSISTENT VOLUME MAPPING"
# Ensure execution in the correct working directory
cd /D/Watchtower_Ops

# Tear down the broken mesh and rebuild with strict volume mapping
docker compose down
docker compose build --no-cache spiderfoot
docker compose up -d

echo "STATUS: MESH RESTORED. REFRESH STREAMLIT DASHBOARD."