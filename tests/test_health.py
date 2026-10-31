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
    lists = r.json()["lists"]
    assert len(lists) == 40
    assert lists[0]["id"] == "inbox"
    assert sum(1 for item in lists if item["pinned"]) >= 3


def test_cors_allows_local_origin():
    origin = "http://127.0.0.1:8080"
    r = client.get("/v1/lists", headers={"Origin": origin})
    assert r.status_code == 200
    assert r.headers["access-control-allow-origin"] == origin


def test_cors_preflight_for_waitlist():
    origin = "http://localhost:8080"
    r = client.options(
        "/v1/waitlist",
        headers={
            "Origin": origin,
            "Access-Control-Request-Method": "POST",
            "Access-Control-Request-Headers": "content-type",
        },
    )
    assert r.status_code == 200
    assert r.headers["access-control-allow-origin"] == origin
    assert "POST" in r.headers["access-control-allow-methods"]


def test_cors_blocks_public_origin():
    r = client.get("/health", headers={"Origin": "https://example.com"})
    assert "access-control-allow-origin" not in r.headers
