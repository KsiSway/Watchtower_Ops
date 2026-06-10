import asyncio
import sys
import json
import urllib.request
import urllib.error
import socket

def sync_ollama_request(req):
    """Synchronous network call isolated with timeout and socket closure."""
    # Enforces timeout and guarantees socket closure via context manager
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            return json.loads(response.read().decode('utf-8'))
    except socket.timeout:
        raise TimeoutError("Ollama request exceeded 120s timeout.")

async def execute_local_payload(prompt: str):
    """Asynchronous payload delivery via local Ollama instance."""
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "dolphin-llama3:latest",
        "prompt": prompt,
        "stream": False
    }
    
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), method='POST')
    req.add_header('Content-Type', 'application/json')
    
    try:
        loop = asyncio.get_running_loop()
        # Offload hardened synchronous call to prevent event loop blocking
        data = await loop.run_in_executor(None, sync_ollama_request, req)
        print(data.get("response", ""))
    except (socket.timeout, urllib.error.URLError) as e:
        sys.exit(f"FATAL ROUTING: Ollama unreachable at :11434. Error: {e}")
    except TimeoutError as e:
        sys.exit(f"FATAL ROUTING: {e}")

async def main():
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        # Read stdin with size limit (10MB max)
        prompt = sys.stdin.read(10485760).strip()
    else:
        sys.exit("USAGE: python watchtower_cli.py <prompt> OR pipe data via stdin.")
    
    if not prompt:
        sys.exit("ERROR: Empty payload detected.")

    await execute_local_payload(prompt)

if __name__ == "__main__":
    if sys.version_info < (3, 11):
        sys.exit("FATAL: Execution requires Python 3.11+.")
    asyncio.run(main())
