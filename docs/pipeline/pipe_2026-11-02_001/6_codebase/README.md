# PreFlight MVP (local scaffold)

Local/demo codebase for `pipe_2026-11-02_001` — pre-build demand & distribution toolkit for vibe-coded indie SaaS (PreFlight).

**Scope of this scaffold:** directory layout, stub FastAPI (health / waitlist / experiments / score / interviews), static PreFlight demo, waitlist page, docker-compose helper. Not production. No remote GitHub push in this pipeline run.

## Run API locally

```bash
cd apps/api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 3000
curl http://127.0.0.1:3000/health
```

## Demo

Open `apps/demo/index.html` in a browser, or publish that folder to Spacefast private.

## Tests

```bash
cd apps/api && source .venv/bin/activate
pip install -r requirements.txt
cd ../.. && PYTHONPATH=apps/api pytest -q
```
