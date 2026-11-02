# Pipeline research (TaskRefuge)

Opportunity discovery runs that led to this product (multi-list task manager for Google Tasks refugees).

| Run | Date | Sources | Top opportunity | Score |
|-----|------|---------|-----------------|------:|
| [pipe_2026-11-01_001](./pipe_2026-11-01_001/) | 2026-11-01 | HN + GitHub Issues + App Store | Multi-list task manager for Google Tasks refugees | 3360 |
| [pipe_2026-11-02_001](./pipe_2026-11-02_001/) | 2026-11-02 | HN-only | PreFlight / validate kit | 1852 |

- [full-exec-summary.zh.md](./full-exec-summary.zh.md) — Chinese exec summary
- [full-opportunity-report.md](./full-opportunity-report.md) — Stage 3 opportunity report
- [pipe_2026-11-02_001/DEMO.md](./pipe_2026-11-02_001/DEMO.md) — PreFlight validate prototype. Snapshot is `pipe_2026-11-02_001/apps/demo/`; root `apps/` stays TaskRefuge.

## Layout

Root `apps/` is the living product mainline. Daily iteration stays there. Do not delete or rewrite that tree to match an old research run.

Each `pipe_YYYY-MM-DD_00x/` folder is a complete package for that run. It holds the stage reports, and it may also hold:

- `apps/` — a frozen snapshot of root `apps/` as it existed for that run (api, demo, ios-stub, waitlist, and anything else that shipped with it). Later edits to root `apps/` must not rewrite this snapshot.
- `DEMO.md` — how to open and privately publish **that run’s** demo.

Private previews publish from that run’s `apps/demo`, not from root `apps/` after later mainline edits. Claim keys and `.env` files stay out of git.

`pipe_2026-11-01_001` follows this convention: reports plus [`apps/`](./pipe_2026-11-01_001/apps/) and [`DEMO.md`](./pipe_2026-11-01_001/DEMO.md).
