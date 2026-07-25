---
type: figure
title: Barry Boehm
description: 1935-2022, TRW/DARPA/USC. The spiral model - risk-driven reasoning framework grounded in empirical cost/risk data.
status: accepted
layer: implementation-mapping
subdomains: [software-engineering-and-architecture]
tags: [figure, accepted]
---

# Barry Boehm

**Dates:** 1935-2022. Worked at TRW, DARPA, and later University of Southern California.

## Why a candidate, with a caveat
The spiral model is a risk-driven reasoning framework for iterative system structure, grounded in empirical cost/risk data rather than opinion — though this leans more toward process methodology than pure structural theory, worth weighing against the vetting standard.

## Top 10 most influential works
1. "A Spiral Model of Software Development and Enhancement" (1988, IEEE Computer) — `public`, confirmed. See `works/a-spiral-model-of-software-development-and-enhancement.md`.
2. *Software Engineering Economics* (1981, book, introduces COCOMO) — `paywalled`, confirmed on recheck. Internet Archive copy exists but is access-restricted (controlled digital lending, no free download); ACM/ResearchGate mirrors return 403. No legitimate open copy found.
3. "Software Engineering" (1976, IEEE Trans. Computers survey) — resolved to `public`. See `works/software-engineering-1976.md`.
4. "A View of 20th and 21st Century Software Engineering" (2006, ICSE) — resolved to `public`. See `works/a-view-of-20th-and-21st-century-software-engineering.md`.
5. *Software Cost Estimation with COCOMO II* (2000, book) — `paywalled`, confirmed on recheck. No legitimate open copy found (Prentice Hall textbook; only a partial internal draft chapter on a USC staff/private path turned up, not a usable public copy of the book itself).

(Phase 1/2 stub listed only 5 of a nominal top 10; Phase 3 verification pass worked from these 5 and did not surface additional clearly-public, clearly-central works beyond them.)

## Phase 3 access flag
The "empirical cost/risk data" half of the why-candidate case is not represented in the public work set. Both books that actually contain Boehm's cost-estimation models — *Software Engineering Economics* (1981, defines original COCOMO) and *Software Cost Estimation with COCOMO II* (2000) — are genuinely unavailable: no author-hosted or institutional copy exists, the Internet Archive scan of the 1981 book is controlled-digital-lending (login/waitlist, no free download), and journal/ACM mirrors of related COCOMO material 403. What's public and linked in `works/` is the spiral model paper (the risk-driven process framework itself) plus two survey/retrospective papers (1976, 2006) — solid on the "risk-driven reasoning" side. **Narrowed in Phase 4 (2026-07-25):** the original wording called the public set "silent on the empirical cost/risk data side," which overstated the gap. What is actually missing is the *estimation models* themselves; much of the underlying empirical data is present in the public papers — the cost-to-fix-by-phase curve across IBM, GTE and TRW (1976, repeated in 2006 with project size as a parameter), the design-versus-coding defect split, life-cycle breakdowns putting maintenance at roughly 60-75% of cost, a $75-versus-$4000 per-instruction develop-versus-maintain comparison, the hardware/software cost crossover, and HP product-line reuse payoff figures. The spiral paper also applies COCOMO productivity-leverage analysis inside its TRW case study. So: lean on this figure for cost-*reasoning* freely; only the calibrated models are out of reach.

## Lessons
Boehm's contribution to how a programmer thinks is the habit of treating
uncertainty as the quantity that organizes everything else. What you build
next is chosen by which unknown is most expensive to keep, how much precision
an artifact deserves is set by what being wrong there would cost, and the
project itself is a claim under test whose refutation is a legitimate result
rather than a disgrace. Around that core sit four lessons about honesty
regarding limits: measured evidence that a mistake's price is set by when it
surfaces and not by its intrinsic size; the observation that most of what a
system costs is spent changing it, so the criterion you optimize silently
chooses the artifact's shape; the recognition that verification always
establishes agreement with something that can itself be wrong; and an audit
habit that asks whether one's tools actually reach the region where the
failures accumulate, since theory tends to grow where theory is easy to make.
Two further lessons come from his willingness to read his own field
skeptically. Long-running methodological fights signal a missing variable
rather than a winner, so the productive move is to find the dimension along
which each camp is right and replace the catalogue of hostile methods with one
framework plus a diagnosis. And every practice is a fit to conditions —
machine time against human time, cost of change, whether the target is even
specifiable in advance, whether the parts are yours to see inside — which
means inherited rules must be re-derived rather than obeyed, because the
conditions move and the rules do not announce their expiry.
