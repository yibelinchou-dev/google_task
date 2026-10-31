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

def test_lists_seeded():
    r = client.get("/v1/lists")
    assert r.status_code == 200
    assert len(r.json()["lists"]) == 40
