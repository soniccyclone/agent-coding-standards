---
type: lesson
title: "Make the mechanism replaceable and the invariant not"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Make the mechanism replaceable and the invariant not

**Lesson:** Every extension point is two decisions pretending to be one. The visible decision is what the user may supply. The invisible and more important one is what must remain true no matter what they supply. Get the pairing right and the extension point is nearly free: a system can let anyone substitute the function that decides which consumer each item is routed to, while holding fixed that each item lands at exactly one consumer. Everything downstream — the correctness of grouping, the absence of double counting, the claim that a consumer sees all of a key's values — rests on the invariant and not at all on the particular routing function, so the customisation cannot break anything, and the implementer does not have to reason about which functions users might write.

The failure mode is exposing the invariant as if it were the mechanism. If the substitution point had been "supply your own distribution policy" with no stated constraint, a user would eventually write one that sends an item to two consumers, or none, and the resulting defect would surface far away, as a wrong aggregate rather than a configuration error. That is what makes the discipline worth the small effort of writing the constraint down as a constraint rather than a suggestion: the property that survives arbitrary user code is the entire basis on which the rest of the system was reasoned about, and if it is not enforced or at minimum stated, the system's guarantees quietly become conditional on plugins nobody reviewed.

Applying this in practice is a two-column exercise done before designing the interface, not after. In one column, the parts of the behaviour that are genuinely matters of policy — which sharding function, which eviction order, which retry schedule, which comparison. In the other, the properties the surrounding code has already assumed — totality, disjointness, determinism, termination, monotonicity. The interface should offer everything in the first column and make the second column unreachable, ideally by construction rather than by documentation. And when a request arrives to make something in the second column configurable, the honest answer is not "no" but "that is not a setting, that is the thing the design is built on; changing it is a different design."

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 2's footnote to the section on grouping by key, which permits users to supply their own hash function or other method for assigning keys to Reduce tasks while stating that whatever algorithm is used, each key must be assigned to one and only one Reduce task.
