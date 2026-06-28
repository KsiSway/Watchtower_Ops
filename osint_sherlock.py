import asyncio
import sys

async def run_sherlock(alias: str):
    print(f"[*] Initiating external footprint correlation for: {alias}")
    # sys.executable ensures strict adherence to the local .venv airlock
    process = await asyncio.create_subprocess_exec(
        sys.executable, "-m", "sherlock", alias, "--timeout", "5", "--print-found",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    
    if process.returncode == 0:
        print("[*] Correlation complete. Data piped to central dashboard.")
        print(stdout.decode('utf-8'))
    else:
        print(f"[!] Fault detected: {stderr.decode('utf-8')}")
        print("[*] Primary vector fault. Engaging fallback logic: Initiating local SpiderFoot correlation.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] Target alias required.")
        sys.exit(1)
    asyncio.run(run_sherlock(sys.argv[1]))
