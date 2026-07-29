---
type: work
title: "Regular Expression Search Algorithm"
figure: thompson
description: Describes what became known as Thompson's construction — a way of compiling a regular expression into IBM 7094 machine code (conceptually, a nondeterministic finite automaton) that matches text by exploring all possible paths in lockstep, giving search time linear in the length of the input rather than exponential in the size of the expression. This sidesteps the blowup that naive backtracking regex matchers suffer on pathological patterns, and the construction it describes still underlies fast regex engines today. It predates Unix itself and is Thompson's earliest widely cited contribution.
subdomains: [algorithms-and-complexity]
year: 1968
url: https://archive.org/details/regular-expression-search-algorithm
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# Regular Expression Search Algorithm

**Venue/year:** Communications of the ACM 11(6), June 1968, pp. 419-422.
**Source:** https://archive.org/details/regular-expression-search-algorithm — Internet Archive "Community Texts" scan, freely downloadable in full (PDF, OCR text, and other formats, not lending-restricted). Resolves the Phase 1/2 `uncertain` flag: this is an openly downloadable public copy, not merely a listing page.

## Lessons
- [Carry the whole set of live possibilities forward instead of backtracking through one](../lessons/carry-the-set-of-live-possibilities-forward-instead-of-backtracking.md)
- [Force the frontier to be a set and its worst case collapses to a static count](../lessons/force-the-frontier-to-be-a-set-and-the-worst-case-becomes-static.md)
- [When every intermediate result is the same kind of thing, composition rules replace case analysis](../lessons/uniform-intermediate-results-turn-case-analysis-into-composition.md)
- [Let the machine's own dispatch be your data structure](../lessons/let-the-machines-own-dispatch-be-your-data-structure.md)
