#!/usr/bin/env bash
set -euo pipefail

# Watchtower MCP Pre-flight Caching & Config Generator
readonly DB_PATH="D:/Watchtower_Brain/watchtower.db"
readonly CONFIG_PATH="/c/Users/Lance/.gemini/config/mcp_config.json"
readonly DEVTOOLS_BIN="D:\\Watchtower_Ops\\chrome-devtools-mcp\\build\\src\\bin\\chrome-devtools-mcp.js"

echo "[*] Initiating pre-flight cache for Node-based MCP servers..."

# 1. Manually cache memory server to prevent timeouts
# Note: Executing via npx caches them in the global npm store
echo "[*] Fetching @beledarian/mcp-local-memory..."
npx -y @beledarian/mcp-local-memory --help > /dev/null 2>&1 || true

# We skip caching chrome-devtools via npx since we execute it from the local binary directly.

echo "[+] Node packages cached. Timeout vectors neutralized."

# 2. Safely merge the corrected MCP architecture configuration into the IDE's config
echo "[*] Generating and merging corrected MCP architecture configuration..."

TMP_JSON=$(mktemp)

if [ -f "$CONFIG_PATH" ]; then
    # Use jq to safely update the specific servers without destroying the others
    jq --arg db "$DB_PATH" --arg devtools "$DEVTOOLS_BIN" '.mcpServers.sqlite = {
      "command": "uvx",
      "args": [
        "mcp-server-sqlite",
        "--db-path",
        $db
      ]
    } | .mcpServers.memory = {
      "command": "npx",
      "args": [
        "-y",
        "@beledarian/mcp-local-memory"
      ]
    } | .mcpServers["local-chrome-devtools"] = {
      "command": "node",
      "args": [
        $devtools,
        "--browser-url=http://host.docker.internal:9222",
        "--isolated"
      ]
    }' "$CONFIG_PATH" > "$TMP_JSON"
else
    # If the file somehow doesn't exist, create it from scratch
    cat <<EOF > "$TMP_JSON"
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
        "@beledarian/mcp-local-memory"
      ]
    },
    "local-chrome-devtools": {
      "command": "node",
      "args": [
        "${DEVTOOLS_BIN}",
        "--browser-url=http://host.docker.internal:9222",
        "--isolated"
      ]
    }
  }
}
EOF
fi

mv "$TMP_JSON" "$CONFIG_PATH"

echo "[+] Configuration safely injected into ${CONFIG_PATH}"
echo "[*] ACTION REQUIRED: Ensure 'uv' is installed in the container for Python execution."
