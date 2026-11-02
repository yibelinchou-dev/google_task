# PreFlight — validate prototype

**Run**: [`pipe_2026-11-02_001`](./)  
**Date**: 2026-11-02  
**Sources**: HN-only  
**Score**: 1852  
**Recommendation**: validate / medium

PreFlight is the clickable validate prototype for the opportunity:

> 面向 vibe-coded 独立 SaaS 的预构建需求验证与分发工具包

The page is one self-contained file, [`apps/demo/index.html`](./apps/demo/index.html). It walks a founder through onboarding, a buyer-discovery worksheet, an interview script, a mock $99 concierge demand sprint, a distribution-wedge picker, a mock $29/mo waitlist, and a kill/continue dashboard. Answers stay in the browser (`localStorage`). Checkout is mock only: no payments, no OAuth, and no network writes.

This snapshot belongs to the pipe folder. Root `apps/` stays the TaskRefuge mainline.

Stage 1–3 research for this run is in this folder: [sample-exec-summary.zh.md](./sample-exec-summary.zh.md) and [sample-opportunity-report.md](./sample-opportunity-report.md). Do not treat this note as a substitute for stage JSON.

## Open locally

From the demo directory:

```bash
cd docs/pipeline/pipe_2026-11-02_001/apps/demo
python3 -m http.server
```

Then open `http://127.0.0.1:8000/`.

## Private Spacefast

Publish this folder’s contents (the static page under `apps/demo/`). Keep claim keys out of git. Do not add `.env` files or bind a domain from this repo.

**Live URL**: placeholder. Space slug: `silent-hill`.

Claim-door URLs contain secrets. Leave them out of git.

Anonymous spaces expire about 33 hours after the last content-changing publish unless the space is claimed.
