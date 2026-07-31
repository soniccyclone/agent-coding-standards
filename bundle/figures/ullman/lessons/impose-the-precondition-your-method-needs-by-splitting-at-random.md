---
type: lesson
title: "Impose the precondition your method needs by splitting at random"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, parallelizability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Impose the precondition your method needs by splitting at random

**Lesson:** A technique often carries a structural precondition that your data does not satisfy — the method wants two disjoint populations with interaction only across the divide, or a strict layering, or an acyclic ordering, and what you have is one homogeneous mass with connections everywhere. The reflex is to treat this as disqualifying and go looking for a general-case algorithm, which is usually much harder and often does not exist. The alternative is to manufacture the precondition: partition your population arbitrarily, declare the partition to be the structure, and throw away everything that does not fit it.

This sounds like vandalism and is not, provided the partition is random and independent of what you are searching for. Any group you hoped to find gets split in proportion, roughly half to each side, and the connections you retain are the ones that happen to straddle the cut — again roughly half. So the target survives at reduced size rather than being destroyed, and crucially it survives *unbiasedly*: the split has no correlation with membership, so it cannot systematically hide one kind of group while preserving another. You pay a constant factor in the size of what you can detect and you buy access to an entire body of technique that was otherwise inapplicable. Repeating with fresh splits recovers most of what any single split happened to cut badly.

The condition on which all of this rests is that the imposed structure is chosen without reference to the thing being sought. A partition that follows some existing attribute — region, tenant, timestamp bucket — is not neutral; it is correlated with exactly the groupings that attribute participates in, and it will annihilate them completely while leaving unrelated ones intact. That produces a systematically distorted result which looks like a finding. Randomness is doing real work here and is not interchangeable with any convenient existing division.

More broadly, this reframes what a precondition is. A precondition is not always a fact about the data that you check; sometimes it is a shape you are allowed to impose, at a cost you can quantify in advance. Before concluding that a method does not apply, work out what would have to be true, then ask whether an arbitrary choice can make it true and what fraction of the signal that choice would cost. The same reasoning licenses random projection, random sharding for locality, and randomized tie-breaking: in each case an arbitrary decision buys a structural property, and being arbitrary is precisely what stops it from biasing the result.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the passage in the social-network chapter explaining how to apply complete-bipartite-subgraph search to an ordinary single-type graph by dividing the nodes at random into two equal groups, on the reasoning that about half a community's nodes and about half its edges will land across the divide, leaving a large enough nucleus to detect and grow.
