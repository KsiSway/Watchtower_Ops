@echo off
REM Watchtower Docker Compose Startup Script for Windows

echo ⚡ Starting Watchtower C2 Infrastructure...

REM Pull all base images
echo [1/4] Pulling base images...
docker pull influxdb:2.7
docker pull grafana/grafana:latest
docker pull ollama/ollama:latest

REM Build custom images
echo [2/4] Building custom Watchtower image...
docker compose build

REM Start all services
echo [3/4] Starting services...
docker compose up -d

REM Wait for services to be ready
echo [4/4] Waiting for services to initialize...
timeout /t 15

REM Display service status
echo.
echo ✅ Watchtower Stack Started
echo.
echo 📊 Access Points:
echo   * Streamlit UI:     http://localhost:8501
echo   * Grafana:          http://localhost:3000 (user: KsiSway)
echo   * SpiderFoot:       http://localhost:5001
echo   * InfluxDB:         http://localhost:8086
echo   * Ollama API:       http://localhost:11434
echo.
echo 🔧 Docker Commands:
echo   View logs:          docker compose logs -f watchtower
echo   Stop stack:         docker compose down
echo   Remove volumes:     docker compose down -v
echo.

REM Show container status
echo 📦 Container Status:
docker compose ps

pause
