---
name: deep-osint-expert
description: Advanced phone, breach, and reputation interrogations. Use when you need to interrogate E.164 phone numbers, hunt for leaked credentials, check IP reputations, or route requests through Tor for dark web intelligence.
---

# Deep OSINT Expert

This skill provides a high-velocity intelligence pipeline for identity and infrastructure interrogation.

## Core Capabilities

- **Phone Intelligence**: Deep interrogation of E.164 phone numbers using `osint_phone.py`. Correlates carrier, geolocation, and digital aliases.
- **Email Interrogation**: Verifying email registrations across 120+ platforms using `osint_holehe_bridge.py`.
- **Breach Hunting**: Identifying leaked credentials and plaintext password patterns via `audit_creds.py`.
- **IP Reputation**: Checking target IPs against AbuseIPDB and other threat feeds via `osint_abuseipdb.py`.
- **Dark Web Routing**: Fetching onion-service data via `osint_tor_fetcher.py`.

## Tactical Workflows

### 1. Identity Dossier Compilation
1. **Phone Interrogation**: Start with `osint_phone.py <number>`.
2. **Email Interrogation**: Deploy `osint_holehe_bridge.py <email>` to map the target's primary digital services.
3. **Username Mapping**: Run recursive dossiers via `osint_maigret.py <alias>`.
3. **Breach Audit**: Check found emails/aliases for leaks using `audit_creds.py`.

### 2. Infrastructure Footprinting
- **Shodan Interrogation**: Query public IP data via `shodan_ip_query.py` or `shodan_uplink_footprint.py`.
- **Reputation Check**: Run `osint_abuseipdb.py <IP>` to detect malicious activity history.

### 3. Dark Web Interception
Route intelligence requests through the Tor proxy (127.0.0.1:9050) using `osint_tor_fetcher.py` to acquire data from hidden services.

## Intelligence Assets
Log all exfiltrated data to `intelligence_log.csv` for downstream analysis.
