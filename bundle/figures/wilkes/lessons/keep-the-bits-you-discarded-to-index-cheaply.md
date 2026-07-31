---
type: lesson
title: "When you index by a lossy function of a key, store the part you discarded so a hit can be told from a coincidence"
figure: wilkes
works: [slave-memories-and-dynamic-storage-allocation]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# When you index by a lossy function of a key, store the part you discarded so a hit can be told from a coincidence

**Lesson:** The cheapest way to find where an item might be is to throw most of its key away — keep the low-order part, or a hash of it — because that converts a search into an address computation. What makes the trick safe is not finding a mapping that avoids ambiguity, which over any key space worth indexing you cannot do, but storing beside each item exactly the portion of the key the mapping destroyed. Lookup then has three steps rather than one: compute the slot, read whatever occupies it, and compare the remembered portion against the corresponding portion of the key you actually wanted. Agreement is a hit; disagreement means the slot belongs to something else and the authoritative source must be consulted.

The property this buys is that the fast path has no way to answer wrongly. Its only failure mode is failing to help, which costs time and nothing else. Compare the family of designs that instead try to make collisions impossible — uniqueness constraints, perfect hashing, exclusive assignment of slots to owners. Those purchase their guarantee with a global invariant over everything that will ever be stored, and that invariant must be understood and preserved by every piece of code that touches the structure. Local collision detection needs a fixed amount of extra storage per slot and cooperation from nobody. The width of the retained portion, not the ingenuity of the mapping, is the real design variable, and it is a variable you can price.

The working rule: any time you compress an identifier to reach a location — bucket index, shard number, ring position, cache line, memo key — say out loud what information the compression destroyed and where the surviving copy of it lives. If no copy survives, the structure cannot distinguish a hit from a coincidence, and what you have built is fast and intermittently wrong. One further constraint on where that copy lives: it belongs in the slot, checked by the same read that produced the candidate, not in a parallel directory of what each slot is supposed to hold. A second structure obliged to agree with the first is a new consistency problem, and it will be wrong at exactly the moments you most need the check.

**Source:** [Slave Memories and Dynamic Storage Allocation](../works/slave-memories-and-dynamic-storage-allocation.md) — the instruction-slave scheme, in which a main-memory address is reduced modulo the slave's size to select a slave register while the high-order remainder of that address is stored alongside the word as tag bits, and a lookup counts as a hit only when the stored tag agrees with the high-order part of the address sought; otherwise the word is taken from main memory and a copy left behind.
