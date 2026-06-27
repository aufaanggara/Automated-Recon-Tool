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
    subdomains = [s for s in result.stdout.split("\n") if s]
    httpx_result = subprocess.run(
        ["/home/aufa/go/bin/httpx", "-silent"],
        input="\n".join(subdomains),
        capture_output=True,
        text=True
    )
    live_hosts = [s for s in httpx_result.stdout.split("\n") if s]
    return {"domain": request.domain, "subdomains": subdomains, "live hosts": live_hosts}