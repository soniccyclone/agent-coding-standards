---
type: work
title: "Nondeterministic Algorithms"
figure: floyd
description: Floyd shows that combinatorial search problems can be written naturally as programs containing multiple-valued "choice" functions that are not directly executable on ordinary hardware, then gives a mechanical translation of such nondeterministic programs into conventional backtracking code. He works through the eight-queens problem and finding all simple cycles in a network as running examples. The paper formalized nondeterminism as a programming construct, later picked up in guarded-command languages and in specification/derivation styles that treat nondeterminism as underspecification.
subdomains: [algorithms-and-complexity, foundations-of-computation]
year: 1967
url: https://doi.org/10.1184/R1/6607739.v1
extraction: complete
access: public
host: institutional
tags: [work]
---

# Nondeterministic Algorithms

**Venue/year:** Journal of the ACM 14(4), October 1967, pp. 636-644.
**Source:** https://doi.org/10.1184/R1/6607739.v1 — resolves to Carnegie Mellon University's KiltHub institutional repository (article record confirmed public via the Figshare API backing KiltHub, author of record Robert W. Floyd; direct PDF download verified as a valid 19-page scan). The KiltHub HTML page itself sits behind an AWS WAF bot challenge that returns HTTP 202 to non-browser clients — that's bot-gating, not a broken link; the DOI and underlying file are confirmed public and resolvable.

## Lessons
- [Write the program for the machine you wish you had, and make the gap down to the real one mechanical](../lessons/write-for-the-machine-you-wish-you-had-then-translate.md)
- [Say which outcomes count as answers, and let the machinery for finding them be derived rather than written](../lessons/say-which-outcomes-count-and-let-the-search-be-derived.md)
- [Put the effort-saving tricks in a layer where they cannot change which answers are found](../lessons/keep-pruning-in-a-layer-where-it-cannot-change-the-answer.md)
