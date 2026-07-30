---
type: lesson
title: "An optimality result bounds the operation set it was proved over, never the problem itself"
figure: strassen
works: [gaussian-elimination-is-not-optimal]
axes: [primitive-count, expressiveness]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# An optimality result bounds the operation set it was proved over, never the problem itself

**Lesson:** When a field believes a cost is unavoidable, the belief is usually resting on a theorem, and the theorem almost always carries a restriction clause that has stopped being read. The classical case: the cubic cost of solving a linear system was known to be optimal — under the assumption that the algorithm manipulates whole rows and columns as indivisible units. That clause is not a technicality; it is the entire content of the result. It says nothing about what is achievable by an algorithm that treats the matrix as a nested arrangement of blocks and combines them in ways the row-and-column vocabulary cannot name. The lower bound was real, sharp, and correctly proved, and it was still not a bound on the problem.

The practical discipline is to read every impossibility or optimality claim as a pair: a cost, and the algebra of moves the cost was minimized over. Then ask whether the algebra is a fact about the problem or a fact about how people have been thinking about it. Operation sets get frozen into place by notation, by the shape of existing implementations, by what the previous generation's proofs happened to be tractable over — none of which are constraints imposed by the mathematics. A restriction adopted for convenience of analysis silently becomes an axiom about reality, and afterward nobody looks for algorithms outside it because a theorem appears to forbid them.

This inverts how a hard cost barrier should feel. A barrier is not a reason to stop; it is a pointer to the assumption doing the work, and therefore the most precisely located place to attack. Find the sentence in the theorem that says "restricted to", widen exactly that, and the bound it protected simply does not apply to you anymore. The corollary is a warning about your own results: whenever you prove your design is as good as it can get, write the operation set down explicitly and treat it as the weakest part of the claim, because it is where someone else will get past you.

**Source:** [Gaussian Elimination is not Optimal](../works/gaussian-elimination-is-not-optimal.md) — the opening section, which sets the new bound against the earlier optimality result for Gaussian elimination and is careful to state the restriction (operations on rows and columns taken whole) under which that earlier result holds.
