# [Environment: Python Virtual Environment]
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Watchtower Administrative API")

# PATCH: Explicit allowed origins to satisfy strict browser CORS requirements
allowed_origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://192.168.68.110:3000",
    "http://192.168.68.110:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TargetPayload(BaseModel):
    target: str

class NodeDiagnosticRequest(BaseModel):
    ip_address: str

@app.get("/api/status")
async def get_status():
    """Health check for the Administrative API."""
    return {"status": "nominal", "environment": "Isolated Python Virtual Environment"}

@app.post("/api/execute/mesh-sync")
async def execute_mesh_sync():
    """Triggers the routine topology synchronization."""
    try:
        process = await asyncio.create_subprocess_exec(
            "python", "mesh_sync_skill.py",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        
        if process.returncode != 0:
             raise HTTPException(status_code=500, detail=f"Synchronization failed: {stderr.decode()}")
             
        return {"output": stdout.decode().strip(), "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/execute/interrogate")
async def execute_interrogate(payload: NodeDiagnosticRequest):
    """Triggers a localized service diagnostic against a specific mesh node."""
    if not payload.ip_address.startswith("192.168.68."):
        raise HTTPException(status_code=403, detail="[!] ERROR: Target IP outside authorized 192.168.68.x boundary.")
        
    try:
        process = await asyncio.create_subprocess_exec(
            "python", "mesh_interrogate.py", payload.ip_address,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        
        if process.returncode != 0:
             raise HTTPException(status_code=500, detail=f"Diagnostic failed: {stderr.decode()}")
             
        return {"output": stdout.decode().strip(), "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    print("[*] Initializing Watchtower Administrative API on 0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
