#!/usr/bin/env python3
# Minimum Requirement: Python 3.11+
# Dependencies: pip install tflite-runtime pycoral
# Note: If running via WSL on the OptiPlex, you must configure USBIPD to pass the Coral USB to the Linux kernel.

import json
import sys
try:
    from pycoral.utils.edgetpu import list_edge_tpus
except ImportError:
    print(json.dumps({"error": "Missing PyCoral library. Install via: pip install pycoral"}))
    sys.exit(1)

def verify_tpu_uplink():
    """Diagnostic check to verify Coral TPU hardware mounting in Watchtower."""
    try:
        tpus = list_edge_tpus()
        
        if not tpus:
            payload = {
                "status": "OFFLINE", 
                "error": "No Edge TPU detected. Verify USB 3.0 connection and Host/WSL passthrough."
            }
        else:
            payload = {
                "status": "ONLINE",
                "hardware": "Google Coral Edge TPU",
                "active_nodes": len(tpus),
                "paths": [tpu['path'] for tpu in tpus]
            }
            
        print(json.dumps(payload, indent=2))
        
    except Exception as e:
        print(json.dumps({"status": "FATAL", "error": str(e)}))

if __name__ == "__main__":
    verify_tpu_uplink()
