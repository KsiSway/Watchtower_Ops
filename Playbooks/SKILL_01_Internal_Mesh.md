# SKILL: Internal Mesh Reconnaissance

## Objective
Map the active 192.168.68.x local subnet, identify live nodes, and log the footprint for intelligence ingestion.

## Execution Steps
1. Execute a fast ping sweep on the internal mesh: nmap -sn 192.168.68.0/24 -oG D:\Watchtower_Ops\mesh_sweep.txt
2. Parse the output to extract all live IP and MAC addresses.
3. Cross-reference findings against known assets (Gateway: .1, OptiPlex: .110, Tab A8: .52).
4. Output a strictly formatted summary table of all discovered rogue or unidentified hosts to the Operator.
5. DEEP SERVICE ENUMERATION: For specific hardened rogue nodes, execute an aggressive full-port scan bypassing ICMP blocks:
   `nmap -Pn -p- -sV --version-intensity 5 -oN D:\Watchtower_Ops\deep_enumeration.txt 192.168.68.105 192.168.68.108 192.168.68.113 192.168.68.120`
