---
type: lesson
title: "Verifiability is a property you design in, not an activity you perform afterwards"
figure: clarke
works: [model-checking-algorithmic-verification-and-debugging]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Verifiability is a property you design in, not an activity you perform afterwards

**Lesson:** The comparison drawn at the end of the Turing lecture is uncomfortable and worth sitting with. Mature engineering disciplines grounded in physics do not lean on verification to reach correctness; they have theory that makes artifacts predictable by construction, so that applying the governing laws yields a circuit that meets its requirements. Computing leans on after-the-fact checking to a degree those disciplines would find strange. The proposal is not to abandon checking but to treat the space between full constructivity and pure post-hoc verification as territory to be occupied: find the conditions under which a property of a given class, in a system of a given architectural shape, becomes cheap to establish, and then build only systems that meet those conditions. Verifiability becomes an explicit design goal in the same way testability is, rather than something you discover you lack once the system exists.

Two supporting observations from the same argument sharpen it. The model you check must be faithful to the system in a way that is itself checkable, which means models should be generated from system descriptions rather than written by hand alongside them, or you have merely moved the correctness problem. And the reason hardware verification succeeded first is not superior tooling but that hardware descriptions have precise semantics from which exact finite models fall out, while for software the language semantics have to be pinned down first, and for mixed hardware/software systems nobody yet knows how to build faithful models at all because the interaction — execution models, interaction mechanisms, granularity, timing, resources — resists composition. Where the semantics are vague, no amount of checking machinery helps.

There is also a candid admission about specifications that belongs here: soundness of requirements, meaning that some model satisfies them, is well understood and decidable, while completeness, meaning that nothing important was left unsaid, has no agreed definition and probably no attainable form. Whole classes of requirement — security, reconfigurability, quality of service — still lack rigorous formalisms. So the practitioner's confidence should scale with how much of what matters has actually been written down, not with how much of what was written down has been checked.

A programmer who takes this seriously chooses architectures for how easy they make the properties that matter to establish, derives checkable models from source rather than maintaining them in parallel, insists on precise semantics at the boundaries where components meet, and remembers that a green verification result covers only the requirements someone thought to state.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/model-checking-algorithmic-verification-and-debugging.md) — Sifakis's part of the lecture: the sections on requirements specification and on building faithful executable models, and the closing argument contrasting a posteriori verification with the constructivity of physics-based engineering disciplines, which proposes identifying conditions that make particular properties and architectures verifiable and turning those into construction rules.
