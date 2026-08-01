---
type: lesson
title: "Normalize away the encodings that could hide what you count"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness, parallelizability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Normalize away the encodings that could hide what you count

**Lesson:** A claim about every possible implementation is only as good as the accounting it rests on, and the usual objection to such a claim is that some cleverer implementation could cheat the count. If you are bounding how much data must move, someone will ask whether a smarter preprocessing step could compress or fuse the messages and evade the bound. The way to close that gap is not to enumerate the tricks and refute them one at a time. It is to show that any implementation can be rewritten into a canonical one that sends the raw items, with every transformation the clever version performed relocated to the receiving side, and that this rewrite never increases the counted quantity. After that, counting on the canonical form bounds the whole class, because every member has a canonical twin that is at least as good.

The rewrite is doing real work and it is worth seeing why it is available here. Work that a sender does to an item before transmitting it is work the receiver could equally do after receiving it, since the receiver gets the item either way; the transformation is not tied to the sender by anything but convenience. Similarly, a sender never needs to emit two messages toward one destination on behalf of one item, because the destination could reconstruct both from the item itself. Both moves rest on the same observation — the sender holds no context the receiver lacks — and when that observation holds, the freedom to be clever at the sending end is a freedom that cannot change the count. When it does *not* hold, that is exactly where the bound is fragile and worth interrogating.

The general habit is to precede any universal claim with a normalisation argument, and to state which degrees of freedom the normalisation removes. It is the same discipline as choosing a canonical form before proving two things equal, or fixing an evaluation order before reasoning about cost: you are shrinking the space of things you must argue about to a set of representatives, at the price of one lemma. Skipping the lemma is what produces bounds that are quietly about the implementations the author happened to imagine — and the ensuing argument, where a reader proposes an encoding trick and the author patches the analysis, is a symptom of a normalisation that was never done rather than of a bound that was nearly right.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's development of mapping schemas, which notes that the value communicated for a related input and output need not be the input itself but is derived from it, and that there is technically never a need for more than one key-value pair per input-output pair, because the input can be transmitted unchanged and whatever the Map function would have done can instead be done by the Reduce function at the covering reducer.
