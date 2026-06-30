{
  "mcpServers": {
    "memory": {
      "command": "npx.cmd",
      "args": [
        "--yes",
        "-y",
        "@modelcontextprotocol/server-memory"
      ],
      "env": {
        "MEMORY_DB_PATH": "./.memory/memory.db"
      }
    }
  }
}
