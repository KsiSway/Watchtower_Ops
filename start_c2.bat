@echo off
TITLE Watchtower C2 Dashboard
cd /d "D:\Watchtower_Ops"
echo [!] Starting Watchtower C2 Dashboard...
C:\Users\Lance\AppData\Local\Programs\Python\Python312\python.exe -m streamlit run watchtower_gui.py
pause
