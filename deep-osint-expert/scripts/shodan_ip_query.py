import shodan
import json

API_KEY = "IQWdvDATOYcnalSbosooLclRaIq7dk7g"
TARGET_IP = "3.234.129.4"

api = shodan.Shodan(API_KEY)
try:
    host = api.host(TARGET_IP)
    print(json.dumps(host, indent=4))
except Exception as e:
    print(f"Error: {e}")
