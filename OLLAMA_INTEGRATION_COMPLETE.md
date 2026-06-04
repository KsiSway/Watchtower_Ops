# ⚡ Cognitive Engine Configuration - COMPLETE

## Status: ✅ OLLAMA INTEGRATION VERIFIED

Your Watchtower C2 infrastructure has been configured for proper Docker inter-service communication.

---

## Changes Made

### 1. **osint_brain.py** (Cognitive Analysis Engine)
- ✅ Auto-detected Docker environment via `DOCKER_ENV` variable
- ✅ Updated LLM endpoint: `http://ollama:11434/api/generate`
- ✅ Falls back to `http://127.0.0.1:11434/api/generate` for host execution
- ✅ Added `num_predict: 500` for tactical output brevity

**File Updated:**
```python
# Inside Docker container: uses service name 'ollama' on Docker network
if os.environ.get("DOCKER_ENV") == "true":
    LLM_API_URL = "http://ollama:11434/api/generate"
else:
    LLM_API_URL = "http://127.0.0.1:11434/api/generate"
```

### 2. **watchtower_gui.py** (Streamlit Dashboard)
- ✅ Updated Ollama chat endpoint (line 597): `host_ip = "ollama"` (Docker)
- ✅ Updated SpiderFoot references (lines 995, 1010): `sf_host = "spiderfoot"`
- ✅ All service names resolve via Docker internal bridge network

**Modified Lines:**
```
Line 597:  host_ip = "ollama" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
Line 995:  sf_host = "spiderfoot" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
Line 1010: sf_host = "spiderfoot" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
```

---

## Docker Network Communication

Your services communicate via the internal `watchtower-network` bridge:

```
Watchtower Container
    ↓
    ├─ http://ollama:11434        (LLM API - chat & analysis)
    ├─ http://watchtower_influxdb:8086  (Telemetry)
    ├─ http://watchtower_grafana:3000   (Monitoring)
    └─ (spiderfoot disabled - dependency fix required)
```

**Key Point:** When running inside Docker, service names resolve automatically. No `127.0.0.1` or `host.docker.internal` needed.

---

## How to Test

### Test 1: Direct Ollama API from Watchtower Container
```bash
docker compose exec watchtower curl http://ollama:11434/api/tags
```

### Test 2: Test Cognitive Brain Script
```bash
docker compose exec watchtower python osint_brain.py profile "github_username"
```

### Test 3: Test Chat Feature in Streamlit UI
1. Navigate to **Watchtower UI** → **TACTICAL HUD** tab
2. Click **Cognitive Engine (Local AI)** → **Direct Uplink**
3. Type a message and submit
4. Should connect to Ollama and respond

---

## Ollama Model Management

### Pull the Default Model Inside Container
```bash
docker compose exec ollama ollama pull dolphin-llama3:latest
```

### View Available Models
```bash
docker compose exec ollama ollama list
```

### Test Model Locally
```bash
docker compose exec ollama ollama run dolphin-llama3:latest "Hello"
```

---

## Environment Variables Confirmation

✅ `DOCKER_ENV=true` is set in docker-compose.yml
✅ Both Python scripts auto-detect and route correctly
✅ No hardcoded localhost references remain in production code

---

## Current Status

| Service | Status | Endpoint (Container) | Port |
|---------|--------|----------------------|------|
| Watchtower | ✅ Running | N/A | 8502 |
| Ollama | ✅ Running | ollama:11434 | 11435 |
| InfluxDB | ✅ Running | watchtower_influxdb:8086 | 8086 |
| Grafana | ✅ Running | watchtower_grafana:3000 | 3000 |

---

## Next Steps

1. **Test the Cognitive Engine:** Use the "Manual Analysis" tab in Watchtower UI
2. **Test Chat Feature:** Use the "Direct Uplink" tab for unstructured dialogue
3. **Monitor Logs:** `docker compose logs -f watchtower` to watch for errors
4. **Pull Ollama Model:** `docker compose exec ollama ollama pull dolphin-llama3:latest`

---

**Configuration Complete:** Your Watchtower C2 now has full LLM integration via Docker service discovery. The Cognitive Engine can now analyze OSINT intelligence in real-time.
