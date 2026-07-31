---
type: lesson
title: "Forbid retraction if you want per-item cost to mean anything"
figure: stearns
works: [on-the-computational-complexity-of-algorithms]
axes: [verifiability, expressiveness]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Forbid retraction if you want per-item cost to mean anything

**Lesson:** A cost measured per item produced is well defined only if produced items cannot be taken back. Build the output channel so that it moves one way, so that what has left the machine is irrevocable and cut off from every later calculation, and the phrase "work required to produce the nth item" acquires a definite referent. Permit revision and it does not: a process could emit a guess immediately, revise it a thousand steps later, and any per-item timing you quoted would be a statement about when guessing happened rather than when answering did. The irrevocability is not a restriction on what can be computed, it is the constraint that makes the measurement exist at all.

The same shift changes what is being asked of the process. The older framing hands a machine a request and waits for an answer, which measures cost per complete job. The framing that supports incremental cost requires the process to emit its results in order, indefinitely, so that cost is a function over prefixes rather than a single number. That is a strictly stronger demand and a much more informative measure — it distinguishes a process that produces early results promptly from one that produces everything at the end, a distinction the whole-job measure cannot see. If you want that distinction, you have to pay for it by committing outputs.

The engineering form of this is the design rule behind every streaming interface worth trusting. An interface that permits amendment of already-delivered results cannot carry a per-item latency guarantee, no matter what its documentation claims, because there is no observable event that constitutes delivering item n. Conversely, an interface that commits — an append-only log, a one-way pipe, a published offset — makes per-item latency measurable, and thereby makes it enforceable and optimisable. The cost of that commitment is real: no revision means every item must be right when it is emitted, which forbids exactly the speculative strategies that would have improved apparent latency. Recognising that trade explicitly is the point. Either commit and get a meaningful measure, or permit revision and stop quoting per-item numbers.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the description of the machine model in the time-limited-computations section, where the output band is restricted to one-way motion so that what has been printed and moved past the head is irrevocable and divorced from further calculation, together with the contrast drawn immediately afterwards between Turing's single-answer formulation and the requirement here that successive terms be printed in order.
