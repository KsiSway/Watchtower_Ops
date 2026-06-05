@echo off
powershell.exe -ExecutionPolicy Bypass -File "D:\Watchtower_Ops\sync_master.ps1"
echo The archive has been generated. Opening...        
start notepad "D:\Watchtower_Ops\Watchtower_Master_Context.md"
