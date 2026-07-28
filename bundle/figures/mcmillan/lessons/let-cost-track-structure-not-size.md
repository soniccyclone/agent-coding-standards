---
type: lesson
title: "Let cost track the description's structure, not the population it describes"
figure: mcmillan
works: [symbolic-model-checking-for-sequential-circuit-verification]
axes: [expressiveness, hardware-affinity]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Let cost track the description's structure, not the population it describes

The bet underneath this work is a claim about where difficulty actually lives. A circuit with a wide data path has an astronomically large set of reachable configurations, and every method that walked those configurations one at a time was therefore hopeless. But the reason the set is enormous is that the data path is wide, and a wide data path is *repetitive* — the same small piece of logic, many times over. Enormous and complicated are different properties, and the paper's authors argue that the state spaces of real hardware are the former without being the latter. So the goal becomes finding a representation whose size responds to how intricate the logic is rather than to how many configurations that logic admits.

This reframing is the whole difference between a method that stalls at toy examples and one that verifies a 32-bit pipeline. Nothing about the underlying mathematics changed — the fixed points being computed are the same fixed points. What changed is that the objects being manipulated are descriptions of sets rather than enumerations of them, so widening a register adds a little to the description instead of multiplying the enumeration. The paper's empirical program is precisely an attempt to confirm this: verification time grows as a modest polynomial in the *number of components*, not in the number of configurations.

The principle generalises well past verification because most interesting large sets in computing are large for boring reasons. They are products, or unions of near-copies, or the closure of a small rule set. Any time you find yourself paying for cardinality, ask whether the thing is actually complicated or merely populous, and whether your representation is charging you for the wrong one. Choosing a representation is choosing which of the two you pay for, and that choice usually dominates every subsequent optimisation.

A programmer who has absorbed this stops accepting "the data set is too big" as a terminal diagnosis and starts asking what generates the data set. They pick representations whose cost is proportional to the generating description, they measure complexity against the number of parts rather than the number of possibilities, and they treat an explicit enumeration as a representation of last resort rather than the natural starting point.

**Source:** [Symbolic Model Checking for Sequential Circuit Verification](../works/symbolic-model-checking-for-sequential-circuit-verification.md) — the motivating argument in the introduction about data-path regularity yielding large but structurally simple state spaces, and the asymptotic results that test the claim.
