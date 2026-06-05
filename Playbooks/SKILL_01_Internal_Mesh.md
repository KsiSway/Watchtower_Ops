# SKILL: Internal Mesh Reconnaissance

## Objective
Map the active 192.168.68.x local subnet, identify live nodes, and log the footprint for intelligence ingestion.

## Execution Steps
1. Execute a fast ping sweep on the internal mesh: nmap -sn 192.168.68.0/24 -oG D:\Watchtower_Ops\mesh_sweep.txt
2. Parse the output to extract all live IP and MAC addresses.
3. Cross-reference findings against known assets (Gateway: .1, OptiPlex: .110, Tab A8: .52).
4. Output a strictly formatted summary table of all discovered rogue or unidentified hosts to the Operator.
