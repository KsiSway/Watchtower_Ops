import subprocess
import sys

def execute_sherlock(username):
    """Executes Sherlock investigation with tactical optimizations."""
    try:
        # Executes Sherlock, suppressing verbosity, fetching only positive hits, 3s timeout per site
        command = ['sherlock', username, '--print-found', '--timeout', '3']
        res = subprocess.run(command, capture_output=True, text=True)
        
        if res.returncode == 0:
            return res.stdout.strip()
        else:
            return f"[-] Engine Error: {res.stderr.strip()}"
    except FileNotFoundError:
        return "[-] Error: Sherlock binary not found in PATH."
    except Exception as e:
        return f"[-] Critical Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(execute_sherlock(sys.argv[1]))
    else:
        print("[-] Target Handle Required.")
