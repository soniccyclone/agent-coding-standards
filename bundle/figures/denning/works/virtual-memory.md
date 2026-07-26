---
type: work
title: "Virtual Memory"
figure: denning
description: A long tutorial/survey that assembles the scattered contemporary research on paging, segmentation, and address translation into one coherent framework, fixing shared terminology (locality, working set, replacement algorithm, thrashing) the field had lacked until then. It reviews and compares page-replacement policies and multiprogramming load-control strategies, and lays out the cost/performance trade-offs among them. Widely credited with consolidating virtual memory into a proper subfield with common vocabulary and evaluation methods, rather than a scatter of ad hoc implementation techniques.
subdomains: [operating-systems-and-systems-programming]
year: 1970
url: https://www.denninginstitute.com/pjd/PUBS/VirtMem_1970.pdf
access: public
host: self-archived
tags: [work]
---

# Virtual Memory

**Venue/year:** ACM Computing Surveys 2(3), September 1970, pp. 153-189.
**Source:** https://www.denninginstitute.com/pjd/PUBS/VirtMem_1970.pdf — live PDF (verified 2026-07-24, HTTP 200), self-archived on Denning's own institute site. Distinct from Denning's later same-titled pieces also hosted there ("Virtual Memory" 1996 Computing Surveys retrospective, and a 2008 encyclopedia entry) — this is the original 1970 survey.

## Lessons
- [A single parameter pulled by two objectives with distant optima cannot be tuned, only split](../lessons/one-knob-two-objectives.md)
- [Choose the unit of allocation so that the hard sub-problem has nothing left to decide](../lessons/choose-the-unit-so-placement-has-no-content.md)
- [Find out which variable the outcome actually obeys before improving the one you find interesting](../lessons/measure-which-variable-the-outcome-obeys.md)
- [More resource can make things worse; only a structural property forbids it](../lessons/monotonicity-must-be-earned.md)
- [When composition destroys foreknowledge, build an observer instead of a predictor](../lessons/observing-beats-preplanning.md)
- [Allocate per unit of work so each one's performance depends only on itself](../lessons/per-unit-isolation-over-global-policy.md)
- [When a technique "doesn't work," suspect the relation between its parts before condemning any one part](../lessons/failure-lives-in-the-relation.md)
