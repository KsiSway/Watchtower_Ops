import subprocess
import json
import sys
import argparse
import os

def run_rtl_scan(frequency, duration=10, output_file="scan.bin"):
    """Runs rtl_sdr to capture raw data."""
    print(f"[*] Initiating RTL_SDR scan at {frequency}Hz for {duration}s...")
    try:
        # Standard command: rtl_sdr -f <freq> -s 2.048e6 -n <samples> <file>
        # 2.048Msps * 10s = 20480000 samples
        num_samples = int(2.048e6 * duration)
        cmd = ["rtl_sdr", "-f", str(frequency), "-s", "2.048e6", "-n", str(num_samples), output_file]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            return {"status": "SUCCESS", "details": f"Scan saved to {output_file}"}
        else:
            return {"status": "FAILURE", "details": stderr}
    except FileNotFoundError:
        return {"status": "FAILURE", "details": "rtl_sdr binary not found in PATH."}

def run_adsb_capture(duration=30):
    """Runs dump1090 to capture ADS-B flight telemetry."""
    print(f"[*] Initiating ADS-B capture for {duration}s...")
    try:
        # dump1090 --net --net-http-port 8080 --quiet
        # We might want to capture the JSON output if it supports it, 
        # or just run it and let the user access the web UI.
        # For tactical extraction, we'll try to use --net and potentially parse local data.
        cmd = ["dump1090", "--net", "--quiet"]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # This usually runs indefinitely, so we wait and then kill it
        try:
            process.wait(timeout=duration)
        except subprocess.TimeoutExpired:
            process.terminate()
            return {"status": "SUCCESS", "details": f"ADS-B receiver ran for {duration}s. Check network ports."}
            
        stdout, stderr = process.communicate()
        return {"status": "SUCCESS", "details": "ADS-B session terminated."}
    except FileNotFoundError:
        return {"status": "FAILURE", "details": "dump1090 binary not found in PATH."}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Watchtower SDR Recon Wrapper")
    parser.add_argument("--mode", choices=["scan", "adsb"], required=True)
    parser.add_argument("--freq", type=int, help="Frequency in Hz for scan mode")
    parser.add_argument("--duration", type=int, default=10, help="Duration in seconds")
    
    args = parser.parse_args()
    
    if args.mode == "scan":
        if not args.freq:
            print(json.dumps({"status": "FAILURE", "details": "Frequency required for scan mode."}))
            sys.exit(1)
        result = run_rtl_scan(args.freq, args.duration)
    elif args.mode == "adsb":
        result = run_adsb_capture(args.duration)
        
    print(json.dumps(result))
