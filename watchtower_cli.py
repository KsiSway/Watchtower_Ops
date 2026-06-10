import asyncio
import sys
import os
from google import genai

async def execute_payload(prompt: str):
    """Asynchronous payload delivery via Google GenAI SDK."""
    # The client automatically extracts the GEMINI_API_KEY environment variable
    try:
        client = genai.Client()
    except Exception as e:
        sys.exit(f"FATAL CONFIG: Ensure GEMINI_API_KEY is set. Error: {e}")

    try:
        response = await client.aio.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        print(response.text)
    except Exception as e:
        sys.exit(f"FATAL ROUTING: Upstream connection failed. Error: {e}")

async def main():
    if len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
    elif not sys.stdin.isatty():
        prompt = sys.stdin.read().strip()
    else:
        sys.exit("USAGE: python watchtower_cli.py <prompt> OR pipe data via stdin.")
    
    if not prompt:
        sys.exit("ERROR: Empty payload detected.")

    await execute_payload(prompt)

if __name__ == "__main__":
    if sys.version_info < (3, 11):
        sys.exit("FATAL: Execution requires Python 3.11+.")
    asyncio.run(main())
