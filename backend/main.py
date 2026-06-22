from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class ScanRequest(BaseModel):
    domain: str
    
@app.get("/")
def local():
    return {"status" : "on"}

@app.post("/scan")
def scan_domain(request: ScanRequest):
    return {"message": f"Scanning domain: {request.domain}"}

result = subprocess.run(["uvicorn main:app --reload"], capture_output=True, text=True)