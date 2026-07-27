---
type: lesson
title: "The static shape of a model decides which execution costs are even possible"
figure: fagin
works: [on-the-desirability-of-acyclic-database-schemes]
axes: [hardware-affinity, parallelizability, verifiability]
subdomains: [databases-and-data-management, algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# The static shape of a model decides which execution costs are even possible

**Lesson:** The paper opens one of its conditions with a scenario every engineer recognizes. Someone combines four collections whose final answer holds ten rows, and along the way materializes an intermediate result of a million, because the two pieces joined first happen to agree on very little. Nobody wrote a bug. The final result is correct and small. The cost was paid entirely by the order in which the pieces were combined, and the order was chosen by whoever wrote the expression or by an optimizer guessing at it.

What the equivalence theorem adds is that whether a blowup-free order exists at all is not a property of the query, the data, or the optimizer. It is a property of the shape of the schema, decided when the design was drawn. A combining order in which no intermediate result is ever larger than the final answer exists precisely when the schema satisfies the same structural condition that makes local consistency checks sufficient. A stronger form, where the pieces are absorbed one at a time so only a single intermediate needs to be held, is equivalent to the same condition. Get the shape wrong and no evaluation strategy can rescue you, because the space of strategies contains nothing acceptable. Get it right and the tree that certifies the property also tells you the order to use.

The general claim is that resource behavior at run time can be entailed by static structure, and that the entailment is worth locating precisely. Engineers habitually sort concerns into design-time and run-time bins and treat memory footprint, message volume, and intermediate materialization as run-time problems to be tuned later with better plans, bigger machines, or a cache. Sometimes the ceiling on tuning was set much earlier. When the achievable cost is a function of the model's shape, tuning is bounded by a decision that was cheap to make differently and is expensive to revisit.

The corresponding practice is to ask, of any structure you are designing, what the best possible execution over it would look like and whether the structure admits it. A schema, a module dependency graph, an event topology, and a normalized data model all constrain the plans that can be written against them. Fagin and his coauthors also show the sharper version of the same point on the distributed side, where the same shape decides whether a communication-frugal pruning program exists before shipping anything. The design does not merely influence performance. It fixes what performance is reachable.

**Source:** [On the Desirability of Acyclic Database Schemes](../works/on-the-desirability-of-acyclic-database-schemes.md) — the conditions on monotone and monotone-sequential join expressions, with the worked scenario of an intermediate result vastly exceeding the final answer, and the companion condition on the existence of a full semijoin reducer for distributed evaluation.
