---
type: figure
title: Haskell Curry
description: 1900-1982, Penn State. Systematized combinatory logic independently of Schönfinkel - the clearest fewer-primitives rival to lambda calculus.
status: accepted
layer: design-thought
subdomains: [foundations-of-computation]
tags: [figure, accepted]
---

# Haskell Curry

**Dates:** 1900-1982. American logician, Penn State.

## Why a candidate
Built out combinatory logic into a full formal system on the same minimal-primitive footing as Church's lambda calculus, explicitly trading bound variables for a small closed combinator basis — pair with Schönfinkel as a deliberate test case for the primitive-count axis.

## Top 10 most influential works
1. "Grundlagen der kombinatorischen Logik" (1930, doctoral thesis, Amer. J. Math.) — `paywalled` (JSTOR)
2. *Combinatory Logic, Vol. I* (with Feys, 1958) — `paywalled`
3. *Combinatory Logic, Vol. II* (with Hindley, Seldin, 1972) — `paywalled`
4. "Some Additions to the Theory of Combinators" (1932) — `paywalled`/`uncertain`
5. *A Theory of Formal Deducibility* (1950) — `uncertain`
6. *Foundations of Mathematical Logic* (1963, later Dover reprint) — `paywalled`

## Phase 3 access flag
Verified 2026-07-24. Resolved public: #1 (both parts, freely downloadable Internet
Archive periodical scans of AJM 52(3) and 52(4), 1930) and #4 (freely downloadable
IA scan of AJM 54(3), 1932) turned out openly available once actually fetched — the
Phase 1 `paywalled` flag was based on the JSTOR listing without checking whether the
underlying journal issue is also on Internet Archive's open "sim_" periodicals
collection, which it is. #5 also resolved public: Project Euclid hosts the "Notre
Dame Mathematical Lectures" series as genuine open access (confirmed per-chapter,
not just the series description — fetched an actual chapter PDF with no login/paywall).

Genuinely unavailable, checked directly and via Wayback: #2 (*Combinatory Logic*
Vol. I, with Feys, 1958) and #3 (*Combinatory Logic* Vol. II, with Hindley/Seldin,
1972) — both are Internet Archive lending-restricted only (`access-restricted-item:
true`, no downloadable files), no self-archived or institutional copy found, and the
only apparent free full-text hosts (vdoc.pub, and a book PDF sitting in an unrelated
GitHub conference-talk repo) are exactly the kind of unvetted reupload the
third-party-rehost carve-out isn't meant to cover — no curation, no standing as a
citable source, likely to vanish or get DMCA'd. Same result for #6 (*Foundations of
Mathematical Logic*, 1963): IA copy is lending-restricted, and the only other hits
(dokumen.pub, vdoc.pub) are the same kind of unvetted reupload site.

This matters because #2 and #3 are arguably *more* central to the "why a candidate"
claim than what did clear — they're the full treatises where combinatory logic
actually gets built out into the complete formal system the candidacy case rests on,
while #1/#4 are the original short-form papers and #5 is adjacent proof-theory
lecture notes, not combinatory logic proper. The confirmed-public works establish
Curry's authorship and the core combinator apparatus but not the mature, complete
system. Flagging for batch review rather than blocking on it, per standing procedure.
