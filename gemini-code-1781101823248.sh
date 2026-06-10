#!/bin/bash
set -euo pipefail

# 1. Initialize OSINT ingestion CLI directly into the mounted Watchtower database
git clone https://github.com/smicallef/spiderfoot.git /D/WATCHTOWER_OSINT/spiderfoot
cd /D/WATCHTOWER_OSINT/spiderfoot
pip install -r requirements.txt

# 2. Verify native Python environment on OptiPlex before installing Kiro/Cursor orchestrators
python3 -m venv /D/Watchtower_Ops/.venv
source /D/Watchtower_Ops/.venv/bin/activate
pip install google-adk