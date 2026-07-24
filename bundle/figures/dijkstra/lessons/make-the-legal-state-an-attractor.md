---
type: lesson
title: "Design distributed rules so the legitimate states are an attractor, not a fortress"
figure: dijkstra
works: [self-stabilizing-systems-in-spite-of-distributed-control]
axes: [parallelizability, verifiability]
subdomains: [distributed-systems-and-concurrency]
tags: [lesson]
---
# Design distributed rules so the legitimate states are an attractor, not a fortress

**Lesson:** The default posture of correctness engineering is defensive: characterize the legal states, then guard every transition so the system never leaves them. In a system with distributed control that posture has a blind spot, because a fault, a bad initialization, or a lost message can deposit the system in an illegal state by a path no transition guard ever sees, and a design that only preserves legality will then preserve illegality just as faithfully, forever. The stronger property to demand is convergence: from any state whatsoever, the ordinary local rules, with no global reset and no privileged observer, drive the system into the legal region within bounded steps and keep it there. Error recovery stops being a separate subsystem and becomes a corollary of normal operation; initialization stops being special because startup from garbage is just another arbitrary state.

What makes this genuinely hard, and genuinely a thinking lesson, is that each participant moves on local information while the target property is global, and an adversary chooses which enabled participant moves next. It was an open question whether nontrivial systems with this property could exist at all; they can, but the constructions carry a structural moral: perfect symmetry is fatal. A ring of identical machines can mirror each other's confusion indefinitely, so at least one node must run a different rule to break the symmetry and anchor convergence.

A designer who adopts this stance asks different questions of any distributed protocol: not "which transitions must I forbid?" but "if the state were arbitrary right now, what pulls it home, and what bounds the time?" And when the honest answer is "operator intervention," the design has quietly reintroduced the central control it claimed to do without.

**Source:** [Self-Stabilizing Systems in Spite of Distributed Control](../works/self-stabilizing-systems-in-spite-of-distributed-control.md) — the definition of self-stabilization against the daemon's adversarial scheduling, the framing of convergence-from-anywhere as the property missing from prior distributed designs, and the ring constructions whose crucial discovery was that the machines could not all be identical.
