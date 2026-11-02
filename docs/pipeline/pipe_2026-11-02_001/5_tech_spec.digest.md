# Stage 5 — Tech Spec Digest

**Pipeline**: `pipe_2026-11-02_001`  
**Product**: Pre-build demand & distribution toolkit for vibe-coded indie SaaS  
**Created**: 2026-11-02T01:44:14.870004Z  
**Estimated effort**: 200 hours

## Architecture
Static PreFlight demo (HTML/CSS/JS) for validate interviews + Spacefast private publish. Thin FastAPI backend for health, waitlist, experiments, and kill-score stubs. Optional SQLite/Postgres later; Redis not required in validate phase. Waitlist and experiment data can live in-memory for local demo.

## Key components
- **PreFlight static demo**: Clickable ICP interviews, waitlist kit, channel experiments, kill/continue score UI (localStorage)
- **FastAPI validate API**: Health, waitlist capture, experiment CRUD stubs, score computation stub
- **SQLite / Postgres (later)**: Persist founders, interviews, waitlist, experiments when leaving pure static demo
- **Spacefast private host**: Anonymous private publish of static demo for stakeholder walkthroughs

## Tech stack
- Frontend: Static HTML + vanilla JS (demo); Next.js optional later
- Backend: FastAPI (Python 3.12)
- DB: In-memory for local stub; SQLite/Postgres 16 later
- Hosting: Local uvicorn + Spacefast private static; Railway/Neon optional later (not this run)

## API contracts: 6 endpoints
## Phases: 3
- Phase 1 — Static PreFlight demo + API stubs (2w)
- Phase 2 — Persistence + memo export + pricing (2w)
- Phase 3 — Validate launch kit (2w)
