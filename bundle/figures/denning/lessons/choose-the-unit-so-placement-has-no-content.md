---
type: lesson
title: "Choose the unit of allocation so that the hard sub-problem has nothing left to decide"
figure: denning
works: [virtual-memory]
axes: [primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---
# Choose the unit of allocation so that the hard sub-problem has nothing left to decide

**Lesson:** Allocation splits into three questions — what to evict, when to load, and where to put the thing — and Denning's survey shows that the third one has wildly different weight depending on a single upstream choice. Let the units be whatever size the program asked for and "where" becomes a subject: you need a list of the gaps, a rule for choosing among them, a story for what happens when the total free space is sufficient but no single gap is, and a policy for shuffling things to consolidate. Make every unit the same size and the question evaporates, because every free unit is exactly the right size. Same three questions, but one of them now has a one-line answer, and the eviction rule can supply it.

What makes this more than an aesthetic preference is that the survey prices the alternative and finds the price is structural rather than incidental. Under steady-state churn, the number of gaps settles at about half the number of occupied units — not because anyone implemented it badly, but as a consequence of insertions and deletions being equally likely on either side of any given occupant. From that, if you insist on keeping the gaps large enough that finding one stays cheap, a derivable fraction of the whole resource has to sit unusable; and if you instead let the gaps get small and periodically shuffle everything together, the fraction of time spent shuffling obeys its own trade curve against the same wasted fraction. The two escapes lead to the same wall from different sides. You can pick where on the curve to sit, but you cannot get off it, and Denning notes the further irony that by the time consolidation looks necessary the resource is nearly full anyway, so it buys almost nothing.

The uniform choice is not free either, and the discipline is to check that its cost is of a better *kind*. Fixed units strand whatever space the last unit doesn't need — but that loss is bounded by the unit size, which is a parameter you control, whereas the variable-size losses emerge from the workload's arrival pattern and are not under anyone's control. Trading an emergent, workload-dependent cost for a bounded, tunable one is almost always the right direction, and it pays a second time in the mechanism: interchangeable units mean the transfer machinery has one size to handle, and the whole class of bugs around length checks and buffer overruns on variable-length moves never comes into being.

So when a design is heading toward a free-list, a best-fit heuristic, a compaction pass, and a defragmentation story, treat that as evidence about the unit and not about the algorithm. Ask what unit would make the choice trivial, find out what that uniformity would cost, and check whether the cost is bounded by a knob or emergent from the load. Concretely, this is the reasoning behind fixed-size pages, slab and arena allocators, fixed-width record layouts, and uniform message frames — in each case the interesting work was choosing the unit, and the placement algorithm nobody had to write is the payoff.

**Source:** [Virtual Memory](../works/virtual-memory.md) — the storage-utilization section: the equilibrium argument giving the ratio of gaps to occupants, the rule bounding unusable space against gap size, the consolidation-overhead result, and the summary comparison arguing that uniform blocks give memory a single interchangeable treatment while variable-size blocks require an up-front investment in wasted space and placement machinery.
