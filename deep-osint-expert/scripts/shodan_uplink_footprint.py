import shodan
import json

API_KEY = "IQWdvDATOYcnalSbosooLclRaIq7dk7g"
TARGET_IP = "3.234.129.4"

api = shodan.Shodan(API_KEY)
try:
    print(f"[*] Querying Shodan for {TARGET_IP}...")
    host = api.host(TARGET_IP)
    results = {
        "ip": host.get('ip_str'),
        "hostnames": host.get('hostnames'),
        "asn": host.get('asn'),
        "org": host.get('org'),
        "ports": host.get('ports'),
        "os": host.get('os'),
        "isp": host.get('isp')
    }
    print(json.dumps(results, indent=4))
except Exception as e:
    print(f"[-] Shodan Query Error: {e}")
