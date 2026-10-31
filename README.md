# TaskRefuge (local demo)

Local **demo** scaffold for a multi-list task manager for people leaving Google Tasks. This is not a production service, not an App Store app, and not a hosted product.

What is included: a stub FastAPI app, a static waitlist page, optional local Postgres/Redis via Docker Compose, a health check test, and placeholder iOS notes. The Google Tasks import route is a stub and does not call Google.

## Run the API (port 3000)

```bash
cd apps/api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 3000
curl http://127.0.0.1:3000/health
```

Useful stub routes: `GET /health`, `GET /v1/lists`, `POST /v1/waitlist`, `POST /v1/import/google-tasks`.

## Run the waitlist page

The waitlist is a static HTML file. With the API already listening on port 3000, serve the page from another terminal:

```bash
python3 -m http.server 8080 --directory apps/waitlist
```

Open `http://127.0.0.1:8080/`. The form posts JSON to `http://127.0.0.1:3000/v1/waitlist`.

You can also exercise that endpoint without a browser:

```bash
curl -s -X POST http://127.0.0.1:3000/v1/waitlist \
  -H 'Content-Type: application/json' \
  -d '{"email":"you@example.com","list_count_estimate":12}'
```

**CORS is not configured yet.** The API does not send `Access-Control-Allow-Origin`. A browser page served from another origin (including `python -m http.server` on port 8080, or a `file://` open of `apps/waitlist/index.html`) will be blocked when it calls port 3000. `curl` and same-process tests are unaffected.

## Docker (optional, local only)

```bash
docker compose -f docker/docker-compose.yml up -d
```

Postgres and Redis are for local experiments. The API stub does not connect to them. The compose file uses a throwaway local database password; do not reuse it outside this demo.
