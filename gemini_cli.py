#!/usr/bin/env python3
# PROJECT WATCHTOWER: Native Gemini CLI (V4 Modernized)
# Architecture: OptiPlex x64 Host (.venv 3.12) -> Google GenAI SDK

import os
import sys
from dotenv import load_dotenv
from google import genai

# 1. Hardcode the absolute vault path to prevent ghost reads
env_path = r"D:\Watchtower_Ops\.env"
load_dotenv(dotenv_path=env_path, override=True)

# 2. Extract and aggressively sanitize the cryptographic signature
clean_key = os.environ.get("GEMINI_API_KEY", "").strip().strip('"').strip("'")

# Safety check
if not clean_key or "EXACT_KEY_HERE" in clean_key:
    print("[!] FAULT: Placeholder or missing key detected in .env vault.")
    sys.exit(1)

# 3. DIRECT INJECTION: Physically pass the sanitized variable into the engine
client = genai.Client(api_key=clean_key)

# 4. CAPEX PROTECTION: Enforce strict routing to the $0.00 free-tier model
chat = client.chats.create(model='gemini-3.1-flash-lite')

print("[+] GEMINI TERMINAL ACTIVE (Unified V4 Architecture).")
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
