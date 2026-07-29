---
type: lesson
title: "A new binding mechanism must be restricted until local reasoning survives it"
figure: reenskaug
works: [a-dci-execution-model]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# A new binding mechanism must be restricted until local reasoning survives it

Any mechanism that decides at runtime which code a name refers to buys expressive power by spending comprehensibility, and the exchange rate depends entirely on how tightly the mechanism is fenced. Reenskaug introduces a dispatch scheme where behavior attached to a participant's position in a collaboration takes precedence over behavior attached to its type — and then, rather than leaving the resulting freedom open, he states the restrictions the mechanism must obey and derives them explicitly from a single requirement: a reader must be able to reason about one unit of code without tracking what other units are doing. The restrictions are not admissions of an unfinished design. They are the design.

Three shapes of restriction appear, and each is recognizable far outside this setting. First, make the assignment of all participants happen as one indivisible act rather than one at a time, so that no intermediate arrangement — a half-populated collaboration whose members do not belong together — is ever observable. Second, allow only one such arrangement to be in force at any moment, so that a name's meaning has exactly one answer at the point where the reader is standing. Third, decline the concurrency case outright rather than shipping semantics you cannot yet defend. Each closes off a way for the mechanism to become ambient, global, and unanalyzable.

There is a subtler move alongside them. Because behavior is now selected by collaborative position, the usual per-type variation is deliberately suppressed for that behavior, and the freedom to vary is relocated to the choice of which set of participants gets bound. Two mechanisms competing to express the same variability is worse than one: the reader must consult both to know what runs. Picking one axis of variation per concern and forcibly closing the other is a real design act, not a limitation.

A programmer holding this stance treats every "and it can also be overridden dynamically at runtime" feature as incurring a debt payable in stated invariants. The question after inventing a flexible mechanism is not what else it can now express, but which uses of it must be forbidden so that reading a single unit still tells the truth — and whether the forbidden cases can be forbidden mechanically rather than by convention.

**Source:** [A DCI Execution Model](../works/a-dci-execution-model.md) — the "Three Constraints" section, which opens by stating the local-reasoning goal and then imposes atomic binding of all participants, a single active collaboration, and single-threaded execution; together with the accompanying note that per-type variation is intentionally suspended for collaboration-scoped behavior.
