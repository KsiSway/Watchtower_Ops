---
name: cognitive-analyst
description: AI-driven intelligence synthesis from dossiers and logs. Use when you need to perform tactical analysis on raw intelligence data (profile, darkweb, telemetry), generate persona summaries, or identify patterns in network logs using local LLMs.
---

# Cognitive Analyst

This skill leverages local LLMs (dolphin-llama3) to transform raw, unstructured data into actionable tactical intelligence.

## Core Capabilities

- **Intelligence Synthesis**: Analyzing raw dossiers, HTML snippets, and network logs via `osint_brain.py`.
- **Autonomous Profiling**: Mapping digital footprints and generating AI persona summaries via `osint_sherlock_bridge.py`.
- **Pattern Recognition**: Identifying anomalies in telemetry and log files.

## Intelligence Vectors

- **`profile`**: Use for synthesizing persona data from Sherlock/Maigret dossiers. Identifies traits, interests, and potential vulnerabilities.
- **`darkweb`**: Use for interpreting HTML data exfiltrated from Tor hidden services. Detects crypto addresses, PGP keys, and service types.
- **`telemetry`**: Use for analyzing network socket data and process logs. Detects unauthorized uplinks or suspicious process behavior.

## Workflow: Autonomous Hunt & Deep Profiling
1. **Standard Hunt**: Deploy the Sherlock Bridge via `osint_sherlock_bridge.py <alias>`. Fast mapping of digital footprint across 300+ platforms.
2. **Deep Profiling**: Deploy the Maigret Bridge via `osint_maigret_bridge.py <alias>`. Recursive biographical extraction and identity correlation.
3. **Email Mapping**: Deploy the Holehe Bridge via `osint_holehe_bridge.py <email>`. Mapping digital services linked to a target email.
4. **Synthesis**: All scripts automatically pipe dossiers to the Cognitive Brain for AI persona summaries.

## Data Integration
Synthesized intelligence should be referenced when updating the `GEMINI.md` project context or the private `MEMORY.md` index.
