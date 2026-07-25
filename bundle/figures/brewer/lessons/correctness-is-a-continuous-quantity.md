---
type: lesson
title: "Widen correctness from a bit to a dial, then engineer the dial"
figure: brewer
works: [harvest-yield-and-scalable-tolerant-systems, towards-robust-distributed-systems]
axes: [expressiveness, parallelizability]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Widen correctness from a bit to a dial, then engineer the dial

**Lesson:** A system whose specification admits only "right answer" or "no answer" has thrown away its cheapest tool for surviving faults. Brewer's move is to split the single bit of correctness into two continuous quantities: how often the system answers at all, and how complete an answer it gives. Once those are separate dials, a component failure no longer has to translate into refusal; it can translate into a slightly thinner answer delivered on time. The trade only exists if the designer widens the definition of acceptable behavior up front, so the real work is in the specification, not the failure handler.

The companion habit is probabilistic honesty. Every large system is already probabilistic, because multiple simultaneous faults always have nonzero probability and the substrate underneath is best-effort; pretending otherwise just means the degradation curve is accidental instead of designed. A designer who accepts this asks what the shape of degradation should be (linear in the number of failed nodes, say), then arranges the mechanism (random placement, selective replication of the valuable fraction of the data) so the average case and the worst case coincide. Deliberately introduced randomness, usually a source of anxiety, here becomes the tool that makes failure behavior predictable.

Note what naming does in this lesson: before there is a vocabulary for partial results, degraded answers look like bugs and get argued about case by case. Giving the two dials names makes graceful degradation something a team can specify, measure, and defend in review. A programmer who believes this builds the reduced-answer path as a first-class output of the system, decides consciously which subset of data deserves the strongest protection, and treats "fails by giving a slightly worse answer" as an achievable design target rather than an excuse.

**Source:** [Harvest, Yield, and Scalable Tolerant Systems](../works/harvest-yield-and-scalable-tolerant-systems.md) — the sections defining the two availability metrics and the first strategy, where broadening "correct behavior" and thinking probabilistically are argued as the preconditions for graceful degradation. [Towards Robust Distributed Systems](../works/towards-robust-distributed-systems.md) — the closing arc, where capacity and completeness are related as a conserved product under faults and "think probabilistically about everything" is the stated conclusion.
