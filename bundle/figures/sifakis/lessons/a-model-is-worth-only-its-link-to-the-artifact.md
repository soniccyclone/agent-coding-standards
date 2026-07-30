---
type: lesson
title: "Everything you prove is about the model; the whole guarantee rests on how the model was derived"
figure: sifakis
works: [turing-lecture-2009]
axes: [verifiability, hardware-affinity]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Everything you prove is about the model; the whole guarantee rests on how the model was derived

**Lesson:** Analysis operates on a description, never on the running thing. So a result about the description transfers to the artifact only if the two are connected by a relation that preserves meaning and that someone can actually check. If the model was drawn by hand from a reading of the source, that relation is an unverified human claim sitting underneath every theorem you subsequently prove, and it is where errors concentrate — not in the checking algorithm, which is the part that gets audited. The way to remove the weak link is to generate the model mechanically from the system description rather than to write it, so the transfer argument is made once, about the generator, instead of once per project by whoever was drawing boxes that week.

This explains an uneven adoption pattern that is otherwise mysterious. Hardware verification took off quickly because a faithful finite-state model falls out of a register-transfer description almost by transcription: the source notation already has an exact, agreed meaning. Software resisted, because before extracting anything you must fix a formal semantics for the implementation language, and for the languages people actually ship in, that means resolving ambiguities and stating assumptions the language definition left open. The missing prerequisite for automatic analysis of a system is usually a precise semantics for the notation the system is written in, not a cleverer analysis.

Hardest is the case where one artifact spans layers with different notions of execution — application code on a platform, timing and memory and energy entering the picture. Composing a software model with a platform model requires formalizing their interaction, and where the industry substituted diagrams or simulation-only extensions for a semantics, no rigorous basis followed. If you cannot say precisely what a description means, its main use is animation; do not mistake the ability to run a description for the ability to reason about it.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Sifakis's section on building executable models: faithfulness as a checkable semantics-preserving relation, automatic model generation, the hardware/software asymmetry, and the difficulty of composing models across mixed hardware/software systems.
