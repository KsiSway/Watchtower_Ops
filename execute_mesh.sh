#!/bin/bash
set -euo pipefail

# Execute from within C:\Users\Lance\Watchtower_Ops\ (using WSL or Git Bash)

# 1. Deploy the receiver payload to the edge nodes
./deploy_to_edge.sh

# 2. Execute the C2 Orchestrator
python3 hybrid_inference.py