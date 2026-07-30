---
type: lesson
title: "If a property only exists over a population you invented, move it onto the object itself"
figure: kolmogorov
works: [three-approaches-to-the-quantitative-definition-of-information]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# If a property only exists over a population you invented, move it onto the object itself

**Lesson:** Statistical machinery is defined over ensembles. To use it on one artifact you must first place that artifact in a set of alternatives and put a distribution on the set — and very often no such set exists outside your own head. Asking how much information a particular novel contains means pretending there is a population of possible novels with known probabilities, which nobody can produce and nobody can check. The machinery still returns a number, and the number is an artifact of the fiction you invented to get it. This failure is easy to miss because the mathematics never complains; the invented ensemble is invisible in the result.

The diagnostic is to ask what the probability in your answer ranges over, and whether that range is a real thing you could enumerate or sample, or a rhetorical device introduced so the formula would type-check. Averaging over a large flow of similar, weakly related messages is legitimate — there the ensemble is the actual situation. One unique artifact is not a sample from anything. The moment you notice the population is fictional, the honest move is not to refine the distribution but to abandon that whole framing.

The constructive half is what makes this more than a critique. When the ensemble is fake, look for a definition that mentions only the object: a property intrinsic to the thing, computed from the thing, with no reference to what else might have occurred. Randomness is the model case. Instead of "produced by a random process," which is a claim about history you cannot inspect, take "not compressible" — no short description generates it — which is a claim about the object in front of you. The relocated definition is harder to evaluate but it is about something real, and it applies to exactly the single case you actually had. The same move is available whenever a metric demands a reference distribution: find the property of the individual artifact that the distribution was standing in for, and measure that instead.

**Source:** [Three Approaches to the Quantitative Definition of Information](../works/three-approaches-to-the-quantitative-definition-of-information.md) — the objection at the end of §2 that no meaningful set of "possible novels" or probability distribution over it exists, contrasted with the legitimate bulk-transmission case, and the closing remark of §4 that members of a simply-specified large set whose complexity is near maximal are the ones properly called random.
