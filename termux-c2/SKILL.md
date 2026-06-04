---
name: termux-c2
description: Mobile node command and control via Termux. Executes background bash scripts and commands within the com.termux environment using ADB.
---

# Termux Command & Control (C2)

This skill enables remote tactical execution within the Termux environment on Android mobile nodes.

## Core Workflows

### 1. Remote Command Execution
Execute arbitrary bash commands inside the Termux environment.
- **Trigger:** "Run 'pkg upgrade' on S25 Edge" or "Check termux storage on Tab A8"
- **Implementation:** Wraps the command and executes it via the Termux bash binary using `adb shell`.

### 2. Background Script Dispatch
Upload and execute persistent scripts in the background.
- **Trigger:** "Start the surveillance script on device <ID> in background"
- **Implementation:** Pushes the script to the device, moves it to the Termux home directory, and executes it using `nohup`.

## Tactical Commands

| Action | Command |
| :--- | :--- |
| Run Command | `python scripts/termux_executor.py --device <SERIAL> --cmd "<BASH_CMD>"` |
| Run in Background | `python scripts/termux_executor.py --device <SERIAL> --cmd "<BASH_CMD>" --bg` |
| Upload & Run Script | `python scripts/termux_executor.py --device <SERIAL> --script <PATH_TO_SH>` |

## Termux Environment Specs
- **Bash Path:** `/data/data/com.termux/files/usr/bin/bash`
- **Home Dir:** `/data/data/com.termux/files/home/`
- **Binary Path:** `/data/data/com.termux/files/usr/bin/`

## Requirements
- Termux must be installed on the target node.
- ADB debugging must be enabled and authorized.
