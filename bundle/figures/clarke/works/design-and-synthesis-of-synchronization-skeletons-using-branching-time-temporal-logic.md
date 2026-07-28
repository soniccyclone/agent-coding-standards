---
type: work
title: "Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic"
figure: clarke
description: The founding paper of model checking, co-authored with E. Allen Emerson. Proposes modeling a finite-state concurrent program as a "synchronization skeleton" (a small state-transition graph capturing only its concurrency-relevant behavior) and checking that graph against a branching-time temporal logic (CTL) specification with an efficient decision procedure, rather than hand-building a correctness proof. Also sketches how to synthesize a skeleton directly from a CTL specification.
subdomains: [formal-methods-and-verification]
year: 1981
url: https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Design%20and%20synthesis%20of%20synchronization%20skeletons%20using%20branching%20time%20temporal%20logic.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# Design and Synthesis of Synchronization Skeletons Using Branching Time Temporal Logic

**Author(s):** Edmund M. Clarke, E. Allen Emerson
**Venue/year:** Logics of Programs Workshop (Yorktown Heights, NY, May 1981), published in Lecture Notes in Computer Science vol. 131, Springer, 1982.
**Source:** https://www.cs.cmu.edu/~emc/papers/Conference%20Papers/Design%20and%20synthesis%20of%20synchronization%20skeletons%20using%20branching%20time%20temporal%20logic.pdf — self-archived scan on Clarke's own CMU faculty page, live and directly downloadable (HTTP 200). Filename and folder match the citation exactly as reference [8] in Clarke/Emerson/Sifakis's own 2009 Turing Award writeup.

## Lessons
- [Ask whether one machine satisfies the claim, not whether the claim is provable](../lessons/ask-whether-one-machine-satisfies-the-claim.md)
- [Model only the part of the program the claim can see](../lessons/model-only-what-the-claim-can-see.md)
- [Buy expressiveness only where you are willing to pay the checking bill](../lessons/buy-expressiveness-only-where-you-pay-the-checking-bill.md)
- [State a property as the equation it solves, and the algorithm falls out](../lessons/state-a-property-as-the-equation-it-solves.md)
- [A specification tight enough to check is tight enough to build from](../lessons/a-spec-tight-enough-to-check-is-tight-enough-to-build-from.md)
