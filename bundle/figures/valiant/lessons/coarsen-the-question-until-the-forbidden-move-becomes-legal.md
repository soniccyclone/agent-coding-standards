---
type: lesson
title: "Coarsen the question until a forbidden move becomes legal, and let the precision you need cap the correction terms"
figure: valiant
works: [the-complexity-of-computing-the-permanent]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Coarsen the question until a forbidden move becomes legal, and let the precision you need cap the correction terms

**Lesson:** Some problem sits next to a problem with a beautiful algorithm, and the algorithm's central step is simply invalid on yours — the transformation that leaves the neighbour's answer unchanged perturbs yours. The usual conclusion, that the technique does not apply, is premature. Ask instead what the perturbation actually is, as an object rather than as an error bar. If the discrepancy introduced by one application has recognizable structure, two things become possible: you may be able to weaken the question until the discrepancy is identically zero, or you may be able to carry the discrepancy along as an explicit extra term and argue that the terms run out.

Both happen in the same construction. Elimination is illegal for the permanent, but the exact difference between the permanent before and after a row operation is the permanent of a matrix with two equal rows — a quantity divisible by two. So if you only want the answer modulo a power of two, each elimination step spawns one correction term, that term carries a duplicated pair of rows, and terms with enough duplicated pairs are divisible by a high enough power of two to be zero at the precision you asked for. The recursion terminates at a depth set by the precision, and an algorithm exists whose cost grows with how exact an answer you demanded. That is the shape to look for: not "the method fails," but "the method costs one extra term per step, and the terms die at depth d, where d is my required precision."

The technique brings a second, easily missed requirement: staying inside the coarser world takes care. Elimination needs a pivot, and dividing by the wrong element leaves the ring you have retreated into, so the pivot rule becomes "prefer an element that is invertible here, failing that the one closest to invertible." Whenever you coarsen, audit each primitive operation for whether it is still available; the arithmetic you took for granted in the fine setting is exactly what the coarse setting restricts.

Finally, the coarsening that makes the problem easy tells you where the hardness has to stop. Having found that powers of two are tractable, you know the accompanying intractability result must carve them out by name — and a hardness theorem whose exception clause is explained by a matching positive result is much better understood than one whose exception is an artifact of the proof. When you locate a regime where a hard problem becomes easy, go back and check that your negative results respect its boundary, because that boundary is where the real mechanism of the difficulty lives.

**Source:** [The Complexity of Computing the Permanent](../works/the-complexity-of-computing-the-permanent.md) — the proof of Theorem 3, which generalizes Gaussian elimination to permanents modulo a power of two by observing that a row addition changes the permanent by the permanent of a matrix with two equal rows, tracks those as additional matrices of a second kind whose contribution vanishes once enough duplicated pairs accumulate, and chooses pivots with the fewest factors of two to keep the arithmetic valid. Read against Theorem 2, whose hardness claim explicitly excludes moduli that are exact powers of two.
