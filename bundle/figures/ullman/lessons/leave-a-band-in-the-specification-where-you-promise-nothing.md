---
type: lesson
title: "Leave a band in the specification where you promise nothing"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [formal-methods-and-verification, algorithms-and-complexity]
tags: [lesson]
---
# Leave a band in the specification where you promise nothing

**Lesson:** A specification written as a single threshold — everything on this side must be accepted, everything on that side must be rejected — is the most expensive kind to satisfy, because all of its difficulty is concentrated at one point where two arbitrarily similar inputs must receive opposite verdicts. The cheap alternative is to state two thresholds with a gap between them, promise a high acceptance rate below the first and a low one above the second, and say explicitly that nothing whatsoever is guaranteed in between. Almost all of the engineering cost lives in that gap, and a specification that declines to enter it is a specification that can be met by crude machinery.

The parameters of such a statement are worth reading as a market. You may narrow the gap as far as you like, but the two probabilities then converge and the guarantee weakens toward saying nothing. You may drive the probabilities apart as far as you like while holding the gap fixed, but you pay in evaluations, since separating them is done by composing many copies of the primitive. Four numbers, two of which you fix by what the application needs and two of which you buy. This is a far more useful conversation than arguing about whether a method is accurate enough, because it names what is being exchanged and lets each side of the exchange be priced independently.

What makes the gap principled rather than evasive is that it usually corresponds to something real. Inputs that fall in the ambiguous band are the ones where the underlying question genuinely has no crisp answer, where the measurement error of the data is comparable to the distinction being drawn, or where a human asked to adjudicate would also hesitate. A specification that demanded a definite verdict there would be demanding that the system invent one. Writing the band down converts an unstated assumption into a contract term that downstream consumers can see and plan for.

The habit generalises to anywhere a system is asked to classify against a boundary: alerting thresholds, admission control, fraud scoring, retry policies, cache eviction. Write the requirement as two levels with an explicitly unspecified middle, and hold the width of that middle as a negotiable quantity rather than letting it default to zero. Hysteresis in a controller, guard bands in signal processing, and staged rollouts that treat a middle cohort as undefined are all the same device. The cost of insisting on a single sharp boundary is rarely visible in the requirements document, and it is always paid later.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's definition of a locality-sensitive family in terms of two distances and two probabilities, which explicitly says nothing about pairs whose distance falls strictly between the two, notes that the two distances can be brought as close together as one wishes at the price of the probabilities converging too, and then shows the probabilities being driven apart by composition while the distances stay fixed.
