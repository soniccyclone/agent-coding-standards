---
type: lesson
title: "Start where the risk is, not at the top of the abstraction ladder"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Start where the risk is, not at the top of the abstraction ladder

**Lesson:** The standard advice for approaching a large design is to work from the abstract to the concrete: build the high-level picture first, then fill in detail as understanding improves. It is good advice and it is frequently the wrong order to actually follow, because it optimizes for tidiness of exposition rather than for reduction of uncertainty. The part of a system most likely to invalidate everything built on top of it is often a low-level one — a performance characteristic, a protocol detail, an interaction with hardware you do not control — and postponing it in the name of orderly progression means every abstract decision above it is provisional in a way nobody is tracking.

The alternative ordering is to attack whatever you expect to be hardest to get right, at whatever level of abstraction it happens to live, and to keep going until the hard parts stop being hard. This produces a working process that looks undisciplined from the outside: a sketch of organizational workflow, then a high-level information model, then abruptly a small concrete prototype of one interface, then a state machine for one critical process. What holds it together is not a progression through levels but a queue ordered by risk, and the resulting artifacts are deliberately islands rather than a single unfolding hierarchy.

This has a consequence for how you assemble the islands, which is where the discipline comes back in. Working risk-first guarantees you will end up with many partial descriptions at different levels rather than one refined whole, so you need a composition mechanism that can relate a detailed description to an abstract one without demanding they be built in dependency order. A programmer who takes this seriously stops asking "have I finished the design layer above this?" and starts asking "what is the most expensive thing I could still be wrong about, and what is the cheapest artifact that would tell me?"

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 3's discussion of creating solution islands, which cites the principle of minimizing risk, acknowledges the conventional abstract-to-concrete recommendation as excellent advice, and then explains why it is not always followable because high-risk problems are often low-level ones.
