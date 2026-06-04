# Watchtower C2 Dashboard Migration to Docker

## Purpose
Migrate the existing `watchtower_gui.py` Streamlit dashboard from the host environment to the newly provisioned Docker Compose stack (`watchtower-stack`), enabling better portability, isolation, and reverse proxy routing via Traefik.

## Architecture & Integration Strategy

### 1. Dockerfile & OS Dependencies
The Docker container will run a Debian-based Linux environment (`python:3.11-slim`). To support the various OSINT and operational capabilities of the dashboard, the following OS-level packages will be installed:
- `android-tools-adb` (for communicating with S25 Edge and Tab A8)
- `tesseract-ocr`, `libtesseract-dev` (for optical character recognition)
- `nmap` (for mesh network scanning)
- `iputils-ping`

Python dependencies will be installed directly from the existing `requirements.txt` via `pip install -r requirements.txt`.

### 2. File Strategy (Volume Mounting & .dockerignore)
Instead of copying the codebase into the container at build time, we will mount the entire project directory from the D: drive (`D:\Watchtower_Ops`) into the `/app` path inside the container. 
- **Benefits:** Live updates to Python scripts will immediately reflect in the container without rebuilding. The container will also read and write logs (`C2_Activity.log`, `Watchtower_Log.json`) directly to the host directory, ensuring continuity of the Master Intelligence Ledger.
- **Docker Compose Update:** The `app` service will be configured with a volume mapping `- D:\Watchtower_Ops:/app`.
- **.dockerignore:** We will ensure a `.dockerignore` file exists to exclude the local Windows virtual environment (e.g., `venv`, `env`, `.venv`) so it doesn't conflict with the Linux container's Python environment.

### 3. Code Adaptations (`watchtower_gui.py`)

#### Localhost Resolution
The dashboard currently references `http://127.0.0.1:5001` (Spiderfoot) and `http://127.0.0.1:11434` (Ollama). Within a Docker container, `127.0.0.1` refers to the container itself.
- **Change:** Replace `127.0.0.1` with `host.docker.internal` across the codebase, allowing the container to egress to the host's localhost interfaces.

#### Windows Subsystem for Linux (WSL) Removal
The script currently uses `wsl` commands to execute Tesseract and parse paths (e.g., `subprocess.run(["wsl", "python3", wsl_script, wsl_img])`).
- **Change:** Since the Docker container is a native Linux environment, the `wsl` and `wslpath` wrappers are obsolete and will fail. These calls will be replaced with direct `python3` subprocess executions using standard POSIX paths.

#### Google Coral Edge TPU Handling
USB passthrough for the Edge TPU (Coral) from a Windows host into Docker Desktop is highly complex and unsupported in basic setups.
- **Change:** Introduce a Docker execution check (e.g., checking for `DOCKER_ENV` or `/.dockerenv`). If running inside Docker, the Edge TPU vision features will be gracefully disabled in the UI (showing a "Not Available in Docker" status) to prevent application crashes and `FileNotFound` errors for the Coral environment.

### 4. Networking
- The Streamlit application will be bound to `0.0.0.0:8501`.
- Traefik labels in `docker-compose.yml` will route traffic seamlessly.
- An explicit port mapping `8501:8501` will remain for direct access.

## Success Criteria
- The dashboard is accessible at `http://localhost:8501`.
- Autonomous Hunt, Dark Web Tor Extraction, and ADB screen captures continue to function.
- OCR works natively via the container's Tesseract installation.
- Application does not crash when attempting to load the Edge TPU vision models.