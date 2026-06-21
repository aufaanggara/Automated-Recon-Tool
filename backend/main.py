from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ScanRequest(BaseModel):
    domain: str
    
@app.get("/")
def local():
    return {"status" : "on"}

@app.post("/scan")
def scan_domain(request: ScanRequest):
    return {"message": f"Scanning domain: {request.domain}"}