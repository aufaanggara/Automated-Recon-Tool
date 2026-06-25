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
    result = subprocess.run(
        ["/home/aufa/go/bin/subfinder", "-d", request.domain, "-timeout", "30"],
        capture_output=True,
        text=True
    )
    return {"subdomains": result.stdout, "error": result.stderr}

    