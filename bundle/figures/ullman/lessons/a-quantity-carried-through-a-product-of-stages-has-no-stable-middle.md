---
type: lesson
title: "A quantity carried through a product of stages has no stable middle"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# A quantity carried through a product of stages has no stable middle

**Lesson:** When a quantity is propagated through a chain by multiplying it by a per-stage factor at each step, its fate over a long chain is decided entirely by whether those factors sit above or below one. Below, and the quantity decays toward nothing at a rate exponential in the chain length, so anything far back in the chain has no measurable influence on the end. Above, and it grows without bound. There is no third case: staying near its original magnitude requires the product of many factors to land near one, which is a knife edge nobody can hold by choosing the factors individually. So the question "does information from the far end of the chain reach this end" has, in a multiplicative propagation scheme, the answer "no" — and the length at which it becomes no is short.

The first thing this tells you is to be suspicious of a fix that just adjusts the factors. Making them slightly larger converts silent decay into overflow, which is at least loud, and can be contained by clamping the quantity into a fixed range at each step. That is a real improvement in diagnosability and stability, and it does not restore long-range influence — the clamped chain still forgets, it just no longer explodes. Distinguishing "I stopped the numbers blowing up" from "the far end now affects the near end" is important, because the first is easy and often mistaken for the second.

The actual fix has to change the topology of the propagation, not its coefficients. Provide a route along which the quantity is carried forward by addition rather than by repeated multiplication — a channel that passes the accumulated value through largely untouched by default, with the multiplicative machinery acting to decide what is added to it and what is removed from it, rather than acting on the whole of it every step. A path whose default is to preserve does not decay with length; the decay was never inherent in having many stages, it was inherent in every stage multiplying everything.

The shape is general. Anything that composes multiplicatively along a long path has this behaviour: confidence scores multiplied down a chain of inferences, per-hop success probabilities, per-layer discount factors, compounding penalties. The diagnostic question is always whether the default per-stage operation preserves or attenuates, and the structural remedy is always to find something that can be carried additively so that length stops being fatal.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the vanishing-and-exploding-gradients section of the recurrent-networks chapter, which unrolls the training recurrence to show each earlier step's contribution as a product of per-step matrices, notes that entries strictly below one drive that product to zero so only the last few steps matter, observes that switching the activation makes the entries large and the product explode instead, remarks that explosion is the easier problem because it can be clipped into a fixed range, and then attributes the long-range capability of the gated variant specifically to its long-term memory update.
