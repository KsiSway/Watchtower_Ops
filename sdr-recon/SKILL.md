---
name: sdr-recon
description: Tactical SDR reconnaissance for RF spectrum analysis and ADS-B flight telemetry extraction. Use when the user needs to scan local radio frequencies or track aircraft via rtl_sdr and dump1090.
---

# SDR Reconnaissance Module

This skill provides tactical wrappers for Software Defined Radio (SDR) tools.

## Core Workflows

### 1. RF Spectrum Scanning
Use `scripts/sdr_telemetry.py` with `--mode scan` to capture raw radio data.
- **Trigger:** "Scan frequency 144.8MHz for 30 seconds"
- **Implementation:** Calls `rtl_sdr` to dump raw samples to a binary file for later analysis.

### 2. ADS-B Flight Tracking
Use `scripts/sdr_telemetry.py` with `--mode adsb` to initiate aircraft telemetry reception.
- **Trigger:** "Start aircraft tracking" or "Capture local flight data"
- **Implementation:** Launches `dump1090` in network mode to ingest Mode-S transponder signals.

## Tactical Commands

| Action | Command |
| :--- | :--- |
| Scan Frequency | `python scripts/sdr_telemetry.py --mode scan --freq <Hz> --duration <sec>` |
| Capture ADS-B | `python scripts/sdr_telemetry.py --mode adsb --duration <sec>` |

## Troubleshooting
- **Binary Missing:** If `rtl_sdr` or `dump1090` are not found, verify hardware connection and PATH environment.
- **Permissions:** Ensure current user has permission to access USB raw devices.
