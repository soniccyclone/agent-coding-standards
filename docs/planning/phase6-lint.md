---
type: punch-list
title: Phase 6 Lint
description: Mechanical lint sweep of the OKF bundle. Result, what was checked, how the checker was validated, and the defect classes it deliberately cannot catch. Run 2026-08-01.
tags: [phase6, lint, okf]
---

# Phase 6 — Lint

Phase 6 is a recurring check rather than a one-time phase, so the checker lives
in the repo at `tools/lint.py` and not in a scratch directory. Re-run it after
any batch of Phase 3-5 work lands.

```
python3 tools/lint.py            # report
python3 tools/lint.py --quiet    # exit 1 on findings, silent — for hooks
```

## Result, 2026-08-01

```
OKF bundle lint — 95 figures, 450 works, 2950 lessons, 21 tensions

CLEAN — no findings.
```

## Why a clean result was not taken at face value

A lint that reports nothing across 2,950 files on its first run is more likely a
broken lint than a perfect corpus, and the standing rule on this project is that
a quiet monitor means the monitor is wrong. So the checker was validated before
the result was believed: a throwaway copy of the bundle was mutated with seven
known defects, one per category, and the lint was required to catch all seven.

It did — invalid axis value, single-quoted title, missing `**Source:**` line,
empty subdomain list, broken internal link, a tension reverted to `status: open`,
and a figure directory with no lessons. The backlink-drift check fired as a
consequence of the retagging, which is the behaviour wanted. Only then was CLEAN
accepted as a real result.

## What is checked

Structural, from the Phase 6 spec: figures with no lessons; duplicate figure
titles across two directories; lessons carrying no axis or no subdomain; axis and
subdomain values outside the six and the nine; lessons with no `**Source:**`
line; lessons not linked from any work file; axis/subdomain backlink files out of
sync in either direction with the tags on the lessons; broken relative links
bundle-wide; works neither attested nor marked `SOURCE-UNOBTAINABLE`; works with
no `url`; and tensions left `status: open`.

One check is narrower than it looks and is load-bearing. Lesson titles must be
**double-quoted**, because `rebuild-backlinks.py` matches `title: "..."` only and
silently falls back to the filename stem otherwise. A single-quoted title
produces a lesson that exists, links correctly, and appears in every shared index
under the wrong name. That defect class shipped once already.

## What this lint cannot catch, by construction

Everything here is structural. None of it reads a lesson and asks whether the
claim is true, whether it is abstract rather than a summary, whether it
duplicates another lesson under a different name, or whether it is grounded in
the source it cites. `extraction: complete` is likewise taken at its word — the
lint confirms the attestation exists, never that the reading behind it happened.
The four confidence tiers in `phase4-flags.md` H.8 and H.10 exist precisely
because that distinction is invisible to any mechanical check.

Known semantic defects therefore do not appear above. They are tracked as Phase 9
in the technical plan: the Cox rebuttal that was never extracted from an attested
work, Knuth's side of the goto argument that was never ingested, the unaudited
Tier 4 attestations, the 92 unverified Tier 3 backlinks, and the rest. A clean
Phase 6 and an open Phase 9 are consistent, and reading the first as evidence
about the second is the mistake this section exists to prevent.
