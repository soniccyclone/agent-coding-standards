---
type: lesson
title: "Once two primitives are both powerful enough, choose between them by what they can detect"
figure: herlihy
works: [a-methodology-for-implementing-highly-concurrent-data-objects]
axes: [hardware-affinity, primitive-count, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
tags: [lesson]
---

# Once two primitives are both powerful enough, choose between them by what they can detect

**Lesson:** A ranking of synchronization primitives by raw power sorts them into classes, and above the class you need, the ranking stops discriminating. Two primitives can both be sufficient for anything while producing implementations that differ in complexity, efficiency, and how much auxiliary machinery they drag in. The deciding difference is what each one can tell you about the interval between your read and your write. A conditional store that fires only if the location changed value since you read it answers "does the location still hold what I expected?" A linked-load followed by a conditional store answers a strictly sharper question: "has anyone written this location at all since I read it?"

That extra sharpness is worth a great deal the moment memory is being recycled, which it always is. If a block can be freed and reused, another participant can replace the current version, take ownership of the old block, and reuse it as the next version — leaving the shared pointer holding the value you originally read, though the world has moved on twice. A value-comparing primitive cannot tell that apart from nothing having happened, so it will happily install a version derived from a stale snapshot. Recovering from that requires an extra protocol in which a reader pins a block against reclamation before touching it, and the resulting algorithms are both slower and harder to think about. The write-detecting primitive makes the whole problem vanish, because staleness, not value equality, is what the algorithm actually cares about. And it is cheap in hardware for a reason worth internalizing: a cache-coherent machine already tracks whether a cached line has been invalidated, so the primitive that fits the algorithm is also the one that asks the memory system a question it is already answering.

The habit here is to look past the sufficiency question to the fit question. When two mechanisms are both adequate, ask which one directly expresses the predicate your algorithm needs to test, and prefer it even when the other is more familiar or more general-looking — the gap will show up as compensating machinery elsewhere. And notice which direction the compensation flows: the weaker-detecting primitive did not make the algorithm impossible, it made it more complex, which is exactly the kind of cost that gets misattributed to the problem rather than to the primitive.

**Source:** [A Methodology for Implementing Highly Concurrent Data Objects](../works/a-methodology-for-implementing-highly-concurrent-data-objects.md) — the introduction's three stated reasons for building on linked-load and conditional-store, the argument that the protocol breaks if a value-comparing primitive is substituted because a recycled block can restore the original pointer value, the reference to the earlier freeze-based protocol needed to work around it, and the conclusion's restatement that the choice of primitive is what made the algorithms simpler.
