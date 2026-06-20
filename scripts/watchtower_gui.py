import streamlit as st
import subprocess
import os
import ipaddress
import shlex
import recon_datastore

st.set_page_config(page_title="Watchtower C2", layout="wide")

# Custom CSS for Global Header
st.markdown("""
    <style>
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        background-color: #f0f2f6;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Inject Header
with st.container():
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    st.subheader("Watchtower C2 Interface")
    global_search = st.text_input("Global Search", placeholder="Search ledger, mesh, or processes...")
    st.markdown('</div>', unsafe_allow_html=True)

if global_search:
    st.write(f"### Results for: {global_search}")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("#### 📋 Ledger")
        results = search_ledger(global_search)
        for item in results["data"]:
            st.info(item)
            
    with col2:
        st.write("#### 🌐 Mesh")
        results = search_mesh(global_search)
        for item in results["data"]:
            st.info(item)
            if st.button(f"Scan {item.split(': ')[-1]}", key=f"btn_{item}"):
                st.session_state.target_range = item.split(': ')[-1]
                st.rerun()
            
    with col3:
        st.write("#### ⚙️ Processes")
        results = search_processes(global_search)
        for item in results["data"]:
            st.info(item)

if "scan_status" not in st.session_state:
    st.session_state.scan_status = "IDLE"

# --- Search Orchestrators ---

def search_ledger(query):
    # Logic to query database
    return {"source": "Ledger", "data": [f"Result 1 for {query}", f"Result 2 for {query}"]}

def search_mesh(query):
    # Logic to query mesh nodes
    return {"source": "Mesh", "data": [f"Mesh node found: {query}"]}

def search_processes(query):
    # Logic to query processes
    return {"source": "Processes", "data": [f"Process found: {query}"]}

def execute_sherlock_sweep(target):
    """
    Capability Integration: Triggers osint_sherlock.py and logs to PostgreSQL.
    """
    try:
        # Executes the script inside the isolated Docker container
        cmd = ["python", "osint_sherlock.py", target, "--print-found"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Structure the raw output for the JSONB database column
        raw_data = {
            "status": "SUCCESS",
            "output": result.stdout
        }
        
        # Persist to the database using your established ledger
        recon_datastore.log_sweep(target, "Sherlock", raw_data)
        return raw_data
        
    except subprocess.CalledProcessError as e:
        error_data = {
            "status": "FAILED",
            "error": e.stderr
        }
        recon_datastore.log_sweep(target, "Sherlock", error_data)
        return error_data
with st.sidebar:
    st.title("Watchtower C2")
    st.markdown("---")
    st.header("Targeting Computer")
    
    # Initialize target_range in session_state if not present
    if "target_range" not in st.session_state:
        st.session_state.target_range = "192.168.68.105"
        
    target_range = st.text_input("Designate Target (IP/CIDR)", value=st.session_state.target_range)
    scan_profile = st.selectbox(
        "Execution Profile", 
        [
            "Stealth ACK Pierce (-sA)", 
            "Fast Ping Sweep (-sn)", 
            "Deep Fingerprint (-sV -p-)",
            "Sherlock (Digital Footprint)"
        ]
    )
    
    st.markdown("---")
    st.header("External Modules")
    st.markdown("[🕸️ SpiderFoot Bridge](http://127.0.0.1:5001)", unsafe_allow_html=True)
    
    st.markdown("---")
    nav_selection = st.radio("Navigation", ["Mesh Matrix", "Airlock Logs", "Cognitive Engine"])

# 2. Expanded Intelligence Workspaces
if nav_selection == "Mesh Matrix":
    st.header("Network Intelligence Matrix")
    
    tab1, tab2, tab3 = st.tabs(["Active Recon", "Asset Ledger", "External OSINT (CVEs)"])
    
    with tab1:
        st.subheader("Tactical Execution")
        
        # Dynamic Payload Construction with Safe Execution
        if st.button("Execute Sweep"):
            st.warning(f"STATUS: Initiating {scan_profile} against {target_range}...")
            
            if scan_profile == "Sherlock (Digital Footprint)":
                report = execute_sherlock_sweep(target_range)
                
                if report["status"] == "SUCCESS":
                    st.success("Sweep Complete. Intelligence committed to PostgreSQL ledger.")
                    st.text(report["output"])
                else:
                    st.error("Sweep Failed. Error committed to ledger.")
                    st.text(report["error"])
            else:
                # OPSEC Safety Interlock (RFC 1918 Airgap)
                try:
                    if "/" in target_range:
                        ip_obj = ipaddress.ip_network(target_range, strict=False)
                        is_private = ip_obj.is_private
                    else:
                        ip_obj = ipaddress.ip_address(target_range)
                        is_private = ip_obj.is_private
                        
                    if is_private:
                        st.error("[SECURITY INTERLOCK] Target is RFC 1918 internal. Deep External Scans Aborted.")
                        st.stop()
                        
                except ValueError:
                    st.error("[!] CRITICAL: Invalid IP or CIDR format. Execution aborted to prevent command injection.")
                    st.stop()

                st.session_state.scan_status = "SCANNING"
                
                flag_map = {
                    "Stealth ACK Pierce (-sA)": "-sA -Pn -p 22,80,443,8080,8443",
                    "Fast Ping Sweep (-sn)": "-sn",
                    "Deep Fingerprint (-sV -p-)": "-Pn -sV -sC -p-"
                }
                active_flags = flag_map[scan_profile]
                
                # Secure Subprocess Execution
                cmd_args = ["nmap"] + shlex.split(active_flags) + [target_range, "-oN", "/D/Watchtower_Ops/dynamic_scan_results.txt"]
                subprocess.Popen(cmd_args) 
                st.rerun()

        st.markdown("---")
        if st.button("Test Data Ingestion"):
            import recon_datastore
            try:
                recon_datastore.log_sweep(target_range, 'MANUAL_TEST', {'profile': scan_profile, 'status': 'SIMULATED'})
                st.success("Test record successfully ingested into PostgreSQL `recon_data.sweeps` table.")
            except Exception as e:
                st.error(f"Ingestion failed: {e}")

        # Automated Fragment Polling
        if st.session_state.scan_status == "SCANNING":
            st.warning(f"Executing {scan_profile} on {target_range} in background...")
            
            @st.fragment(run_every="3s")
            def poll_scan_status():
                if os.path.exists("/D/Watchtower_Ops/dynamic_scan_results.txt"):
                    st.session_state.scan_status = "COMPLETE"
                    st.rerun()
                    
            poll_scan_status()
                
        elif st.session_state.scan_status == "COMPLETE":
            st.success("Reconnaissance complete.")
            try:
                with open("/D/Watchtower_Ops/dynamic_scan_results.txt", "r") as f:
                    st.code(f.read(), language="text")
            except Exception as e:
                st.error(f"Read fault: {e}")
                
            if st.button("Clear Cache & Reset Target"):
                st.session_state.scan_status = "IDLE"
                if os.path.exists("/D/Watchtower_Ops/dynamic_scan_results.txt"):
                    os.remove("/D/Watchtower_Ops/dynamic_scan_results.txt")
                st.rerun()

    with tab2:
        st.subheader("Known Hardware Ledger")
        st.write("Future integration: SQLite database mapping MAC addresses to known devices.")
        
    with tab3:
        st.subheader("Vulnerability Cross-Referencing")
        st.write("Future integration: Automated Shodan API footprinting and CVE database mapping.")

elif nav_selection == "Airlock Logs":
    st.header("Airlock Operations")
    st.write("OSINT text artifacts and sync_master.ps1 output render here.")

elif nav_selection == "Cognitive Engine":
    st.header("AI Cognitive Engine (Ollama)")
    ai_query = st.text_area("Provide tactical inquiry:", height=150, placeholder="Analyze Shodan telemetry...")
    if st.button("Submit Query"):
        st.info("Query submitted to local Ollama framework (dolphin-llama3:latest).")
