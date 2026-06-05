# SKILL: Deep Service Enumeration (Dark Nodes)

## Objective
Pierce port filters and extract deep service fingerprints from unidentified dark nodes (.105, .108, .113, .120) and verify service status on .114.

## Targets
- Dark Nodes: 192.168.68.105, 192.168.68.108, 192.168.68.113, 192.168.68.120
- Verification Node: 192.168.68.114

## Execution Steps
1. Execute aggressive service detection and script scanning on dark nodes:
   nmap -sV -sC -Pn -p- --min-rate 1000 -oN D:\Watchtower_Ops\dark_nodes_deep_scan.txt 192.168.68.105,108,113,120
2. Verify lighttpd anomaly on .114:
   nmap -sV -Pn -p 8080 -oN D:\Watchtower_Ops\node_114_verification.txt 192.168.68.114
3. Parse fingerprints for specific versions (lighttpd, ssh, UPnP) and log to airlock.
4. Update the Mesh Intelligence ledger with corrected service states.
