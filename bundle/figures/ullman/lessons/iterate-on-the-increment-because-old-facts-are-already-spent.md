---
type: lesson
title: "Iterate on the increment, because old facts are already spent"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Iterate on the increment, because old facts are already spent

**Lesson:** A computation that grows a set until it stops growing is naturally written as: combine everything known so far with the rules, take the union, repeat. That formulation is correct and does an enormous amount of redundant work, because a fact that has been in the set for several rounds has already been combined with every rule and every partner it will ever meet, and combining it again cannot produce anything new. The repair is to carry the increment separately — the facts first derived on the previous round — and drive each round from the increment alone, merging it into the accumulated set as you go. The set still grows the same way and the fixpoint is identical; only the wasted re-derivation disappears.

The saving is not a constant factor. Under the whole-set formulation each fact participates in a round for every round it survives, so its cost is multiplied by how early it was discovered; under the increment formulation each fact participates exactly once, ever. That collapses the total work across all rounds to something proportional to the size of the data rather than the size of the data times the number of rounds — which is the difference between a computation whose cost tracks the graph and one whose cost tracks the graph times its depth.

The soundness condition is worth stating because it is what limits the technique. Deriving only from the increment is valid when the rules are monotone — nothing already derived can later be retracted — and when combining two old facts genuinely cannot yield anything that was not already produced when the later of them was new. The first condition fails in the presence of negation or deletion, where an accumulated conclusion can become invalid and the whole set really must be reconsidered. The second needs care whenever a rule combines two derived relations rather than a derived one with a fixed one, since then a new fact can pair with an old one on either side and the increment must be applied to each position in turn.

The general shape — "what changed, and what does that change entail" — is the same idea behind incremental builds, dirty-region redraw, and change-data-capture pipelines. It is nearly always available, it is nearly always a large win, and the interesting part of adopting it is never the mechanism but the analysis of when re-deriving from the increment alone is complete.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the seminaive-evaluation sections of the social-network chapter, which keep a relation of newly discovered facts alongside the accumulated relation and join only the new ones with the arc relation each round, together with the cost comparison showing that seminaive reachability costs on the order of the number of arcs across all rounds because each node enters the new-fact relation exactly once, and the footnote on the term's origin.
