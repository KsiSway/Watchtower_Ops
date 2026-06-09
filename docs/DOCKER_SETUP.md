# Watchtower Docker Compose Setup

## What Was Added

Your `docker-compose.yml` now includes 5 services:

### 1. **watchtower** (Main Application)

- Streamlit UI on port **8501**
- Mounts Docker socket for ADB/container commands
- All API keys loaded from `.env`

### 2. **ollama** (Local LLM)

- For `dolphin-llama3:latest` inference
- Port **11434**
- Required for the "Direct Uplink" chat tab in your GUI

### 3. **influxdb** (Time-Series Database)

- Port **8086**
- Stores telemetry data from your devices
- User: `lance` / Pass: `LANCE-1985-SECURE`

### 4. **grafana** (Monitoring Dashboard)

- Port **3000**
- User: `KsiSway` / Pass: `DOCnomore1!`
- Connected to InfluxDB for visualization

### 5. **spiderfoot** (OSINT Framework)

- Port **5001**
- Built from `./spiderfoot/Dockerfile`
- Embedded in your main UI

## Environment Variables

All API keys are loaded from `.env` file which was created with your existing credentials from the `.env` file in root.

## How to Start

### On Linux/Mac

```bash
chmod +x start-watchtower.sh
./start-watchtower.sh
```

### On Windows

```powershell
.\start-watchtower.bat
```

### Or manually

```bash
docker compose up -d
```

## Access Your Services

Once running:

- **Streamlit UI**: <http://localhost:8501>
- **Grafana**: <http://localhost:3000>
- **SpiderFoot**: <http://localhost:5001>
- **InfluxDB**: <http://localhost:8086>
- **Ollama API**: <http://localhost:11434>

## Useful Commands

```bash
# View all services
docker compose ps

# View logs
docker compose logs -f watchtower

# View specific service
docker compose logs -f ollama

# Stop everything
docker compose down

# Stop and remove volumes
docker compose down -v

# Restart watchtower app
docker compose restart watchtower

# Execute command in container
docker compose exec watchtower bash

# Pull latest Ollama model
docker compose exec ollama ollama pull dolphin-llama3:latest
```

## Important Notes

1. **Ollama Model**: The first time you use the chat feature, it will download `dolphin-llama3:latest`. This may take several minutes.

2. **Docker Socket**: The watchtower container mounts `/var/run/docker.sock` to run ADB and other docker commands from inside the container.

3. **Volumes**: All persistent data is stored in Docker volumes (influxdb_data, grafana_data, spiderfoot_data, ollama_data).

4. **Networking**: All services communicate via the internal `watchtower-network` bridge.

5. **Build Time**: Initial `docker compose build` may take 5-10 minutes as it builds the Watchtower and SpiderFoot images.

## Files Modified/Created

- ✅ `docker-compose.yml` — Updated with all services
- ✅ `.env` — Environment variables (from your existing .env)
- ✅ `Dockerfile` — Added Streamlit environment variables
- ✅ `start-watchtower.sh` — Startup script for Linux/Mac
- ✅ `start-watchtower.bat` — Startup script for Windows

Ready to run!
