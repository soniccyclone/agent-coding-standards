---
type: lesson
title: "When both extremes of a parameter are easy for opposite reasons, the hard case is the middle"
figure: yao
works: [should-tables-be-sorted]
axes: [expressiveness, hardware-affinity]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# When both extremes of a parameter are easy for opposite reasons, the hard case is the middle

**Lesson:** Sweep a design parameter to its limits and you sometimes find the problem is cheap at both ends. That looks like good news and is usually a warning. If the two ends are cheap for the *same* reason, fine — the problem is just easy. If they are cheap for two different mechanisms, then somewhere between them each mechanism is running out of room while the other has not yet taken over, and the true worst case is hiding there, unaddressed by either technique and invisible to anyone who only tested the endpoints. The interesting question is never "what happens at the limits" but "where does the crossover sit, and what is the cost at the crossover."

Consider what makes each end cheap in the storage-lookup setting. When the space of possible values is barely larger than the collection you are storing, position itself is informative: an address computed from the value you are seeking already narrows things almost to a point, so the ability to choose where things go carries the day. When the value space is astronomically larger than the collection, position is useless — any addressing rule collides — but now a single stored cell can hold a value from a space so vast that it can name which of an enormous prearranged catalogue of arrangements was used, so the ability to encode carries the day. Both mechanisms deliver a constant number of lookups. Neither is available in strength in between, where the value space is large enough to defeat addressing but not large enough to make a directory cell expressive enough to matter, and that regime is where the honest answer was still unknown.

Two working habits follow. First, when you validate a design by probing extremes, name the mechanism responsible for each extreme's success rather than recording only the number; if the mechanisms differ, you have not covered the range, you have covered two special cases. Second, treat the crossover as the design's actual specification point. Systems get built for the regime they will really run in, and that regime is normally neither degenerate end — so a technique justified by asymptotic behavior and a technique justified by small-case behavior can both be inappropriate for the same deployment. The two mechanisms are also worth holding separately in mind as independent levers, because a real system can have one of them cheaply available and the other not, and knowing which one your speed is coming from tells you what breaks when the parameter drifts.

**Source:** [Should Tables Be Sorted?](../works/should-tables-be-sorted.md) — the conclusions section, which observes that in either extreme case, a value space barely exceeding the collection or one exponentially larger, a constant number of probes suffices, and attributes the two results to addressing power and encoding power respectively while leaving the intermediate range open; together with the pointer to the polynomially-bounded-space result that occupies the near end.
