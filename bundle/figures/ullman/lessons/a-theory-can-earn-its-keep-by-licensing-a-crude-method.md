---
type: lesson
title: "A theory can earn its keep by licensing a crude method"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# A theory can earn its keep by licensing a crude method

**Lesson:** A general framework is usually presented as a recipe to instantiate, and the instantiation is expected to look like the framework: if the theory speaks of families of randomised functions composed into layered decision rules, the implementation is expected to contain families of randomised functions. That expectation is what makes people either build far more machinery than their problem needs or dismiss the theory as academic. The third option, and often the right one, is to use the theory to identify the shape a solution must have, then supply the crudest object of that shape available.

The shape here is a cheap grouping under which any pair worth examining lands together at least once. Exact equality on a single field is a legitimate instance: it groups, it is cheap, and used across a few different fields it forms a disjunction with a real, if unanalysed, error profile. The implementation need not even hash. Sorting the records by a field and walking the runs of equal values produces exactly the same grouping using a primitive that every system already has, that streams, that spills to disk gracefully, and that nobody has to be taught. Three sorts and three linear scans replaced a scheme whose full form would have required minhashing, banding, and parameter selection, and the theory is what made it defensible rather than a hack.

Two judgements have to be made honestly for this to be sound rather than lazy. First, what the crude instance's error profile actually is: exact-match grouping misses any pair that agrees closely but not exactly on every field, and that omission has to be checked against the requirement rather than hoped away. Second, whether the omission matters to whoever consumes the answer. A near-match that no field pins down exactly may be a pair the downstream decision would have rejected anyway, in which case the false negative costs nothing real. That is a question about the consumer, not about the algorithm, and answering it is what converts an unprincipled shortcut into a deliberate one.

The habit worth forming is to read a general technique twice: once for the mechanism it proposes, and once for the requirements it proves are sufficient. The second reading is the more valuable, because it tells you the space of things that would work, and the cheapest member of that space is frequently something you already have and would not have thought to justify. The theory's return on investment comes from knowing you are allowed to do the simple thing, not from doing the elaborate thing.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's entity-resolution case study, where two million-record customer databases are matched by three grouping functions that fire only on identical names, identical addresses, and identical phone numbers, implemented not by hashing but by sorting the records three times and scoring consecutive equal runs, with the acknowledged miss of any true pair matching exactly on no field dismissed on the ground that a court would not have accepted such a pair as proof anyway.
