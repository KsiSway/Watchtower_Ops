import os
import sys
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from google import genai
from dotenv import load_dotenv

app = FastAPI(title="Watchtower IPC Bridge")

env_path = r"D:\Watchtower_Ops\.env"
load_dotenv(dotenv_path=env_path, override=True)

clean_key = os.environ.get("GEMINI_API_KEY", "").strip().strip('"').strip("'")

if not clean_key or "EXACT_KEY_HERE" in clean_key:
    print("[!] FAULT: Invalid key detected in .env vault.")
    sys.exit(1)

client = genai.Client(api_key=clean_key)

@app.post("/stream_inference")
async def stream_inference(payload: dict):
    prompt = payload.get("prompt", "")

    def generate():
        # CAPEX OVERRIDE: Strictly routed to the free-tier 3.1 model
        response = client.chats.create(model='gemini-3.1-flash-lite').send_message_stream(prompt)
        for chunk in response:
            yield f"data: {chunk.text}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")
