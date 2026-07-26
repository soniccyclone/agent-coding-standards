---
type: work
title: "The Working Set Model for Program Behavior"
figure: denning
description: Defines a program's working set as the set of pages it referenced in the most recent theta virtual-memory references, and argues this sliding-window measure captures a program's locality of reference closely enough to predict its real memory demand moment to moment. Denning proposes using working-set size, rather than a fixed per-process allocation, as the basis for both page-replacement decisions and multiprogramming load control. It became the theoretical foundation that essentially every later paging and cache-replacement scheme built on.
subdomains: [operating-systems-and-systems-programming]
year: 1968
url: https://www.denninginstitute.com/pjd/PUBS/WSModel_1968.pdf
access: public
host: self-archived
tags: [work]
---

# The Working Set Model for Program Behavior

**Venue/year:** Communications of the ACM 11(5), May 1968, pp. 323-333. ACM Best Paper Award for Systems.
**Source:** https://www.denninginstitute.com/pjd/PUBS/WSModel_1968.pdf — live PDF (verified 2026-07-24, HTTP 200), self-archived on Denning's own institute site (denninginstitute.com/pjd/PUBS/, the publications directory of his personal site).

## Lessons
- [Give the hand-waved quantity a one-parameter definition, then make its consequences derivable](../lessons/define-then-derive.md)
- [Knowing what will be needed is not permission to fetch it early](../lessons/speculation-defeated-by-its-own-trigger.md)
- [When composition destroys foreknowledge, build an observer instead of a predictor](../lessons/observing-beats-preplanning.md)
- [Two resources that constrain each other need one allocator, not two good ones](../lessons/coupled-resources-single-decision.md)
- [Find out which variable the outcome actually obeys before improving the one you find interesting](../lessons/measure-which-variable-the-outcome-obeys.md)
