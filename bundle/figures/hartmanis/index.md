---
type: figure
title: Juris Hartmanis
description: 1928-2022, Cornell. Co-authored the foundational paper defining computational complexity as a formal discipline.
status: accepted
layer: implementation-mapping
subdomains: [algorithms-and-complexity]
tags: [figure, accepted]
---

# Juris Hartmanis

**Dates:** 1928-2022. Latvian-American computer scientist, Cornell University; founded and chaired Cornell's CS department.

## Why a candidate
Co-authored (with Stearns) the foundational paper that defined computational complexity as a formal discipline — introduced the Turing-machine-based complexity class framework this subdomain rests on. Thin body of individually-landmark work beyond the joint 1965 paper — consider vetting as a pair with Stearns.

## Top 10 most influential works
1. "On the Computational Complexity of Algorithms" (1965, with Stearns, Trans. AMS) — `public` (AMS open backfile)
2. "Computational Complexity of Random Access Stored Program Machines" (1971, with Hopcroft) — `paywalled`
3. 1993 Turing Award lecture — `uncertain`
4. Work on relativized complexity/oracle Turing machines (with students Baker, Gill) — `uncertain` attribution

## Lessons

Hartmanis teaches that cost is the only interesting thing about a computable
problem, and that every claim about cost is a claim relative to a machine
model whose hypotheses you owe. He founded the practice of indexing problems
by resource budget instead of by possibility, showed the layering is forced
because listable collections can always be escaped, and showed that the
insensitivity to finite detail which makes such a measure meaningful is
precisely what makes membership in it undecidable — so classification is
argument, never tooling. From there his instinct runs consistently toward
accounting rather than self-reference: bound how many pasts a machine must
keep distinguishable, or how fast any one primitive can grow the answer, and
you have bounded every implementation at once, more sharply than a diagonal
construction ever could. The register-machine work is where he turns that
instinct against the field's own comforts, demonstrating that constant-factor
freedom is an artifact of a formalism generous enough to let you re-encode,
that self-modifying code is worth exactly one constant unless it is secretly
manufacturing primitives the language should have had, and that an
architectural feature is worth no more than the cost of faking it — with
features that merely shorten access provably cheap to fake and features that
change how fast values grow provably not. His retrospective on relativization
closes the loop by turning the same skepticism on a belief he helped the field
accumulate: an impossibility result about a technique is not a property of the
problem, two characterizations equal in the base system come apart the instant
the system is extended, and the small local steps a realistic model seems to
want relaxed are in fact the only handles anyone has ever had on a
computation. Taken together: measure in the model you are actually in, know
which of your invariances are theorems and which are habits, and treat
every barrier — including your own — as something to re-derive rather than
inherit.
