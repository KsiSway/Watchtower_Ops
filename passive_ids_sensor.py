# [Environment: Python Virtual Environment]
import time
from collections import deque, defaultdict
from scapy.all import sniff, IP

class DualEngineSensor:
    def __init__(self, window_seconds=86400, jitter_threshold=20.0, persistence_threshold=50):
        self.history = defaultdict(deque)
        self.window_seconds = window_seconds
        self.jitter_threshold = jitter_threshold
        self.persistence_threshold = persistence_threshold

    def log_connection(self, source_ip, dest_ip, tx_bytes, rx_bytes):
        current_time = time.time()
        flow_key = f"{source_ip}->{dest_ip}"
        
        # Pruning
        while self.history[flow_key] and self.history[flow_key][0]['time'] < current_time - self.window_seconds:
            self.history[flow_key].popleft()

        self.history[flow_key].append({'time': current_time, 'tx': tx_bytes, 'rx': rx_bytes})
        self.evaluate_heuristics(flow_key)

    def evaluate_heuristics(self, flow_key):
        records = self.history[flow_key]
        if len(records) < 5: return

        # Persistence/Symmetry Check
        connection_count = len(records)
        tx_total = sum(pkt['tx'] for pkt in records)
        rx_total = sum(pkt['rx'] for pkt in records)
        symmetry_ratio = (tx_total / rx_total) if rx_total > 0 else 1.0

        if connection_count > self.persistence_threshold and 0.8 < symmetry_ratio < 1.2:
            print(f"[!] ANOMALY [PERSISTENCE]: Flow {flow_key} exhibits highly symmetrical telemetry.")
            print(f"    Connections: {connection_count} | Symmetry: {symmetry_ratio:.2f}")

        # Jitter Check
        deltas = [records[i]['time'] - records[i-1]['time'] for i in range(1, len(records))]
        if len(deltas) >= 5:
            avg_delta = sum(deltas) / len(deltas)
            variance = sum([abs(d - avg_delta) for d in deltas]) / len(deltas)
            jitter = (variance / avg_delta) * 100 if avg_delta > 0 else 0
            if jitter < self.jitter_threshold:
                print(f"[!] ANOMALY [JITTER]: Flow {flow_key} exhibits rigid intervals ({jitter:.2f}%).")

def start_sensor():
    print("[*] Initializing Watchtower Dual-Engine Administrative Sensor...")
    sensor = DualEngineSensor(persistence_threshold=50)
    local_subnet = "192.168.8."

    def process_packet(packet):
        if IP in packet:
            src, dst, length = packet[IP].src, packet[IP].dst, packet[IP].len
            if src.startswith(local_subnet) and not dst.startswith(local_subnet):
                sensor.log_connection(src, dst, tx_bytes=length, rx_bytes=0)
            elif dst.startswith(local_subnet) and not src.startswith(local_subnet):
                sensor.log_connection(dst, src, tx_bytes=0, rx_bytes=length)

    sniff(iface="Realtek PCIe GBE Family Controller", prn=process_packet, store=0)

if __name__ == "__main__":
    start_sensor()
