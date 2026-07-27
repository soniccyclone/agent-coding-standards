---
type: lesson
title: "Several unrelated-looking defects usually share one representational cause, and names that encode structure are a frequent culprit"
figure: rashid
works: [from-rig-to-accent-to-mach]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Several unrelated-looking defects usually share one representational cause, and names that encode structure are a frequent culprit

**Lesson:** A system in trouble presents its problems as a list, and the list looks like a work queue: this part cannot protect itself from misbehaving clients, that part cannot tell anyone when a dependency dies, another part cannot relocate a service without informing everybody, and the identifier format keeps having to grow. Treated as four items, each gets its own mechanism — a registry process that tracks who died and notifies subscribers, a convention that clients behave, a migration protocol, a wider field. Treated as evidence, they point at one decision: the thing that identifies a service is a value any party can construct and store as ordinary data. Every symptom on the list follows from that, and each of the four separate mechanisms is a workaround for the same missing property.

The general skill is refusing to accept a defect list at face value until you have tried to derive it from a single representational choice. The test is mechanical enough to apply: for each symptom, ask what would have to be true of the representation for the symptom to be impossible. If the answers converge, you have found the actual bug, and the four scheduled fixes collapse into one change that also fixes things nobody had noticed yet. If they diverge, at least you know the problems are genuinely independent. This is the difference between a system that gets patched and a system that gets corrected, and the reason the correction usually feels disproportionately powerful is that a representation is quantified over everything that uses it.

The specific instance is worth keeping because it recurs constantly outside operating systems: putting structure inside a name. An identifier composed of the pieces that locate its referent — which machine, which process, which slot — is a schema, and every fact about the world it encodes becomes a fact that cannot change without changing the schema. Expand from one machine to a network, from a network to interconnected networks, and the name must widen, which means every program that handled a name must be revisited. Worse, a name that can be assembled from its parts is a name that can be forged, which is why the protection failure and the format-churn failure are the same failure viewed from two sides. Opaque, unforgeable, locally-meaningful references have neither problem, and get dependency tracking thrown in, because a reference that only the substrate can create is a reference the substrate can enumerate.

A programmer who has internalized this stops proposing new subsystems in response to symptom lists, and instead asks what single property of the representation would make all of them unstateable. They also treat any structured identifier as a schema decision requiring the same care as a database schema, since it is exactly as hard to change later.

**Source:** [From RIG to Accent to Mach: The Evolution of a Network Operating System](../works/from-rig-to-accent-to-mach.md) — the section enumerating what went wrong with the earliest of the three systems (unrestricted senders, no way to detect dependencies, services pinned to their implementors, identifier widening as the network grew) and the observation that a single change in how references are represented resolved the whole cluster.
