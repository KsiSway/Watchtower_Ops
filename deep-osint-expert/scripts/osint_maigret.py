import subprocess
import sys
import os

def run_maigret(username):
    try:
        # Executes maigret against all supported sites in its database (~3000+)
        # Automatically generates an HTML report in the reports/ directory
        command = ['maigret', username, '-a', '--html']
        res = subprocess.run(command, capture_output=True, encoding='utf-8', env={**os.environ, "PYTHONIOENCODING": "utf-8"})
        
        stdout_output = res.stdout if res.stdout is not None else ""
        stderr_output = res.stderr if res.stderr is not None else ""

        if res.returncode == 0:
            return stdout_output.strip()
        else:
            return f"[-] Engine Error: {stderr_output.strip()}"
    except FileNotFoundError:
        return "[-] Error: Maigret not found. Install: pip install maigret"
    except Exception as e:
        return f"[-] Critical Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(run_maigret(sys.argv[1]))
