# Tactical Phone OSINT Vector for Project Watchtower
# Optimized for high-fidelity intelligence gathering and SQLite caching.

import asyncio
import aiohttp
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import json
import sys
import os
import sqlite3
import datetime
import subprocess
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING, format='%(levelname)s: %(message)s')

# Import existing search vector if available
try:
    from exa_search import search as exa_search
except ImportError:
    exa_search = None

# Configure Environment
load_dotenv()
ABSTRACT_KEY = os.getenv("ABSTRACT_API_KEY")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DB = os.getenv("CACHE_DB_PATH", os.path.join(os.path.expanduser("~"), ".cache", "watchtower_intel_cache.db"))
LOG_FILE = os.path.join(BASE_DIR, "C2_Activity.log")

# Ensure cache directory exists
os.makedirs(os.path.dirname(CACHE_DB), exist_ok=True)

def log_activity(target, status, details=""):
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [OSINT_PHONE] TARGET: {target} | STATUS: {status} | DETAILS: {details}\n"
        with open(LOG_FILE, "a") as f:
            f.write(log_entry)
    except Exception as e:
        logger.error(f"Failed to write log entry: {e}")

def init_cache():
    try:
        conn = sqlite3.connect(CACHE_DB)
        conn.execute('''CREATE TABLE IF NOT EXISTS phone_cache 
                        (number TEXT PRIMARY KEY, data TEXT, timestamp DATETIME)''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logger.error(f"Cache initialization failed: {e}")

def get_cached_intel(number):
    try:
        conn = sqlite3.connect(CACHE_DB)
        cursor = conn.execute("SELECT data, timestamp FROM phone_cache WHERE number = ?", (number,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            data, ts = row
            try:
                # Cache valid for 48 hours for phone data (less volatile than IPs)
                ts_dt = datetime.datetime.fromisoformat(ts)
                if datetime.datetime.now() - ts_dt < datetime.timedelta(hours=48):
                    return json.loads(data)
            except (ValueError, TypeError, json.JSONDecodeError) as e:
                logger.warning(f"Malformed cache entry for {number}: {e}")
                return None
    except sqlite3.Error as e:
        logger.error(f"Cache retrieval failed: {e}")
    return None

def save_to_cache(number, data):
    try:
        conn = sqlite3.connect(CACHE_DB)
        conn.execute("INSERT OR REPLACE INTO phone_cache VALUES (?, ?, ?)", 
                     (number, json.dumps(data), datetime.datetime.now().isoformat()))
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logger.error(f"Cache save failed: {e}")
    except Exception as e:
        logger.error(f"Failed to save cache: {e}")

def offline_baseline(target_number: str) -> dict:
    try:
        parsed_num = phonenumbers.parse(target_number, None)
        if not phonenumbers.is_valid_number(parsed_num):
            return {"error": "Invalid E.164 format"}

        return {
            "is_valid": True,
            "national_format": phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.NATIONAL),
            "international_format": phonenumbers.format_number(parsed_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
            "country_code": parsed_num.country_code,
            "geolocation": geocoder.description_for_number(parsed_num, "en"),
            "carrier": carrier.name_for_number(parsed_num, "en"),
            "timezones": timezone.time_zones_for_number(parsed_num),
            "type": phonenumbers.number_type(parsed_num) 
        }
    except Exception as e:
        logger.error(f"Offline baseline parsing error: {e}")
        return {"error": str(e)}

async def fetch_abstract(session, number):
    if not ABSTRACT_KEY:
        return {"error": "Missing ABSTRACT_API_KEY in .env"}
    
    url = "https://phonevalidation.abstractapi.com/v1/"
    params = {"api_key": ABSTRACT_KEY, "phone": number}
    try:
        async with session.get(url, params=params, timeout=10) as response:
            if response.status == 200:
                return await response.json()
            return {"error": f"HTTP {response.status}"}
    except asyncio.TimeoutError:
        return {"error": "Abstract API timeout (10s limit exceeded)"}
    except aiohttp.ClientError as e:
        logger.error(f"HTTP client error in fetch_abstract: {e}")
        return {"error": str(e)}
    except Exception as e:
        logger.error(f"Unexpected error in fetch_abstract: {e}")
        return {"error": str(e)}

async def execute_vector(target_number: str):
    if not target_number.startswith("+"):
        target_number = "+" + target_number
    
    clean_num = target_number.replace("+", "")
    
    init_cache()
    cached = get_cached_intel(target_number)
    if cached:
        cached["_source"] = "CACHE"
        return cached

    baseline = offline_baseline(target_number)
    if baseline.get("error"):
        return {"target": target_number, "baseline": baseline}

    intel = {"baseline": baseline, "external": {}, "search": []}

    async with aiohttp.ClientSession() as session:
        intel["external"]["abstract"] = await fetch_abstract(session, target_number)

    # Tactical Search Vector (Exa)
    if exa_search:
        try:
            # Use exact match quotes to prevent prefix collision (e.g. Chinese 136... numbers)
            query = f'"{target_number}" OR "{target_number.replace("+", "")}" owner carrier'
            search_results = exa_search(query, num_results=10)
            intel["search"] = search_results.get("results", [])
            
            # Heuristic: Try to identify carrier from search snippets if baseline fails
            if not intel["baseline"].get("carrier") and intel["search"]:
                carrier_keywords = ["Verizon", "AT&T", "T-Mobile", "Sprint", "Whidbey", "Comcast", "Spectrum"]
                for result in intel["search"]:
                    snippet = result.get("text", "").lower()
                    for cw in carrier_keywords:
                        if cw.lower() in snippet:
                            intel["baseline"]["carrier_guess"] = cw
                            break
                    if intel["baseline"].get("carrier_guess"): break
        except Exception as e:
            logger.error(f"Search vector error: {e}")
            intel["search_error"] = str(e)
    else:
        logger.debug("Exa search not available")

    # Tactical Persona Correlation (Local Alias Match)
    intel["alias_match"] = []
    # Check both with and without country code (e.g. 13609299009 vs 3609299009)
    possible_files = [f"{clean_num}.txt", f"{clean_num[1:] if clean_num.startswith('1') else clean_num}.txt"]
    for pf in possible_files:
        local_alias_file = os.path.join(BASE_DIR, pf)
        if os.path.exists(local_alias_file):
            try:
                with open(local_alias_file, "r") as f:
                    intel["alias_match"].extend([line.strip() for line in f.readlines() if line.strip().startswith("http")])
            except Exception as e:
                logger.warning(f"Failed to read alias file {pf}: {e}")
    
    # Remove duplicates
    intel["alias_match"] = list(set(intel["alias_match"]))

    # Vector 5: Social Deep-Links (Surgical Search)
    intel["social_links"] = {
        "WhatsApp": f"https://wa.me/{clean_num}",
        "LinkedIn": f"https://www.linkedin.com/search/results/all/?keywords=%22{target_number}%22",
        "Facebook": f"https://www.facebook.com/search/top/?q=%22{target_number}%22",
        "Truecaller": f"https://www.truecaller.com/who-called-me/{clean_num}"
    }

    # Vector 6: Auto-Dossier Generation (Maigret Integration)
    # Use the shorter number (without country code) for Maigret as it's more likely to be the handle
    handle = clean_num[1:] if clean_num.startswith('1') and len(clean_num) == 11 else clean_num
    report_file = os.path.join(BASE_DIR, "..", "reports", f"report_{handle}_plain.html")
    if not os.path.exists(report_file):
        log_activity(target_number, "DOSSIA_GEN_START", f"Triggering recursive scan for handle: {handle}")
        try:
            subprocess.Popen(['python', os.path.join(BASE_DIR, "osint_maigret.py"), handle],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            logger.error(f"Failed to spawn maigret process: {e}")
            log_activity(target_number, "DOSSIA_GEN_FAILED", str(e))
        intel["dossier_status"] = "GENERATING"
    else:
        intel["dossier_link"] = os.path.abspath(report_file)
        intel["dossier_status"] = "READY"

    intel["_source"] = "LIVE"
    save_to_cache(target_number, intel)
    log_activity(target_number, "SUCCESS", f"Carrier: {baseline.get('carrier')}")
    
    return intel

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_phone.py <number>"}))
        sys.exit(1)
        
    target = sys.argv[1]
    result = asyncio.run(execute_vector(target))
    print(json.dumps(result, indent=2))
