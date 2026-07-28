---
type: lesson
title: "Change the representation underneath your algorithms, not the algorithms"
figure: mcmillan
works: [symbolic-model-checking-an-approach-to-the-state-explosion-problem]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Change the representation underneath your algorithms, not the algorithms

The striking thing about this thesis is how little of the mathematics it disturbs. The fixed-point characterisations of the temporal operators were already known; the iterate-until-stable procedure for computing extremal fixed points was already standard; the correctness criteria being checked were already formalised. What the thesis changes is one layer below all of that — how a *set of configurations* and a *relation between configurations* are stored. Everything above that layer is untouched and simply inherits the improvement.

The payoff comes from a deliberate choice of where to make the intervention. Rather than reimplementing each verification technique symbolically, the thesis identifies a single fixed-point notation expressive enough to state all of them — reachability, branching-time checking with fairness, bisimulation, the asymmetric simulation relation, language inclusion between automata, machine equivalence — and then writes one symbolic interpreter for *that*. Every technique expressible in the notation becomes symbolic as a corollary. The translation from the notation down to operations on the representation is described as merely mechanical, which is exactly the point: the interesting work was locating the chokepoint, not the many things flowing through it.

This is a general strategy and an underused one. Programmers reach instinctively for algorithmic improvements — a better traversal, a smarter heuristic — because algorithms are where we are taught to look. But when a family of procedures all bottom out in the same few primitive operations over the same few data shapes, the leverage is concentrated in those shapes, and an improvement there multiplies across the family while an algorithmic improvement helps one member. The corollary is that finding the right intermediate notation is itself the engineering work: a notation too weak covers only some of your procedures, one too strong has no efficient realisation.

Someone who has internalised this asks, before optimising anything, what the shared substrate beneath their procedures actually is, and whether a family of apparently different problems is really one problem with a common vocabulary. They invest in an intermediate representation whose cost they can attack once, and they treat "this reduces mechanically to the notation" as a finished result rather than an unimplemented one.

**Source:** [Symbolic Model Checking: An Approach to the State Explosion Problem](../works/symbolic-model-checking-an-approach-to-the-state-explosion-problem.md) — the progression from the fixed-point characterisation of the temporal logic, to encoding sets and relations as quantified Boolean formulas, to the chapter section that recasts every correctness notion in the fixed-point calculus and gives it a single symbolic interpreter.
