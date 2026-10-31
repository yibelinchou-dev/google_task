"""Local/demo FastAPI stub for TaskRefuge — not production."""
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

app = FastAPI(title="TaskRefuge API (local demo)", version="0.1.0-local")

LISTS = [
    {"id": str(uuid.uuid4()), "name": f"List {i}", "pinned": i < 3, "task_count": 10 + i}
    for i in range(1, 41)
]


class WaitlistIn(BaseModel):
    email: EmailStr
    list_count_estimate: Optional[int] = None


@app.get("/health")
def health():
    return {"status": "healthy", "env": "local-demo"}


@app.get("/v1/lists")
def lists():
    return {"lists": LISTS}


@app.post("/v1/waitlist")
def waitlist(body: WaitlistIn):
    return {"ok": True, "id": str(uuid.uuid4()), "email": body.email}


@app.post("/v1/import/google-tasks")
def start_import():
    return {"job_id": str(uuid.uuid4()), "status": "queued", "note": "stub — no Google calls"}
