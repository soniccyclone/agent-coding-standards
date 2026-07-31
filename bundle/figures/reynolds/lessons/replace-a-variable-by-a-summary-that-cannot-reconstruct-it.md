---
type: lesson
title: "A representation that cannot reconstruct the thing it represents is fine, provided every question asked of it factors through the summary"
figure: reynolds
works: [the-craft-of-programming]
axes: [primitive-count, hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# A representation that cannot reconstruct the thing it represents is fine, provided every question asked of it factors through the summary

**Lesson:** The instinct when replacing an abstract variable with a concrete one is to insist the mapping be reversible — anything less feels like losing information, and losing information feels like a bug waiting to happen. Drop the requirement. What actually matters is narrower: for every question the program asks of the abstract variable, the answer must be computable from the summary. If the only query is a threshold comparison, a single number can stand in for a whole set, and the fact that many different sets collapse to the same number is irrelevant, because the program can never tell them apart anyway. This is a different move from picking an encoding that covers only some abstract values; here every value has an image, but the image does not determine it.

The way to find such a summary is to enumerate the uses, not to contemplate the data. Go through every place the abstract variable is read and ask what fact is actually being extracted. If they all reduce to one derived quantity, that quantity is your representation. Then the obligations are mechanical and, notably, easier than for a faithful representation: each update site must be augmented to restore the summary, and because the summary is a min or a max or a count rather than the structure itself, those augmentations are usually a comparison and an occasional assignment rather than a structural edit. The proof that a merge restores the summary reduces to arithmetic on a handful of terms, with the ordering facts you already have in hand knocking most of them out.

The reward is the elimination of the original entirely. Once every read has been rewritten in terms of the summary, the abstract variable is written but never consulted, and it goes — along with its saves and restores at every recursion level, which were quietly the most expensive thing about it. What survives is one scalar per activation. Be honest in the write-up about which direction the correspondence runs, though: it is worth stating plainly that the summary is ambiguous and cannot express the original, because a later reader who assumes reversibility will introduce a new query that the summary cannot answer and will not discover the problem from the type.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 5.4.3's treatment of the reachable-set variable in the strongly-connected-components program, where it is represented by a single integer holding the smallest array position occupied by any member, or an out-of-range value if there is none; Reynolds notes explicitly that this gives an ambiguous representation, that the set cannot be expressed in terms of it and the other concrete variables, but that it supplies just the information the algorithm actually needs — the emptiness test on the intersection with the saved set becoming a comparison of that integer against the saved position, and the union operations becoming minimum computations — after which the set variables and their per-call saves are eliminated as auxiliary.
