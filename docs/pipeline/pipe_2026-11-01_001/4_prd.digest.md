# Stage 4 — PRD Digest

**Pipeline**: `pipe_2026-11-01_001`  
**Product**: Multi-list task manager for Google Tasks refugees  
**Created**: 2026-11-01T13:47:21.772786Z  
**Timeline**: 8 weeks

## Vision
Build an iOS-first multi-list task app that lets longtime Google Tasks power users keep 30–40 lists, switch lists in one tap, archive and search history, and migrate with a guided import—so they are not stuck after Google’s list-menu regressions. North star: percentage of imported Google Tasks lists actively used weekly without users falling back to Google Tasks.

## Core features (6)
- **Multi-list sidebar switcher**: Restore fast navigation across dozens of lists with a persistent sidebar/dropdown and pin favorites for power users.
- **Google Tasks import concierge**: Guided import from Google Tasks (API and/or export) with progress, retries, and a migration checklist for calendar and recurring items.
- **Archive and full-text search**: Archive completed work with timestamps and search across active and archived tasks.
- **Google Calendar recurring sync**: Optional Google Calendar connection for recurring tasks so daily rituals survive migration.
- **Pro subscription and IAP**: Freemium core with Pro unlocking multi-device sync, archive search depth, and import concierge.
- **Migration waitlist landing**: Lightweight web waitlist capturing App Store switch-intent reviewers before full App Store launch.

## Monetization
{
  "model_type": "freemium",
  "pricing_strategy": "Free limited lists for trial; Pro at $4–8/mo or ~$40/yr unlocking unlimited lists, archive search depth, import concierge, and calendar sync via App Store IAP.",
  "target_arr": 500000,
  "customer_acquisition_cost": 25
}

## Competitive positioning
{
  "unique_value_prop": "The Google Tasks refugee app: multi-list speed plus guided import/archive/search, not another generic Todoist clone.",
  "why_us_over_competitors": [
    "Positioned explicitly for Google Tasks power users with 30–40 lists",
    "Import concierge and migration checklist reduce decade-long switching cost",
    "Archive+search restores workflows reviewers say Google removed"
  ],
  "market_window": "Window is the App Store regression echo; validate before Google fixes or competitors ship one-click import."
}
