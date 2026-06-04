---
name: mobile-forensics
description: Deep Android forensics, process profiling, and mobile node telemetry. Use when you need to interrogate Android nodes (S25 Edge, Tab A8), exfiltrate system logs, profile active processes, or perform secure optical captures via ADB.
---

# Mobile Forensics

This skill provides specialized procedures for interrogating and controlling Android nodes within the Watchtower mesh.

## Core Capabilities

- **Deep Interrogation**: Service-level interrogation of S25 and Tab A8 nodes via `interrogate_s25.py`.
- **Process Profiling**: Real-time profiling of active processes and memory load.
- **Telemetry Exfiltration**: Extraction of battery, network, and hardware HUD data.
- **Secure Visual Capture**: Zero-footprint `screencap` exfiltration with automated root escalation (Magisk).

## Tactical Workflows

### 1. Node Interrogation
- **S25 Edge**: Use `interrogate_s25.py` to map active socket connections and identify AWS/C2PA uplinks.
- **Generic ADB**: Use `adb_wrapper.py <ID> <CMD>` for raw shell execution.

### 2. Forensic Profiling
Execute process profiling via ADB shell commands (`top`, `ps`) to identify suspicious activity or high-load services on target nodes.

### 3. Mesh Tripwire
Deploy the Passive ARP Tripwire on the Tab A8 (Rooted) using `mesh_tripwire.py <ID>` to sniff physical MAC/IP announcements on the `wlan0` interface.

## Target Node Reference
- **S25 Edge**: `adb-R5CY53NEAAY-IYwX0h._adb-tls-connect._tcp`
- **Tab A8 [ROOT]**: `adb-R8YW40WRQLA-xrOfga._adb-tls-connect._tcp`
