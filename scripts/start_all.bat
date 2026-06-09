@echo off
TITLE Watchtower Tactical Startup
cd /d "C:\Users\Lance\Watchtower_Ops"

echo [!] Launching Watchtower C2 Dashboard...
start "Watchtower C2" streamlit run watchtower_gui.py

echo [!] Launching SpiderFoot Intelligence Matrix...
cd spiderfoot
start "SpiderFoot" python sf.py -l 127.0.0.1:5001

echo [!] All tactical interfaces initialized.
timeout /t 5
