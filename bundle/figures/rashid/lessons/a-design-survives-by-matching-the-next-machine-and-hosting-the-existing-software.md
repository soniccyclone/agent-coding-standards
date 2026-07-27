---
type: lesson
title: "Whether a design survives is decided outside its own quality: does it match the next machine, and can it host the software that already exists"
figure: rashid
works: [from-rig-to-accent-to-mach]
axes: [hardware-affinity, primitive-count, expressiveness]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Whether a design survives is decided outside its own quality: does it match the next machine, and can it host the software that already exists

**Lesson:** Designs do not usually die of being wrong. They die because the hardware they were shaped around stops being manufactured, or because the body of software people actually want to run grows faster than the design can absorb it. Both causes are external to the qualities engineers argue about, and both are visible years in advance if you look for them. Taking this seriously changes what you consider part of the design: the question is not only whether the abstractions are clean but whether they will still be the right shape for machines nobody has built yet, and whether the code the world already depends on can be made to run on them without the design having to pretend to be something else.

For the hardware half, the useful test is correspondence. An abstraction basis is durable when its primitives line up one for one with the physical structures the machines are actually made of — a bundle of memory, some number of processors attached to it, a channel to elsewhere, units of data moving over that channel, and storage behind it all. A basis with that property survives a hardware generation change because the change rearranges the quantities rather than introducing a structure the primitives cannot name. A basis that fused two of those structures into one abstraction, or that assumed one of each, must be renegotiated whenever the machines stop matching the assumption. This is not a claim that abstractions should be low-level; it is a claim that the *count and kind* of primitives should mirror the count and kind of physical things, because that is what makes the mapping stay total as the hardware moves.

For the software half, the lesson is less comfortable and more often ignored: a design whose merits are real can still be killed by an accumulating pile of software written against a different interface, and the response has to be engineering rather than argument. Being able to run that software unchanged — not approximately, not through a compatibility veneer that is always behind — is a survival property, and it is worth building the design so that the incumbent interface can be provided as one of several things the system hosts rather than as the thing the system is. That framing is what makes compatibility affordable instead of corrupting: the incumbent's semantics live in replaceable components above a core that has no opinion about them, so supporting it costs the design nothing conceptually while buying it the population it needs to survive.

A programmer who believes this asks two questions of every foundational design: what does each primitive correspond to in the physical machine, and what existing body of software must be able to run here unmodified. Neither question is about elegance, and both decide whether the elegance ever gets used.

**Source:** [From RIG to Accent to Mach: The Evolution of a Network Operating System](../works/from-rig-to-accent-to-mach.md) — the narrative of the first system's demise with its hardware base, the frank assessment that the second would follow it partly for failing to absorb the surrounding software ecosystem, the choice to make the third both compatible with the incumbent system interface and suited to shared-memory multiprocessors, and the closing observation that the surviving primitives parallel the physical structures of contemporary machines.
