---
type: work
title: "Structured Multiprogramming"
figure: brinch-hansen
description: Argues that concurrent programs should be built from disciplined structuring elements rather than ad hoc shared variables and low-level signaling, in the same spirit as the structured-programming case against goto for sequential code. Brinch Hansen lays out design principles for organizing cooperating processes around shared data protected by well-defined procedures, work that fed directly into the monitor concept he formalized a few years later. It's a bridge paper between the sequential structured-programming movement and structured concurrent programming.
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
year: 1972
url: http://www.brinch-hansen.net/papers/1972a.pdf
access: public
host: self-archived
tags: [work]
---

# Structured Multiprogramming

**Venue/year:** Communications of the ACM 15(7), July 1972, pp. 574-578.
**Source:** http://www.brinch-hansen.net/papers/1972a.pdf — author's self-archived papers site (brinch-hansen.net/papers), verified resolving 2026-07-24. Note: the site's HTTPS certificate is currently expired; the HTTP URL above resolves cleanly.

## Lessons
- [Design concurrent code for reproducible behavior, because the errors that matter are the ones testing can never reach](../lessons/design-for-reproducibility-because-testing-cannot-reach.md)
- [Put the permitted operations next to the data they touch, and give up language power until the compiler can enforce it](../lessons/put-the-operations-where-the-data-lives.md)
