#!/usr/bin/env python3
# PROJECT WATCHTOWER: Native Gemini CLI (V4 Modernized)
# Architecture: OptiPlex x64 Host (.venv 3.12) -> Google GenAI SDK

from google import genai
import os
import sys
from dotenv import load_dotenv

# 1. Hardware/Authentication Verification via Secure .env
load_dotenv(r"D:\Watchtower_Ops\.env")
API_KEY = os.environ.get("GEMINI_API_KEY", "").strip().strip('"').strip("'")

if not API_KEY:
    print("[!] FAULT: GEMINI_API_KEY missing from D:\\Watchtower_Ops\\.env")
    sys.exit(1)

# 2. Engine Initialization (Modern Client Architecture)
client = genai.Client(api_key=API_KEY)
chat = client.chats.create(model='gemini-1.5-flash')

print("[+] GEMINI TERMINAL ACTIVE (V4 Architecture). Streaming enabled.")
print("[+] Type 'exit' or 'quit' to terminate.\n")

# 3. Persistent Execution Loop
while True:
    try:
        user_input = input("Operator> ")
        if user_input.strip().lower() in ['exit', 'quit']:
            print("[*] Severing connection...")
            break
        if not user_input.strip():
            continue
            
        print("Gemini> ", end="", flush=True)
        # Modern streaming method
        response = chat.send_message_stream(user_input)
        
        # Stream chunks to terminal as they generate
        for chunk in response:
            if chunk.text:
                print(chunk.text, end="", flush=True)
        print("\n")
        
    except KeyboardInterrupt:
        print("\n[*] Execution aborted by Operator.")
        break
    except Exception as e:
        print(f"\n[!] API FAULT: {e}")
