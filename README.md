# TaskRefuge (local demo)

Local **demo** for a multi-list task manager for people leaving Google Tasks. This is not a production service, not an App Store app, and not a hosted product.

What is included: a clickable task UI, a stub FastAPI app, a static waitlist page, optional local Postgres/Redis via Docker Compose, a health check test, and placeholder iOS notes. The Google Tasks import route is a stub and does not call Google. Tasks you add, complete, or delete in the demo stay in the browser.

## Run the API (port 3000)

```bash
cd apps/api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 3000
curl http://127.0.0.1:3000/health
```

Useful stub routes: `GET /health`, `GET /v1/lists`, `POST /v1/waitlist`, `POST /v1/import/google-tasks`.

`GET /v1/lists` returns 40 mock lists. Several are pinned (Inbox, Today, Errands, and others). The API does not store tasks.

## Open the task demo

With the API already listening on port 3000, serve this repo from another terminal:

```bash
python3 -m http.server 8080
```

Open [http://127.0.0.1:8080/apps/demo/](http://127.0.0.1:8080/apps/demo/).

The page loads lists from `GET http://127.0.0.1:3000/v1/lists` (or `localhost:3000` if you opened the page as `localhost`). The sidebar shows pinned lists and the rest. Select a list, then add a task, mark one complete, or delete one. Those edits are saved in `localStorage` on this browser only. If the API is not running, the page falls back to the same offline mock lists and labels the status **Offline mock**.

You can also serve just the demo folder. Then the page is [http://127.0.0.1:8080/](http://127.0.0.1:8080/):

```bash
python3 -m http.server 8080 --directory apps/demo
```

## Run the waitlist page

With the API on port 3000 and the repo server from the previous section still running, open [http://127.0.0.1:8080/apps/waitlist/](http://127.0.0.1:8080/apps/waitlist/). The form posts JSON to `http://127.0.0.1:3000/v1/waitlist`.

Or serve that folder alone:

```bash
python3 -m http.server 8080 --directory apps/waitlist
```

You can also exercise the endpoint without a browser:

```bash
curl -s -X POST http://127.0.0.1:3000/v1/waitlist \
  -H 'Content-Type: application/json' \
  -d '{"email":"you@example.com","list_count_estimate":12}'
```

## CORS

CORS allows pages served from `http://localhost` or `http://127.0.0.1` on any port, so the demo and waitlist can call the API from another local port. Other origins are rejected. Opening the HTML files via `file://` still will not work; use the local static server. This rule is for the local demo only.

## Docker (optional, local only)

```bash
docker compose -f docker/docker-compose.yml up -d
```

Postgres and Redis are for local experiments. The API stub does not connect to them. The compose file uses a throwaway local database password; do not reuse it outside this demo.

## Opportunity research

The demo follows an ai-pain-pipeline run checked in under [`docs/pipeline/`](docs/pipeline/).

Run [`pipe_2026-11-01_001`](docs/pipeline/pipe_2026-11-01_001/) (2026-11-01) rescanned Hacker News, GitHub Issues, and the App Store (Product Hunt and Reddit were skipped: no credentials). The top opportunity is **Multi-list task manager for Google Tasks refugees**, score **3360**, recommendation **validate**, confidence **medium**. The reports mark the score tier high and still keep validate/medium, because the cluster is one App Store product. Stage 3 preferred that multi-member Google Tasks cluster over higher single-post ICE scores (the top single post was open-source agent memory at 448).

- Index: [`docs/pipeline/README.md`](docs/pipeline/README.md)
- Chinese exec summary: [`docs/pipeline/full-exec-summary.zh.md`](docs/pipeline/full-exec-summary.zh.md)
- Opportunity report: [`docs/pipeline/full-opportunity-report.md`](docs/pipeline/full-opportunity-report.md)

Stage JSON, digests, judgments, and slim raw tops for that run live in the run folder. Product code stays in `apps/`.
