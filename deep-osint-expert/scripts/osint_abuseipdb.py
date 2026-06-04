# Updated Watchtower_Ops/osint_abuseipdb.py with SQLite Caching
import requests
import sys
import json
import sqlite3
import datetime
from dotenv import load_dotenv
import os
import logging

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# Use environment variable or default to user cache directory
CACHE_DB = os.getenv("CACHE_DB_PATH", os.path.join(os.path.expanduser("~"), ".cache", "watchtower_intel_cache.db"))

# Ensure cache directory exists
os.makedirs(os.path.dirname(CACHE_DB), exist_ok=True)

def init_cache():
    try:
        conn = sqlite3.connect(CACHE_DB)
        conn.execute('''CREATE TABLE IF NOT EXISTS abuse_cache 
                        (ip TEXT PRIMARY KEY, data TEXT, timestamp DATETIME)''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logger.error(f"Cache initialization failed: {e}")

def get_cached_intel(ip):
    try:
        conn = sqlite3.connect(CACHE_DB)
        cursor = conn.execute("SELECT data, timestamp FROM abuse_cache WHERE ip = ?", (ip,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            data, ts = row
            try:
                # Cache valid for 24 hours
                ts_dt = datetime.datetime.fromisoformat(ts)
                if datetime.datetime.now() - ts_dt < datetime.timedelta(hours=24):
                    return data
            except (ValueError, TypeError):
                # Malformed timestamp, treat as expired
                logger.warning(f"Malformed timestamp for IP {ip}, treating as expired")
                return None
    except sqlite3.Error as e:
        logger.error(f"Cache retrieval failed: {e}")
    return None

def check_ip_reputation(ip_address):
    init_cache()
    
    # Try Cache First
    cached = get_cached_intel(ip_address)
    if cached:
        # Indication of cache hit for verification
        return f"[CACHE HIT] {cached}"

    # Query API
    api_key = os.getenv("ABUSEIPDB_API_KEY")
    if not api_key:
        return "[-] Error: ABUSEIPDB_API_KEY not found in .env file"
    
    url = 'https://api.abuseipdb.com/api/v2/check'
    headers = {'Accept': 'application/json', 'Key': api_key}
    params = {'ipAddress': ip_address, 'maxAgeInDays': '90'}

    try:
        res = requests.get(url, headers=headers, params=params, timeout=10)
        if res.status_code == 200:
            data_str = json.dumps(res.json()['data'])
            # Save to Cache
            try:
                conn = sqlite3.connect(CACHE_DB)
                conn.execute("INSERT OR REPLACE INTO abuse_cache VALUES (?, ?, ?)", 
                             (ip_address, data_str, datetime.datetime.now().isoformat()))
                conn.commit()
                conn.close()
            except sqlite3.Error as e:
                logger.error(f"Cache save failed: {e}")
            return data_str
        return f"[-] API Error {res.status_code}: {res.text}"
    except requests.exceptions.Timeout:
        return "[-] Request Timeout: API did not respond within 10 seconds"
    except requests.exceptions.RequestException as e:
        return f"[-] Request Error: {e}"
    except Exception as e:
        return f"[-] Critical Failure: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(check_ip_reputation(sys.argv[1]))
