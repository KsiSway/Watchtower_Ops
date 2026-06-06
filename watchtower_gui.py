import streamlit as st
import subprocess
import os
import ipaddress
import shlex

st.set_page_config(page_title="Watchtower C2", layout="wide")

if "scan_status" not in st.session_state:
    st.session_state.scan_status = "IDLE"

# 1. Dynamic Targeting Computer (Sidebar)
with st.sidebar:
    st.title("Watchtower C2")
    st.markdown("---")
    st.header("Targeting Computer")
    
    target_range = st.text_input("Designate Target (IP/CIDR)", value="192.168.68.105")
    scan_profile = st.selectbox(
        "Execution Profile", 
        [
            "Stealth ACK Pierce (-sA)", 
            "Fast Ping Sweep (-sn)", 
            "Deep Fingerprint (-sV -p-)"
        ]
    )
    
    st.markdown("---")
    nav_selection = st.radio("Navigation", ["Mesh Matrix", "Airlock Logs"])

# 2. Expanded Intelligence Workspaces
if nav_selection == "Mesh Matrix":
    st.header("Network Intelligence Matrix")
    
    tab1, tab2, tab3 = st.tabs(["Active Recon", "Asset Ledger", "External OSINT (CVEs)"])
    
    with tab1:
        st.subheader("Tactical Execution")
        
        # Dynamic Payload Construction with Safe Execution
        if st.button(f"Initiate {scan_profile.split(' ')[0]} Sweep"):
            # OPSEC Safety Interlock
            try:
                if "/" in target_range:
                    ipaddress.ip_network(target_range, strict=False)
                else:
                    ipaddress.ip_address(target_range)
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
            cmd_args = ["nmap"] + shlex.split(active_flags) + [target_range, "-oN", "D:\\Watchtower_Ops\\dynamic_scan_results.txt"]
            subprocess.Popen(cmd_args) 
            st.rerun()

        # Automated Fragment Polling
        if st.session_state.scan_status == "SCANNING":
            st.warning(f"Executing {scan_profile} on {target_range} in background...")
            
            @st.fragment(run_every="3s")
            def poll_scan_status():
                if os.path.exists("D:\\Watchtower_Ops\\dynamic_scan_results.txt"):
                    st.session_state.scan_status = "COMPLETE"
                    st.rerun()
                    
            poll_scan_status()
                
        elif st.session_state.scan_status == "COMPLETE":
            st.success("Reconnaissance complete.")
            try:
                with open("D:\\Watchtower_Ops\\dynamic_scan_results.txt", "r") as f:
                    st.code(f.read(), language="text")
            except Exception as e:
                st.error(f"Read fault: {e}")
                
            if st.button("Clear Cache & Reset Target"):
                st.session_state.scan_status = "IDLE"
                if os.path.exists("D:\\Watchtower_Ops\\dynamic_scan_results.txt"):
                    os.remove("D:\\Watchtower_Ops\\dynamic_scan_results.txt")
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
