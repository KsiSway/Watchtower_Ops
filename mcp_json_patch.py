#!/usr/bin/env python3
"""
Watchtower MCP Architecture Configurator
Target: C:\\Users\\Lance\\.gemini\\config\\mcp_config.json
Standards: Python 3.11+, Native JSON execution (Bypasses missing 'jq')
"""

import json
import sys
from pathlib import Path

# Handle execution from both Docker/WSL (/c/...) and native Windows (C:/...)
CONFIG_PATHS = [
    Path("/c/Users/Lance/.gemini/config/mcp_config.json"),
    Path("C:/Users/Lance/.gemini/config/mcp_config.json")
]

def patch_architecture():
    target_config = next((p for p in CONFIG_PATHS if p.exists()), None)
    
    if not target_config:
        print("[-] CRITICAL: mcp_config.json not found in expected directories.")
        sys.exit(1)

    with open(target_config, 'r') as f:
        config = json.load(f)

    servers = config.get("mcpServers", {})

    # 1. Purge generic DevTools to prevent port contention
    if "chrome-devtools-mcp" in servers:
        print("[*] Purging redundant 'chrome-devtools-mcp' node...")
        del servers["chrome-devtools-mcp"]

    # 2. Re-inject the missing SQLite core database link
    if "sqlite" not in servers:
        print("[*] Re-establishing SQLite memory core via uvx...")
        servers["sqlite"] = {
            "command": "uvx",
            "args": [
                "mcp-server-sqlite",
                "--db-path",
                "/D/Watchtower_Brain/watchtower.db"
            ]
        }

    config["mcpServers"] = servers

    # Write patched configuration back to disk
    with open(target_config, 'w') as f:
        json.dump(config, f, indent=2)

    print(f"[+] Architecture successfully realigned at {target_config}")
    print("[*] Standing by for NotebookLM Mango blueprint synthesis.")

if __name__ == "__main__":
    patch_architecture()
