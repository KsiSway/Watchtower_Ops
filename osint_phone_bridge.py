# DEPLOYMENT: Watchtower_Ops/osint_phone_bridge.py
# Dependency: pip install phonenumbers

import json
import sys
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import asyncio
import os

async def execute_phone_sweep(phone_number: str):
    """Fingerprints a phone number for location and carrier."""
    try:
        parsed_number = phonenumbers.parse(phone_number, None) # Assumes international format (+1...)
        
        if not phonenumbers.is_valid_number(parsed_number):
             return {"status": "success", "analysis": "Invalid phone number format. Please ensure E.164 format (e.g., +15555555555)."}

        location = geocoder.description_for_number(parsed_number, "en")
        service_provider = carrier.name_for_number(parsed_number, "en")
        time_zones = timezone.time_zones_for_number(parsed_number)
        
        dossier = f"PHONE TARGET: {phone_number}\nLOCATION: {location}\nCARRIER: {service_provider}\nTIMEZONE: {', '.join(time_zones)}"

        # Resolve brain script location
        script_dir = os.path.dirname(os.path.abspath(__file__))
        brain_path = os.path.join(script_dir, "osint_brain.py")

        # Send to brain for context
        brain_proc = await asyncio.create_subprocess_exec(
            "python", brain_path, "telemetry", dossier,
            stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        b_stdout, b_stderr = await brain_proc.communicate()

        if brain_proc.returncode == 0:
            return json.loads(b_stdout.decode().strip())
        else:
             return {"status": "success", "analysis": f"Phone Data: Location: {location}, Carrier: {service_provider}. Brain pipeline unavailable."}

    except phonenumbers.phonenumberutil.NumberParseException:
         return {"status": "success", "analysis": "Unable to parse number. Missing country code (e.g., +1)?"}
    except Exception as e:
        return {"status": "error", "message": f"Phone fingerprinting failed: {str(e)}"}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(json.dumps({"error": "Usage: python osint_phone_bridge.py '<phone_number>'" }))
        sys.exit(1)
    # Run synchronously as phonenumbers is a local DB, but wrap in asyncio to match architecture
    print(json.dumps(asyncio.run(execute_phone_sweep(sys.argv[1])), indent=2))
