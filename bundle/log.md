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
- **2026-07-24** — Phase 3 (source discovery) complete. 447 `work` files
  written across 94 of 95 figures (Pnueli is the sole zero-work-file case —
  every one of the four works named in his "why a candidate" case, including
  the founding "The Temporal Logic of Programs" 1977 FOCS paper, turned out
  genuinely inaccessible through legal open channels). Scope was a
  seminal-works verification pass against each figure's existing Phase 1/2
  top-10 list, not an exhaustive bibliography sweep — see the 2026-07-24
  amendment in `docs/planning/technical-plan.md`. Third-party rehosts of
  otherwise-paywalled originals (course mirrors, preservation nonprofits,
  fan archives) were accepted as public link-only citations per an explicit
  scope decision, and are marked `host: third-party-rehost` in every work
  file that uses one; `host: self-archived` and `host: institutional` cover
  the rest. 31 of 95 figures carry a `## Phase 3 access flag` section in
  their own `index.md` documenting works that were checked directly plus a
  Wayback fallback and confirmed genuinely unavailable (not just
  unchecked) — see `docs/planning/ledger.md`'s Phase 3 status section for
  the full per-figure breakdown. Executed as a ~95-agent rolling-queue
  fan-out (harness cap: 20 concurrent), each agent scoped to one figure's
  own `works/` directory and forbidden from touching this log or any other
  figure's files. Next: Phase 4, lesson extraction.
- **2026-07-24** — Pnueli source gap closed. Follow-up pass on the sole
  zero-work-file figure found NYU Courant's preserved copy of Pnueli's
  complete homepage (`cs.nyu.edu/home/people/in_memoriam/pnueli/`), with
  self-archived files the main run's Wayback-of-Weizmann check predated.
  3 `work` files added: "The Temporal Logic of Programs" (1977 FOCS,
  self-archived scan, render-verified), "On the Synthesis of a Reactive
  Module" (1989 POPL, ACM open backfile — gold per Unpaywall and Semantic
  Scholar; ACM bot-check still blocks automated fetch, sole such caveat in
  the corpus), and Manna-Pnueli's "The Anchored Version of the Temporal
  Framework" (LNCS 354, 1989, self-archived) as the public stand-in for the
  two still-paywalled Springer books. Corpus now at 450 works across all 95
  figures; Pnueli's access flag trimmed to the two books, non-blocking for
  Phase 4.
- **2026-07-24** — Phase 4 pilot (dijkstra, lamport, codd). 36 `lesson` files
  from 28 works (27 catalogued + EWD123's second transcription page), one
  agent per figure reading full sources. Every work's `## Lessons` section
  filled or dedup-marked; per-figure `## Lessons rollup` added to each
  index.md. Two Phase 3 data errors caught and fixed during extraction:
  Dijkstra's 1965 CACM work file wrongly credited it with introducing
  semaphores/P-V (those are EWD123 §3.2 — description corrected), and Codd's
  1970 work file URL pointed at Grinnell course discussion questions about
  the paper rather than the paper (replaced with the verified UPenn CIS 550
  mirror). Shared axis/subdomain files untouched per the single-writer
  fence — backlink sweep runs after the full fan-out. Awaiting Nathan's
  quality gate before the remaining 92 figures run.
