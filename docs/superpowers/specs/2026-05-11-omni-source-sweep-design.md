# Design Doc: Omni-Source Global OSINT Sweep

**Date:** 2026-05-11
**Status:** Approved

## Overview
Implement a "Global OSINT Sweep" in the Watchtower C2 Dashboard that concurrently fires multiple OSINT extraction engines (bridges) against a single target. This provides a unified "barrage" of intelligence gathering instead of requiring individual manual runs.

## Architecture

### 1. Async Orchestrator (`run_omni_sweep`)
A new asynchronous function will be added to `watchtower_gui.py` to manage concurrent script execution.

- **Technology:** `asyncio` for non-blocking I/O.
- **Subprocess Management:** `asyncio.create_subprocess_exec` to run Python bridge scripts.
- **Error Handling:** Graceful handling of missing scripts or malformed JSON output from bridges.
- **Concurrency:** `asyncio.gather` to execute all scripts in parallel.

### 2. UI Integration (Hunt Matrix)
The "Autonomous Hunt" tab in the `Cognitive Engine` segment will be updated.

- **User Input:** A new option "Omni-Source Sweep (Global)" in the `Extraction Engine` select box.
- **Feedback:** A tactical spinner indicating the global barrage is in progress.
- **Results:** Dynamic expanders for each source, displaying:
    - **Header:** Source name (e.g., SHERLOCK, BREACH).
    - **Content:** Intelligence analysis if successful, or error messages.
    - **Raw Data:** JSON dump of the extracted intelligence (if available).

## Data Flow
1. **User Selection:** User chooses "Omni-Source Sweep (Global)" and enters target data.
2. **Action Trigger:** User clicks "Execute Autonomous Hunt".
3. **Orchestration:** `run_omni_sweep` is called via `asyncio.run`.
4. **Concurrent Execution:** Multiple bridge scripts (`osint_sherlock_bridge.py`, etc.) are launched.
5. **Data Collection:** Results are captured from `stdout` and parsed as JSON.
6. **UI Rendering:** Streamlit dynamic components render the results in the HUD.

## Test Plan
1. **Unit Test (Manual):** Verify individual bridges still work.
2. **Integration Test (Manual):** Execute Global Sweep with a test alias (e.g., "testuser").
3. **Verification:**
    - Check that multiple expanders appear.
    - Check that results appear concurrently or nearly so.
    - Verify error handling by temporarily renaming a bridge script.

## Security
- No API keys or credentials will be logged.
- Subprocess execution is limited to local bridge scripts.
