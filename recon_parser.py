# DEPLOYMENT: Watchtower_Ops/recon_parser.py
# Advanced regex-based data extraction for recon ledger entries.

import re
import json
import logging

class ReconParser:
    """Extracts high-value indicators (IPs, Emails, Domains, SSIDs) from raw recon data."""
    def __init__(self):
        self.patterns = {
            "ipv4": r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
            "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            "domain": r'\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]\b',
            "mac_address": r'\b(?:[0-9A-Fa-f]{2}[:-]){5}(?:[0-9A-Fa-f]{2})\b'
        }

    def extract_indicators(self, raw_data: str) -> dict:
        """Parses a raw string and returns unique identified indicators."""
        results = {}
        for key, pattern in self.patterns.items():
            matches = re.findall(pattern, raw_data)
            if matches:
                results[key] = list(set(matches))
        return results

    def parse_ledger_entry(self, source: str, raw_json: str) -> dict:
        """Surgically extracts relevant data based on the source bridge."""
        try:
            data = json.loads(raw_json)
            # Combine all string values for a global extraction
            global_text = str(data)
            indicators = self.extract_indicators(global_text)
            
            return {
                "source": source,
                "indicators": indicators,
                "summary": f"Extracted {sum(len(v) for v in indicators.values())} unique indicators."
            }
        except Exception as e:
            return {"error": f"Parsing failed: {str(e)}"}

if __name__ == "__main__":
    # Test case
    parser = ReconParser()
    test_data = '{"info": "Target found at 1.1.1.1 and 8.8.8.8, email admin@example.com"}'
    print(json.dumps(parser.parse_ledger_entry("test", test_data), indent=2))
