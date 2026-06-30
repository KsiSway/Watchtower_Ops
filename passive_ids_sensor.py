# [Environment: Python Virtual Environment]
from scapy.all import sniff, conf, IP, TCP
import time
from collections import deque, defaultdict
import sys

# Enforce promiscuous mode to capture Port Mirrored (SPAN) traffic
conf.sniff_promisc = True

class DualEngineSensor:
    def __init__(self, window_seconds=86400, jitter_threshold=20.0, persistence_threshold=50):
        # O(1) Time-Series Rolling Window
        self.history = defaultdict(deque)
        self.window_seconds = window_seconds
        self.jitter_threshold = jitter_threshold
        self.persistence_threshold = persistence_threshold

    def log_connection(self, internal_ip, external_ip, tx_bytes, rx_bytes):
        current_time = time.time()
        flow_key = f"{internal_ip} <-> {external_ip}"
        
        # O(1) Pruning Mechanics: Silently drop connections older than 24 hours
        while self.history[flow_key] and self.history[flow_key][0]['time'] < current_time - self.window_seconds:
            self.history[flow_key].popleft()
            
        self.history[flow_key].append({'time': current_time, 'tx': tx_bytes, 'rx': rx_bytes})
        self.evaluate_heuristics(flow_key)

    def evaluate_heuristics(self, flow_key):
        records = self.history[flow_key]
        if len(records) < 5:
            return # Insufficient data for statistical baseline
            
        # 1. Destination Persistence Engine (High-Entropy / Volume Checks)
        connection_count = len(records)
        tx_total = sum(pkt['tx'] for pkt in records)
        rx_total = sum(pkt['rx'] for pkt in records)
        
        # Calculate Data Volume Symmetry
        symmetry_ratio = (tx_total / rx_total) if rx_total > 0 else 1.0
        
        # If persistence exceeds threshold and traffic is highly symmetrical (ratio near 1.0)
        if connection_count > self.persistence_threshold and 0.8 < symmetry_ratio < 1.2:
            # Modulo prevents terminal flooding
            if connection_count % 10 == 0:
                print(f"[!] ANOMALY [PERSISTENCE]: Flow {flow_key} exhibits highly symmetrical telemetry.")
                print(f"    Connections: {connection_count} | TX: {tx_total}B | RX: {rx_total}B | Symmetry: {symmetry_ratio:.2f}")

        # 2. Jitter Analysis Engine (Low-Entropy / Rigid Timers)
        # Only calculate jitter based on outbound (TX) polling intervals
        outbound_times = [pkt['time'] for pkt in records if pkt['tx'] > 0]
        if len(outbound_times) >= 5:
            deltas = [outbound_times[i] - outbound_times[i-1] for i in range(1, len(outbound_times))]
            avg_delta = sum(deltas) / len(deltas)
            
            if avg_delta > 0:
                variance = sum([abs(d - avg_delta) for d in deltas]) / len(deltas)
                jitter_percent = (variance / avg_delta) * 100
                
                if jitter_percent < self.jitter_threshold:
                    if len(outbound_times) % 5 == 0:
                        print(f"[!] ANOMALY [JITTER]: Flow {flow_key} exhibits rigid intervals.")
                        print(f"    Jitter: {jitter_percent:.2f}% | Avg Interval: {avg_delta:.2f}s")


# Initialize the primary sensor engine
sensor = DualEngineSensor()

def analyze_traffic(packet):
    """Parses mirrored L2 traffic and routes flow bytes to the heuristic engine."""
    if IP in packet and TCP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        pkt_len = len(packet[IP])
        
        # Track outbound vs inbound payload symmetry
        if src_ip.startswith("192.168.68.") and not dst_ip.startswith("192.168.68."):
            sensor.log_connection(src_ip, dst_ip, tx_bytes=pkt_len, rx_bytes=0)
        elif dst_ip.startswith("192.168.68.") and not src_ip.startswith("192.168.68."):
            sensor.log_connection(dst_ip, src_ip, tx_bytes=0, rx_bytes=pkt_len)


if __name__ == "__main__":
    print("[*] Initializing Watchtower Dual-Engine Administrative Sensor...")
    print("[*] Execution Zone: Isolated Python Virtual Environment")
    print("[*] Engines Active: [1] Jitter Variance [2] Destination Persistence (Symmetry)")
    print("[*] Listening on interface in Promiscuous Mode...")
    
    try:
        # Sniff traffic silently without sending any packets (Zero Security Footprint)
        sniff(prn=analyze_traffic, store=0)
    except PermissionError:
        print("[!] CRITICAL: Insufficient Privileges.")
        print("[!] You must run this terminal as Administrator to enable Promiscuous Mode.")
        sys.exit(1)
