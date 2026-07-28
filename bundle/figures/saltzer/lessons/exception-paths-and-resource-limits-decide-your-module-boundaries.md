---
type: lesson
title: "Exception paths and resource limits decide your module boundaries"
figure: saltzer
works: [the-multics-kernel-design-project]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Exception paths and resource limits decide your module boundaries

**Lesson:** Decompose a system around its normal operation and the structure will look
right and be wrong. The parts that wreck it are the ones usually postponed: what happens
when something runs out, when a limit is hit, when an operation fails partway, who is
charged for what. These have a shape that is hostile to layering by nature — the
condition is *detected* at the bottom, where the physical constraint lives, but it is
*meaningful* at the top, where the intent and the accounting live. So handling one
naturally reaches from the depths of the system to its surface, and a design that did not
plan for that reach will get it as a set of shortcuts: a low component reading a high
one's tables, or calling upward and waiting.

The methodological half of the problem is worse than the intrinsic half, and it is
entirely self-inflicted. Limits, quotas, failure recovery, and reliability strategies get
treated as things to add once the interesting part works. By then the boundaries are set,
and the additions cannot respect them, because respecting them was never a constraint
while they were being drawn. This is the concrete reason a modular design cannot be
developed against a partial function list: the deferred functions are exactly the ones
whose paths cut across the modules, so deferring them means deferring the information you
needed to place the modules.

The practical inversion is to bring the awkward cases forward. Sketch the resource
limits, the exhaustion conditions, the partial-failure recoveries, and the accounting
before committing to a decomposition, and let them argue with it — because they will win
later anyway, silently, in the form of couplings nobody chose. When one of these paths
still refuses to fit, the two moves that actually work are to make the condition get
detected at the level where it means something rather than where it is first noticed, or
to change the semantics of the feature that generates the awkward condition. Both are
available and both are cheaper than the structural damage.

**Source:** [The Multics Kernel Design Project](../works/the-multics-kernel-design-project.md)
— the worked dependency-loop cases involving storage quotas and full storage volumes,
the summary observation that the hardest structural problems come from exception handling
tied to resource control and are partly caused by adding those controls last, and the
closing lesson that a modular design cannot be developed without the complete set of
intended functions in hand.
