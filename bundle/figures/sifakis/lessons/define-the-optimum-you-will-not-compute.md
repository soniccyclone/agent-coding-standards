---
type: lesson
title: "Define the best possible version of the thing you are approximating, even when you intend to ship something worse"
figure: sifakis
works: [property-preserving-abstractions-1995]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# Define the best possible version of the thing you are approximating, even when you intend to ship something worse

**Lesson:** Once you fix how concrete detail maps onto coarse detail, there are still many coarse models compatible with that mapping — all of them sound, differing only in how much they throw away. Rather than treat the choice among them as taste, the paper constructs the single most precise one and characterizes it: it is the model whose transition relation is exactly the concrete relation viewed through the mapping and back, and under stated conditions on the mapping it is provably the least such model, so it satisfies every property any compatible coarse model satisfies. Alongside it, a separate and weaker criterion is defined — a floor rather than a ceiling — naming the minimum any candidate must clear to count as an abstraction at all.

Neither object is obliged to be the one you use. The optimum can be more expensive to compute than the analysis it was meant to accelerate, and the paper is explicit that any coarser model standing in the right relation may be substituted. The point of constructing the optimum is that it converts vague comparisons into arithmetic. Without it, two engineers with two hand-built simplified models have no way to say which is stronger, or how far either sits from what the mapping could in principle have delivered, and the eventual argument is about intuitions. With it, every candidate has a distance to a fixed reference, and "we gave up this much for that much speed" becomes a statement rather than a feeling.

The habit is to define the ideal even in projects where the ideal is unreachable, because the ideal is not a target but a coordinate system. A cache with a stated optimal replacement policy makes real policies comparable; a scheduler with a stated optimal ordering makes heuristics measurable; a compiler pass with a stated best-possible result makes a pragmatic pass auditable. Pairing the ceiling with an explicit floor is what makes the whole thing usable day to day: the floor is what you check on every candidate to catch outright errors, and the ceiling is what you check against occasionally to notice that your practical construction has drifted much further from the achievable than anyone realizes.

**Source:** [Property Preserving Abstractions for the Verification of Concurrent Systems](../works/property-preserving-abstractions-1995.md) — section 4's observation that many abstract programs correspond to a given abstraction relation and that one wants the one satisfying as many properties as possible, section 4.1's faithfulness criterion, and the results establishing the constructed abstract system as the least abstraction under totality and functionality conditions, together with the remark permitting substitution of any coarser system standing in the required relation.
