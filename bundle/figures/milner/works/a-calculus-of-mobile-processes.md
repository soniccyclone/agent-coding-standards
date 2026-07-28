---
type: work
title: "A Calculus of Mobile Processes, I and II"
figure: milner
description: The two-part paper introducing the π-calculus, extending Milner's earlier CCS by letting processes pass around the very channel names used for further communication, so a system's communication topology can itself change over time. Part I builds the calculus and its notion of behavioral equivalence; Part II works out the supporting theory — algebraic laws and proof techniques — in full technical detail. Together they gave concurrency theory a minimal formalism expressive enough to model mobility and name-passing without leaving first-order process algebra.
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
year: 1992
url: https://www.lfcs.inf.ed.ac.uk/reports/89/ECS-LFCS-89-85/
extraction: complete
access: public
host: institutional
tags: [work]
---

# A Calculus of Mobile Processes, I and II

**Author(s):** Robin Milner, Joachim Parrow, David Walker
**Venue/year:** Information and Computation 100(1), pp. 1-40 (Part I) and pp. 41-77 (Part II), September 1992; originally circulated as University of Edinburgh LFCS technical reports ECS-LFCS-89-85 (Part I) and ECS-LFCS-89-86 (Part II) in 1989.
**Source:** https://www.lfcs.inf.ed.ac.uk/reports/89/ECS-LFCS-89-85/ (Part I) and https://www.lfcs.inf.ed.ac.uk/reports/89/ECS-LFCS-89-86/ (Part II) — live pages on the University of Edinburgh Laboratory for Foundations of Computer Science's own technical report archive, each with a full-text PostScript download; both verified live (HTTP 200).

## Lessons
- [When a new capability threatens to multiply your primitives, collapse a distinction instead](../lessons/collapse-distinctions-instead-of-adding-primitives.md)
- [Transmit access, not the thing itself, and make duplication an explicit act](../lessons/transmit-access-not-the-thing-itself.md)
- [Privacy is a runtime invariant to maintain, not a lexical fact to read off the text](../lessons/privacy-is-a-runtime-invariant-not-a-lexical-fact.md)
- [A freshly created private name buys atomicity and isolation without a new primitive](../lessons/a-fresh-private-name-buys-atomicity-for-free.md)
- [When equality is not stable, index it by the assumptions that make it hold](../lessons/index-equality-by-the-assumptions-that-make-it-hold.md)
- [Weaken the proof obligation, not the theorem, when the obvious witness will not close](../lessons/weaken-the-proof-obligation-not-the-theorem.md)
