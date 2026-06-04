---
name: mesh-specialist
description: High-velocity mesh reconnaissance, multimedia node control, and visual intelligence exfiltration. Use when the user needs to interrogate local network nodes (192.168.68.0/24), control IoT/Multimedia devices (TV, Fan, Xbox), or perform AI-driven analysis on exfiltrated node data.
---

# Mesh Specialist

This skill provides a unified command interface for Project Watchtower, specializing in mesh network operations and autonomous intelligence gathering.

## Core Capabilities

- **Mesh Reconnaissance**: Autonomous subnet sweeps, service interrogation, and mDNS hostname resolution.
- **Multimedia Command (C2)**: Remote control of Samsung TVs/Monitors, Smart Fans, and Xbox consoles.
- **Visual Intelligence**: Zero-footprint Android screencap exfiltration (S25 Edge, Tab A8) with Edge TPU classification and Tesseract OCR.
- **Cognitive Pipeline**: Automated alias footprint hunting (Sherlock) piped to local LLM (dolphin-llama3) for profile synthesis.

## Tactical Workflows

### 1. Mesh Interrogation
Use `recon_core.py` for full subnet baseline generation. For specific node interrogation, use `mesh_interrogate.py <IP>`. Hostname resolution is handled via `resolve_mesh.py`.

### 2. Multimedia Control
- **Samsung TV/Monitor**: Use `tv_weapon.py <CMD> <IP>`. Common commands: `KEY_POWER`, `KEY_VOLUP`, `KEY_VOLDOWN`.
- **Smart Fan**: Use `smartfan_bridge.py <IP> <POWER_ON|POWER_OFF>`.
- **Xbox**: Use `xbox_weapon.py` for status probing and WOL deployment.

### 3. Visual Intelligence Pipeline
1. **Exfiltration**: Capture node screens using `adb_wrapper.py`.
2. **Analysis**:
   - Run `osint_tpu_vision.py` for Edge TPU-based object classification.
   - Run `osint_ocr_engine.py` for hard text extraction.

### 4. Autonomous Alias Hunting
Use `osint_sherlock_bridge.py <alias>` to execute a multi-vector hunt (Sherlock + AIOHTTP fallbacks) and receive an AI-synthesized intelligence dossier.

## Node Reference
See [topology.md](references/topology.md) for a complete manifest of active mesh nodes and persistent device IDs.

## Troubleshooting
Verify local hardware status with `tpu_diagnostic.py` before initiating visual intelligence tasks.
