import sys
import argparse
import socket
import struct

def wake_on_lan(macaddress):
    """ Switches on remote computers using WOL. """
    # Check macaddress format and try to separate it
    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 12 + 5:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, '')
    else:
        raise ValueError('Incorrect MAC address format')

    # Pad the synchronization stream.
    data = b'FFFFFFFFFFFF' + (macaddress * 20).encode()
    send_data = b''

    # Split up the hex values and pack.
    for i in range(0, len(data), 2):
        send_data += struct.pack('B', int(data[i: i + 2], 16))

    # Broadcast it to the network.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, ('255.255.255.255', 9))
    print(f"[+] Magic Packet Transmitted to {macaddress}")

def main():
    parser = argparse.ArgumentParser(description="Watchtower Xbox Node Controller")
    parser.add_argument("--wake", action="store_true", help="Deploy Wake-on-LAN packet")
    args = parser.parse_args()

    target_ip = "192.168.68.115" 
    target_mac = "D8-E2-DF-6D-94-DB" 

    if args.wake:
        try:
            wake_on_lan(target_mac)
            print(f"[+] Magic Packet deployed to {target_ip} [{target_mac}]")
        except Exception as e:
            print(f"[-] WOL Failed: {e}")
    else:
        # Simple ping check for status
        import subprocess
        res = subprocess.run(["ping", "-n", "1", "-w", "500", target_ip], capture_output=True)
        if res.returncode == 0:
            print(f"[*] Xbox Node ({target_ip}) Status: ONLINE")
        else:
            print(f"[*] Xbox Node ({target_ip}) Status: OFFLINE (Standby Mode)")

if __name__ == "__main__":
    main()
