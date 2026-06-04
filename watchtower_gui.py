import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import json
import os
import re
import subprocess
import datetime
import time
import shodan
import asyncio
import networkx as nx
import matplotlib.pyplot as plt
import requests
import ipaddress
try:
    import psutil
    PSUTIL_AVAILABLE = True
except ImportError:
    PSUTIL_AVAILABLE = False
from dotenv import load_dotenv

st.set_page_config(page_title="Watchtower C2", page_icon="⚡", layout="wide")

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
    /* Glassmorphism tactical containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border: 1px solid rgba(0, 212, 255, 0.2) !important;
        background: linear-gradient(180deg, rgba(14, 17, 23, 0.9) 0%, rgba(20, 25, 35, 0.9) 100%) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Persistent Mobile Node IDs (mDNS / Paired)
S25_ID = "adb-R5CY53NEAAY-IYwX0h._adb-tls-connect._tcp"
TABA8_ID = "adb-R8YW40WRQLA-xrOfga._adb-tls-connect._tcp"

# Initialize Exocortex Environment
load_dotenv()
SHODAN_KEY = os.getenv("SHODAN_API_KEY")
api = shodan.Shodan(SHODAN_KEY)

# Define base path relative to this script for consistent path resolution
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "C2_Activity.log")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
CORAL_PYTHON = r"C:\Users\Lance\Coral_Env\Scripts\python.exe"
PYTHON_EXE = r"C:\Users\Lance\AppData\Local\Programs\Python\Python312\python.exe"
if not os.path.exists(REPORTS_DIR):
    os.makedirs(REPORTS_DIR)

async def secure_screencap_exfil(adb_id: str, local_output_path: str = "./staging_cap.png") -> dict:
    """Executes secure visual exfiltration with automated Privilege Escalation (Root Fallback)."""
    # Standard path for non-rooted nodes
    std_path = "/data/local/tmp/tactical_cap.png"
    # Fallback path for rooted Samsung nodes (Tab A8)
    root_path = "/sdcard/tactical_cap.png"
    
    try:
        # Step 0: Wake State Enforcement
        await asyncio.create_subprocess_exec("adb", "-s", adb_id, "shell", "input", "keyevent", "224")
        await asyncio.sleep(0.5) 
        
        # Step 1: Attempt Standard Exfiltration (Target: S25 Edge)
        cap_proc = await asyncio.create_subprocess_exec(
            "adb", "-s", adb_id, "shell", "screencap", "-p", std_path,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        await cap_proc.communicate()
        
        target_remote_path = std_path

        # Step 2: Automated Root Escalation (Target: Tab A8)
        if cap_proc.returncode != 0:
            # Use /sdcard/ for root vector to bypass Samsung SELinux restrictions
            root_cmd = f"su -c 'screencap -p {root_path} && chmod 777 {root_path}'"
            cap_root = await asyncio.create_subprocess_exec(
                "adb", "-s", adb_id, "shell", root_cmd,
                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )
            await cap_root.communicate()
            
            if cap_root.returncode != 0:
                return {"status": "error", "message": "Failed to capture screen (Standard and Root vectors both failed)."}
            target_remote_path = root_path

        # Step 3: Pull the clean binary file
        pull_proc = await asyncio.create_subprocess_exec(
            "adb", "-s", adb_id, "pull", target_remote_path, local_output_path,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        await pull_proc.communicate()
            
        # Step 4: Evidence Purge
        if target_remote_path == root_path:
            # Rooted path needs su to delete
            await asyncio.create_subprocess_exec("adb", "-s", adb_id, "shell", f"su -c 'rm {root_path}'")
        else:
            await asyncio.create_subprocess_exec("adb", "-s", adb_id, "shell", f"rm {std_path}")
        
        return {"status": "success", "file_path": local_output_path}
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

def log_activity(module, target, status, details=""):
    """Logs tactical activity to a local file using the user-defined format."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{module}] TARGET: {target} | STATUS: {status} | DETAILS: {details}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def send_discord_comms(content, image_url=None):
    """Relays tactical intelligence to Discord C2 channel."""
    webhook = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook: return
    payload = {"content": content}
    if image_url:
        payload["embeds"] = [{"image": {"url": image_url}}]
    try:
        requests.post(webhook, json=payload, timeout=5)
    except:
        pass

def hex_to_ip(hex_str):
    """Converts hex string from /proc/net/tcp to human-readable IP and port."""
    try:
        ip_hex, port_hex = hex_str.split(':')
        ip = ".".join(map(str, [int(ip_hex[i:i+2], 16) for i in range(6, -1, -2)]))
        port = int(port_hex, 16)
        return f"{ip}:{port}"
    except:
        return hex_str

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
    start_idx = -1
    for i, line in enumerate(lines):
        if "PID" in line and "USER" in line:
            start_idx = i + 1
            break
            
    if start_idx != -1:
        for line in lines[start_idx:]:
            parts = line.split()
            if len(parts) >= 9:
                try:
                    pid = parts[0]
                    cpu_idx = 8 if '%' not in parts[7] else 7 # Handle formatting variations
                    cpu = float(parts[cpu_idx].replace('%', ''))
                    name = parts[-1]
                    data.append({"Process": name, "CPU %": cpu})
                except (IndexError, ValueError):
                    continue
    return pd.DataFrame(data)

def render_system_health(container):
    """Renders live system telemetry and Watchtower jobs."""
    with container.container(border=True):
        if PSUTIL_AVAILABLE:
            st.markdown("### 🎛️ Core Telemetry")
            col1, col2, col3 = st.columns(3)
            col1.metric("CPU Usage", f"{psutil.cpu_percent()}%")
            col2.metric("RAM Usage", f"{psutil.virtual_memory().percent}%")
            col3.metric("Disk Usage", f"{psutil.disk_usage('/').percent}%")
            
            st.markdown("### ⚙️ Background Jobs (Watchtower)")
            jobs = []
            for p in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    if p.info['name'] in ['python.exe', 'python3', 'python'] and p.info['cmdline']:
                        cmd = " ".join(p.info['cmdline'])
                        if 'Watchtower_Ops' in cmd or 'watchtower' in cmd:
                            jobs.append({"PID": p.info['pid'], "Command": cmd})
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
            
            if jobs:
                st.dataframe(pd.DataFrame(jobs), use_container_width=True, hide_index=True)
            else:
                st.caption("No active Watchtower background jobs detected.")
        else:
            st.warning("`psutil` library is required for live system telemetry. Run `pip install psutil`.")

async def run_omni_sweep(target, active_scripts: list, lat_range=None, long_range=None):
    """Fires multiple OSINT bridges concurrently."""
    try:
        if ipaddress.ip_address(target).is_private:
            for drop in ["osint_shodan_bridge.py", "osint_zoomeye_bridge.py", "osint_crtsh_bridge.py", "osint_leakcheck_bridge.py"]:
                if drop in active_scripts:
                    active_scripts.remove(drop)
    except ValueError:
        pass
    
    async def run_script(script):
        if not os.path.exists(os.path.join(BASE_DIR, script)):
            return script, {"status": "error", "message": "Script not found locally."}
        
        args = ["python", os.path.join(BASE_DIR, script), target]
        if script == "osint_wigle_bridge.py":
            if lat_range:
                args.extend(["--lat", str(lat_range[0]), str(lat_range[1])])
            if long_range:
                args.extend(["--long", str(long_range[0]), str(long_range[1])])
                
        proc = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()
        try:
            return script, json.loads(stdout.decode())
        except:
            return script, {"status": "error", "message": "Parse failure.", "raw": stdout.decode()}

    tasks = [run_script(s) for s in active_scripts]
    return await asyncio.gather(*tasks)

def get_adb_telemetry():
    st.subheader("📱 S25 Edge Live Interrogation")
    cmd = f'adb -s {S25_ID} shell "cat /proc/net/tcp | grep 1F40"'
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()
        if output:
            lines = output.strip().split('\n')
            for line in lines:
                parts = line.split()
                if len(parts) > 3:
                    local = hex_to_ip(parts[1])
                    remote = hex_to_ip(parts[2])
                    state = parts[3]
                    
                    if state == "01": # ESTABLISHED
                        st.success(f"🔥 ACTIVE UPLINK: Connected to {remote}")
                    elif state == "0A": # LISTEN
                        st.info(f"📡 LISTEN MODE: Local port {local.split(':')[-1]} is open")
            
            with st.expander("Raw Socket Data"):
                st.code(output)
        else:
            st.warning("Uplink Dormant (Port 8000 not found).")
    except subprocess.CalledProcessError:
        st.error("ADB Bridge Offline or Device Unreachable.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

def render_topology():
    st.subheader("🕸️ Tactical Mesh Topology (192.168.68.x)")
    G = nx.Graph()
    
    # Define Nodes with service vector intelligence and manufacturer data
    nodes = {
        "Gateway (.1)": {"type": "Router", "services": "HTTP/S", "color": "#ff4b4b"},
        "OptiPlex (.110)": {"type": "Server", "services": "SSH(VULN)/SMB(BLK)/HTTP", "color": "#faca2b"},
        "S25 Edge (.109)": {"type": "Mobile", "services": "AWS Uplink (C2PA)", "color": "#00d4ff"},
        "Tab A8 (.112)": {"type": "Mobile/Root", "services": "ADB", "color": "#00d4ff"},
        "M7 Monitor (.101)": {"type": "Multimedia", "services": "Samsung/Cast (ONLINE)", "color": "#a29bfe"},
        "Node (.102)": {"type": "Multimedia", "services": "Cast", "color": "#a29bfe"},
        "Xbox (.115)": {"type": "Console", "services": "IIS/UPnP", "color": "#107c10"},
        "TPV Display (.100)": {"type": "Display", "services": "None", "color": "#54a0ff"},
        "Samsung Node (.103)": {"type": "IoT", "services": "None", "color": "#a29bfe"},
        "Research Node (.105)": {"type": "Workstation", "services": "None", "color": "#54a0ff"},
        "Cloud Node (.108)": {"type": "IoT", "services": "None", "color": "#54a0ff"},
        "Ring 1 (.116)": {"type": "Security", "services": "Surveillance", "color": "#ff9f43"},
        "Ring 2 (.117)": {"type": "Security", "services": "Surveillance", "color": "#ff9f43"},
        "Ring 3 (.118)": {"type": "Security", "services": "Surveillance", "color": "#ff9f43"},
        "Ring 4 (.119)": {"type": "Security", "services": "Surveillance", "color": "#ff9f43"},
        "Sat (.246)": {"type": "Mesh Satellite", "services": "HTTP/S", "color": "#ff7675"},
        "Sat (.248)": {"type": "Mesh Satellite", "services": "HTTP/S", "color": "#ff7675"},
        "Sat (.249)": {"type": "Mesh Satellite", "services": "HTTP/S", "color": "#ff7675"},
        "Sat (.250)": {"type": "Mesh Satellite", "services": "HTTP/S", "color": "#ff7675"}
    }
    
    for node, attr in nodes.items():
        G.add_node(node, **attr)
        if "Gateway" not in node:
            G.add_edge("Gateway (.1)", node)
        
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#0E1117')
    
    pos = nx.spring_layout(G, k=0.7, iterations=60)
    
    # Draw nodes with specific colors
    node_colors = [G.nodes[n]['color'] for n in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2000, alpha=0.9, ax=ax)
    nx.draw_networkx_edges(G, pos, edge_color='#4a4e69', width=2, alpha=0.5, ax=ax)
    
    # Draw labels with service metadata
    labels = {n: f"{n}\n[{G.nodes[n]['services']}]" if 'services' in G.nodes[n] else n for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=8, font_color='white', font_weight='bold', ax=ax)
    
    plt.axis('off')
    st.pyplot(fig)

def render_darkweb_intel(payload: dict):
    """Transforms raw Tor extraction payload into a tactical HUD."""
    
    with st.container(border=True):
        st.subheader("🕸️ Dark Web Intelligence Report")
        
        if payload.get("status") == "error":
            st.error(f"Uplink Failed: {payload.get('message')}")
            return
            
        intel = payload.get("intel", {})
        
        # 1. Live Metrics Grid (HUD)
        c1, c2, c3, c4 = st.columns(4)
        
        btc_count = len(intel.get("bitcoin_addresses", []))
        xmr_count = len(intel.get("monero_addresses", []))
        email_count = len(intel.get("emails", []))
        pgp_status = "DETECTED" if intel.get("pgp_keys_found") else "None"
        
        # Use delta to create visual 'live' indicators when targets are acquired
        c1.metric("BTC Vectors", btc_count, delta="Acquired" if btc_count > 0 else None, delta_color="off")
        c2.metric("XMR Vectors", xmr_count, delta="Acquired" if xmr_count > 0 else None, delta_color="off")
        c3.metric("Comms (Emails)", email_count, delta="Acquired" if email_count > 0 else None, delta_color="off")
        c4.metric("PGP Blocks", pgp_status)
        
        st.divider()

        # 2. Actionable Data Display (Tabbed formatting)
        if btc_count > 0 or xmr_count > 0 or email_count > 0:
            st.markdown("### 🎯 Target Manifest")
            
            tab_btc, tab_xmr, tab_email = st.tabs(["Bitcoin", "Monero", "Emails"])
            
            with tab_btc:
                if btc_count > 0:
                    st.dataframe(pd.DataFrame(intel["bitcoin_addresses"], columns=["BTC Addresses"]), use_container_width=True, hide_index=True)
                else:
                    st.caption("No Bitcoin signatures detected.")
                    
            with tab_xmr:
                if xmr_count > 0:
                    st.dataframe(pd.DataFrame(intel["monero_addresses"], columns=["XMR Addresses"]), use_container_width=True, hide_index=True)
                else:
                    st.caption("No Monero signatures detected.")
                    
            with tab_email:
                if email_count > 0:
                    st.dataframe(pd.DataFrame(intel["emails"], columns=["Extracted Emails"]), use_container_width=True, hide_index=True)
                else:
                    st.caption("No email vectors detected.")

        # 3. Raw Source Snippet 
        with st.expander("View Raw Source Snippet"):
            st.code(payload.get("data", ""), language="html")

def get_unified_ledger():
    rows = []
    
    # 1. Watchtower_Log.json
    wt_path = os.path.join(BASE_DIR, "Watchtower_Log.json")
    try:
        if os.path.exists(wt_path):
            with open(wt_path, "r", encoding="utf-8") as f:
                wt_data = json.load(f)
                for item in wt_data:
                    rows.append({
                        "Timestamp": item.get("timestamp", "N/A"),
                        "Source": "Watchtower Core",
                        "Target": item.get("target", item.get("ip", "N/A")),
                        "Details": item.get("binary", str(item.get("shodan", {})))
                    })
    except (FileNotFoundError, json.JSONDecodeError): pass

    # 2. C2_Activity.log
    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    match = re.match(r'\[(.*?)\] \[(.*?)\] TARGET: (.*?) \| STATUS: .*? \| DETAILS: (.*)', line)
                    if match:
                        rows.append({
                            "Timestamp": match.group(1),
                            "Source": f"C2_{match.group(2)}",
                            "Target": match.group(3),
                            "Details": match.group(4)
                        })
    except Exception: pass
    
    # 3. Gemini_Memory_Extraction.json
    mem_path = os.path.join(BASE_DIR, "Gemini_Memory_Extraction.json")
    try:
        if os.path.exists(mem_path):
            with open(mem_path, "r", encoding="utf-8") as f:
                mem_data = json.load(f)
                for item in mem_data:
                    rows.append({
                        "Timestamp": item.get("created_at", "N/A"),
                        "Source": "Exocortex Memory",
                        "Target": "Global",
                        "Details": item.get("content", "N/A")
                    })
    except (FileNotFoundError, json.JSONDecodeError): pass

    if rows:
        df = pd.DataFrame(rows)
        # Handle sorting safely
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
        df = df.sort_values(by="Timestamp", ascending=False)
        df['Timestamp'] = df['Timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S').fillna("N/A")
        df = df.fillna("N/A")
        return df
    return pd.DataFrame()

def search_internal_ledger(query, ledger_df):
    if query.strip() == "" or ledger_df.empty:
        return pd.DataFrame()
    # Search across Target and Details columns
    mask = ledger_df.apply(lambda row: query.lower() in str(row['Target']).lower() or query.lower() in str(row['Details']).lower(), axis=1)
    return ledger_df[mask].head(5)

def search_network_mesh(query):
    baseline_path = os.path.join(BASE_DIR, "Watchtower_Final_Baseline.csv")
    if not os.path.exists(baseline_path):
        return pd.DataFrame()
    df = pd.read_csv(baseline_path)
    mask = df.apply(lambda row: query.lower() in str(row['IP']).lower() or query.lower() in str(row['MAC']).lower() or query.lower() in str(row['Vendor']).lower(), axis=1)
    return df[mask].head(5)

def search_live_processes(query):
    results = []
    nodes = [("S25 Edge", S25_ID), ("Tab A8", TABA8_ID)]
    for name, adb_id in nodes:
        try:
            # Use ps -A for comprehensive search, grep for the query
            cmd = f'adb -s {adb_id} shell "ps -A | grep -i {query}"'
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, timeout=3).decode()
            for line in output.strip().split('\n'):
                parts = line.split()
                if len(parts) >= 9:
                    results.append({
                        "Node": name,
                        "PID": parts[1],
                        "Process": parts[-1]
                    })
        except:
            continue
    return pd.DataFrame(results).head(5)

def render_tactical_hud():
    """Renders the high-density Global Command Matrix."""
    st.title("⚡ Project Watchtower C2")
    st.divider()
    
    # --- Top-Level Metrics ---
    h1, h2, h3, h4 = st.columns(4)
    h1.metric("VPN UPLINK", "192.168.68.110", delta="SECURE")
    h2.metric("MESH LATENCY", "1.2ms", delta="18 Nodes")
    h3.metric("C2 LOAD", "0.4", delta="Nominal")
    h4.metric("INTEL", "142", delta="Records")
    st.divider()
    
    # --- Target Profiles & Timeline ---
    ca, cb = st.columns(2)
    with ca:
        st.subheader("🎯 Target Profiles")
        for t in [{"n": "Raynard", "r": "Ghost"}, {"n": "Ikaika", "r": "Architect"}]:
            st.info(f"{t['n']} - {t['r']}")
    with cb:
        st.subheader("⏳ Target Intelligence Timeline")
        st.markdown("""
        * **08:00** - Ghost (Raynard) detected on Mesh via mDNS.
        * **08:15** - Architect (Ikaika) deployed NIDS.
        * **09:30** - Threat footprint confirmed.
        """)
    st.divider()
    
    col_alpha, col_bravo, col_charlie = st.columns(3)
    
    # --- COLUMN 1: NODE CONTROL ---
    with col_alpha:
        st.subheader("📱 Target Nodes")
        with st.container(border=True):
            adb_target = st.radio("Select Target", ["S25 Edge", "Tab A8 [ROOT]"], horizontal=True)
            target_id = TABA8_ID if "Tab A8" in adb_target else S25_ID
            
            if st.button("Intercept Visual Feed", use_container_width=True):
                with st.spinner("Exfiltrating..."):
                    # Use asyncio.run() to trigger your async secure_screencap_exfil
                    st.session_state['last_capture'] = asyncio.run(secure_screencap_exfil(target_id))

    # --- COLUMN 2: COGNITIVE ENGINE ---
    with col_bravo:
        st.subheader("🧠 Cognitive Engine (Local AI)")
        with st.container(border=True):
            
            # Implement tabs to separate manual analysis from autonomous hunting
            tab_manual, tab_hunt, tab_chat, tab_doc = st.tabs(["Manual Analysis", "Autonomous Hunt", "Direct Uplink", "Doc Interrogator"])
            
            with tab_doc:
                st.markdown("**docling File Interrogator**")
                uploaded_doc = st.file_uploader("Upload Intel Document", type=["pdf", "txt", "md"])
                if st.button("Extract Data", use_container_width=True, key="doc_extract"):
                    if uploaded_doc:
                        st.info("Processing via Cognitive Core...")
                    else:
                        st.warning("Upload a document first.")

            with tab_manual:
                intel_vector = st.selectbox("Intelligence Vector", ["profile", "darkweb", "telemetry"])
                raw_data = st.text_area("Raw Intelligence Data", height=100)
                
                if st.button("Execute Cognitive Analysis", use_container_width=True):
                    with st.spinner("Processing via dolphin-llama3..."):
                        brain_path = os.path.join(BASE_DIR, "osint_brain.py")
                        brain_result = subprocess.run(
                            [PYTHON_EXE, brain_path, intel_vector, raw_data], 
                            capture_output=True, text=True
                        )
                        try:
                            brain_payload = json.loads(brain_result.stdout)
                            if brain_payload.get("status") == "success":
                                st.info(brain_payload.get("analysis"))
                            else:
                                st.error(brain_payload.get("message"))
                        except Exception as e:
                            st.error(f"Brain Error: {str(e)}")
                            
            with tab_hunt:
                st.markdown("### Select Intelligence Bridges")
                c1, c2, c3, c4 = st.columns(4)
                active_scripts = []
                if c1.checkbox("Sherlock"): active_scripts.append("osint_sherlock_bridge.py")
                if c1.checkbox("Maigret"): active_scripts.append("osint_maigret_bridge.py")
                if c1.checkbox("Holehe"): active_scripts.append("osint_holehe_bridge.py")
                if c2.checkbox("Shodan"): active_scripts.append("osint_shodan_bridge.py")
                if c2.checkbox("ZoomEye"): active_scripts.append("osint_zoomeye_bridge.py")
                if c2.checkbox("URLScan"): active_scripts.append("osint_urlscan_bridge.py")
                if c3.checkbox("crt.sh"): active_scripts.append("osint_crtsh_bridge.py")
                if c3.checkbox("Wayback"): active_scripts.append("osint_wayback_bridge.py")
                if c3.checkbox("LeakCheck"): active_scripts.append("osint_leakcheck_bridge.py")
                if c4.checkbox("Breach"): active_scripts.append("osint_breach_bridge.py")
                if c4.checkbox("WiGLE"): active_scripts.append("osint_wigle_bridge.py")
                if c4.checkbox("Brave"): active_scripts.append("osint_brave_bridge.py")

                target_input = st.text_input("Target Data", placeholder="Alias, Email, IP, Address, Phone, Domain, or BSSID")
                
                # Dynamic Geospatial Fields for WiGLE
                lat_range = None
                long_range = None
                if "osint_wigle_bridge.py" in active_scripts:
                    with st.expander("Geospatial Bounding Box (Optional)", expanded=True):
                        g_col1, g_col2 = st.columns(2)
                        lat_min = g_col1.number_input("Lat Min", value=0.0, format="%.6f")
                        lat_max = g_col1.number_input("Lat Max", value=0.0, format="%.6f")
                        long_min = g_col2.number_input("Long Min", value=0.0, format="%.6f")
                        long_max = g_col2.number_input("Long Max", value=0.0, format="%.6f")
                        
                        if lat_min != 0.0 or lat_max != 0.0:
                            lat_range = [lat_min, lat_max]
                        if long_min != 0.0 or long_max != 0.0:
                            long_range = [long_min, long_max]

                if st.button("Execute Multi-Vector Sweep", use_container_width=True):
                    if not target_input:
                        st.warning("Input valid target data.")
                    elif not active_scripts:
                        st.warning("Select at least one extraction engine.")
                    else:
                        with st.spinner(f"Initiating Sweep against '{target_input}'..."):
                            results = asyncio.run(run_omni_sweep(target_input, active_scripts, lat_range, long_range))
                            for script_name, payload in results:
                                with st.expander(f"Data Source: {script_name.replace('_bridge.py', '').replace('osint_', '').upper()}", expanded=False):
                                    if payload.get("status") == "success":
                                        st.success("Target footprint extracted and profiled.")
                                        st.info(payload.get("analysis", "Data extracted."))
                                        
                                        # Intercept JARM Hashes for Display
                                        if script_name in ["osint_shodan_bridge.py", "osint_zoomeye_bridge.py"]:
                                            raw_data = payload.get("raw_data") or [payload]
                                            for item in raw_data:
                                                if isinstance(item, dict) and item.get("jarm"):
                                                    st.metric(f"JARM Hash ({item.get('ip', 'Target')})", item.get("jarm"))

                                        # Intercept URLScan Visuals for Discord Payload
                                        if script_name == "osint_urlscan_bridge.py":
                                            records = payload.get("records", [])
                                            for r in records:
                                                if r.get("screenshot_url"):
                                                    send_discord_comms(f"URLScan Visual Snapshot: {target_input}", image_url=r.get("screenshot_url"))
                                                    break # Send top result

                                        if script_name == "osint_spiderfoot_bridge.py" and "intel" in payload:
                                            findings = payload["intel"].get("findings", {})
                                            if findings:
                                                df = pd.DataFrame(list(findings.items()), columns=["Intelligence Type", "Data Points"])
                                                st.dataframe(df, use_container_width=True, hide_index=True)
                                    else:
                                        st.error(payload.get("message", "Failure."))

            with tab_chat:
                st.caption("Unstructured dialogue with dolphin-llama3. Context is preserved for this session.")
                
                # Initialize chat memory if it doesn't exist
                if "chat_memory" not in st.session_state:
                    st.session_state.chat_memory = []

                # Render existing conversation history in the UI
                for message in st.session_state.chat_memory:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])

                # Handle new user input
                if user_prompt := st.chat_input("Initiate dialogue with local AI..."):
                    
                    # Display user message and append to memory
                    with st.chat_message("user"):
                        st.markdown(user_prompt)
                    st.session_state.chat_memory.append({"role": "user", "content": user_prompt})

                    # Transmit memory array to local Ollama daemon
                    with st.chat_message("assistant"):
                        with st.spinner("Processing..."):
                            payload = {
                                "model": "orca-mini:latest",
                                "messages": st.session_state.chat_memory,
                                "stream": False
                            }
                            try:
                                host_ip = "ollama" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
                                response = requests.post(f"http://{host_ip}:11434/api/chat", json=payload, timeout=300)
                                if response.status_code == 200:
                                    ai_response = response.json().get("message", {}).get("content", "")
                                    st.markdown(ai_response)
                                    # Append AI response to memory
                                    st.session_state.chat_memory.append({"role": "assistant", "content": ai_response})
                                else:
                                    st.error(f"Ollama API Error: HTTP {response.status_code}")
                            except Exception as e:
                                st.error(f"Connection failed. Is Ollama running in the tray? Error: {str(e)}")

    # --- COLUMN 3: MESH DEFENSE ---
    with col_charlie:
        st.subheader("🕸️ Mesh Defense")
        with st.container(border=True):
            st.caption("Passive ARP Tripwire via Tab A8 wlan0")
            if st.button("Deploy NIDS Sensor", use_container_width=True):
                with st.spinner("Sniffing Mesh..."):
                    trip_result = subprocess.run(
                        [PYTHON_EXE, "mesh_tripwire.py", TABA8_ID], 
                        capture_output=True, text=True
                    )
                    try:
                        trip_payload = json.loads(trip_result.stdout)
                        if trip_payload.get("status") == "success":
                            packets = [p['packet'] for p in trip_payload.get("telemetry", [])]
                            if packets:
                                st.dataframe(pd.DataFrame(packets, columns=["ARP Telemetry"]), use_container_width=True, hide_index=True)
                            else:
                                st.caption("No ARP broadcasts detected.")
                        else:
                            st.error(trip_payload.get("message"))
                    except json.JSONDecodeError:
                        st.error(f"[!] Subprocess failed to return JSON. Raw output:\n{trip_result.stdout}\n{trip_result.stderr}")
                        trip_payload = {"status": "error", "message": "OCR engine crashed. Check terminal logs."}
                    except Exception as e:
                        st.error(f"Tripwire parsing failed: {str(e)}")

    # --- VISUAL INTELLIGENCE FEED (LOWER SEGMENT) ---
    if 'last_capture' in st.session_state and st.session_state['last_capture'].get("status") == "success":
        st.divider()
        st.subheader("👁️ Visual Intelligence Feed")
        
        img_path = st.session_state['last_capture']['file_path']
        v_col1, v_col2, v_col3 = st.columns([1, 1, 1])
        
        with v_col1:
            st.image(img_path, caption="Raw Exfiltration")
            
        with v_col2:
            st.markdown("**Edge TPU Classification**")
            with st.status("Analyzing visual data via Edge TPU...", expanded=True) as status:
                model_dir = r"C:\Users\Lance\coral_test"
                model_path = os.path.join(model_dir, "imagenet_model.tflite")
                label_path = os.path.join(model_dir, "imagenet_labels.txt")
                
                if os.path.exists(model_path) and os.path.exists(label_path):
                    vision_res = subprocess.run([CORAL_PYTHON, os.path.join(BASE_DIR, "osint_tpu_vision.py"), img_path, model_path, label_path], capture_output=True, text=True)
                    try:
                        v_data = json.loads(vision_res.stdout)
                        if v_data.get("status") == "success":
                            for item in v_data.get("intel", []):
                                st.metric(f"Classification: {item['classification']}", f"{item['confidence']}%")

                            status.update(label="Vision Analysis Complete", state="complete")
                        else:
                            st.error(f"Vision Analysis Failed: {v_data.get('message')}")
                            status.update(label="Analysis Error", state="error")
                    except json.JSONDecodeError:
                        st.error("Failed to parse vision payload.")
                        status.update(label="Parsing Error", state="error")
                else:
                    st.warning("TPU Vision Models not found.")
                    status.update(label="Models Missing", state="error")
            
        with v_col3:
            st.markdown("**Tesseract OCR**")
            with st.spinner("Extracting hard text via Tesseract..."):
                is_docker = os.environ.get("DOCKER_ENV") == "true"
                
                if is_docker:
                    ocr_result = subprocess.run(
                        ["python3", os.path.join(BASE_DIR, "osint_ocr_engine.py"), img_path],
                        capture_output=True, text=True
                    )
                else:
                    # Convert Windows paths to WSL paths for Linux-based Tesseract execution
                    wsl_script = subprocess.check_output(["wsl", "wslpath", os.path.join(BASE_DIR, "osint_ocr_engine.py")]).decode().strip()
                    wsl_img = subprocess.check_output(["wsl", "wslpath", img_path]).decode().strip()
                    
                    ocr_result = subprocess.run(
                        ["wsl", "python3", wsl_script, wsl_img],
                        capture_output=True, text=True
                    )
                try:
                    ocr_payload = json.loads(ocr_result.stdout)
                    if ocr_payload.get("status") == "success":
                        extracted_text = ocr_payload.get("intel", [])
                        with st.expander("View Extracted Text", expanded=True):
                            for line in extracted_text:
                                st.code(line, language="text")
                    else:
                        st.error(f"OCR Engine Failure: {ocr_payload.get('message')}")
                except Exception as e:
                    st.error("Failed to parse OCR output.")

# --- SIDEBAR: TACTICAL COMMAND MATRIX ---
st.sidebar.title("⚡ OMEGA NODE C2")
st.sidebar.markdown("---")

with st.sidebar.expander("[ COMMAND & CONTROL ]", expanded=True):
    st.markdown("**Node Selection**")
    c2_node = st.radio("Select Target:", ["Bedroom TV (.114)", "S25 Edge (.109)", "M7 Monitor (.101)", "Smart Fan (.113)", "Xbox (.115)"])
    
    if "TV" in c2_node or "Monitor" in c2_node or "S25" in c2_node:
        if "Bedroom" in c2_node: target_ip = "192.168.68.114"
        elif "S25" in c2_node: target_ip = "192.168.68.109"
        else: target_ip = "192.168.68.101"
        
        tv_cmd = st.selectbox("Select Payload", ["KEY_POWER", "KEY_MUTE", "KEY_VOLUP", "KEY_VOLDOWN", "KEY_CHUP", "KEY_CHDOWN"])
        if st.button("Transmit Payload", use_container_width=True, key="tv_button"):
            with st.spinner(f"Transmitting to {target_ip}..."):
                try:
                    payload_path = os.path.join(BASE_DIR, "..", "tv_weapon.py")
                    res = subprocess.run([PYTHON_EXE, payload_path, tv_cmd, target_ip], capture_output=True, text=True)
                    if "DELIVERED" in res.stdout: 
                        st.toast("Uplink Successful", icon="📡")
                        log_activity("PAYLOAD_TRANSMIT", target_ip, "SUCCESS", tv_cmd)
                    else: 
                        st.toast("Uplink Failed", icon="⚠️")
                        log_activity("PAYLOAD_TRANSMIT", target_ip, "FAILURE", res.stdout.strip())
                    st.info(res.stdout)
                except Exception as e:
                    st.error(f"Module Error: {e}")
                    log_activity("PAYLOAD_TRANSMIT", target_ip, "ERROR", str(e))

    elif "Fan" in c2_node:
        target_ip = "192.168.68.113"
        fan_cmd = st.selectbox("Select Payload", ["POWER_ON", "POWER_OFF"])
        if st.button("Transmit Payload", use_container_width=True, key="fan_button"):
            with st.spinner(f"Transmitting to {target_ip}..."):
                try:
                    bridge_path = os.path.join(BASE_DIR, "mesh-specialist", "scripts", "smartfan_bridge.py")
                    res = subprocess.run([PYTHON_EXE, bridge_path, target_ip, fan_cmd], capture_output=True, text=True)
                    if "SUCCESS" in res.stdout: 
                        st.toast("Uplink Successful", icon="📡")
                        log_activity("FAN_CONTROL", target_ip, "SUCCESS", fan_cmd)
                    else: 
                        st.toast("Uplink Failed", icon="⚠️")
                        log_activity("FAN_CONTROL", target_ip, "FAILURE", res.stdout.strip())
                    st.info(res.stdout)
                except Exception as e:
                    st.error(f"Module Error: {e}")
                    log_activity("FAN_CONTROL", target_ip, "ERROR", str(e))

    elif "Xbox" in c2_node:
        st.info("Xbox Node (.115) identified. Status: ONLINE. Controller bridge active.")
        xbox_payload = os.path.join(BASE_DIR, "mesh-specialist", "scripts", "xbox_weapon.py")
        st.markdown("---")
        st.subheader("Xbox Node Control (192.168.68.115)")
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Probe Xbox Node Status", use_container_width=True):
                try:
                    res = subprocess.run(['python', xbox_payload], capture_output=True, text=True)
                    st.toast("Xbox Probe Complete", icon="🎮")
                    log_activity("XBOX_CONTROL", "192.168.68.115", "PROBE", res.stdout.strip())
                except Exception as e:
                    st.error(f"Execution Error: {e}")
                    log_activity("XBOX_CONTROL", "192.168.68.115", "ERROR", str(e))

        with col2:
            if st.button("Deploy WOL Packet (Xbox)", use_container_width=True):
                try:
                    res = subprocess.run(['python', xbox_payload, '--wake'], capture_output=True, text=True)
                    if "[+]" in res.stdout:
                        st.toast("WOL Packet Sent", icon="🚀")
                        log_activity("XBOX_CONTROL", "192.168.68.115", "SUCCESS", "WOL Packet Sent")
                    else:
                        st.toast("WOL Failed", icon="⚠️")
                        log_activity("XBOX_CONTROL", "192.168.68.115", "FAILURE", res.stdout.strip())
                except Exception as e:
                    st.error(f"Execution Error: {e}")
                    log_activity("XBOX_CONTROL", "192.168.68.115", "ERROR", str(e))

    if st.button("Sentry Video Feed", use_container_width=True):
        with st.spinner("Scanning for Receivers..."):
            try:
                sweep_path = os.path.join(BASE_DIR, "..", "cast_sweep.py")
                result = subprocess.run([PYTHON_EXE, sweep_path], capture_output=True, text=True)
                st.toast("Sentry Sweep Complete", icon="👁️")
            except Exception as e:
                st.error(f"Sentry Error: {e}")
                
    if st.button("Establish Root (Kali WSL)", use_container_width=True):
        subprocess.Popen(["cmd", "/c", "start", "powershell", "-NoExit", "-Command", "wsl -u root"])
        st.toast("Root terminal session initiated", icon="💀")

with st.sidebar.expander("[ SENSORS & DIAGNOSTICS ]"):
    st.markdown("**Diagnostic Target**")
    diag_target = st.radio("Select Target:", ["Tab A8 [ROOT]", "S25 Edge"], key="diag_rad", label_visibility="collapsed")
    diag_id = TABA8_ID if "Tab A8" in diag_target else S25_ID

    st.markdown("---")
    is_live = st.toggle("🟢 Enable Live Telemetry Feed (5s Polling)")
    
    if is_live:
        st.session_state['live_poll'] = True
    else:
        st.session_state['live_poll'] = False

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
                log_activity("TELEMETRY_EXFIL", diag_id, "ERROR", str(e))

    if st.button("Profile Active Processes", use_container_width=True):
        with st.spinner(f"Profiling {diag_target}..."):
            try:
                shell_cmd = "top -n 1 -m 15"
                if "Tab A8" in diag_target:
                    shell_cmd = f"su -c '{shell_cmd}'"
                
                res = subprocess.run(["adb", "-s", diag_id, "shell", shell_cmd], capture_output=True, text=True, timeout=15)
                st.success(f"Process Profile Acquired: {diag_target}")
                log_activity("PROCESS_PROFILE", diag_id, "SUCCESS", "Top 15 Processes")
                with st.expander("Active Process Ledger", expanded=True):
                    df_proc = parse_top_data(res.stdout.strip())
                    if not df_proc.empty:
                        st.bar_chart(df_proc.set_index("Process"))
                    else:
                        st.warning("Could not parse process data.")
                        st.code(res.stdout.strip())
            except Exception as e:
                st.error(f"Profile Failure: {e}")
                log_activity("PROCESS_PROFILE", diag_id, "ERROR", str(e))

    st.markdown("---")
    if st.button("Intercept Visual Feed (screencap)", use_container_width=True):
        with st.spinner(f"Extracting secure optical data from {diag_target}..."):
            try:
                img_path = os.path.join(BASE_DIR, "node_capture.png")
                # Execute async secure exfiltration
                res_exfil = asyncio.run(secure_screencap_exfil(diag_id, img_path))
                
                if res_exfil["status"] == "success":
                    st.success(f"Visual Exfiltration Complete: {diag_target}")
                    log_activity("VISUAL_EXFIL", diag_id, "SUCCESS", "Zero-footprint capture verified.")
                    st.image(img_path, use_container_width=True)
                    
                    # Handoff to TPU Vision Intelligence Vector
                    st.markdown("---")
                    st.subheader("👁️ TPU Vision Intelligence")
                    with st.status("Analyzing visual data via Edge TPU...", expanded=True) as status:
                        model_dir = r"C:\Users\Lance\coral_test"
                        model_path = os.path.join(model_dir, "imagenet_model.tflite")
                        label_path = os.path.join(model_dir, "imagenet_labels.txt")
                        
                        if os.path.exists(model_path) and os.path.exists(label_path):
                            vision_res = subprocess.run([CORAL_PYTHON, os.path.join(BASE_DIR, "osint_tpu_vision.py"), img_path, model_path, label_path], capture_output=True, text=True)
                            try:
                                v_data = json.loads(vision_res.stdout)
                                if v_data.get("status") == "success":
                                    for item in v_data.get("intel", []):
                                        st.metric(f"Classification: {item['classification']}", f"{item['confidence']}%")

                                    status.update(label="Vision Analysis Complete", state="complete")
                                    log_activity("TPU_VISION", diag_id, "SUCCESS", str(v_data.get("intel")))
                                else:
                                    st.error(f"Vision Analysis Failed: {v_data.get('message')}")
                                    status.update(label="Analysis Error", state="error")
                            except json.JSONDecodeError:
                                st.error("Failed to parse vision payload.")
                                st.code(vision_res.stdout)
                                status.update(label="Parsing Error", state="error")
                        else:
                            st.warning("TPU Vision Models not found in C:\\Users\\Lance\\coral_test")
                            status.update(label="Models Missing", state="error")
                    
                    # OCR Engine Integration
                    st.markdown("---")
                    st.markdown("### 👁️ Optical Character Recognition (Host CPU)")
                    with st.spinner("Extracting hard text via Tesseract..."):
                        is_docker = os.environ.get("DOCKER_ENV") == "true"
                        
                        if is_docker:
                            ocr_result = subprocess.run(
                                ["python3", os.path.join(BASE_DIR, "osint_ocr_engine.py"), img_path],
                                capture_output=True, text=True
                            )
                        else:
                            # Convert Windows paths to WSL paths for Linux-based Tesseract execution
                            wsl_script = subprocess.check_output(["wsl", "wslpath", os.path.join(BASE_DIR, "osint_ocr_engine.py")]).decode().strip()
                            wsl_img = subprocess.check_output(["wsl", "wslpath", img_path]).decode().strip()
                            
                            ocr_result = subprocess.run(
                                ["wsl", "python3", wsl_script, wsl_img],
                                capture_output=True, text=True
                            )
                        try:
                            ocr_payload = json.loads(ocr_result.stdout)
                            if ocr_payload.get("status") == "success":
                                extracted_text = ocr_payload.get("intel", [])
                                
                                # Display the extracted text arrays in a clean expander
                                with st.expander("View Extracted Text", expanded=True):
                                    for line in extracted_text:
                                        st.code(line, language="text")
                                log_activity("OCR_ENGINE", diag_id, "SUCCESS")
                            else:
                                st.error(f"OCR Engine Failure: {ocr_payload.get('message')}")
                                log_activity("OCR_ENGINE", diag_id, "FAILURE", ocr_payload.get("message"))
                        except Exception as e:
                            st.error("Failed to parse OCR output. Verify Tesseract host installation.")
                            log_activity("OCR_ENGINE", diag_id, "ERROR", str(e))
                else:
                    st.error(f"Optical extraction failed: {res_exfil['message']}")
                    log_activity("VISUAL_EXFIL", diag_id, "FAILURE", res_exfil['message'])
            except Exception as e:
                st.error(f"Process Error: {e}")
                log_activity("VISUAL_EXFIL", diag_id, "ERROR", str(e))

    st.markdown("---")
    st.markdown("**Local Hardware**")
    if st.button("Verify TPU Hardware Uplink", use_container_width=True):
        with st.spinner("Probing Google Coral Edge TPU hardware..."):
            try:
                res = subprocess.run([CORAL_PYTHON, os.path.join(BASE_DIR, "mesh-specialist", "scripts", "tpu_diagnostic.py")], capture_output=True, text=True)
                try:
                    data = json.loads(res.stdout)
                    if data.get("status") == "ONLINE":
                        st.success(f"🔥 TPU UPLINK ACTIVE: {data.get('hardware')}")
                        st.metric("Active TPU Nodes", data.get("active_nodes"))
                        with st.expander("Hardware Paths"):
                            st.json(data.get("paths", []))
                    else:
                        st.error(f"TPU OFFLINE: {data.get('error')}")
                except json.JSONDecodeError:
                    st.error("Hardware probe failure. Library or binary mismatch.")
                    st.code(res.stdout)
            except Exception as e:
                st.error(f"Diagnostic Error: {e}")

with st.sidebar.expander("[ LOGISTICS & DEPLOYMENT ]"):
    adb_target = st.radio("Select ADB Target", ["S25 Edge", "Tab A8"])
    adb_id = TABA8_ID if "Tab A8" in adb_target else S25_ID
    
    if st.button("Scan for ADB Devices", use_container_width=True):
        with st.spinner("Discovery initiated..."):
            try:
                adb_path = os.path.join(BASE_DIR, "mobile-forensics", "scripts", "adb_wrapper.py")
                result = subprocess.run([PYTHON_EXE, adb_path, "list"], capture_output=True, text=True, env={**os.environ, "ADB_TARGET": adb_id})
                st.info("Mobile Node Manifest")
                st.code(result.stdout)
                log_activity("ADB_DISCOVERY", adb_id, "COMPLETE")
            except Exception as e:
                st.error(f"ADB Error: {e}")
                log_activity("ADB_DISCOVERY", adb_id, "ERROR", str(e))

st.sidebar.markdown("---")
if st.sidebar.button("Execute Core Sweep", type="primary", use_container_width=True):
    with st.spinner("Executing recon_core.py..."):
        try:
            recon_path = os.path.join(BASE_DIR, "recon_core.py")
            result = subprocess.run([PYTHON_EXE, recon_path], capture_output=True, text=True)
            st.sidebar.success("Sweep Complete.")
            with st.sidebar.expander("View Terminal Output"):
                st.code(result.stdout)
        except Exception as e:
            st.sidebar.error(f"Execution Failure: {e}")

st.sidebar.markdown("---")
with st.sidebar.expander("[ INTELLIGENCE FRAMEWORKS ]", expanded=False):
    st.markdown("**SpiderFoot Node (Port 5001)**")
    sf_host = "spiderfoot" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
    sf_base_url = f"http://{sf_host}:5001"
    
    st.link_button("Open Dedicated Window", sf_base_url, use_container_width=True)
    if st.button("Embed OSINT Matrix", use_container_width=True):
        st.session_state['show_sf'] = True
    if st.button("Close OSINT Matrix", use_container_width=True):
        st.session_state['show_sf'] = False
        
    st.markdown("**SpiderFoot API Controls**")
    sf_target = st.text_input("SpiderFoot Target", placeholder="IP, Domain, Email...")
    if st.button("Start API Scan", use_container_width=True):
        if sf_target:
            with st.spinner(f"Initiating SpiderFoot scan on {sf_target}..."):
                try:
                    payload = {
                        "scanname": f"Watchtower_{sf_target}",
                        "scantarget": sf_target,
                        "usecase": "all",
                        "modulelist": "",
                        "typelist": ""
                    }
                    res = requests.post(f"{sf_base_url}/startscan", data=payload, timeout=5)
                    if res.status_code == 200:
                        st.success(f"Scan started successfully. ID: {res.text}")
                    else:
                        st.error(f"API Error: HTTP {res.status_code} - {res.text}")
                except Exception as e:
                    st.error(f"Connection failed: {e}")
        else:
            st.warning("Please provide a target.")
            
    if st.button("Stop Active Scans", use_container_width=True):
        with st.spinner("Halting SpiderFoot operations..."):
            try:
                list_res = requests.get(f"{sf_base_url}/scanlist", timeout=5)
                if list_res.status_code == 200:
                    scans = list_res.json()
                    active = [s for s in scans if isinstance(s, list) and len(s) > 3 and s[3] in ["RUNNING", "STARTING", "INITIALIZING"]]
                    if not active:
                        st.info("No active scans detected.")
                    else:
                        for s in active:
                            requests.get(f"{sf_base_url}/stopscan?id={s[0]}", timeout=5)
                        st.success(f"Successfully aborted {len(active)} active scan(s).")
                else:
                    st.error(f"API Error: HTTP {list_res.status_code}")
            except Exception as e:
                st.error(f"Connection failed: {e}")

    if st.button("Fetch Scan List", use_container_width=True):
        with st.spinner("Querying API..."):
            try:
                res = requests.get(f"{sf_base_url}/scanlist", timeout=5)
                if res.status_code == 200:
                    st.dataframe(res.json(), use_container_width=True)
                else:
                    st.error(f"API Error: HTTP {res.status_code}")
            except Exception as e:
                st.error(f"Connection failed: {e}")
    
    st.markdown("---")
    st.markdown("**Monitoring Node (Port 3000)**")
    st.link_button("Access Tactical Grafana Feed", "http://192.168.68.110:3000/dashboards", use_container_width=True, type="primary")
    if st.button("Embed Grafana Feed", use_container_width=True):
        st.session_state['show_grafana'] = True
    if st.button("Close Grafana Feed", use_container_width=True):
        st.session_state['show_grafana'] = False

# Render the Iframe in the main body if toggled
if st.session_state.get('show_sf', False):
    st.markdown("---")
    st.markdown("### 🕸️ SpiderFoot Tactical Intercept")
    sf_host = "spiderfoot" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
    components.iframe(f"http://{sf_host}:5001", height=900, scrolling=True)

# Render Grafana Iframe in the main body if toggled
if st.session_state.get('show_grafana', False):
    st.markdown("---")
    st.markdown("### 📊 Grafana Performance Feed")
    components.iframe("http://192.168.68.110:3000/dashboards?kiosk=tv", height=600, scrolling=True)

# --- MAIN INTERFACE: GLOBAL COMMAND MATRIX ---
tab_hud, tab_mesh, tab_osint, tab_ledger, tab_health = st.tabs(["⚡ HUD", "🕷️ MESH", "🎯 RECON", "📖 LEDGER", "🏥 HEALTH"])

with tab_hud:
    render_tactical_hud()

with tab_mesh:
    render_topology()
    st.divider()
    
    st.subheader("📡 Network Discovery Matrix")
    d1, d2, d3 = st.columns(3)
    with d1:
        if st.button("SSDP Sweep", use_container_width=True):
            with st.spinner("Broadcasting..."):
                res = subprocess.run([PYTHON_EXE, "ssdp_sweep.py"], capture_output=True, text=True)
                st.code(res.stdout)
        if st.button("mDNS Discovery", use_container_width=True):
            with st.spinner("Polling..."):
                res = subprocess.run([PYTHON_EXE, "mdns_discovery.py"], capture_output=True, text=True)
                st.code(res.stdout)
    with d2:
        if st.button("Tuya Local Keys", use_container_width=True):
            with st.spinner("Extracting..."):
                res = subprocess.run([PYTHON_EXE, "tuya_key_extractor.py"], capture_output=True, text=True)
                st.code(res.stdout)
        if st.button("Xbox Controller Bridge", use_container_width=True):
            with st.spinner("Probing Xbox..."):
                res = subprocess.run([PYTHON_EXE, "xbox_controller_bridge.py"], capture_output=True, text=True)
                st.code(res.stdout)
    with d3:
        if st.button("SmartThings Sync", use_container_width=True):
            with st.spinner("Syncing..."):
                res = subprocess.run([PYTHON_EXE, "discover_smartthings.py"], capture_output=True, text=True)
                st.code(res.stdout)
        if st.button("Fingerprint Mesh", use_container_width=True):
            with st.spinner("Fingerprinting..."):
                res = subprocess.run([PYTHON_EXE, "fingerprint_mesh.py"], capture_output=True, text=True)
                st.code(res.stdout)
                
    st.divider()
    
    mesh_col1, mesh_col2 = st.columns(2)
    with mesh_col1:
        if st.button("Initiate Fresh Mesh Sync (nmap)", use_container_width=True):
            with st.spinner("Synchronizing local mesh..."):
                sync_res = subprocess.run([PYTHON_EXE, os.path.join(BASE_DIR, "mesh_sync_skill.py")], capture_output=True, text=True)
                st.code(sync_res.stdout)
                if sync_res.returncode == 0:
                    st.success("Mesh synchronization complete.")
                    st.rerun()
    with mesh_col2:
        if st.button("Run Health Check (watchtower_sync.py)", use_container_width=True):
            with st.spinner("Probing mesh nodes..."):
                health_res = subprocess.run([PYTHON_EXE, os.path.join(BASE_DIR, "watchtower_sync.py")], capture_output=True, text=True)
                st.code(health_res.stdout)

with tab_ledger:
    st.subheader("📚 Master Intelligence Ledger")
    
    unified_df = get_unified_ledger()
    
    # Global Search & Filter Implementation
    col_search, col_filter = st.columns([3, 1])
    with col_search:
        search_query = st.text_input("🔍 Global Intelligence Search", placeholder="IP, Alias, Email, or Keyword...")
    with col_filter:
        source_filter = "All"
        if not unified_df.empty:
            sources = ["All"] + sorted(list(unified_df["Source"].unique()))
            source_filter = st.selectbox("📂 Filter by Source", sources)

    if search_query:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**Ledger Results**")
            res_ledger = search_internal_ledger(search_query, unified_df)
            if not res_ledger.empty:
                st.dataframe(res_ledger, use_container_width=True, hide_index=True)
            else:
                st.caption("No matches in ledger.")
        with col2:
            st.markdown("**Mesh Results**")
            res_mesh = search_network_mesh(search_query)
            if not res_mesh.empty:
                st.dataframe(res_mesh, use_container_width=True, hide_index=True)
            else:
                st.caption("No matches in mesh baseline.")
        with col3:
            st.markdown("**Live Process Results**")
            res_proc = search_live_processes(search_query)
            if not res_proc.empty:
                st.dataframe(res_proc, use_container_width=True, hide_index=True)
            else:
                st.caption("No matching processes found on mobile nodes.")
        st.divider()

    if not unified_df.empty:
        display_df = unified_df
        if source_filter != "All":
            display_df = display_df[display_df["Source"] == source_filter]
        st.dataframe(display_df, use_container_width=True, hide_index=True)
    else:
        st.warning("No intelligence logs found on disk.")

with tab_osint:
    st.subheader("🕵️ Tor Dark Web Interceptor")
    target_onion = st.text_input("Target Onion URL", placeholder="http://vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceob7chgoowv...onion")
    if st.button("Initiate Tor Extraction", use_container_width=True):
        with st.spinner("Routing via SOCKS5 Proxy (Port 9050)..."):
            try:
                # Call the fetcher bridge
                fetch_script = os.path.join(BASE_DIR, "deep-osint-expert", "scripts", "osint_tor_fetcher.py")
                fetch_res = subprocess.run([PYTHON_EXE, fetch_script, target_onion], capture_output=True, text=True)
                payload = json.loads(fetch_res.stdout)
                render_darkweb_intel(payload)
            except Exception as e:
                st.error(f"Uplink Error: {str(e)}")
                if 'fetch_res' in locals():
                    st.code(fetch_res.stdout)

with tab_health:
    st.subheader("🖥️ Local C2 System Health & Services")
    health_placeholder = st.empty()
    render_system_health(health_placeholder)

if st.session_state.get('live_poll', False):
    time.sleep(5)
    st.rerun()
