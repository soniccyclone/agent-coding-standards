---
type: lesson
title: "Prefer the algorithm that behaves well on the instances you get, not the one with the better bound"
figure: sifakis
works: [turing-lecture-2009]
axes: [verifiability, hardware-affinity]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Prefer the algorithm that behaves well on the instances you get, not the one with the better bound

**Lesson:** A worst-case bound describes an adversary's best move, not the distribution of problems you will actually be handed. Real instances arrive with structure — repeated subcomponents, locality, sparse dependence between parts, symmetry inherited from the way engineers build things — and an algorithm that exploits that structure can dominate in practice while looking worse on paper. The canonical demonstration is that the archetypal intractable decision problem became the load-bearing engine of industrial verification, because solvers got very good at the shapes of instances that circuits and protocols produce. Nobody repealed the complexity result; it simply stopped being the relevant prediction.

Two disciplines follow. First, when comparing candidate algorithms, weight repeated observed behavior on representative inputs above asymptotic class, and treat a proven bound as a statement about which failures are possible rather than which are likely. Second, when your method saturates, look for the structural regularity in your instances that you are not yet exploiting: independence between concurrent actions means whole interleavings need never be examined; replication of similar parts means a symmetry quotient can shrink the problem exponentially; a family parameterized by size may collapse to a single fixed instance. Each of these is a bet on a property of real systems, not a general theorem, and each pays only where that property holds.

The corollary is to keep the bet visible. A technique that depends on a structural assumption should announce it, because when the assumption fails the degradation is usually not graceful. Choosing to exploit regularity is choosing a class of inputs to be fast on and accepting that everything else is off the happy path.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Emerson's efficiency section on preferring observed over theoretical complexity and on strategies for large state spaces, together with Clarke's accounts of SAT-based bounded checking, partial order reduction, and symmetry reduction.
