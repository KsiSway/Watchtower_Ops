# Watchtower C2 Migration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Migrate the Watchtower C2 Streamlit dashboard to run natively within a Docker container while retaining full interoperability with host-dependent tools.

**Architecture:** We will update `docker-compose.yml` to mount the live codebase from the host (`D:\Watchtower_Ops`) into the container. We will modify the `Dockerfile` to include necessary system packages (ADB, Tesseract, Nmap). The `watchtower_gui.py` application will be refactored to disable WSL wrappers for Tesseract, skip Edge TPU processing when containerized, and route network calls to `host.docker.internal` instead of `127.0.0.1`.

**Tech Stack:** Docker, Python, Streamlit, Tesseract OCR, ADB, Nmap

---

### Task 1: Update `docker-compose.yml` and `.dockerignore`

**Files:**
- Modify: `D:\Watchtower\watchtower-stack\docker-compose.yml`
- Create: `D:\Watchtower\watchtower-stack\app\.dockerignore`

- [ ] **Step 1: Update the volume mount and environment variable in `docker-compose.yml`**

Replace the `build: context` and `volumes` configuration for the `app` service to point to `D:\Watchtower_Ops` instead of the local `./app` directory, and add the `DOCKER_ENV=true` variable.

```yaml
  app:
    build: 
      context: D:\Watchtower_Ops
      dockerfile: Dockerfile
    container_name: watchtower-app
    depends_on:
      - db
      - cache
    environment:
      - DATABASE_URL=postgresql://watchtower:${POSTGRES_PASSWORD:-secure_password_here}@db:5432/watchtower
      - REDIS_URL=redis://cache:6379/0
      - DOCKER_ENV=true
    volumes:
      - D:\Watchtower_Ops:/app
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.app.rule=Host(`localhost`)"
      - "traefik.http.services.app.loadbalancer.server.port=8501"
    ports:
      - "8501:8501"
    restart: unless-stopped
    networks:
      - watchtower-net
```

- [ ] **Step 2: Create the `.dockerignore` file**

```text
.git
.venv
venv
env
__pycache__
*.pyc
*.pyo
*.pyd
.Python
```

- [ ] **Step 3: Commit**

```bash
git add docker-compose.yml app/.dockerignore
git commit -m "chore: configure docker compose volume mounts and ignore files"
```

### Task 2: Update the `Dockerfile`

**Files:**
- Modify: `D:\Watchtower_Ops\Dockerfile` (Create this file since we are shifting the context to `Watchtower_Ops`)

- [ ] **Step 1: Create the new Dockerfile in the project root**

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y \
    android-tools-adb \
    tesseract-ocr \
    libtesseract-dev \
    nmap \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "watchtower_gui.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

- [ ] **Step 2: Commit**

```bash
git add Dockerfile
git commit -m "chore: add Dockerfile with OSINT OS dependencies"
```

### Task 3: Refactor Localhost Network References

**Files:**
- Modify: `C:\Users\Lance\Watchtower_Ops\watchtower_gui.py`

- [ ] **Step 1: Update API URLs to use `host.docker.internal`**

Search for `127.0.0.1:11434` and `127.0.0.1:5001` in `watchtower_gui.py` and replace them.

```python
# Replace:
# response = requests.post("http://127.0.0.1:11434/api/chat", json=payload, timeout=300)
# With:
                                host_ip = "host.docker.internal" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
                                response = requests.post(f"http://{host_ip}:11434/api/chat", json=payload, timeout=300)

# Replace:
# st.link_button("Open Dedicated Window", "http://127.0.0.1:5001", use_container_width=True)
# With:
    sf_host = "host.docker.internal" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
    st.link_button("Open Dedicated Window", f"http://{sf_host}:5001", use_container_width=True)

# Replace:
# components.iframe("http://127.0.0.1:5001", height=900, scrolling=True)
# With:
    sf_host = "host.docker.internal" if os.environ.get("DOCKER_ENV") == "true" else "127.0.0.1"
    components.iframe(f"http://{sf_host}:5001", height=900, scrolling=True)
```

- [ ] **Step 2: Commit**

```bash
git add watchtower_gui.py
git commit -m "refactor: use host.docker.internal for local API services"
```

### Task 4: Refactor WSL Tesseract Wrappers

**Files:**
- Modify: `C:\Users\Lance\Watchtower_Ops\watchtower_gui.py`

- [ ] **Step 1: Replace WSL subprocess calls with native Linux calls**

Search for the OCR Engine Integration block and update it.

```python
                    # OCR Engine Integration
                    st.markdown("---")
                    st.markdown("### 👁️ Optical Character Recognition (Host CPU)")
                    with st.spinner("Extracting hard text via Tesseract..."):
                        is_docker = os.environ.get("DOCKER_ENV") == "true"
                        
                        if is_docker:
                            ocr_result = subprocess.run(
                                ["python3", os.path.join(BASE_DIR, "osint_ocr_engine.py"), img_path],
                                capture_output=True, text=True
                            )
                        else:
                            # Convert Windows paths to WSL paths for Linux-based Tesseract execution
                            wsl_script = subprocess.check_output(["wsl", "wslpath", os.path.join(BASE_DIR, "osint_ocr_engine.py")]).decode().strip()
                            wsl_img = subprocess.check_output(["wsl", "wslpath", img_path]).decode().strip()
                            
                            ocr_result = subprocess.run(
                                ["wsl", "python3", wsl_script, wsl_img],
                                capture_output=True, text=True
                            )
```

- [ ] **Step 2: Commit**

```bash
git add watchtower_gui.py
git commit -m "refactor: use native python execution for OCR when containerized"
```

### Task 5: Handle Edge TPU in Docker

**Files:**
- Modify: `C:\Users\Lance\Watchtower_Ops\watchtower_gui.py`

- [ ] **Step 1: Disable TPU Vision Analysis when containerized**

Search for the Edge TPU Classification block and add the `DOCKER_ENV` check.

```python
            with st.status("Analyzing visual data via Edge TPU...", expanded=True) as status:
                is_docker = os.environ.get("DOCKER_ENV") == "true"
                model_dir = r"C:\Users\Lance\coral_test"
                model_path = os.path.join(model_dir, "imagenet_model.tflite")
                label_path = os.path.join(model_dir, "imagenet_labels.txt")
                
                if is_docker:
                    st.warning("TPU Vision Analysis is disabled when running in Docker.")
                    status.update(label="Analysis Disabled", state="complete")
                elif os.path.exists(model_path) and os.path.exists(label_path):
```

Also, update the local hardware diagnostic button in the sidebar:
```python
    if st.button("Verify TPU Hardware Uplink", use_container_width=True):
        with st.spinner("Probing Google Coral Edge TPU hardware..."):
            is_docker = os.environ.get("DOCKER_ENV") == "true"
            if is_docker:
                st.error("TPU hardware diagnostics are disabled in Docker.")
            else:
                try:
```

- [ ] **Step 2: Commit**

```bash
git add watchtower_gui.py
git commit -m "feat: gracefully disable Edge TPU features when containerized"
```
