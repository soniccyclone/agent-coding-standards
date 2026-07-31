---
type: lesson
title: "Deduplicating derivations is not deduplicating conclusions"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Deduplicating derivations is not deduplicating conclusions

**Lesson:** A search that combines partial results to build larger ones will reach the same conclusion many times over, and there are two entirely different reasons why. The first is that a single underlying object can be assembled in many ways — split at any of its internal joints, and each split is a distinct route to the same assembly. The second is that many distinct underlying objects genuinely justify the same conclusion. These look identical from inside the algorithm, which just sees a result it has produced before, and they have completely different remedies. Confusing them leads to either wasted engineering or a false expectation of how much waste is left.

The first kind can be eliminated outright, and the way to do it is to fix a canonical decomposition. Instead of allowing an object of size k to be built from any of its k splits, insist that the first piece have a size from some sparse set — powers of two, say — with the remainder constrained relative to it. Then every object has exactly one legal decomposition, and it is assembled exactly once no matter how many joints it has. Making this work usually needs a companion step that keeps the intermediate collections disjoint, subtracting off what is already known so each stage holds only what is genuinely new at that stage; without it the canonical scheme leaks duplicates back in through overlapping stages.

The second kind cannot be eliminated by any decomposition scheme, because the redundancy is in the world rather than in your enumeration. If two genuinely different structures both establish the same fact, then any complete method will encounter both. The only defence is to detect the repeat when it happens and drop it — which is what the duplicate-elimination step in each round is for, and why that step does not become unnecessary once the canonical scheme is in place. Recognising this in advance stops you from hunting for a cleverer enumeration that does not exist.

The practical value of separating them is in setting expectations before you build. Ask, of any combining search: how many ways can one object be assembled, and how many distinct objects support one conclusion? The first number is a property of your algorithm and is yours to reduce to one. The second is a property of the domain and bounds how much duplication you will still be paying for afterwards. Two systems with identical worst-case bounds can differ enormously in practice because one of them only pays the second cost — which is also why worst-case analysis often cannot distinguish the sharper method from the blunt one.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the smart transitive closure section of the social-network chapter, which decomposes every path into a head whose length is a power of two and a shorter tail so each path is discovered once, subtracts the accumulated relation to keep the staged relation to exactly the pairs whose shortest path has the current length, and the accompanying box distinguishing a path from a path fact and noting that multiple genuinely distinct paths between the same endpoints still cause the same fact to be discovered repeatedly.
