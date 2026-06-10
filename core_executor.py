import asyncio
import sys
import os
import json
from google import genai
from google.genai import types
from google.genai import errors
from pydantic import BaseModel, Field

# 1. Define the rigid steel molds (The Schema)
class NetworkInterface(BaseModel):
    name: str = Field(description="The name of the network adapter (e.g., 'Wireless LAN adapter Wi-Fi')")
    ip_address: str = Field(description="The assigned IPv4 address. Exclude 169.254.x.x addresses.")

class NetworkTelemetry(BaseModel):
    active_interfaces: list[NetworkInterface] = Field(description="A list of active, internet-routable network interfaces.")

async def execute_tactical_payload(command_list: list) -> dict:
    """Production-grade asynchronous execution wrapper."""
    safe_dir = r"D:\Watchtower_Ops"
    
    if not isinstance(command_list, list):
        raise TypeError("FATAL: Command must be a list of arguments.")
    
    process = await asyncio.create_subprocess_exec(
        *command_list,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=safe_dir
    )
    
    stdout, stderr = await process.communicate()
    
    return {
        "status_code": process.returncode,
        "stdout": stdout.decode('utf-8').strip(),
        "stderr": stderr.decode('utf-8').strip()
    }

async def extract_tactical_data(client: genai.Client, raw_ipconfig_output: str):
    print("[*] Initiating Phase 3: Structured Output Extraction...")
    
    # 2. Apply the mask during inference
    response = await client.aio.models.generate_content(
        model='gemini-2.5-flash',
        contents=[
            "Extract the active, internet-routable interfaces from this telemetry block. Ignore disconnected media and APIPA (169.254.x.x) addresses.",
            raw_ipconfig_output
        ],
        config=types.GenerateContentConfig(
            # Force the model to output JSON matching our exact Pydantic class
            response_mime_type="application/json",
            response_schema=NetworkTelemetry,
            temperature=0.0
        )
    )

    # 3. Access the automatically parsed Pydantic object
    print("[+] Phase 3 Extraction Complete.")
    return response.parsed

async def arm_autonomous_bridge(objective: str):
    print("[*] Arming Phase 2: AI Telemetry Bridge (with Exponential Backoff)...")
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("FATAL: GEMINI_API_KEY not found in session memory.")

    print("[*] Neural Link Established. Initializing Exocortex Agent...")
    client = genai.Client(api_key=api_key)

    sys_instruct = (
        "You are the Watchtower Exocortex Executor. "
        "Convert the user's objective into a strict JSON list of string arguments for Windows subprocess execution. "
        "Do NOT chain commands. Do NOT use shell operators like | or &. "
        "Output strictly valid JSON and nothing else. "
        "Example output: [\"ping\", \"-n\", \"4\", \"8.8.8.8\"]"
    )

    print(f"[*] Dispatching Objective: {objective}")
    
    max_retries = 4
    base_delay = 2
    raw_text = ""

    for attempt in range(max_retries):
        try:
            response = await client.aio.models.generate_content(
                model='gemini-2.5-flash',
                contents=objective,
                config=types.GenerateContentConfig(
                    system_instruction=sys_instruct,
                    temperature=0.0
                )
            )
            raw_text = response.text
            break
            
        except errors.ServerError as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                if attempt == max_retries - 1:
                    sys.exit(f"FATAL: Upstream API persistently unavailable after {max_retries} attempts. Aborting.")
                wait_time = base_delay * (2 ** attempt)
                print(f"[!] NETWORK ANOMALY: 503 UNAVAILABLE. Executing exponential backoff. Retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)
            else:
                raise e
        except Exception as e:
            raise e

    try:
        raw_text = raw_text.replace('```json', '').replace('```', '').strip()
        command_list = json.loads(raw_text)
        print(f"[+] AI Generated Payload: {command_list}")
    except json.JSONDecodeError:
        sys.exit(f"FATAL: Agent hallucinated invalid JSON structure or returned empty string.")

    telemetry = await execute_tactical_payload(command_list)

    if telemetry['status_code'] != 0:
        print(f"[!] EXECUTION FAILED.\n[!] TRACE: {telemetry['stderr']}")
    else:
        print(f"[+] OBJECTIVE SECURED.")
        # Proceed to Phase 3
        parsed_data = await extract_tactical_data(client, telemetry['stdout'])
        print(f"[+] PARSED TELEMETRY:\n{parsed_data}")

if __name__ == "__main__":
    if sys.version_info < (3, 11):
        sys.exit("FATAL: Execution requires Python 3.11+.")
        
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    target_objective = "Check the current IP configuration of the Windows machine."
    asyncio.run(arm_autonomous_bridge(target_objective))
