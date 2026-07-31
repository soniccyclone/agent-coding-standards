---
type: lesson
title: "Let the consumer's capacity to act set the threshold, then build on that assumption"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Let the consumer's capacity to act set the threshold, then build on that assumption

**Lesson:** A discovery system's output volume is normally treated as a consequence of the data and the algorithm, with the threshold tuned to whatever seems statistically defensible. That gets the dependency backwards. Every result the system emits has to be consumed by something with finite capacity — a person who must read it, an experiment that must be run, a review that must be scheduled — and if the emission rate exceeds that capacity, the excess results have no value whatsoever. Not diminished value: none, because they will never be acted on. So the threshold's real determinant is downstream throughput, and it should be set from that number and then justified statistically, rather than the reverse.

This sounds like a product concern and is actually a load-bearing engineering input, which is the part worth internalising. Once you have committed to a threshold that keeps output within acting capacity, you have asserted something strong about the shape of the intermediate results: there are not many of them. That assertion is exactly the assumption that makes aggressive implementation strategies safe — you can afford to keep the surviving candidates resident, you can afford a structure indexed by them, you can plan passes on the basis that the surviving set is small. A system designed for an output volume nobody could use is also a system that cannot make any of those assumptions, so it is slower as well as less useful. The two problems have the same cause and the same fix.

The general form: find the narrowest capacity anywhere along the path from raw input to realised effect, and let it propagate backwards as a constraint on everything upstream. Teams routinely optimise a stage in isolation and produce more throughput than the next stage can absorb, which converts into queue depth, staleness, or silently discarded work. Recognising the acting step as part of the system, subject to the same accounting as the compute steps, is what prevents that — and it usually reveals that the correct move is to raise the bar rather than to scale the machinery.

The uncomfortable corollary is that the threshold is not a scientific parameter and should not be defended as one. It encodes a decision about how much attention is available, which will change when the consumer changes, and pretending otherwise leads to arguments about statistical significance that are really arguments about staffing. Naming it honestly makes the tuning tractable and makes it obvious when the right fix is elsewhere.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the association-rules section of the frequent-itemsets chapter, which argues that a million rules meeting the thresholds cannot be read or acted upon, that the threshold is therefore adjusted so the surviving set stays small, and that this assumption has consequences for the efficiency of the algorithms developed later in the chapter.
