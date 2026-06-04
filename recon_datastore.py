# DEPLOYMENT: Watchtower_Ops/recon_datastore.py
# Local SQLite storage for Watchtower recon sweeps.

import sqlite3
import json
import logging
import os
from datetime import datetime

class ReconDatastore:
    """Local SQLite storage for Watchtower recon sweeps."""
    def __init__(self, db_path=None):
        if db_path is None:
            # Ensure it's in the Watchtower_Ops directory
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.db_path = os.path.join(script_dir, "recon_ledger.db")
        else:
            self.db_path = db_path
            
        self._initialize_db()

    def _initialize_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Initialize schema for storing unstructured JSON recon data
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sweeps (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                target TEXT NOT NULL,
                source TEXT NOT NULL,
                raw_data TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def log_sweep(self, target: str, source: str, data: dict):
        """Ingests JSON output from individual recon modules."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            timestamp = datetime.utcnow().isoformat()
            
            # Serialize payload
            json_data = json.dumps(data) if isinstance(data, dict) else str(data)
            
            cursor.execute(
                "INSERT INTO sweeps (timestamp, target, source, raw_data) VALUES (?, ?, ?, ?)",
                (timestamp, target, source, json_data)
            )
            conn.commit()
            conn.close()
            logging.info(f"Sweep logged to database for {target} via {source}.")
        except Exception as e:
            logging.error(f"Failed to log sweep to database: {str(e)}")

if __name__ == "__main__":
    # Test initialization
    db = ReconDatastore()
    print(f"[+] Datastore initialized at: {db.db_path}")
