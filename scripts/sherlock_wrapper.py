import subprocess
import sys
import os

def run_sherlock(username):
    print(f"[*] INITIATING GLOBAL OSINT SWEEP FOR USERNAME: {username}")
    
    # Ensuring the results directory exists
    results_dir = "sherlock_results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
        
    output_file = os.path.join(results_dir, f"{username}.txt")
    
    try:
        # Running sherlock with a timeout and output redirection
        # --timeout 5 to keep it relatively fast for the C2 dashboard
        cmd = ["sherlock", username, "--timeout", "5", "--output", output_file]
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                data = f.read()
            print(f"[+] SWEEP COMPLETE. {len(data.splitlines())} HITS IDENTIFIED.")
            print("-" * 30)
            print(data)
        else:
            print(f"[-] NO HITS FOUND FOR {username} OR ERROR OCCURRED.")
            print(result.stderr)
            
    except Exception as e:
        print(f"[!] FATAL MODULE ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python sherlock_wrapper.py [USERNAME]")
    else:
        run_sherlock(sys.argv[1])
