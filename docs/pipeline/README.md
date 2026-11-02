# Pipeline research (TaskRefuge)

Opportunity discovery runs that led to this product (multi-list task manager for Google Tasks refugees).

| Run | Date | Sources | Top opportunity | Score |
|-----|------|---------|-----------------|------:|
| [pipe_2026-11-01_001](./pipe_2026-11-01_001/) | 2026-11-01 | HN + GitHub Issues + App Store | Multi-list task manager for Google Tasks refugees | 3360 |
| [pipe_2026-11-02_001](./pipe_2026-11-02_001/) | 2026-11-02 | HN-only | PreFlight / validate kit — [S1 痛点](./pipe_2026-11-02_001/1_pain_points.digest.zh.md) · [S2 评分](./pipe_2026-11-02_001/2_scored_pain_points.digest.zh.md) · [S3 机会](./pipe_2026-11-02_001/3_opportunity.digest.zh.md) · [S4 PRD](./pipe_2026-11-02_001/4_prd.digest.md) · [S5 spec](./pipe_2026-11-02_001/5_tech_spec.digest.md) · [S6 code](./pipe_2026-11-02_001/6_codebase/) · [S7 delivery](./pipe_2026-11-02_001/7_code_delivery.digest.md) · [S8 deploy](./pipe_2026-11-02_001/8_deployment.digest.md) · [S9 growth](./pipe_2026-11-02_001/9_growth_metrics.digest.md) · [中文摘要](./pipe_2026-11-02_001/sample-exec-summary.zh.md) · [机会报告](./pipe_2026-11-02_001/sample-opportunity-report.md) · [DEMO](./pipe_2026-11-02_001/DEMO.md) · [FLOW_COMPLETE](./pipe_2026-11-02_001/FLOW_COMPLETE.md) | 1852 |

- [full-exec-summary.zh.md](./full-exec-summary.zh.md) — Chinese exec summary (TaskRefuge, `pipe_2026-11-01_001`)
- [full-opportunity-report.md](./full-opportunity-report.md) — Stage 3 opportunity report (TaskRefuge, `pipe_2026-11-01_001`)
- [pipe_2026-11-02_001/sample-exec-summary.zh.md](./pipe_2026-11-02_001/sample-exec-summary.zh.md) — HN-sample Chinese exec summary (stages 1–3)
- [pipe_2026-11-02_001/sample-opportunity-report.md](./pipe_2026-11-02_001/sample-opportunity-report.md) — HN-sample opportunity report
- [pipe_2026-11-02_001/DEMO.md](./pipe_2026-11-02_001/DEMO.md) — PreFlight clickable demo. Snapshot is `pipe_2026-11-02_001/apps/demo/`; root `apps/` stays TaskRefuge. Private Spacefast preview exists; the live URL is shared in chat only.
- [pipe_2026-11-02_001/FLOW_COMPLETE.md](./pipe_2026-11-02_001/FLOW_COMPLETE.md) — Stages 1–9 close-out (validate path: GO → PROCEED → MERGE → OPTIMIZE)

## Layout

Root `apps/` is the living product mainline. Daily iteration stays there. Do not delete or rewrite that tree to match an old research run.

Each `pipe_YYYY-MM-DD_00x/` folder is a complete package for that run. It holds the stage reports, and it may also hold:

- `apps/` — a frozen snapshot of root `apps/` as it existed for that run (api, demo, ios-stub, waitlist, and anything else that shipped with it). Later edits to root `apps/` must not rewrite this snapshot.
- `DEMO.md` — how to open and privately publish **that run’s** demo.

Private previews publish from that run’s `apps/demo`, not from root `apps/` after later mainline edits. Claim keys and `.env` files stay out of git.

`pipe_2026-11-01_001` follows this convention: reports plus [`apps/`](./pipe_2026-11-01_001/apps/) and [`DEMO.md`](./pipe_2026-11-01_001/DEMO.md).

`pipe_2026-11-02_001` is the HN-only PreFlight run through Stage 9, laid out like `pipe_2026-11-01_001` (stage JSON + digests, judgments, `_state.json`, `DEMO.md`, `FLOW_COMPLETE.md`) plus `6_codebase/` and `8_local_artifacts/`. Stage 1–3 research digests and the Chinese summaries stay. `_raw/` is the slim pack (HN dumps stay on the pipeline runner). Clickable UI: [`apps/demo/`](./pipe_2026-11-02_001/apps/demo/) and [`DEMO.md`](./pipe_2026-11-02_001/DEMO.md). Close-out: [`FLOW_COMPLETE.md`](./pipe_2026-11-02_001/FLOW_COMPLETE.md). Root `apps/` stays TaskRefuge. A private Spacefast preview exists; the live URL is shared in chat only.
