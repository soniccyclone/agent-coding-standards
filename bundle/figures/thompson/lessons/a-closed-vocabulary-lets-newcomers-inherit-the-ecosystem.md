---
type: lesson
title: "A closed interface vocabulary is what lets every newcomer inherit the ecosystem"
figure: thompson
works: [plan-9-from-bell-labs]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# A closed interface vocabulary is what lets every newcomer inherit the ecosystem

The instinct when designing an interface that many unlike things must implement is to make the operation set extensible, so that each implementor can express whatever it uniquely needs. Plan 9 argues the opposite instinct is the productive one: fix the operation set, refuse to grow it, and force every new kind of resource to say what it has to say inside that fixed alphabet. The payoff is not economy for its own sake. It is that a closed vocabulary can accumulate machinery around it — access control, naming, remote transport, browsing tools, permissions inheritance, an audience that already knows the rules — and every latecomer that speaks the vocabulary receives all of that machinery at no cost. An extensible interface cannot accumulate anything, because nothing generic can be built over a set of operations that is still growing.

This is the concrete difference the authors draw against object-oriented framing, and it is worth taking seriously as an engineering claim rather than a taste. Both approaches let you present dissimilar resources through a common shape. Only one of them settles the questions that surround the resource rather than the operations on it: who may touch this, what is it called, how do I reach it from another machine, what happens when I hand its name to a program written before it existed. Under a per-class extensible interface each new class re-litigates all of those; under a fixed one they are already answered, because they were answered for the vocabulary and not for any member of it. The generality you give up in the operation set is repaid many times over in generality of everything built around it.

The cost is real and worth stating plainly, since the authors do. Occasionally a resource genuinely wants a shape the fixed vocabulary does not fit, and the encoding gets awkward — a request-and-reply pattern squeezed into a write followed by a read, doubling the operations and forcing the server to hold state between them. The judgment the paper models is to accept that local awkwardness because it is rare and never fatal, and because the alternative buys smoothness in a few places by destroying uniformity everywhere.

A programmer who believes this stops treating "we can extend the protocol later" as a virtue and starts treating it as the thing that will prevent the protocol from ever being worth conforming to. When designing the interface many components will implement, they will spend their effort on getting a small operation set to cover the space, and will hold that set closed even under pressure from an awkward case — because the closure, not the coverage, is what makes conformance pay.

**Source:** [Plan 9 from Bell Labs](../works/plan-9-from-bell-labs.md) — the design section's argument for representing every resource as a file, and the discussion section's explicit contrast between a fixed-method protocol and object models where protection, naming, and networking must be settled anew per class.
