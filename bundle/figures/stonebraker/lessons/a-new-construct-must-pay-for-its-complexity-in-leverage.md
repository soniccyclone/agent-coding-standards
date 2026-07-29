---
type: lesson
title: "A new construct must pay for its complexity in leverage, not in elegance"
figure: stonebraker
works: [what-goes-around-comes-around]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [databases-and-data-management, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A new construct must pay for its complexity in leverage, not in elegance

The recurring failure mode in three decades of data-model proposals was not bad taste; it was constructs that made a program marginally nicer to write while doing nothing an existing, simpler mechanism could not already do at the same cost. Set-valued attributes, tuple-typed columns, inheritance graphs, multiple inheritance, class variables — each was defensible in isolation and each could be simulated on plain tables and foreign keys with comparable performance. Simulability at parity is the test that kills a construct. If an existing primitive already reaches the same place at the same speed, the new primitive is pure addition to the surface area a user must learn and an implementer must support, paid for out of nobody's budget.

The interesting asymmetry is which additions survived. What stuck was not the semantically expressive machinery but the crudely powerful kind: the ability to inject user-written code and user-written access paths into the engine's own evaluation. Those changed what was achievable rather than what was sayable — a two-dimensional search that was impossible to run quickly became possible, and computation over a huge dataset stopped requiring the dataset to be dragged out to the computation. That is a different category of gain from expressive convenience, and it is the only category that reliably repaid its complexity.

So the discipline is to ask, of every proposed addition, what becomes newly *possible* or newly *fast*, and to reject the answer "it becomes more natural to express." Naturalness is real but cheap, and it is almost always obtainable at the layer above without touching the core. A designer who internalizes this defends a small primitive set aggressively and spends their complexity budget only where the existing primitives hit a wall in capability or performance — and pushes everything else out to libraries, tools, and conventions where a mistake is retractable.

**Source:** [What Goes Around Comes Around](../works/what-goes-around-comes-around.md) — the argument runs through the survey's treatment of the extended-relational and semantic-data-model eras and its verdict on which object-relational features actually mattered once benchmarked.
