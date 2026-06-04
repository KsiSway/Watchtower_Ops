import socket
import sys
import time

def send_payload(target_ip, command):
    port = 8080
    
    # Hex payloads extracted from your script
    payloads = {
        "POWER_ON": b"\xAA\x55\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
        "POWER_OFF": b"\xAA\x55\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    }

    if command not in payloads:
        print(f":: ERROR: UNKNOWN PAYLOAD '{command}'")
        return

    print(f":: TRANSMITTING {command} TO {target_ip}:{port}...")
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target_ip, port))
        s.send(payloads[command])
        s.close()
        print(f":: UPLINK SUCCESS. PAYLOAD DELIVERED.")
    except Exception as e:
        print(f":: UPLINK FAILED: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(":: USAGE: py smartfan_bridge.py [TARGET_IP] [COMMAND]")
        sys.exit(1)
        
    target_ip = sys.argv[1]
    command = sys.argv[2].upper()
    send_payload(target_ip, command)
