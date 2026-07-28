---
type: lesson
title: "Choose primitives for fidelity to whoever executes them, then earn expressiveness by reduction"
figure: post
works: [finite-combinatory-processes-formulation-1]
axes: [primitive-count, cognitive-load, expressiveness, hardware-affinity]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Choose primitives for fidelity to whoever executes them, then earn expressiveness by reduction

The usual instinct when designing a minimal core is to minimize for mathematical tidiness: find the fewest constructs from which everything else can be built, and take elegance as the selection criterion. Post picks his handful of acts on a different basis entirely. Each one corresponds to something a person sitting in front of a row of boxes could unmistakably do — put a mark here, take the mark away, step one box over, look at whether this box has a mark — and the control structure is a numbered list of orders with a branch on the one observation available. He says outright that the goal is not merely a system of adequate power but one with fidelity to the situation of the worker. The base is small because the executing agent's real repertoire is small, not because smallness is beautiful.

This matters because the two criteria diverge, and diverge in a direction that damages the argument you actually want to make. A core chosen for elegance leaves you unable to say why the claim "nothing exceeds this" should be believed — the boundary of the core is a mathematical accident, so there is no reason the world should respect it. A core chosen for fidelity to the executor makes that boundary an argument in itself: exceeding it would require the worker to do something the worker cannot do. Expressiveness then arrives not by admitting more primitives up front but by adding richer notations later and demonstrating each reduces to the base — Post anticipates exactly this, expecting wider formulations and taking the burden of showing they all collapse downward. Convenience is a derived layer, and the base pays for its own credibility.

The practical consequence is a discipline about where flexibility lives. When you define an instruction set, an intermediate representation, a bytecode, or the operation vocabulary of a distributed log, the question to ask first is what the thing at the bottom can genuinely perform and observe in one step — the hardware, the storage device, the network endpoint. Fit the primitives to that, then build every convenience above it as a translation that provably bottoms out. The alternative is the core that grew a primitive because some higher construct was awkward to express, which is how the bottom of a system quietly stops corresponding to anything real and how nobody can any longer say what the machine actually does.

Post also notes, unprompted, that programming in this vocabulary is awkward, and that a definitive version might trade some of its bareness for workability — extra mark types, a couple of movable pointers. That is the honest version of the trade: the minimal base is right for the argument, and the argument is allowed to cost the user something as long as you say so rather than sneaking the ergonomics into the foundation.

**Source:** [Finite Combinatory Processes — Formulation 1](../works/finite-combinatory-processes-formulation-1.md) — the enumeration of primitive acts and direction forms, together with the later remark that psychological fidelity rather than power alone is the aim and that wider formulations should be shown reducible to this one.
