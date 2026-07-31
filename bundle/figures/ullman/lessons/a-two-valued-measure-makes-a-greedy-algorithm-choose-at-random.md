---
type: lesson
title: "A two-valued measure makes a greedy algorithm choose at random"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# A two-valued measure makes a greedy algorithm choose at random

**Lesson:** Most procedures that build structure incrementally — merge the closest pair, assign each item to the nearest anchor, expand along the cheapest edge — are not really consuming a measure. They are consuming an *ordering* the measure induces. That distinction is invisible while the measure takes many values and becomes fatal the moment it takes few. If every related pair scores identically and every unrelated pair scores identically, the ordering is one enormous tie, and every step of the procedure is settled by whatever the tie-break happens to be: insertion order, hash order, the random seed. The code is correct, the measure is well defined, and the output is arbitrary. Nobody notices, because the procedure still terminates and still emits a plausible-looking answer.

The usual diagnosis is to check whether the measure obeys the axioms of a metric, and it is worth noticing that a two-valued one typically fails the triangle inequality — two hops of length one can span a gap you scored at one. But repairing the axioms does not repair the problem. Widening the gap between "related" and "unrelated" so the triangle inequality holds leaves the ordering exactly as flat as it was. The axioms govern whether the measure is coherent; the number of distinct values it takes governs whether it can decide anything. Those are separate properties, and only the second one is what the algorithm actually needs.

The damage compounds with the schedule on which the decisions are made. An incremental procedure makes its most consequential commitments at the start, when almost nothing has been assigned and there is therefore the least evidence available to break a tie — and those early commitments are exactly the ones that everything downstream inherits and cannot revisit. Later, once groups have accumulated members, the same tie can be broken well, by scoring a candidate against the whole group instead of against a single element. So the procedure has the information it needs, just never at the moment it needs it. Reversing that order is often the whole fix: defer the ambiguous assignments, resolve the ones the measure genuinely separates, and come back.

Practically, this argues for auditing the *distribution* of a measure over your data before adopting any algorithm that ranks by it — not its definition, not its correctness, but how many distinguishable values it actually produces and how the ties are distributed. A measure that separates a few percent of pairs and shrugs at the rest is not a weak measure to be compensated for with more iterations or restarts; it is a measure carrying too little information for a ranking algorithm to run on, and the right response is to find a richer signal, or to switch to a method that consumes something other than an ordering.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the discussion of why standard clustering fails on unlabelled social graphs: the 0/1 and 1/∞ edge distances, the note that fixing the triangle inequality does not fix the underlying problem, the observation that hierarchical merging is likely to join nodes across community boundaries because all edge distances are equal, and the remark that a point-assignment method decides correctly if the ambiguous node is deferred until other nodes are placed.
