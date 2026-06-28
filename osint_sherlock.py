import asyncio
import sys

async def run_sherlock(alias: str):
    print(f"[*] Initiating external footprint correlation for: {alias}")
    process = await asyncio.create_subprocess_exec(
        sys.executable, "-m", "sherlock", alias, "--timeout", "5", "--print-found",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    out_data = stdout.decode('utf-8')
    err_data = stderr.decode('utf-8')

    if process.returncode == 0:
        print("[*] Correlation complete. Data piped to central dashboard.")
        print(out_data)
    else:
        print(f"[!] Timeout/Fault detected (Exit Code: {process.returncode}). Salvaging partial footprint:")
        if out_data.strip():
            print(out_data)
        if err_data.strip():
            print(f"[!] Stderr: {err_data}")
        print("[*] Primary vector fault. Engaging fallback logic: Initiating local SpiderFoot correlation.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] Target alias required.")
        sys.exit(1)
    # CRITICAL FIX: The alias is located at index 1
    asyncio.run(run_sherlock(sys.argv[1]))
