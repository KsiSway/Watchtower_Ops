# Watchtower Dashboard Overhaul Phase 2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Overhaul the Watchtower C2 dashboard by injecting high-contrast custom CSS for tactical aesthetics, deploying a native Live Feed auto-refresh loop, and integrating an Omni-Source Global OSINT sweep.

**Architecture:** We will inject CSS via `st.markdown(unsafe_allow_html=True)` for button and metric styling. A native Streamlit loop (`st.rerun()`) will act as the live feed mechanism. An asynchronous subprocess orchestrator will be added to trigger all OSINT bridges concurrently when "Omni-Source Sweep" is selected.

**Tech Stack:** Python, Streamlit, Asyncio, CSS.

---

### Task 1: UI/UX Tactical CSS Overhaul

**Files:**
- Modify: `C:\Users\Lance\Watchtower_Ops\watchtower_gui.py`

- [ ] **Step 1: Write Custom CSS Injection**
Insert the following CSS injection right after `st.set_page_config(...)`.

```python
st.markdown("""
<style>
    /* Tactical Matrix Styling */
    .stButton > button {
        background-color: transparent !important;
        border: 1px solid #00d4ff !important;
        color: #00d4ff !important;
        transition: all 0.3s ease;
        box-shadow: 0 0 5px rgba(0, 212, 255, 0.2);
    }
    .stButton > button:hover {
        background-color: rgba(0, 212, 255, 0.1) !important;
        box-shadow: 0 0 15px rgba(0, 212, 255, 0.6);
        border-color: #00ffff !important;
        color: #ffffff !important;
    }
    div[data-testid="stMetricValue"] {
        color: #00ff00 !important;
        font-family: monospace;
        text-shadow: 0 0 10px rgba(0, 255, 0, 0.4);
    }
    div[data-testid="stMetricLabel"] {
        color: #a29bfe !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    hr {
        border-bottom: 1px solid #4a4e69 !important;
    }
</style>
""", unsafe_allow_html=True)
```

- [ ] **Step 2: Verify Syntax**
Run: `python -c "import watchtower_gui"`
Expected: Clean exit.

- [ ] **Step 3: Commit changes**
```bash
git add watchtower_gui.py
git commit -m "style: apply tactical cyber CSS overhaul"
```

### Task 2: Live Feed Mechanism

**Files:**
- Modify: `C:\Users\Lance\Watchtower_Ops\watchtower_gui.py`

- [ ] **Step 1: Add Live Feed toggle logic**
In the `[ SENSORS & DIAGNOSTICS ]` expander, right under `diag_id = TABA8_ID if "Tab A8" in diag_target else S25_ID`, add a toggle and a polling loop implementation:

```python
    import time
    st.markdown("---")
    is_live = st.toggle("🟢 Enable Live Telemetry Feed (5s Polling)")
    
    if is_live:
        st.session_state['live_poll'] = True
    else:
        st.session_state['live_poll'] = False
```

- [ ] **Step 2: Automate data extraction when live**
Update the "Extract Node Telemetry (HUD)" block. Instead of relying solely on `if st.button(...)`, allow the block to run if `st.session_state.get('live_poll')` is true.

```python
    # Locate the telemetry block and modify the condition:
    if st.button("Extract Node Telemetry (HUD)", use_container_width=True) or st.session_state.get('live_poll', False):
        with st.spinner(f"Extracting HUD from {diag_target}..."):
            try:
                shell_cmd = "dumpsys battery"
                if "Tab A8" in diag_target:
                    shell_cmd = f"su -c '{shell_cmd}'"
                
                res = subprocess.run(["adb", "-s", diag_id, "shell", shell_cmd], capture_output=True, text=True, timeout=15)
                # Only show success message and log if it was manually triggered to avoid log spam
                if not st.session_state.get('live_poll', False):
                    st.success(f"Telemetry Acquired: {diag_target}")
                    log_activity("TELEMETRY_EXFIL", diag_id, "SUCCESS", "HUD/Battery Data")
                    
                with st.expander("Node HUD Data", expanded=True):
                    parsed_bat = parse_battery_data(res.stdout.strip())
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Battery Level", f"{parsed_bat['level']}%")
                    c2.metric("Voltage", f"{parsed_bat['voltage']} V")
                    c3.metric("Temperature", f"{parsed_bat['temperature']} °C")
            except Exception as e:
                st.error(f"HUD Failure: {e}")
```

- [ ] **Step 3: Trigger the rerun**
At the very end of the `[ SENSORS & DIAGNOSTICS ]` expander block (or end of file), add the auto-refresh trigger:

```python
    # Add at the end of the expander block
    if st.session_state.get('live_poll', False):
        time.sleep(5)
        st.rerun()
```

- [ ] **Step 4: Commit changes**
```bash
git add watchtower_gui.py
git commit -m "feat: integrate live telemetry auto-refresh loop"
```

### Task 3: Omni-Source Global OSINT Sweep

**Files:**
- Modify: `C:\Users\Lance\Watchtower_Ops\watchtower_gui.py`

- [ ] **Step 1: Add Omni-Source to UI options**
Locate the `hunt_vector = st.selectbox(...)` under the "Autonomous Hunt" tab. Add `"Omni-Source Sweep (Global)"` to the top of the list.

- [ ] **Step 2: Write async orchestrator logic**
Add an async orchestrator function near the top of the file (e.g., after `parse_top_data`).

```python
async def run_omni_sweep(target):
    """Fires multiple OSINT bridges concurrently."""
    scripts = [
        "osint_sherlock_bridge.py",
        "osint_holehe_bridge.py",
        "osint_maigret_bridge.py",
        "osint_shodan_bridge.py",
        "osint_breach_bridge.py",
        "osint_urlscan_bridge.py"
    ]
    
    async def run_script(script):
        if not os.path.exists(os.path.join(BASE_DIR, script)):
            return script, {"status": "error", "message": "Script not found locally."}
        proc = await asyncio.create_subprocess_exec(
            "python", os.path.join(BASE_DIR, script), target,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        try:
            return script, json.loads(stdout.decode())
        except:
            return script, {"status": "error", "message": "Parse failure.", "raw": stdout.decode()}

    tasks = [run_script(s) for s in scripts]
    return await asyncio.gather(*tasks)
```

- [ ] **Step 3: Integrate Orchestrator into Hunt Button**
Locate the execution block `if st.button("Execute Autonomous Hunt"...):`. Modify the logic to handle the new "Omni-Source" vector:

```python
                if st.button("Execute Autonomous Hunt", use_container_width=True):
                    if not target_input:
                        st.warning("Input valid target data.")
                    else:
                        if "Omni-Source" in hunt_vector:
                            with st.spinner(f"Initiating Global Omni-Source Barrage against '{target_input}'..."):
                                results = asyncio.run(run_omni_sweep(target_input))
                                for script_name, payload in results:
                                    with st.expander(f"Data Source: {script_name.replace('_bridge.py', '').replace('osint_', '').upper()}", expanded=False):
                                        if payload.get("status") == "success":
                                            st.info(payload.get("analysis", "Data extracted."))
                                            # Dump raw intel if available
                                            if "intel" in payload:
                                                st.json(payload["intel"])
                                        else:
                                            st.error(payload.get("message", "Failure."))
                        else:
                            # Existing logic for individual scripts
                            with st.spinner(f"Deploying {hunt_vector.split(' ')[0]} against '{target_input}'..."):
                                # ... existing individual script execution code remains here ...
```
*(Ensure you preserve the existing `cmd = ["python"]` logic inside the `else:` block for individual executions).*

- [ ] **Step 4: Commit changes**
```bash
git add watchtower_gui.py
git commit -m "feat: deploy async omni-source global intel sweep"
```