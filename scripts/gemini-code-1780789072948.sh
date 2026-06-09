#!/usr/bin/env bash
set -euo pipefail

# Watchtower MCP Pre-flight Caching & Config Generator
readonly DB_PATH="/D/Watchtower_Brain/watchtower.db"
readonly CONFIG_PATH="/D/Watchtower_Ops/mcp.json"

echo "[*] Initiating pre-flight cache for Node-based MCP servers..."

# 1. Manually cache memory and devtools servers to prevent timeouts
# Note: Executing via npx caches them in the global npm store
echo "[*] Fetching @modelcontextprotocol/server-memory..."
npx -y @modelcontextprotocol/server-memory --help > /dev/null 2>&1 || true

echo "[*] Fetching Chrome DevTools MCP..."
npx -y @modelcontextprotocol/server-puppeteer --help > /dev/null 2>&1 || true
# Alternatively, if using a specific community devtools package, replace above line.

echo "[+] Node packages cached. Timeout vectors neutralized."

# 2. Generate the corrected mcp.json for the orchestrator
echo "[*] Generating corrected MCP architecture configuration..."

cat <<EOF > "$CONFIG_PATH"
{
  "mcpServers": {
    "sqlite": {
      "command": "uvx",
      "args": [
        "mcp-server-sqlite",
        "--db-path",
        "${DB_PATH}"
      ]
    },
    "memory": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-memory"
      ]
    },
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-puppeteer"
      ]
    }
  }
}
EOF

echo "[+] Configuration written to ${CONFIG_PATH}"
echo "[*] ACTION REQUIRED: Ensure 'uv' is installed in the container for Python execution."