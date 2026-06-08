#!/bin/bash
set -euo pipefail

# Verify Docker container status and port bindings for the telemetry stack
echo "Scanning Watchtower Telemetry Containers..."
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}" | grep -E -i "grafana|influx" || echo "WARNING: Telemetry containers are not actively running."

# Output real-time resource allocation for the dashboard infrastructure
echo "Evaluating Telemetry Memory/CPU Load..."
docker stats --no-stream --format "table {{.Name}}\t{{.MemUsage}}\t{{.CPUPerc}}" | grep -E -i "grafana|influx"