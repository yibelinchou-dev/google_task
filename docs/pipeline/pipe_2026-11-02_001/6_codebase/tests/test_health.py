import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "apps" / "api"))
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"
    assert r.json()["product"] == "PreFlight"

def test_experiments_seeded():
    r = client.get("/v1/experiments")
    assert r.status_code == 200
    assert len(r.json()["experiments"]) >= 5

def test_waitlist_and_score():
    r = client.post("/v1/waitlist", json={"email": "founder@example.com", "paid_intent": True})
    assert r.status_code == 200 and r.json()["ok"]
    s = client.get("/v1/score", params={"interviews": 3, "waitlist": 10, "paid_intent": 2, "experiments_done": 1})
    assert s.status_code == 200
    assert s.json()["decision"] in {"kill", "continue", "more_data"}
