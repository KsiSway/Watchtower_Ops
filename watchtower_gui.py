import streamlit as st
import requests
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

st.markdown("---")
st.subheader("V4 Intelligence Bridge (Local C2 -> Uvicorn)")

def stream_intelligence_bridge(target_prompt):
    url = "http://host.docker.internal:5050/stream_inference"
    payload = {"prompt": target_prompt}
    
    try:
        with requests.post(url, json=payload, stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    if decoded_line.startswith("data: "):
                        yield decoded_line.replace("data: ", "")
    except requests.exceptions.RequestException as e:
        yield f"[!] C2 IPC BRIDGE FAULT: {e}"

# UI Execution Trigger
user_input = st.text_input("Enter OSINT Query:")
if st.button("Transmit to V4 Engine"):
    with st.spinner("Establishing secure uplink..."):
        response_stream = stream_intelligence_bridge(user_input)
        st.write_stream(response_stream)
