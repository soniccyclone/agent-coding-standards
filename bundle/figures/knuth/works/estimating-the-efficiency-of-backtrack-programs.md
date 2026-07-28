---
type: work
title: "Estimating the Efficiency of Backtrack Programs"
figure: knuth
description: Backtracking search programs are notoriously hard to reason about because their running time depends on how much of the search tree gets pruned, which you generally don't know in advance. Knuth's fix is to estimate the cost by doing a cheap randomized walk down the tree, weighting nodes by the branching factor encountered along the way, rather than trying to enumerate or bound the tree analytically. The paper works through several combinatorial puzzle examples, including the "Instant Insanity" cube problem, to show the estimator matches actual run counts closely.
subdomains: [algorithms-and-complexity]
year: 1975
url: http://web.archive.org/web/20250124085742/https://www.ams.org/journals/mcom/1975-29-129/S0025-5718-1975-0373371-6/S0025-5718-1975-0373371-6.pdf
access: public
host: institutional
tags: [work]
---

# Estimating the Efficiency of Backtrack Programs

**Venue/year:** Mathematics of Computation 29(129), January 1975, pp. 121-136
**Source:** Wayback Machine snapshot (2025-01-24) of the official AMS journal PDF (https://www.ams.org/journals/mcom/...). Semantic Scholar flags the AMS copy as open ("BRONZE" — freely readable, no login wall), but ams.org returns HTTP 403 to automated/scripted fetches (bot-blocking, not a paywall); the Wayback snapshot resolves cleanly (HTTP 200) and is used here to guarantee a verifiable link.

## Lessons
- [When a cost cannot be derived or afforded, sample it: one weighted traversal estimates a structure you can never build](../lessons/sample-the-aggregate-instead-of-analyzing-or-running-it.md)
- [Right on average is not the same as informative — the shape of the error distribution is the real question](../lessons/right-on-average-is-not-informative-variance-is-the-real-question.md)
- [Correctness pins down a family of programs, not one program — cost is the free parameter you then choose](../lessons/correctness-pins-down-a-family-of-programs-not-one-program.md)
- [A theoretical weakness is a hypothesis about your inputs — measure whether it bites before building the machinery that fixes it](../lessons/a-theoretical-weakness-is-a-hypothesis-about-inputs-measure-before-you-fix-it.md)
