import os
from dotenv import load_dotenv
from google import genai

# 1. Force reload and strip whitespace/quotes
load_dotenv(override=True)
raw_key = os.getenv('GEMINI_API_KEY', '').strip().strip('"').strip("'")
os.environ['GEMINI_API_KEY'] = raw_key

try:
    print(f'[+] Extracted Key Signature: {raw_key[:5]}...{raw_key[-4:]} (Length: {len(raw_key)})')
    client = genai.Client()
    print('[+] Initiating Live-Fire Ping to gemini-3.1-flash-lite...')
    response = client.models.generate_content(
        model='gemini-3.1-flash-lite', 
        contents='Acknowledge uplink. Reply with: UPLINK SECURE.'
    )
    print(f'[+] Response: {response.text}')
except Exception as e:
    print(f'[!] FAULT: {e}')
