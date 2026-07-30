---
type: lesson
title: "A generalization earns its place only with several real instances below it and nontrivial laws above it"
figure: reynolds
works: [the-craft-of-programming]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# A generalization earns its place only with several real instances below it and nontrivial laws above it

**Lesson:** Replacing a fixed thing by a parameter is trivially always possible, so the interesting question is when it is worth doing, and there is a two-sided test. Look downward: does the parameterized form have several genuinely useful special cases, ones you would have wanted separately and can now get by supplying an argument? Look upward: does it satisfy nontrivial general laws — statements provable about the parameterized form itself, once, and then available at every instance? A candidate that passes only the downward test is a naming convention, and you have merely collected some unrelated things under one heading. A candidate that passes only the upward test is a piece of theory with no customers. Both sides have to hold, and requiring both is what separates abstraction from the reflex of adding a parameter because a parameter can be added.

Generalizing the notion of a collection being sorted illustrates the shape. Fix the comparison and you have increasing order. Make the comparison a parameter and one definition instantly yields increasing, strictly increasing, decreasing, strictly decreasing, all-equal and all-distinct — six familiar properties that would otherwise have been six definitions with six sets of lemmas. That is the downward side, and it is substantial. The upward side is what makes it pay: the general form obeys laws saying that sortedness survives restriction to any subregion, that it holds vacuously on regions too small to compare anything, and — the load-bearing one — that a collection split into two adjacent regions is sorted exactly when each region is sorted and every value in the first stands in the relation to every value in the second. That last law is a decomposition principle, proved once at the general level, and it is precisely what an argument about merging or partitioning needs. Six definitions would have needed it six times.

The test is worth applying in the other direction too, as a way of pruning. When you catch yourself introducing a parameter, try to name three instantiations you actually want and one law that becomes provable at the general level. If the instantiations are strained or the only "laws" are restatements of the definition, take the parameter out. And when a generalization does pass, expect a second dividend: the laws usually come in a family — restriction, the degenerate case, and composition of adjacent pieces — and if one of the three is missing, that gap tends to mark exactly the case your later arguments will stumble on.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 2.2.10's generalization of ordering from a fixed comparison to an arbitrary relation, which states as its criterion that a worthwhile generalization should have several useful special cases and satisfy nontrivial general laws, then exhibits the six special cases and the laws for restriction, for domains too small to constrain, and for splitting a domain into two adjacent parts.
