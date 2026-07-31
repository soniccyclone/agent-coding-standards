---
type: lesson
title: "Find the ratio that governs behaviour, not the magnitude"
figure: wirth
works: [algorithms-and-data-structures]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Find the ratio that governs behaviour, not the magnitude

**Lesson:** Cost analyses usually come out as functions of size, and size is what people then reason about. Sometimes the analysis simplifies to something better: a function of a dimensionless ratio between two quantities, with the absolute quantities cancelling out. When that happens it is worth stopping to notice, because the consequence is unusually strong. Behaviour becomes scale-free — the expected cost at a given ratio is the same whether the structure holds a thousand items or a billion — and the operational question shifts from "how big is it" to "how full is it", which is a question with a defensible answer and a knob attached. A system whose governing parameter is a ratio can be run at a chosen point on a known curve, and capacity planning becomes arithmetic instead of extrapolation.

Reading the curve is where the value is. Such curves are typically flat and forgiving through most of their range and then steepen sharply near the limit, so the operating decision is not "keep the ratio low" but "identify where the knee is and stay left of it." That framing is what turns an analysis into an operational rule, and it also prices the alternatives: the difference between a good and a poor repair strategy may be invisible at a moderate ratio and enormous near the limit, which means the choice between them is really a choice about how close to the limit you intend to run. Compare candidate mechanisms at the ratio you will actually operate at, not at the extremes where their differences are either invisible or irrelevant.

Two cautions belong with the result. A scale-free expected cost usually rests on an assumption of even distribution, and the worst case underneath it can be dreadful — every probe landing on an occupied slot, cost proportional to the whole structure — so the guarantee is probabilistic in a way the earlier structures' guarantees were not, and adopting it means accepting that the argument for the design is statistical rather than absolute. That is a legitimate engineering position but it should be taken deliberately, not absorbed from a table of averages. And where the analysis is intractable, or where a mechanism deviates from the idealized assumption, take the measured curve for the mechanism you are actually using rather than the derived curve for the idealized one; the two agree at low ratios and diverge exactly where the decision matters.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 5.4's probabilistic derivation of the expected number of probes for insertion and retrieval, its reduction via the harmonic function to an expression in the load factor alone, the accompanying table of expected probes against load factor showing about 2.56 probes at 90% occupancy, the explicit note that this figure does not depend on the absolute number of keys present but only on the load factor, the separate table for linear probing showing markedly worse behaviour at high load while agreeing closely at low load, and the section's opening acknowledgement that the worst-case performance is miserable and that the method requires confidence in the laws of probability.
