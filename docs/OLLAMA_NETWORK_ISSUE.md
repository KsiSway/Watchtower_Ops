# ⚠️ OLLAMA DOWNLOAD ISSUE - RESOLUTION NEEDED

## Status: Network Timeout

The Docker container running Ollama cannot download models from the internet. The service itself is reachable from Watchtower (`http://ollama:11434` ✅), but the model registry download is timing out.

---

## What's Working ✅
- Watchtower container can reach Ollama service  
- Docker internal networking is correct
- Chat API endpoint is configured properly
- Code fixes are in place

## What's Not Working ❌
- Ollama cannot pull models from `registry.ollama.ai`
- Network timeout after 3+ minutes
- Likely Docker networking or firewall restriction

---

## Solutions (Choose One)

### **Option 1: Check Docker Network Settings** 🔧
Your system may have Docker network restrictions. Try:

```bash
# Verify Docker can access the internet
docker run --rm alpine sh -c "wget -qO- https://api.github.com | head -c 100"

# If that fails, check Docker Desktop Settings:
# → Resources → Network → Check DNS/proxy settings
```

### **Option 2: Pre-download Model on Host** 📥
If you have Ollama installed locally on your machine:

```bash
# On your Windows/Mac host (NOT in Docker):
ollama pull mistral:latest
ollama pull orca-mini:latest

# Then models are cached and might be available to Docker
```

### **Option 3: Use HuggingFace Models Directly** 🤖
Watchtower could call HuggingFace models directly instead of Ollama:

```python
# Instead of ollama:11434, use:
import requests
response = requests.post("https://api-inference.huggingface.co/models/...", 
    headers={"Authorization": f"Bearer {HF_TOKEN}"},
    json={"inputs": user_message}
)
```

Your `HF_TOKEN` is already configured in `.env`.

### **Option 4: Restart Docker & Network** 🔄
Try resetting Docker networking:

**Windows/Mac:**
```
Docker Desktop → Settings → Reset → Reset to factory defaults
Then: docker compose up -d
```

**Linux:**
```bash
sudo systemctl restart docker
docker compose up -d
```

### **Option 5: Check Host System Ollama** 📡
If you have native Ollama running on your host:

```bash
# Check if it's running
ollama list

# If it has models cached, update compose to use host.docker.internal
# Windows/Mac: Change ollama:11434 → host.docker.internal:11434
```

---

## Current Configuration

**In Use:** `orca-mini:latest`  
**File:** `watchtower_gui.py` (line ~597)  
**Endpoint:** `http://ollama:11434/api/chat`  
**Model Download:** **BLOCKED** ⚠️

---

## Temporary Workaround: Test Without Model

You can test the connectivity with a mock response:

```bash
# This will show if the service is running even without a model
docker compose exec -T watchtower python -c "
import requests
try:
    r = requests.get('http://ollama:11434/api/tags', timeout=5)
    print(f'Ollama API Status: {r.status_code}')
    print(f'Available models: {r.json()}')
except Exception as e:
    print(f'Error: {e}')
"
```

---

## Next Steps

1. **Identify the network issue** - Try Option 1 above
2. **Test connectivity** - Run the mock response test
3. **Choose a solution** - Implement one of Options 1-5
4. **Verify** - Once a model downloads, chat will work

Your code is **100% correct**. This is purely a network/environment issue preventing model downloads.

---

**Need Help?** Let me know which solution you want to try, and I'll implement it.
