"""Local/demo FastAPI stub for PreFlight — not production."""
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Literal
import uuid

app = FastAPI(title="PreFlight API (local demo)", version="0.1.0-local")

WAITLIST = []
EXPERIMENTS = [
    {"id": str(uuid.uuid4()), "name": "ICP interview sprint", "channel": "interview", "status": "planned", "reach": 0, "signups": 0},
    {"id": str(uuid.uuid4()), "name": "Waitlist smoke test", "channel": "landing", "status": "planned", "reach": 0, "signups": 0},
    {"id": str(uuid.uuid4()), "name": "Non-spam Show HN sequencing", "channel": "hackernews", "status": "planned", "reach": 0, "signups": 0},
    {"id": str(uuid.uuid4()), "name": "OSS adopter interviews", "channel": "oss", "status": "planned", "reach": 0, "signups": 0},
    {"id": str(uuid.uuid4()), "name": "Star→user conversion test", "channel": "github", "status": "planned", "reach": 0, "signups": 0},
]
INTERVIEWS = []


class WaitlistIn(BaseModel):
    email: EmailStr
    paid_intent: bool = False
    product_one_liner: Optional[str] = None


class ExperimentIn(BaseModel):
    name: str
    channel: str
    reach: int = 0
    replies: int = 0
    signups: int = 0
    status: Literal["planned", "running", "done", "killed"] = "planned"


class InterviewIn(BaseModel):
    persona: str
    notes: str
    wtp: Optional[int] = Field(default=None, ge=0, le=10)
    icp_fit: Optional[int] = Field(default=None, ge=0, le=10)


@app.get("/health")
def health():
    return {"status": "healthy", "env": "local-demo", "product": "PreFlight"}


@app.post("/v1/waitlist")
def waitlist(body: WaitlistIn):
    entry = {"id": str(uuid.uuid4()), "email": body.email, "paid_intent": body.paid_intent}
    WAITLIST.append(entry)
    return {"ok": True, **entry}


@app.get("/v1/experiments")
def list_experiments():
    return {"experiments": EXPERIMENTS}


@app.post("/v1/experiments")
def create_experiment(body: ExperimentIn):
    row = {"id": str(uuid.uuid4()), **body.model_dump()}
    EXPERIMENTS.append(row)
    return {"ok": True, "id": row["id"]}


@app.post("/v1/interviews")
def create_interview(body: InterviewIn):
    row = {"id": str(uuid.uuid4()), **body.model_dump()}
    INTERVIEWS.append(row)
    return {"ok": True, "id": row["id"]}


@app.get("/v1/score")
def score(
    interviews: Optional[int] = None,
    waitlist: Optional[int] = None,
    paid_intent: Optional[int] = None,
    experiments_done: Optional[int] = None,
):
    iv = interviews if interviews is not None else len(INTERVIEWS)
    wl = waitlist if waitlist is not None else len(WAITLIST)
    pi = paid_intent if paid_intent is not None else sum(1 for w in WAITLIST if w.get("paid_intent"))
    ed = experiments_done if experiments_done is not None else sum(1 for e in EXPERIMENTS if e.get("status") == "done")
    points = iv * 8 + min(wl, 80) * 0.5 + pi * 4 + ed * 10
    rationale = [
        f"interviews={iv} (target ≥12)",
        f"waitlist={wl} (target ≥80)",
        f"paid_intent={pi} (target ≥12)",
        f"experiments_done={ed}",
    ]
    if iv >= 8 and (pi >= 5 or wl >= 40) and ed >= 1:
        decision = "continue"
    elif iv >= 3 or wl >= 10 or ed >= 1:
        decision = "more_data"
    else:
        decision = "kill" if iv == 0 and wl == 0 else "more_data"
    # Soft kill only when evidence is weakly negative after some data
    if iv >= 8 and pi == 0 and wl < 20 and ed >= 2:
        decision = "kill"
        rationale.append("Weak WTP after interviews + experiments")
    return {"decision": decision, "score": round(points, 1), "rationale": rationale}
