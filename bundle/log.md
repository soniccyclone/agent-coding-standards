---
type: log
title: Ingest Log
description: Chronological audit trail of bundle changes, per the Karpathy llm-wiki pattern.
---

# Ingest Log

- **2026-07-24** — Phase 0 (bundle scaffolding) complete. Directory structure
  created; six `axis` files and nine `subdomain` files written with
  definitions only, rollups empty. No figures, works, lessons, or tensions
  yet. Next: Phase 1, author discovery fan-out by subdomain.
- **2026-07-24** — Phase 1 (author discovery) complete. 95 `figure` stubs
  written under `figures/` — 92 from the nine-subdomain fan-out (post-dedup),
  plus Chuck Moore, Manfred von Thun, and Jerome Saltzer added out-of-band.
  All `status: candidate`, each carrying a titles-only top-10 works list with
  public/paywalled/uncertain flags. No `work`, `lesson`, or `tension` files
  yet.
- **2026-07-24** — Phase 2 (vetting) complete. All 95 figures reviewed and
  accepted, zero rejections; every stub updated in place with
  `status: accepted` and a `layer` field (design-thought / both /
  implementation-mapping). One tension flagged for Phase 5 (Dijkstra vs.
  Knuth on goto). Next: Phase 3, per-figure public-source discovery.
