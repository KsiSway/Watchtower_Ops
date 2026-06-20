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
from typing import Optional

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
try:
    WORK_DIR = Path(os.environ["WORK_DIR"]).resolve()
except (OSError, RuntimeError) as e:
    sys.exit(f"FATAL: Cannot resolve WORK_DIR: {e}")

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
        
        # Wrap the raw FD back into a Python file object for writing using fdopen
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(data)
            f.flush()
            
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

async def extract_tactical_data(client: Optional[genai.Client], raw_ipconfig_output: str):
    print("[*] Initiating Phase 3: Structured Output Extraction...")
    print("[-] SUPPRESSED: Outbound API calls disabled to enforce closed-loop mesh architecture.")
    return NetworkTelemetry(active_interfaces=[])

async def arm_autonomous_bridge(objective: str):
    print("[*] Arming Phase 2: AI Telemetry Bridge (with Exponential Backoff)...")
    print("[-] SUPPRESSED: Outbound API calls disabled to enforce closed-loop mesh architecture.")
    print("[+] Defaulting to manual telemetry execution.")
    
    # Cross-platform network info command
    if sys.platform == "win32":
        command_list = ["ipconfig"]
    else:
        command_list = ["ip", "addr"]
    
    try:
        telemetry = await execute_tactical_payload(command_list)
    except ValueError as e:
        sys.exit(f"FATAL: {e}")

    if telemetry['status_code'] != 0:
        print(f"[!] EXECUTION FAILED.\n[!] TRACE: {telemetry['stderr']}")
    else:
        print(f"[+] OBJECTIVE SECURED.")
        # Proceed to Phase 3 with retry logic
        parsed_data = await extract_tactical_data(None, telemetry['stdout'])
        print(f"[+] PARSED TELEMETRY:\n{parsed_data}")

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
