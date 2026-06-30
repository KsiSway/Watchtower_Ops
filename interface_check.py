# [Environment: Python Virtual Environment]
from scapy.all import show_interfaces

print("[*] Interrogating Npcap/WinPcap for active interface bindings...")
print("[*] Locate the exact Name/Index of the physical adapter assigned to 192.168.68.110:\n")
show_interfaces()
