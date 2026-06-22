#!/usr/bin/env python3
# PROJECT WATCHTOWER: Native Gemini CLI (Hardened)
# Architecture: OptiPlex x64 Host -> Google Generative AI API

import google.generativeai as genai
import os
import sys
from dotenv import load_dotenv

# 1. Hardware/Authentication Verification via Secure .env
load_dotenv(r"D:\Watchtower_Ops\.env")
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("[!] FAULT: GEMINI_API_KEY missing from D:\\Watchtower_Ops\\.env")
    sys.exit(1)

genai.configure(api_key=API_KEY)

# 2. Engine Initialization
# Using 1.5 Flash for high-speed terminal I/O.
model = genai.GenerativeModel('gemini-1.5-flash') 
chat = model.start_chat(history=[])

print("[+] GEMINI TERMINAL ACTIVE. Streaming enabled.")
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
        response = chat.send_message(user_input, stream=True)
        
        # Stream chunks to terminal as they generate
        for chunk in response:
            print(chunk.text, end="", flush=True)
        print("\n")
        
    except KeyboardInterrupt:
        print("\n[*] Execution aborted by Operator.")
        break
    except Exception as e:
        print(f"\n[!] API FAULT: {e}")
