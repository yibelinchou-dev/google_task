# Stage 3 — User Research 摘要

**Pipeline**: `pipe_2026-11-02_001`  
**Researched**: 2026-11-02T01:16:36Z  
**Recommendation**: **VALIDATE** (confidence: medium)

## Pre-build demand & distribution toolkit for vibe-coded indie SaaS

> Help solo founders validate buyers and pick a distribution wedge before shipping another short-lived feature dump that dies in ~1.5 years.

## 市场规模

- **TAM**: $5,000,000,000
- **SAM**: $250,000,000
- **SOM** (realistic Y1): $3,000,000

## 目标用户

### Vibe-coding indie founder about to launch

Pain 8/10 · WTP 7/10 · ~300,000 people

- "A lot of products are being vibe coded, released, and soon after that abandoned."
- "Distribution and marketing have become much more important than before - within the context that everyone can build "features" for free."

### OSS-first SaaS founder stuck on linear adoption

Pain 7/10 · WTP 6/10 · ~80,000 people

- "We've been trying to grow the project for months, and it's lowkey growing in stars and adoption. But it's linear."
- "I hate to spam in places like hn or other forums, but what strategies have you found working?"

## 现有方案 & 弱点

| 方案 | 定价 | 主要弱点 |
|------|------|----------|
| Generic indie GTM courses / Twitter gurus / Launch checklists | $49–$499 courses; free Twitter threads | Advice is generic and not tied to the founder's actual ICP evidence · No continuous measurement of whether demand exists before build |
| Product Hunt / HN Show / launch-day bursts | Free–agency retainers | One-day spikes without retention; OP already distrusts spam launches · Does not prevent building the wrong product first |
| Full marketing suites (HubSpot, Mailchimp, SEO agencies) | $50–$1000+/mo or agency fees | Overkill and expensive for pre-PMF solo founders · Assume you already have a product and list |

## 产品假设

MVP in 4–6 weeks: a guided pre-build kit that forces ICP interviews, waitlist smoke tests, channel experiments, and a kill/continue score before more vibe-coding. Pair with a lightweight distribution playbook for OSS-first SaaS (non-spam HN/X sequencing, adopter interviews, star→user conversion). Differentiator vs courses: instrumented experiments + decision score, not content. Monetize $19–$49/mo or $99 one-shot for indie founders; later B2B cohort.

## Commercial Assessment (V2)

**Opportunity Score**: **1852** (medium)  · formula: Pain × Frequency × ROI × SwitchingWill × Buyer × Persistence ÷ Competition ÷ WorkaroundQuality

| Dimension | Score | Notes |
|-----------|------:|-------|
| Pain | 7/10 | |
| Frequency | 6/10 | |
| ROI / Economic Impact | 6/10 | Primary loss is months of build+hosting with near-zero revenue when products die |
| Switching willingness | 7/10 | cost=3/10 |
| Buyer exists | 7/10 | buyer: Founder on personal card or tiny bootstrap budget |
| Persistence | 6/10 | structural_permanent / market |
| Competition (÷) | 8/10 | |
| Workaround quality (÷) | 5/10 | satisfaction=3/10 |

### Switching Cost Breakdown

Data migration 2 · Learning 4 · Team 2 · Ecosystem 3 · Sunk cost 5

Switching from 'just ship features' to a validation ritual has low data migration; main cost is sunk vibe-coding ego/time and learning a new weekly habit.

### Workarounds Users Already Use

- Ship first, ask HN/X for growth tips later
- Buy indie marketing courses / follow GTM influencers
- One-shot Product Hunt / Show HN launches
- Hire freelancers for SEO/content without ICP proof

Workarounds are abundant but OP evidence shows products still die fast; OSS founder still stuck on linear growth and rejects spam. Advice market is crowded; quality uneven and unmeasured.

### Buyer Mapping

- **User**: Solo indie founder / OSS-first SaaS builder
- **Beneficiary**: Same founder (avoids wasted build months)
- **Buyer**: Founder on personal card or tiny bootstrap budget
- **Champion**: Founder who already felt a failed or flat launch

## External Signals (Phase 2c)

**Mode**: broad · cluster `misc@ask_hn`

**GitHub persistence prefill**: 7/10 — unknown / Cluster persistence_hint=structural; no GitHub lifecycle data.

**Suggested scores (heuristic)**: switching=1 workaround÷=1 persistence=7


## Confidence Basis

- Sources: 1 · Products: 2 · Cross-run: True
- Switch intent present: True
- WTP signal present: True
- Rationale: Two HN posts in one month (graveyard lifespan + OSS growth ask) describe distribution as the bottleneck after vibe-coding made building cheap. Same lifespan thread also appeared in the prior HN sample but was not Top then; this week it is the strongest ICE cluster after agent-memory posts left the set. Still single-source (HN), so confidence stays medium.

## Evidence Ledger

### [high] Indie SaaS product lifespan is collapsing as vibe-coding makes shipping features cheap while distribution fails.

- `hackernews` · SaaSHub / indie SaaS: "A lot of products are being vibe coded, released, and soon after that abandoned. It's become too cheap to produce software."
- `hackernews` · SaaSHub / indie SaaS: "Distribution and marketing have become much more important than before - within the context that everyone can build "features" for free."

Assumptions:
- Median lifespan drop on SaaSHub generalizes beyond that directory's selection bias.

### [medium] OSS-first founders already shipping still struggle to convert linear stars into non-spammy adoption jumps.

- `hackernews` · OSS SaaS startups: "We've been trying to grow the project for months, and it's lowkey growing in stars and adoption. But it's linear."
- `hackernews` · OSS SaaS startups: "I hate to spam in places like hn or other forums, but what strategies have you found working? Specially in the realm of AI."

Assumptions:
- Founders will pay for structured experiments rather than free HN comment advice.

## Unsupported Assumptions

- Solo founders will pay for another validation toolkit instead of consuming free Twitter/HN advice.
- An instrumented kill-score changes build behavior more than guilt/FOMO does.
- OSS star growth tactics generalize into a retainable SaaS workflow.

## Validation Required

1. **[high] Interview 12 founders who shipped a vibe-coded MVP in 2026 and saw weak distribution.** — ≥8 admit they would have paused build if a credible kill-score existed; ≥5 name a budget ≥$20/mo or ≥$99 one-shot.
2. **[high] Concierge MVP: run 5 paid ($99) 2-week demand sprints (ICP calls + waitlist + one channel test) without building product UI.** — ≥3 of 5 say the kill/continue memo changed their next sprint; ≥2 refer another founder.
3. **[medium] Landing-page smoke test: 'Don't vibe-code into the graveyard' waitlist with $29/mo intent checkbox.** — ≥80 emails or ≥12 paid-intent checks in 2 weeks from HN/IndieHackers alone.

## 研究结论

Anchored on highest ICE item this HN-only run (product lifespan collapse, ICE 336) plus related Ask HN on growing OSS projects (ICE 210). Agent-memory theme that topped pipe_2026-10-29_001 dropped out of this week's top50; Top theme therefore shifts to indie distribution/GTM. Evidence remains HN-only—treat as directional. Prefill switching_willingness=1 is a heuristic miss: posts explicitly say features became free and marketing/distribution is the bottleneck, and OSS founder is actively seeking non-spam growth tactics. Competition is crowded content/agencies; wedge must be instrumented validation not more advice. Next: interview 12 founders who shipped a vibe-coded MVP in 2026; measure whether they would pay for a kill-score before next build. Avoid build+high until a second source (Reddit/IndieHackers) confirms WTP.
