---
type: lesson
title: "Minimality is a means, and treating it as the goal loses to whoever spends their budget on outcomes instead"
figure: cutler
works: [oral-history-of-david-cutler]
axes: [primitive-count, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Minimality is a means, and treating it as the goal loses to whoever spends their budget on outcomes instead

**Lesson:** A small, regular design is valuable because it is cheap to implement, easy to reason about, and leaves resources free for the things that actually deliver performance. Those are instrumental justifications, and they hold only as long as the resource constraint that motivated them does. When the constraint loosens — when there are far more transistors, or engineers, or verification capacity, than the minimal design needs — the party that keeps optimizing minimality is optimizing a proxy while the party that spends the surplus on prediction, caching, speculation, and out-of-order machinery collects the actual advantage. Boasting about how few parts a thing was built from becomes a claim with no consequent attached: correct as a fact about the design, irrelevant as an argument about the outcome.

This is a specific and uncomfortable warning for anyone who takes small-primitive-basis thinking seriously, and it is worth stating in full rather than softening. A minimal design is easier to get right, and it is easier to implement well with limited resources, and those are exactly the reasons it wins in the regime where resources are the binding constraint. It does not follow that it wins in a regime where the binding constraint is something else, and it certainly does not follow that a competitor who accepts a more complicated design is making an error. If your competitor has the engineering capacity to verify a design you consider unmanageable, then your simplicity advantage has been neutralized by their budget, and no amount of insisting that your design is cleaner recovers it.

There is a corollary about deciding whether to accept complexity in a mechanism you are implementing. Sometimes the complete, general version of a mechanism costs less overall than the trimmed version, because the trimmed one forces a large body of software above it to be modified while the complete one lets that software run untouched. The reflex to strip a mechanism down should therefore be checked against the total cost including everything that depends on it, not just the cost of the mechanism itself. Simplicity is a real value, but it has to be argued for against the actual constraint in play rather than assumed to be self-justifying.

**Source:** [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — his explanation of why the reduced-instruction-set machines lost their performance advantage, resting on the claim that their designers preferred to keep implementations simple while a competitor spent a much larger transistor and verification budget on making a more complicated architecture run fast. The corollary appears in his account of choosing to implement a processor's full memory-management scheme in microcode rather than the trimmed one, on the grounds that the complete version was less total work because it let an existing operating system run unmodified.
