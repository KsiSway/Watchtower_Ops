import subprocess
import sys

ADB_PATH = r"C:\adb\platform-tools\adb.exe"

def execute_adb_payload(target_ip_port, command):
    """Force TCP connection and deploy raw shell command to target."""
    try:
        # Force TCP connection first
        subprocess.run([ADB_PATH, 'connect', target_ip_port], capture_output=True, timeout=5)
        # Deploy raw shell command
        res = subprocess.run([ADB_PATH, '-s', target_ip_port, 'shell', command], capture_output=True, text=True, timeout=10)
        return res.stdout.strip() if res.returncode == 0 else f"[-] ADB Shell Error: {res.stderr.strip()}"
    except subprocess.TimeoutExpired:
        return "[-] Error: Connection to Android daemon timed out."
    except Exception as e:
        return f"[-] Critical Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(execute_adb_payload(sys.argv[1], sys.argv[2]))
