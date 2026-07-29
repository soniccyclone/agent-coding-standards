---
type: lesson
title: "Redundancy is only available to components whose behavior depends on nothing but their input history"
figure: schneider
works: [implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial]
axes: [verifiability, expressiveness]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Redundancy is only available to components whose behavior depends on nothing but their input history

The entire mechanism of replication rests on a property that is easy to state and easy to violate by accident: a component's observable behavior must be a function of the sequence of inputs it has consumed, and of nothing else — not elapsed time, not the speed it happens to be running at, not any concurrent activity anywhere in the system. If that property holds, two copies fed the same inputs in the same order are indistinguishable, and disagreement between them becomes hard evidence of a fault. If it fails even slightly, copies drift for legitimate reasons, disagreement stops meaning anything, and no amount of voting machinery recovers the guarantee.

The practical consequence is a rule about where to draw component boundaries rather than a rule about how to write code. Every real service must eventually touch something nondeterministic — a sensor, a clock, an arriving connection, a random draw. The discipline is to refuse to let that touching happen inside the component you intend to replicate. Move the reading of the world outside the boundary, and let its results enter the replicated core only as ordinary inputs in the input stream. A loop that samples a sensor and reacts is unreplicable; the same logic becomes replicable the moment the sampling loop is lifted out and each sample arrives as an explicit request. Nothing about the computation changed — only which side of the line the nondeterminism sits on.

This inverts the usual instinct about encapsulation. The tempting design hides the sensor read inside the component that needs the value, because that keeps the interface small and the dependency local. But hiding a nondeterministic input is hiding exactly the thing that determines whether the component can ever be made fault tolerant, and the cost of that concealment does not appear until you try to run a second copy. Nondeterminism is the one implementation detail worth promoting into the interface.

A programmer who has internalized this asks, of any component meant to be fault tolerant, replicated, replayed, or tested deterministically: what does this read that is not in its inputs? The answers are the same short list every time — wall-clock time, ambient state, arrival order, local randomness — and each one either gets pushed out through the interface as data or forfeits the component's claim to redundancy. The payoff extends well past fault tolerance: the same discipline is what makes a component replayable from a log, testable without mocks, and reasonable to argue about at all.

**Source:** [Implementing Fault-Tolerant Services Using the State Machine Approach: A Tutorial](../works/implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial.md) — the semantic characterization given in the opening section on state machines, and the process-control example that follows it, where a component is shown to be disqualified purely by where its sampling loop sits.
