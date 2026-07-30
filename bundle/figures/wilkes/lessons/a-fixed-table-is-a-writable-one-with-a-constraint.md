---
type: lesson
title: "Ask what your fixed part is a special case of, then price the version where it varies"
figure: wilkes
works: [best-way-to-design-an-automatic-calculating-machine]
axes: [expressiveness, primitive-count, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# Ask what your fixed part is a special case of, then price the version where it varies

**Lesson:** Once a design has been reorganized so that behaviour lives in data rather than in structure, a question becomes available that was previously unaskable: what happens if that data is allowed to change? A table of fixed information is a degenerate case of a writable store, and the difference between the two is a single constraint. Relaxing it does not produce a marginally more flexible version of the same machine — it produces a machine of a different kind, in this instance one whose users define the vocabulary they program in and may redefine it while running. The insight is not the flexibility itself; it is that the reorganization made the question visible, which is a general property of moving behaviour out of structure and into data.

The right response to seeing such a possibility is neither to build it because it is fascinating nor to ignore it because it is expensive. It is to state what it would be, estimate what it would cost with the means actually to hand, and record the judgment. A possibility identified and priced out is a permanent contribution: it tells later readers exactly which constraint is load-bearing and what the payoff for lifting it would be, so that when the cost of lifting it falls the decision can be revisited on the evidence rather than rediscovered from nothing. Costs move; the structural analysis does not.

So the habit worth keeping is to look for the constraint that distinguishes your design from its more general relative, name it, and say why it is there. The most consequential ideas in a design are often not the ones implemented but the ones correctly identified as one economic step away — and identifying them is only possible after the design has been arranged so that the varying part and the fixed part are different things.

**Source:** [The Best Way to Design an Automatic Calculating Machine](../works/best-way-to-design-an-automatic-calculating-machine.md) — the final paragraph, which observes that the matrices holding the elementary-step sequences amount to a very fast store of fixed information, describes the machine with no fixed instruction set that an erasable store would yield, and judges the equipment cost unjustifiable at the time.
