# [Environment: Python Virtual Environment]
from scapy.all import get_working_ifaces
import sys

def interrogate_interfaces():
    print("[*] Interrogating Windows NT Kernel for active Npcap interfaces...")
    print("[*] -----------------------------------------------------------")
    
    faces = get_working_ifaces()
    for face in faces:
        # Highlight the primary mesh interface if detected
        if face.ip == "192.168.68.110":
            print(f"[!] PRIMARY MESH NIC FOUND:")
            print(f"    Name: {face.name}")
            print(f"    Description: {face.description}")
            print(f"    MAC: {face.mac} | IP: {face.ip}\n")
        else:
            print(f"[-] Interface: {face.name} | IP: {face.ip} | Desc: {face.description}")

if __name__ == "__main__":
    interrogate_interfaces()