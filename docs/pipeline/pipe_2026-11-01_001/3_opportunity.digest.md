# Stage 3 — User Research 摘要

**Pipeline**: `pipe_2026-11-01_001`  
**Researched**: 2026-11-01T13:47:13Z  
**Recommendation**: **VALIDATE** (confidence: medium)

## Multi-list task manager for Google Tasks refugees

> Give power users with dozens of lists fast list switching, archive/search, and painless migration off Google Tasks iOS regressions.

## 市场规模

- **TAM**: $5,000,000,000
- **SAM**: $800,000,000
- **SOM** (realistic Y1): $15,000,000

## 目标用户

### Longtime Google Tasks power user (30–40 lists)

Pain 8/10 · WTP 7/10 · ~500,000 people

- "I’ve used Google Tasks for 10+ years, multiple times a day, with 30–40 lists"
- "I’m now being forced to look for something different"

### Multi-list iPad/iPhone task switcher

Pain 7/10 · WTP 6/10 · ~800,000 people

- "I need to find a new now because this is no longer efficient"
- "For the biggest tech company this side of the Sun, it’s clunky, unreliable, not nearly as smooth and intuitive as gTasks"

## 现有方案 & 弱点

| 方案 | 定价 | 主要弱点 |
|------|------|----------|
| Todoist | $0–$5/user/mo (Pro) | Migration of 30–40 Google Tasks lists still manual/frictionful · Not positioned as Google Tasks replacement with one-click import |
| Apple Reminders / Things 3 | Free / $49.99 one-time | Reminders weaker for many-list power workflows · Things is Apple-only and no Google Calendar parity for all users |
| gTasks (third-party Google Tasks client) | Freemium / IAP | Still depends on Google Tasks backend and API limits · Does not solve Google removing features server-side |

## 产品假设

MVP in 6–8 weeks: iOS-first task app with hierarchical/multi-list sidebar (restore the removed dropdown UX), full-text search, archive with timestamps, Google Tasks import + Google Calendar recurring sync, and a migration concierge checklist. Lead with App Store reviews citing hamburger/list regression; charge $4–8/mo or $40/yr for power-user sync.

## Commercial Assessment (V2)

**Opportunity Score**: **3360** (high)  · formula: Pain × Frequency × ROI × SwitchingWill × Buyer × Persistence ÷ Competition ÷ WorkaroundQuality

| Dimension | Score | Notes |
|-----------|------:|-------|
| Pain | 8/10 | |
| Frequency | 8/10 | |
| ROI / Economic Impact | 5/10 | Primarily daily friction minutes for multi-list navigation and broken recurring  |
| Switching willingness | 7/10 | cost=7/10 |
| Buyer exists | 8/10 | buyer: Same individual on personal App Store / subscription card |
| Persistence | 6/10 | unknown / platform |
| Competition (÷) | 8/10 | |
| Workaround quality (÷) | 4/10 | satisfaction=3/10 |

### Switching Cost Breakdown

Data migration 8 · Learning 4 · Team 3 · Ecosystem 7 · Sunk cost 8

Decade of lists and personal reference data create high sunk cost and Google ecosystem lock-in; learning curve for another task app is moderate if import works.

### Workarounds Users Already Use

- Horizontal scrolling across many lists
- Using browser Google Tasks for search
- Third-party clients like gTasks still on Google backend
- Manual move to Todoist/Things/Reminders

Workarounds are clumsy; browser search helps but mobile regressions remain; gTasks does not remove Google dependency.

### Buyer Mapping

- **User**: Individual power user living in Google Tasks daily
- **Beneficiary**: Same individual (personal productivity / reference system)
- **Buyer**: Same individual on personal App Store / subscription card
- **Champion**: Longtime user publicly writing 1★ switch-intent reviews

## External Signals (Phase 2c)

**Mode**: broad · cluster `migration@ask_hn`

**GitHub persistence prefill**: 5/10 — unknown / Cluster persistence_hint=unknown; no GitHub lifecycle data.

**Suggested scores (heuristic)**: switching=1 workaround÷=1 persistence=5


## Confidence Basis

- Sources: 1 · Products: 1 · Cross-run: True
- Switch intent present: True
- WTP signal present: False
- Rationale: Eight App Store reviews on Google Tasks share multi-list UX regression and switch language; cluster also appeared in pipe_2026-10-30_001. Still one store/one product—medium confidence, validate not build+high.

## Evidence Ledger

### [high] Longtime power users treat Google Tasks as a personal reference system and are being forced to look for alternatives after iOS list-menu removal.

- `app_store` · Google Tasks: "I’m now being forced to look for something different"
- `app_store` · Google Tasks: "I’ve used Google Tasks for 10+ years, multiple times a day, with 30–40 lists"

Assumptions:
- Users will pay for import+better list UX rather than wait for Google to restore the menu.

### [medium] Hamburger/list navigation regression creates explicit switch intent among multi-list users.

- `app_store` · Google Tasks: "I need to find a new now because this is no longer efficient"

Assumptions:
- Enough users will complete migration if import is one-click.

### [medium] Missing in-app search and archive keeps Completed lists congested versus the browser experience.

- `app_store` · Google Tasks: "Browser version works better because you can key word search, but not in the app"

Assumptions:
- Search+archive are table-stakes for paid power users.

### [medium] Users already compare Google Tasks unfavorably to third-party clients like gTasks.

- `app_store` · Google Tasks: "not nearly as smooth and intuitive as gTasks"

Assumptions:
- Willingness to try another client extends to leaving Google Tasks backend.

## Unsupported Assumptions

- A new indie task app can win paid conversions against Todoist/Things solely on list UX.
- Google will not restore the multi-list dropdown within one release cycle.
- Users will trust an indie with decade-long personal reference data.

## Validation Required

1. **[high] Message 30 Google Tasks 1★ reviewers who mention lists/hamburger/switch; offer free guided import + $39/yr founding plan waitlist.** — ≥8 reply; ≥5 join waitlist; ≥3 complete import trial.
2. **[high] Ship clickable prototype of multi-list sidebar + search/archive; 5 moderated usability tests with 20+ list users.** — ≥4/5 say they would switch within 30 days if import works.

## 研究结论

Nov 1 fullest-available rescan (HN+GitHub+App Store; PH/Reddit still tokenless) again yields a Google Tasks App Store echo: 8 of 20 merged posts sit in misc@google_tasks_get_things_done, citing multi-list nav regressions, missing archive/search, calendar sync breaks, and explicit switch intent. Raw ICE leaders are agent-memory (384→448 after enrich) and product-lifespan (336), but Stage 3 prioritizes the multi-member Tasks cluster over single-thread HN spikes. Caveats: single-product App Store dominance (enricher flags single-source echo), crowded task market, Google may restore UI, decade of lists = high switching cost. Next: interview switch-intent reviewers and test paid import waitlist before build.
