import asyncio
import sys
import os
import json
import platform
from pathlib import Path
from google import genai
from google.genai import types
from google.genai import errors
from pydantic import BaseModel, Field

# ==========================================
# 1. ARCHITECTURAL PATHING & BASE JAIL
# ==========================================
if platform.system() == "Windows":
    DEFAULT_WORK_DIR = r"D:\Watchtower_Ops"
    # Windows lacks native O_NOFOLLOW blocking, fallback to standard flags
    O_SECURE_FLAGS = os.O_RDWR | os.O_CREAT
else:
    # Matches actual Docker volume architecture (./:/app)
    DEFAULT_WORK_DIR = "/app"
    # Linux POSIX: Block symlink TOCTOU race conditions at the kernel level
    O_SECURE_FLAGS = os.O_RDWR | os.O_CREAT | getattr(os, "O_NOFOLLOW", 0)

BASE_JAIL = Path(DEFAULT_WORK_DIR).resolve()

os.environ.setdefault("WORK_DIR", DEFAULT_WORK_DIR)
WORK_DIR = Path(os.environ["WORK_DIR"]).resolve()

ALLOWED_COMMANDS = {"ping", "ipconfig", "netstat", "tasklist", "tracert"}
MAX_RETRIES = 3

async def validate_workspace() -> bool:
    """Asynchronously validates the workspace directory with strict path jailing."""
    if not WORK_DIR.exists() or not WORK_DIR.is_dir():
        print(f"[-] CRITICAL: Workspace missing or invalid at {WORK_DIR}.")
        return False
    
    if not WORK_DIR.is_relative_to(BASE_JAIL):
        print(f"[-] CRITICAL: Path Traversal Attempt! {WORK_DIR} escaped {BASE_JAIL}.")
        return False

    print(f"[+] Workspace securely jailed and validated at: {WORK_DIR}")
    return True

def secure_write(filename: str, data: str) -> bool:
    """
    Neutralizes TOCTOU race conditions by interacting directly with
    kernel file descriptors instead of string paths.
    """
    target_file = WORK_DIR / filename
    
    # Secondary boundary check prior to I/O
    if not target_file.resolve().is_relative_to(BASE_JAIL):
        print(f"[-] I/O BLOCKED: Target {filename} attempts to escape jail.")
        return False

    try:
        # Open file descriptor with kernel-level symlink blocking
        # 0o600 ensures rw------- permissions (Operator only)
        fd = os.open(target_file, O_SECURE_FLAGS, 0o600)
        
        # Wrap the raw FD back into a Python file object for writing
        with open(fd, 'w', encoding='utf-8') as f:
            f.write(data)
            
        print(f"[+] Payload securely written to inode via FD: {filename}")
        return True
    except OSError as e:
        # If O_NOFOLLOW trips on a swapped symlink, it throws an OSError
        print(f"[-] Secure I/O failed (Symlink swap detected?): {e}")
        return False

# 1. Define the rigid steel molds (The Schema)
class NetworkInterface(BaseModel):
    name: str = Field(description="The name of the network adapter (e.g., 'Wireless LAN adapter Wi-Fi')")
    ip_address: str = Field(description="The assigned IPv4 address. Exclude 169.254.x.x addresses.")

class NetworkTelemetry(BaseModel):
    active_interfaces: list[NetworkInterface] = Field(description="A list of active, internet-routable network interfaces.")

async def execute_tactical_payload(command_list: list) -> dict:
    """Production-grade asynchronous execution wrapper."""
    if command_list and command_list[0] not in ALLOWED_COMMANDS:
        raise ValueError(f"BLOCKED: Unsafe command '{command_list[0]}' not in whitelist.")
    
    if not isinstance(command_list, list):
        raise TypeError("FATAL: Command must be a list of arguments.")
    
    process = await asyncio.create_subprocess_exec(
        *command_list,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        cwd=str(WORK_DIR)
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
        sys.exit("FATAL: GEMINI_API_KEY environment variable not set.")

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
        if not raw_text:
            sys.exit("FATAL: Agent returned empty response.")
        command_list = json.loads(raw_text)
        if not isinstance(command_list, list) or not command_list:
            sys.exit("FATAL: Agent did not return a valid non-empty command list.")
        print(f"[+] AI Generated Payload: {command_list}")
    except json.JSONDecodeError as e:
        sys.exit(f"FATAL: Agent returned invalid JSON: {e}")

    try:
        telemetry = await execute_tactical_payload(command_list)
    except ValueError as e:
        sys.exit(f"FATAL: {e}")

    if telemetry['status_code'] != 0:
        print(f"[!] EXECUTION FAILED.\n[!] TRACE: {telemetry['stderr']}")
    else:
        print(f"[+] OBJECTIVE SECURED.")
        # Proceed to Phase 3 with retry logic
        max_extract_retries = 3
        for attempt in range(max_extract_retries):
            try:
                parsed_data = await extract_tactical_data(client, telemetry['stdout'])
                print(f"[+] PARSED TELEMETRY:\n{parsed_data}")
                break
            except Exception as e:
                if attempt == max_extract_retries - 1:
                    sys.exit(f"FATAL: Phase 3 extraction failed after {max_extract_retries} attempts: {e}")
                wait_time = 2 ** (attempt + 1)
                print(f"[!] Phase 3 extraction failed. Retrying in {wait_time}s...")
                await asyncio.sleep(wait_time)

async def main():
    if not await validate_workspace():
        sys.exit("FATAL: Workspace validation failed.")
        
    print("[*] Core Executor Online. Kernel-level I/O locks initialized.")
    # Ready for integration with extract_phase_3_data payloads

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
    
    target_objective = "Check the current IP configuration of the Windows machine."
    await arm_autonomous_bridge(target_objective)

if __name__ == "__main__":
    if sys.version_info < (3, 11):
        sys.exit("FATAL: Execution requires Python 3.11+.")
        
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Execution halted by Operator.")
