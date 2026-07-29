---
type: lesson
title: "An atomic unit can only be as large as what you can undo"
figure: stonebraker
works: [the-design-and-implementation-of-ingres]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# An atomic unit can only be as large as what you can undo

Choosing the unit of all-or-nothing is usually discussed as a matter of user convenience, and it is not. The unit is fixed by reversibility. Everything inside a boundary you promise to abandon cleanly must be abandonable, and the moment a sequence can contain an act that leaves the system's reach — a message shown to a person, a device advanced, a file created outside the managed store — the promise is unkeepable, because there is nothing to undo those with. Enumerating the candidate boundaries and rejecting each one whose interior can hold an irreversible act is the actual design procedure, and it usually lands you somewhere much smaller than the boundary users would prefer.

Two consequences follow that people find unpalatable and that honesty requires stating anyway. First, some workflows people genuinely want simply cannot be atomic: a sequence that offers choices, waits on a human, and then commits against what it showed spans an interval you cannot hold still, and pretending otherwise substitutes a hidden failure for a visible limitation. Second, the interior of the unit determines whether you can even reason about contention, because deciding in advance whether two pending units conflict requires knowing what they will touch — and a unit whose later actions depend on values a person or an external device supplies is not knowable in advance, which is the same reason it cannot be safely scheduled as it is the reason it cannot be rolled back. The two problems are one problem.

So the useful move is to state the guarantee's scope as a consequence of what you can reverse and what you can predict, then say plainly what falls outside it. A programmer who thinks this way stops asking how big a transaction can be and starts asking which actions in a proposed sequence are irreversible, then either pushes those to the very end, replaces them with something reversible, or accepts a smaller unit and designs the application to tolerate the gap. The alternative — a wide boundary that quietly cannot deliver on its promise the first time an external call sits inside it — is worse than the narrow honest one, because its users have built on a guarantee that was never there.

**Source:** [The Design and Implementation of INGRES](../works/the-design-and-implementation-of-ingres.md) — the concurrency-control discussion, which enumerates five candidate transaction scopes and rejects the multi-statement ones by reasoning about the impossibility of backing out through intervening external calls and the unpredictability of what such a unit will conflict with.
