# Stage 5 — Tech Spec Digest

**Pipeline**: `pipe_2026-11-01_001`  
**Product**: Multi-list task manager for Google Tasks refugees  
**Created**: 2026-11-01T13:47:21.793259Z  
**Effort**: 280 hours

## Architecture
iOS client (SwiftUI) talks to a thin FastAPI backend for auth, sync, and Google import jobs. PostgreSQL stores users/lists/tasks; Redis queues import workers; optional local-only mode keeps tasks on-device until Pro sync is enabled. Waitlist is a static Next.js page posting to the same API.

## Stack
{
  "frontend": {
    "framework": "SwiftUI (iOS) + Next.js 15 (waitlist)",
    "languages": [
      "Swift",
      "TypeScript"
    ],
    "key_libraries": [
      "StoreKit 2",
      "SwiftData/SQLite",
      "TanStack Query",
      "Tailwind"
    ]
  },
  "backend": {
    "framework": "FastAPI",
    "language": "Python 3.12",
    "runtime": "uvicorn",
    "key_libraries": [
      "SQLAlchemy",
      "Pydantic v2",
      "httpx",
      "celery/rq",
      "Sentry SDK"
    ]
  },
  "database": {
    "primary": "PostgreSQL 16",
    "cache": "Redis 7",
    "search": "PostgreSQL full-text search"
  },
  "infrastructure": {
    "hosting": "Local Docker Compose for demo; Railway/Neon optional later (not used this run)",
    "container_orchestration": "Docker Compose (local/staging demo)",
    "monitoring": [
      "Sentry (stub)",
      "structured logs"
    ],
    "ci_cd": "GitHub Actions (local workflow files only; no remote push in this run)"
  }
}

## API contracts (5)
- GET /v1/lists
- GET /v1/lists/{list_id}/tasks
- POST /v1/import/google-tasks
- GET /v1/import/jobs/{job_id}
- POST /v1/waitlist

## Phases
- {'phase': 'Phase 1 — Core lists + offline iOS shell', 'duration_weeks': 3, 'deliverables': ['SwiftUI multi-list sidebar', 'Local SQLite CRUD', 'Basic FastAPI auth + lists API'], 'dependencies': [], 'success_criteria': ['Demo with 40 seeded lists switches smoothly', 'Unit tests for list/task models pass']}
- {'phase': 'Phase 2 — Import, archive/search, Pro gate', 'duration_weeks': 3, 'deliverables': ['Google import worker', 'Archive + FTS', 'StoreKit paywall stub'], 'dependencies': ['Phase 1 — Core lists + offline iOS shell'], 'success_criteria': ['Fixture import completes with <1% loss', 'Search finds archived tasks']}
- {'phase': 'Phase 3 — Validate launch kit', 'duration_weeks': 2, 'deliverables': ['Waitlist page', 'Calendar sync MVP', 'Local staging demo + metrics stubs'], 'dependencies': ['Phase 2 — Import, archive/search, Pro gate'], 'success_criteria': ['Waitlist captures emails', 'Stage 8/9 local artifacts generated']}
