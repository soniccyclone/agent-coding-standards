---
type: lesson
title: "When nothing co-occurs, manufacture overlap by lowering resolution a little on each side"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# When nothing co-occurs, manufacture overlap by lowering resolution a little on each side

**Lesson:** Comparing two entities by their recorded interactions requires that they have interacted with some of the same things. When the interaction record is extremely sparse — each party touching a vanishing fraction of an enormous catalogue — that requirement fails almost everywhere. Two parties with essentially identical taste may share not one interaction, and the comparison correctly reports no evidence. Nothing is broken; there is genuinely no overlap to measure. Collecting more data does not fix it either, because the catalogue grows alongside the activity and sparsity is preserved.

The move that does fix it is to lower the resolution of the thing being counted. Group the catalogue into families of near-identical members, replace each party's individual interactions with their aggregate over each family, and two parties who touched different members of the same family now demonstrably overlap. Evidence that was spread too thin to register is concentrated until it registers. This is not an approximation forced by resource limits; it is a statement that the original granularity was finer than the question, and that distinctions between near-identical members were never what the comparison was about.

Two details make the technique work rather than destroy the signal. Coarsen gently — halving the number of distinct groups, not collapsing to a handful — because the goal is to create just enough co-occurrence to compare, and aggressive grouping erases the distinctions the comparison exists to find. And coarsen alternately on both sides: group the catalogue, recompute the table, group the parties on the coarsened table, recompute again, and repeat. Each pass on one axis makes the next pass on the other axis better informed, because grouping parties is itself a similarity computation suffering from the same sparsity, and it has just been given denser input.

The resulting hierarchy is then used as a fallback ladder rather than a replacement. Answer a question at the finest level that has evidence; when a pair has none, ask the same question of the groups they belong to; when even that is empty, look to neighbouring groups. The general habit worth taking away is to treat granularity as a dial you are allowed to turn rather than a property of the schema, and to reach for it whenever a method is failing not because it is wrong but because it is being asked to compute over an empty intersection.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the section on clustering users and items in the recommendation-systems chapter, which observes that even same-genre items are rarely rated by the same people, prescribes hierarchical grouping stopped early at roughly half as many groups as members, alternates the grouping between the two axes with the table recomputed in between, and answers a query from the group-level table when the pair itself has no entry.
