---
type: lesson
title: "A component that consumes the same interface it provides can be interposed anywhere"
figure: thompson
works: [the-use-of-name-spaces-in-plan-9]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# A component that consumes the same interface it provides can be interposed anywhere

**Lesson:** Almost all layered systems are built asymmetrically. A server speaks one language downward to its resources and a different, richer language upward to its clients, so the layer cannot be stacked on itself, cannot be placed between two existing layers, and cannot be moved to another machine without a translation shim written specially for the occasion. Insisting on symmetry instead — that a component's output interface be the very same interface it requires as input — turns interposition from an engineering project into a matter of rebinding a name. Anything that speaks the protocol can sit between any two things that speak the protocol, and neither of them needs to be told.

The payoff shows up as a class of capabilities that were never separately designed. A window system whose clients get a conventional console and display can host itself in one of its own windows, because what it hands out is exactly what it asked for. A cache becomes a component that answers requests by making requests, requiring no cache-awareness in either the client or the server. A measurement tool becomes a component that forwards everything and counts as it goes, so you can profile what a program demands of the outside world without instrumenting the program. Remoting becomes a component that forwards over a wire, which is why a program that never contemplated networks can reach a device attached to a machine down the hall. None of these are features of the system; they are consequences of the shape of the interface, and each would have required its own mechanism in an asymmetric design.

The discipline this demands is that the interface be narrow and total. It must be small enough that a middlebox can implement all of it without heroics, and complete enough that a client never needs a side channel to get real work done — because the moment there is an escape hatch the interposed component does not implement, transparency is gone and every intermediary becomes a special case again. So the working question when designing a layer is not merely "is this interface clean" but "could I insert an extra copy of this layer into the middle of a running system, and would anything notice?" If the answer is no, the boundary is asymmetric somewhere, and the asymmetry will be paid for later in one-off adapters.

**Source:** [The Use of Name Spaces in Plan 9](../works/the-use-of-name-spaces-in-plan-9.md) — visible in the paper's observation that the window system offers its clients precisely the environment it itself runs under, and in the series of examples where caching, usage measurement, remote device access and whole-machine substitution are all realized as ordinary servers of the same protocol placed into a client's view.
