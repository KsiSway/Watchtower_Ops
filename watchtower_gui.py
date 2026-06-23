import streamlit as st

# [Antigravity Dispatch]: Hardened OSINT Engine Execution Block
# Injecting into Tab 2 (OSINT Engine section)

st.subheader("Sherlock Digital Footprint Sweep")

# 1. Generate the UI input specifically for the target alias
target_username = st.text_input("Enter Target Alias (Username):", placeholder="e.g., Ksisway")

# 2. Map the execution button to the UI
if st.button("Execute Sherlock Sweep", use_container_width=True):
    if not target_username:
        st.warning("Please enter a target username before initiating the sweep.")
    else:
        with st.status(f"Tracking footprint for {target_username}...", expanded=True) as status:
            import sys
            import subprocess
            import os
            
            script_path = r"D:\Watchtower_Ops\osint_sherlock.py"
            
            if not os.path.exists(script_path):
                st.error(f"[!] FAULT: Payload missing at {script_path}")
            else:
                try:
                    # 15-second circuit breaker actively protecting the OptiPlex CPU
                    result = subprocess.run(
                        [sys.executable, script_path, target_username], 
                        capture_output=True, 
                        text=True,
                        timeout=15 
                    )
                    
                    if result.returncode != 0:
                        st.error(f"Execution Fault:\n{result.stderr}")
                    else:
                        st.code(result.stdout)
                        
                except subprocess.TimeoutExpired:
                    st.error("[!] TIMEOUT: Sweep exceeded 15 seconds. Target node unresponsive. Thread severed.")
                    
            status.update(label="Sweep Complete", state="complete")
