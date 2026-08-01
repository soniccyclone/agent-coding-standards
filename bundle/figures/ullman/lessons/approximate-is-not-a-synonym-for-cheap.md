---
type: lesson
title: "Approximate is not a synonym for cheap"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Approximate is not a synonym for cheap

**Lesson:** Approximate methods are habitually filed as the fast option and exact methods as the expensive one, so the choice between them gets framed as how much correctness you can afford to give up. That framing is wrong often enough to be dangerous. An approximation's advantage exists in a regime, and outside that regime the exact method can be strictly better on every axis at once — faster to run, simpler to reason about, and free of the missed answers the approximation quietly accepts. Nothing is being traded there. One option dominates, and a team that framed the decision as a trade-off will never look for it.

The regime in question is usually set by how demanding the query is. A machinery of summaries and probabilistic screens earns its cost when the criterion is loose, because a loose criterion admits a large and diffuse answer set that no simple structural fact can isolate. Tighten the criterion toward near-identity and the picture inverts: near-identical objects are forced to agree in structural ways that can be checked directly and cheaply. They must be of nearly the same size, they must share elements early in any fixed ordering, and each such necessary condition prunes almost everything without any probability entering the discussion. The tighter the requirement, the more constraints the requirement itself hands you.

So the diagnostic question to ask of any approximate scheme is what happens to it as the tolerance shrinks, and the corresponding question to ask of the exact alternative is what necessary conditions the tolerance implies. If the answers cross somewhere inside the range of thresholds you care about, the threshold is a design input and not just a tuning knob, and the honest architecture may be two implementations selected by regime. If the crossing lies outside the range you will ever use, you have learned that one of the two candidates was never in the running, which is also worth the ten minutes.

The wider habit is to distrust the intuition that relaxing a requirement always makes a problem cheaper. Requirements are constraints, and constraints are information; a demanding requirement can be easier to satisfy efficiently than a lax one precisely because it rules out so much. Exact duplicate detection is easier than near-duplicate detection. Equality joins are easier than similarity joins. The lax version of a problem is frequently the hard one, and noticing that inverts the usual advice about starting with the loosest specification you can get away with.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's section on methods for high degrees of similarity, which opens by observing that the locality-sensitive machinery is most effective when the accepted degree of similarity is relatively low, and that when near-identical sets are wanted there are methods that are both faster and exact, with no false negatives, going on to derive filters from length alone and from indexed prefixes whose required length shrinks as the similarity threshold rises.
