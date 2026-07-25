---
type: lesson
title: "When you cannot measure a problem's cost, measure the cheap translations between problems instead"
figure: cook
works: [the-complexity-of-theorem-proving-procedures, the-p-versus-np-problem, an-overview-of-computational-complexity]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# When you cannot measure a problem's cost, measure the cheap translations between problems instead

**Lesson:** The absolute question — how much work does this problem actually require — is usually beyond reach. The relative question is not. If you can cheaply rewrite instances of one problem as instances of another, you have established an inequality between their costs without knowing either cost, and because cheap rewriting composes, the inequalities accumulate into an ordering rather than a pile of isolated observations. Problems that rewrite into each other in both directions occupy the same rung, and a single representative on that rung stands in for all of them. This is how an unanswerable measurement question becomes a tractable classification question, and why a field that has proved almost no interesting absolute lower bounds nonetheless knows a great deal about what is hard.

The engineering leverage is that the ordering is cumulative and cheap to extend. Once one problem is known to sit at the top of a class, showing a new problem also sits there costs one translation rather than a fresh proof from first principles, and every such addition strengthens the evidence for the whole rung at once. Hundreds of unrelated-looking scheduling, routing, and graph questions collapse into one object of study, so effort spent understanding that object pays out everywhere. The corresponding cost discipline is that the translation itself must be cheap relative to the resource you are reasoning about; a rewriting step that consumes the very budget under examination proves nothing.

The move generalizes past the resource it was invented for. Ask whether a problem parallelizes and the same structure appears: rather than proving no fast parallel algorithm exists, show the problem is as hard as anything else solvable sequentially in reasonable time under translations that are cheap in the parallel sense, and you have converted "I could not find a parallel algorithm" into "finding one would overturn everything." The generic recipe is to pick the resource you care about, define translations that are negligible with respect to it, and use them to bind unknown quantities to each other.

A programmer who internalizes this stops demanding absolute answers about difficulty and starts hunting for correspondences. Faced with a component whose cost is unclear, the productive question is not how expensive it is but what known problem it is secretly the same as, because the second question is answerable and drags the first behind it.

**Source:** [The Complexity of Theorem Proving Procedures](../works/the-complexity-of-theorem-proving-procedures.md) — the opening section, where reducibility via a bounded oracle machine is defined, observed to be transitive, and used to carve problems into equivalence classes described as degrees of difficulty. Also [The P versus NP Problem](../works/the-p-versus-np-problem.md) — the propositions establishing that reducibility transfers tractability downward and completeness upward, and the deliberate analogy drawn to the older reducibility notions of computability theory. Also [An Overview of Computational Complexity](../works/an-overview-of-computational-complexity.md) — the parallel-computation section, which applies the identical device to the question of which problems resist speedup from many processors.
