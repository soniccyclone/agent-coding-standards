---
type: lesson
title: "A worst case only counts if it is reachable through legal operations and pays for its own setup"
figure: tarjan
works: [efficiency-of-a-good-but-not-linear-set-union-algorithm]
axes: [verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# A worst case only counts if it is reachable through legal operations and pays for its own setup

**Lesson:** Half of this paper builds an adversary, and the care in that construction is the lesson. It is not enough to draw the pathological shape and observe that queries on it are expensive: a shape the algorithm can never actually be in proves nothing about the algorithm. So the construction is recursive, and each step is accompanied by a proof that the shape can be *reached* using only the operations under study, with an explicit accounting of how many of them it took — at most one query per eligible element, none on the parts that must stay untouched. Only then can the expensive queries be fired, and their cost is claimed against a budget that already includes everything spent getting there. A worst case whose setup costs more than the behaviour it is meant to expose demonstrates nothing, because the total was legitimate all along.

This is the discipline that separates a real stress test from a contrived one, and it applies directly outside of proofs. Pathological inputs constructed by reaching past the interface — hand-writing a corrupted file, poking a field the API would never produce, populating a cache with entries no request could generate — establish nothing about the system as deployed, because no sequence of legal operations reaches that state. The rigorous form of the question is always: what is the cheapest sequence of *permitted* operations that puts the system where I want it, and is the cost of that sequence small relative to the damage I am claiming? If the setup dominates, you have found an expensive way to spend money, not a vulnerability or a performance bug. If it doesn't, you have a genuine worst case, and you also have the recipe for reproducing it.

The construction's other virtue is that it names its own scope. The bound is proved to hold no matter which rule the algorithm uses for deciding attachment direction on a merge, which makes it a statement about a whole family of methods rather than one implementation, and it identifies a knob that cannot be adjusted to escape. Tarjan is then scrupulous about not overclaiming past that scope: whether some entirely different approach could do better is left open, with his belief stated separately as a conjecture rather than smuggled in as a consequence. Stating what a negative result is indifferent to, and stating the boundary where it stops applying, is what makes it usable — it tells a reader which future attempts are futile and which are still open.

**Source:** [Efficiency of a Good But Not Linear Set Union Algorithm](../works/efficiency-of-a-good-but-not-linear-set-union-algorithm.md) — the lower-bound section's recursively defined family of bad trees, the lemma establishing that each may be constructed from single elements using any union rule and at most one find per non-leaf non-root vertex, the remark that the resulting bound is independent of the union rule used, the accounting of construction finds against the total operation budget, and the conclusion's separate statement of the linear-time question as an open problem with the author's conjecture labelled as such.
