# [Environment: Python Virtual Environment]
import sys

def analyze_jitter(timestamps, base_interval):
    print("[*] Analyzing connection telemetry for baseline variance...")
    
    if len(timestamps) < 2:
        print("[!] CRITICAL EXECUTION FAILURE: Insufficient telemetry data. Require at least two data points to calculate variance.")
        sys.exit(1)

    deltas = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    avg_delta = sum(deltas) / len(deltas)
    
    variance = sum([abs(d - avg_delta) for d in deltas]) / len(deltas)
    jitter_percent = (variance / base_interval) * 100
    
    print(f"[*] Base Interval: {base_interval}s | Calculated Avg Delta: {avg_delta:.2f}s")
    print(f"[*] Jitter Variance: {variance:.2f}s | Jitter: {jitter_percent:.2f}%\n")
    
    if jitter_percent < 5.0:
        print("[!] ANOMALY: Highly rigid connection intervals detected (Low Jitter). Possible automated uplink.")
    elif jitter_percent > 20.0:
        print("[*] WARNING: High Entropy/Jitter Detected. Flagged for osint_brain.py analysis.")
    else:
        print("[*] Status: Traffic pattern within acceptable operational thresholds.")

if __name__ == "__main__":
    # Simulated telemetry array: A sequence of epoch timestamps
    simulated_timestamps = [100, 158, 221, 280, 342, 399]
    analyze_jitter(simulated_timestamps, 60)
