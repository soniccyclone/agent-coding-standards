---
type: lesson
title: "A faster structure that cannot retire the old one is an addition, not a replacement"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A faster structure that cannot retire the old one is an addition, not a replacement

**Lesson:** The standing recommendation to replace a linear arrangement with a searchable one is stated as if it were a swap: same information, better lookup. Before accepting it, ask what the linear arrangement is currently expressing besides membership. Very often it is also expressing an order — the sequence in which things were introduced — and that order is consulted by something. If it is, the searchable structure cannot take the linear one's place, because the reorganization that makes searching fast is exactly what destroys the order. What you get is not a replacement but a second structure over the same elements, with two sets of links to keep consistent on every insertion and removal, two things to reason about when something goes wrong, and a new invariant tying them together that nothing enforces. That is a considerably worse bargain than the one you thought you were considering, and it should be priced before, not after.

The second question is whether the speed-up is real at the sizes that actually occur. Asymptotic superiority is a claim about growth, and it becomes a claim about your program only when the populations are large enough for growth to dominate the constants. Many collections in real systems are structurally small — bounded not by data volume but by what a human wrote in one place — and for those the linear scan is not a compromise, it is the correct choice, and no amount of analysis will show that because the analysis is about the wrong regime. Measurement settles it, and the honest form of the result is not "the tree is not better" but "the tree is better only past a size these collections do not reach," which also tells you which collection to revisit if that ever changes.

Put the two together and the decision procedure is short: identify every property the current structure carries, not just the one you are trying to improve; determine whether the candidate preserves them or merely coexists with them; and only then measure, at the sizes that actually occur, whether the improvement it does offer is worth having. Skipping the first step is how a system acquires redundant structures whose consistency is a standing liability, in exchange for a gain that was never measured.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.6's discussion of symbol table search, which states that the linear list of objects is by far the simplest implementation, that a tree structure would in many cases be more efficient for searching and would therefore seem more recommendable, that experiments showed the gain in speed to be marginal because the lists are typically quite short and a tree's superiority becomes manifest only when a large number of global objects is declared, and that even when a tree is used for each scope the linear lists must still be present because the order of declarations is sometimes relevant in interpretation, as in parameter lists.
