---
type: lesson
title: "A degenerate optimum means your objective is missing a term, not a filter"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A degenerate optimum means your objective is missing a term, not a filter

**Lesson:** State a goal as "minimise X" and check what happens at the extreme before you build anything. Very often the true optimum is a trivial configuration that satisfies the letter of the goal and none of its intent: partition a network to minimise severed connections and the winner is one isolated element against everything else; minimise latency and the winner serves nothing; minimise disagreement and the winner is unanimity among one participant. The optimiser is not misbehaving. It found the best answer to the question you asked, which turns out not to be the question you meant.

The usual patch is a side condition — reject any answer where a part is smaller than some threshold — and it is worth understanding why that is the weaker fix. A hard filter introduces a cliff: candidates just inside it are accepted at full value and candidates just outside are discarded entirely, so the answer becomes sensitive to a number nobody can justify, and the search wastes effort in regions it will later throw away. Worse, it does not express the actual preference. You do not, in fact, believe that a 51/49 split is fine and a 49/51 split is worthless; you believe that imbalance is a cost that trades against the thing you were minimising.

Encoding that as a ratio says it properly. Divide the quantity you are minimising by the capacity of each part it touches, and add the results. A part with very little capacity now inflates its own term, so the trivial answer scores badly by the objective itself rather than by an external veto — and the badness scales smoothly with how trivial it is. Every candidate stays comparable to every other, the trade-off between the two concerns is stated once in the formula instead of being split across an objective and a rule, and there is no magic cutoff to defend. The scaling denominator should be whatever measures how much of the structure each part is actually responsible for, which is usually not simply how many members it has.

The transferable move is to probe every objective function for its degenerate solutions before implementing it, and to read each one as a missing term rather than a case to exclude. The degenerate answer is diagnostic: it names precisely the dimension your objective is silent about. Adding that dimension as a denominator or a penalty converts an unstated preference into a stated one, which is also the only form in which it can be reviewed, tuned, or argued with.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the graph-partitioning section of the social-network chapter: the observation that a newly joined member with no connections would be the minimum cut, the rejection of a bare size constraint in favour of a definition of "good cut" that balances cut size against the sizes of the resulting parts, and the normalized-cut formula that divides the cut by the volume of each side and sums the two ratios.
