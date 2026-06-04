# Watchtower Dashboard Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the C2 dashboard to include Visual Telemetry (Plotly/Streamlit charts for ADB data) and a Unified Threat Timeline (aggregated Pandas DataFrame for all intelligence logs).

**Architecture:** We will refactor the `[ SENSORS & DIAGNOSTICS ]` expander to parse the raw stdout of `dumpsys battery` and `top` into structured metrics and charts. We will also add a new "Master Intelligence Ledger" section to the main interface that reads JSON and log files into a unified, sortable Pandas DataFrame.

**Tech Stack:** Python, Streamlit, Pandas, Regex.

---

### Task 1: Implement Visual Telemetry Parsing

**Files:**
- Modify: `C:\Users\Lance\Watchtower_Ops\watchtower_gui.py`

- [ ] **Step 1: Write telemetry parsing logic**
Add regex parsing for battery metrics and process tables to the top of the file (after `hex_to_ip`).

```python
import re

def parse_battery_data(raw_text):
    level = re.search(r'level:\s+(\d+)', raw_text)
    voltage = re.search(r'voltage:\s+(\d+)', raw_text)
    temp = re.search(r'temperature:\s+(\d+)', raw_text)
    return {
        "level": int(level.group(1)) if level else 0,
        "voltage": int(voltage.group(1)) / 1000 if voltage else 0.0,
        "temperature": int(temp.group(1)) / 10 if temp else 0.0
    }

def parse_top_data(raw_text):
    lines = raw_text.strip().split('\n')
    data = []
    start_idx = 0
    for i, line in enumerate(lines):
        if "PID" in line and "USER" in line:
            start_idx = i + 1
            break
            
    for line in lines[start_idx:]:
        parts = line.split()
        if len(parts) >= 9:
            try:
                pid = parts[0]
                cpu_idx = 8 if '%' not in parts[7] else 7 # Handle formatting variations
                cpu = float(parts[cpu_idx].replace('%', ''))
                name = parts[-1]
                data.append({"Process": name, "CPU %": cpu})
            except:
                continue
    return pd.DataFrame(data)
```

- [ ] **Step 2: Update UI rendering for Battery Metrics**
Locate the `dumpsys battery` execution block under `Extract Node Telemetry (HUD)` and replace `st.code(res.stdout.strip())` with:

```python
                    parsed_bat = parse_battery_data(res.stdout.strip())
                    c1, c2, c3 = st.columns(3)
                    c1.metric("Battery Level", f"{parsed_bat['level']}%")
                    c2.metric("Voltage", f"{parsed_bat['voltage']} V")
                    c3.metric("Temperature", f"{parsed_bat['temperature']} °C")
```

- [ ] **Step 3: Update UI rendering for Process Profile**
Locate the `top` execution block under `Profile Active Processes` and replace `st.code(res.stdout.strip())` with:

```python
                    df_proc = parse_top_data(res.stdout.strip())
                    if not df_proc.empty:
                        st.bar_chart(df_proc.set_index("Process"))
                    else:
                        st.warning("Could not parse process data.")
                        st.code(res.stdout.strip())
```

- [ ] **Step 4: Verify parsing syntax locally (Test)**

Run: `python -c "import watchtower_gui"`
Expected: Clean exit (no syntax errors).

- [ ] **Step 5: Commit changes**

```bash
git add watchtower_gui.py
git commit -m "feat: upgrade adb telemetry with visual metrics"
```

### Task 2: Implement Unified Threat Timeline

**Files:**
- Modify: `C:\Users\Lance\Watchtower_Ops\watchtower_gui.py`

- [ ] **Step 1: Write log aggregation logic**
Add this function before `render_tactical_hud()`:

```python
def get_unified_ledger():
    rows = []
    
    # 1. Watchtower_Log.json
    try:
        if os.path.exists("Watchtower_Log.json"):
            with open("Watchtower_Log.json", "r") as f:
                wt_data = json.load(f)
                for item in wt_data:
                    rows.append({
                        "Timestamp": item.get("timestamp", "N/A"),
                        "Source": "Watchtower Core",
                        "Target": item.get("target", item.get("ip", "N/A")),
                        "Details": item.get("binary", str(item.get("shodan", {})))
                    })
    except: pass

    # 2. C2_Activity.log
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                for line in f:
                    match = re.match(r'\[(.*?)\] \[(.*?)\] TARGET: (.*?) \| STATUS: .*? \| DETAILS: (.*)', line)
                    if match:
                        rows.append({
                            "Timestamp": match.group(1),
                            "Source": f"C2_{match.group(2)}",
                            "Target": match.group(3),
                            "Details": match.group(4)
                        })
    except: pass
    
    # 3. Gemini_Memory_Extraction.json
    try:
        if os.path.exists("Gemini_Memory_Extraction.json"):
            with open("Gemini_Memory_Extraction.json", "r", encoding="utf-8") as f:
                mem_data = json.load(f)
                for item in mem_data:
                    rows.append({
                        "Timestamp": item.get("created_at", "N/A"),
                        "Source": "Exocortex Memory",
                        "Target": "Global",
                        "Details": item.get("content", "N/A")
                    })
    except: pass

    if rows:
        df = pd.DataFrame(rows)
        # Handle sorting safely
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        df = df.sort_values(by="Timestamp", ascending=False).fillna("N/A")
        return df
    return pd.DataFrame()
```

- [ ] **Step 2: Inject Master Ledger Tab into UI**
Add this at the bottom of `render_tactical_hud()` before closing the function:

```python
    st.divider()
    st.subheader("📚 Master Intelligence Ledger")
    unified_df = get_unified_ledger()
    if not unified_df.empty:
        st.dataframe(unified_df, use_container_width=True, hide_index=True)
    else:
        st.warning("No intelligence logs found on disk.")
```

- [ ] **Step 3: Commit changes**

```bash
git add watchtower_gui.py
git commit -m "feat: integrate unified threat timeline ledger"
```