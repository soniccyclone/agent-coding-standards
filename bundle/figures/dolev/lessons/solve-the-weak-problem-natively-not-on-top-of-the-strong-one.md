---
type: lesson
title: "Having weakened the requirement, solve it directly instead of layering it over the strong primitive"
figure: dolev
works: [reaching-approximate-agreement-in-the-presence-of-faults]
axes: [primitive-count, cognitive-load, parallelizability]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Having weakened the requirement, solve it directly instead of layering it over the strong primitive

**Lesson:** Weakening a requirement and then implementing the weak requirement by calling the strong mechanism is the most common way a relaxation is wasted. If everyone only needs values within a tolerance of each other, the obvious construction is to run full exact agreement on every participant's input, hand every participant the same table of values, and let each compute the same average. It works. It is also strictly worse than solving the weak problem on its own terms, and the ways in which it is worse are the ways that matter: it inherits every assumption the strong mechanism needs, it cannot exist at all in environments where the strong mechanism is impossible, and it pays the strong mechanism's worst-case cost in every run.

Solving the weak problem natively looks completely different. Each participant repeatedly publishes its current value, trims the incoming batch by rank to neutralize the failure budget, averages what survives, and repeats. The contraction of the spread per round is what does the work, so the construction never needs the thing that makes exact agreement expensive: a single point in a continuum that everybody must land on. That is why the same three-line loop keeps working when timing guarantees are withdrawn, where exact agreement provably cannot terminate. It also tolerates more failures than typical exact-agreement constructions and can finish sooner than their round floor, neither of which the layered version could ever do, since a wrapper cannot outperform what it wraps.

The general shape is worth internalizing: a layered implementation inherits the union of the lower layer's assumptions and costs, so it can only be as portable and as cheap as the thing underneath it. When you have deliberately relaxed a specification in order to escape a limit, building on the unrelaxed mechanism puts the limit straight back. The right test after any relaxation is whether the weaker goal has its own natural mechanism, usually one that exploits precisely the slack you just created. Iterative convergence exploits tolerance the way exact agreement never can, because approaching is a fundamentally cheaper relationship than matching.

The honest cost of going native is that you give up reuse and have to prove the new thing from scratch, including a convergence rate and a validity argument. That is the trade. It is usually worth taking when the relaxation was motivated by a hard limit rather than by mere expense, because in that case the layered version does not merely cost more, it does not exist.

**Source:** [Reaching Approximate Agreement in the Presence of Faults](../works/reaching-approximate-agreement-in-the-presence-of-faults.md) — the passage that spells out the layered construction over exact agreement, concedes it would suffice, and then enumerates why the direct successive-approximation algorithm is preferred: simpler, more resilient, sometimes faster than the round floor, and extensible to the setting where exact agreement is unattainable.
