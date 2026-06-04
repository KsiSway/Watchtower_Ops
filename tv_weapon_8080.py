# Contingency: Watchtower_Ops/tv_weapon_8080.py
import asyncio
import websockets
import json
import base64
import sys

TARGET_IP = "192.168.68.103"
APP_NAME = base64.b64encode(b"Watchtower C2").decode('utf-8')
# Port 8080 variant
WS_URL = f"ws://{TARGET_IP}:8080/api/v2/channels/samsung.remote.control?name={APP_NAME}"

async def execute_pairing():
    print(f"[*] [Contingency] Initiating pairing sequence on port 8080...")
    try:
        async with websockets.connect(WS_URL, ping_interval=None) as websocket:
            while True:
                response = await websocket.recv()
                data = json.loads(response)
                if data.get("event") == "ms.channel.connect":
                    token = data.get("data", {}).get("token")
                    if token:
                        print(f"\n[+] PAIRING SUCCESSFUL (8080)")
                        with open("samsung_token.key", "w") as f: f.write(token)
                        break
                elif data.get("event") == "ms.channel.unauthorized":
                    print("\n[-] Pairing rejected on 8080.")
                    break
    except Exception as e:
        print(f"\n[-] 8080 failed: {str(e)}")

if __name__ == "__main__":
    asyncio.run(execute_pairing())
