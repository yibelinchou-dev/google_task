"""Local/demo FastAPI stub for TaskRefuge — not production."""
import uuid
from typing import Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

app = FastAPI(title="TaskRefuge API (local demo)", version="0.1.0-local")

# Local demo only. Waitlist and the task UI are static pages on another port.
# Allow localhost and 127.0.0.1 on any port. Do not use this in production.
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Accept"],
)

# Stable ids so the browser demo can keep local task edits across API restarts.
# (id, name, pinned)
_CATALOG = [
    ("inbox", "Inbox", True),
    ("today", "Today", True),
    ("errands", "Errands", True),
    ("work", "Work — Q4 launch", True),
    ("groceries", "Groceries", True),
    ("home", "Home projects", True),
    ("kids", "Kids — school", False),
    ("bills", "Bills & admin", False),
    ("health", "Health", False),
    ("reading", "Reading list", False),
    ("side", "Side project", False),
    ("travel", "Travel — Kyoto", False),
    ("house", "House hunting", False),
    ("car", "Car maintenance", False),
    ("family", "Family", False),
    ("gifts", "Gift ideas", False),
    ("recipes", "Recipes to try", False),
    ("move", "Apartment move", False),
    ("taxes", "Taxes", False),
    ("garden", "Garden", False),
    ("fitness", "Fitness", False),
    ("calls", "Calls to make", False),
    ("waiting", "Waiting on", False),
    ("someday", "Someday / maybe", False),
    ("writing", "Writing", False),
    ("oss", "Open source", False),
    ("jobs", "Job search", False),
    ("wedding", "Wedding planning", False),
    ("pets", "Pet care", False),
    ("subs", "Subscriptions", False),
    ("weekend", "Weekend", False),
    ("parents", "Parents", False),
    ("languages", "Languages", False),
    ("music", "Music practice", False),
    ("photos", "Photo backlog", False),
    ("budget", "Budget", False),
    ("clients", "Clients", False),
    ("research", "Research", False),
    ("packing", "Packing list", False),
    ("reference", "Reference", False),
]

LISTS = [
    {
        "id": list_id,
        "name": name,
        "pinned": pinned,
        "task_count": 4 + (index % 5),
    }
    for index, (list_id, name, pinned) in enumerate(_CATALOG)
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
