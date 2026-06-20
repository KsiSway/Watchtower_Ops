# Multi-stage build: compile stage (keeps build tools out of final image)
FROM python:3.11-slim as builder

WORKDIR /build

# Install build dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Runtime stage: lean final image
FROM python:3.11-slim

WORKDIR /app

# Install runtime OS dependencies only (no build tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    android-tools-adb \
    tesseract-ocr \
    libtesseract-dev \
    nmap \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# Copy Python packages from builder stage
COPY --from=builder /root/.local /root/.local

# Set PATH to use local Python packages
ENV PATH=/root/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_HEADLESS=true

COPY requirements.txt .

# Copy application code last (most frequently changed layer)
COPY . .

EXPOSE 8501

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501').getcode() == 200" || exit 1

CMD ["streamlit", "run", "watchtower_gui.py", "--server.port=8501", "--server.address=0.0.0.0"]
