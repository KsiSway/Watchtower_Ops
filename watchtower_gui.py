import streamlit as st

# [Antigravity Dispatch]: Hardened OSINT Engine Execution Block
# Injecting into Tab 2 (OSINT Engine section)

if st.button("Execute Digital Sweep"):
    with st.status("Searching digital footprint...", expanded=True) as status:
        import sys
        import subprocess
        import os
        
        script_path = r"D:\Watchtower_Ops\osint_sherlock.py"
        
        if not os.path.exists(script_path):
            st.error(f"[!] FAULT: Script missing at {script_path}")
        else:
            try:
                # ENFORCE STRICT LOCAL TIMEOUT: 15-second execution ceiling
                result = subprocess.run(
                    [sys.executable, script_path, username], 
                    capture_output=True, 
                    text=True,
                    timeout=15 
                )
                
                if result.returncode != 0:
                    st.error(f"Execution Fault:\n{result.stderr}")
                else:
                    st.code(result.stdout)
                    
            except subprocess.TimeoutExpired:
                st.error("[!] TIMEOUT: Sherlock sweep exceeded 15 seconds. Target node unresponsive. Thread severed to protect host CPU.")
                
        status.update(label="OSINT Sweep Complete", state="complete")
