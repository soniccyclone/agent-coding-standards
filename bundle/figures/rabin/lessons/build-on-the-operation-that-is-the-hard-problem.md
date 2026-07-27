---
type: lesson
title: "Build on the operation that already is the hard problem, and pay for it in interface tidiness"
figure: rabin
works: [digitalized-signatures-and-public-key-functions-as-intractable-as-factorization]
axes: [verifiability, primitive-count, hardware-affinity]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Build on the operation that already is the hard problem, and pay for it in interface tidiness

**Lesson:** A guarantee you cannot derive is not a guarantee. This work's target is a scheme whose predecessor rested on a one-directional relationship: breaking it was known to be no harder than a well-studied problem, with nothing ruling out that it was much easier. That gap is not a theoretical blemish. It means the whole edifice depends on nobody finding a shortcut, and no amount of unsuccessful attack accumulates into evidence that no shortcut exists. The fix is to stop hoping the relationship goes both ways and instead pick the underlying operation so that it must: choose an operation whose inversion is *itself* known to be interchangeable with the hard problem, so that any method of undoing it can be turned, in a handful of extra steps, into a method of solving the hard problem outright.

The design discipline that produces this is unfamiliar because it runs backward from the usual one. Instead of designing the construct you want and then arguing about its safety, you start from the property you must be able to prove, identify what would have to be true for the proof to close, and let that dictate the construct — even when the resulting construct is uglier. The concrete ugliness paid here is that the chosen operation is not one-to-one: each output has several valid preimages, which forces small awkwardnesses everywhere it is used, and not every intended input is even usable, so the sender retries until one is. Those are real costs, accepted deliberately, because the tidier alternative was tidy in a dimension that bought nothing and untidy in the one dimension that mattered.

There is a second payoff worth noticing, because it contradicts the reflex that guarantees cost performance. The operation selected is about as small as arithmetic gets — a single addition, a single multiplication, one reduction — and it evaluates orders of magnitude faster than the thing it replaces. Minimality served both ends at once: the fewer moving parts the construct has, the shorter both the execution path and the proof about it. When a rigorous argument and a fast implementation seem to be in tension, that is often a signal the construct is carrying parts that neither the argument nor the machine needs.

A programmer who takes this seriously changes what they ask during design review. Not "can anyone think of a way this fails" but "what would breaking this let the breaker do, and is that something we already believe is out of reach?" If the answer is nothing recognizable, you have no argument at all, only an absence of counterexamples, and the honest move is to redesign until the answer becomes something concrete.

**Source:** [Digitalized Signatures and Public-Key Functions as Intractable as Factorization](../works/digitalized-signatures-and-public-key-functions-as-intractable-as-factorization.md) — the introduction's contrast between a one-directional and a two-directional hardness relationship, the choice of a deliberately non-injective quadratic operation that makes the second direction provable, and the section converting an inversion procedure into a factoring procedure.
