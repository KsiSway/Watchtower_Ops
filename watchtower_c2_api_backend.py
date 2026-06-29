# [Environment: Host OS (OptiPlex) - Python Virtual Environment]

import asyncio
import subprocess
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Watchtower C2 Execution API")

# Configure CORS to allow the React dashboard to communicate with this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Restrict to 192.168.68.x subnet in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TargetPayload(BaseModel):
    target: str

class NmapPayload(BaseModel):
    ip_address: str

@app.get("/api/status")
async def get_status():
    """Health check for the C2 API."""
    return {"status": "nominal", "environment": "OptiPlex Host (192.168.68.110)"}

@app.post("/api/execute/mesh-sync")
async def execute_mesh_sync():
    """Triggers the local mesh baseline synchronization script."""
    try:
        # Utilize asyncio.create_subprocess_exec for non-blocking execution
        process = await asyncio.create_subprocess_exec(
            "python", "mesh_sync_skill.py",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        
        if process.returncode != 0:
             raise HTTPException(status_code=500, detail=f"Execution failed: {stderr.decode()}")
             
        return {"output": stdout.decode().strip(), "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/execute/nmap")
async def execute_nmap(payload: NmapPayload):
    """Triggers an active perimeter scan against a specific mesh node."""
    # SECURITY BINDING: Ensure target is within the local mesh subnet
    if not payload.ip_address.startswith("192.168.68."):
        raise HTTPException(status_code=403, detail="[!] ERROR: Target IP outside authorized 192.168.68.x boundary.")
        
    try:
        process = await asyncio.create_subprocess_exec(
            "nmap", "-sV", "-T4", "-F", payload.ip_address,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {"output": stdout.decode().strip(), "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # Bind to 0.00.0.0 to allow the Docker container shell to reach the host API
    print("[*] Initializing Watchtower C2 Backend API on 0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)