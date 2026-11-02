# pipe_2026-11-01_001 — private demo

This run’s private preview publishes from **this folder’s** `apps/demo` only.

`docs/pipeline/pipe_2026-11-01_001/apps/` is a snapshot of root `apps/` frozen with this research run (api, demo, ios-stub, waitlist). Later edits to the root `apps/` mainline do not change what this preview serves. Publish this run’s `apps/demo`, not a later copy of root `apps/demo`.

## Open locally

The demo is one static page: `apps/demo/index.html` (relative to this run folder).

Open that file in a browser. List loading falls back to the built-in offline mock, because the page cannot call the local API from a `file://` URL. Adding, completing, and deleting tasks still stays in this browser’s `localStorage`.

To serve the same snapshot over HTTP, from this run folder:

```bash
python3 -m http.server 8080 --directory apps/demo
```

Then open http://127.0.0.1:8080/ .

If you also want live lists from the snapshotted API stub, run it from this run’s `apps/api` (not from root `apps/api` after later edits) and keep the static server above. The page requests `http://127.0.0.1:3000/v1/lists` (or `localhost:3000` when the page host is `localhost`). If that API is down, the page stays on the offline mock.

```bash
cd apps/api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 127.0.0.1 --port 3000
```

Leave `.venv` untracked. Do not commit it.

## Private hosting

Publish the **contents** of this run’s `apps/demo` (the static files inside that directory) to a private Spacefast space, or a similar static host.

- Keep claim keys and any `.env` out of git forever. They are not part of this snapshot.
- Anonymous short-slug links expire. Prefer a deep-slug private Space so the preview URL stays stable.
- Do not bind a domain, take payments, or post the preview publicly from this package.

URL: (fill after private publish)
