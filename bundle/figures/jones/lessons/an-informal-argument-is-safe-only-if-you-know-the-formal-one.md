---
type: lesson
title: "An informal argument is safe only if you know how the formal one would go"
figure: jones
works: [systematic-software-development-using-vdm]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# An informal argument is safe only if you know how the formal one would go

**Lesson:** Almost all serious reasoning about programs is informal, and it should be — the fully mechanical version of even a trivial algebraic rearrangement runs to a page, and nobody has the patience or the need. But there is a sharp line between an informal argument that is a compressed formal one and an informal argument that is a hope. The test is whether, at every step you skipped, you could say which precise steps would fill the gap if someone doubted you. If you could, the compression is a service to the reader. If you could not, you have not made an argument shorter; you have made a different and much weaker kind of claim while keeping the vocabulary of the stronger one.

This gives a practical calibration rule for how much rigour to apply, and it is a local rule rather than a policy. Work at the level of detail the problem needs, and go finer exactly where doubt appears. What licenses the coarse level is that the fine level is available on demand — which in turn means you have to have done the fine-grained work often enough to know what it looks like. That is the real reason to grind through elementary derivations at excruciating detail at some point: not because anyone will need those particular results written out, but because it is the only way to acquire the ability to judge whether a large step is legitimate. Someone who has never constructed a complete argument cannot tell a safe abbreviation from an unsafe one, and will make both with equal confidence.

The same relationship holds one level up, between a model and the tools for reasoning about it. Confidence in an informal argument ultimately rests on the existence of a mechanically checkable version — something a program could verify — even when no program is ever run. That backstop is what distinguishes a discipline from a habit of speaking carefully. And it explains why studying the derivations pays a second dividend: working through why a rule holds deepens and fixes your understanding of the thing the rule is about, in a way that reading the rule's statement never does.

**Source:** [Systematic Software Development Using VDM](../works/systematic-software-development-using-vdm.md) — the concept-of-proof section, which states that most proof obligations can be discharged by rigorous arguments but that such arguments are only safe if undertaken with a knowledge of how a formal proof could be constructed, and that studying the inference rules deepens understanding of the operators; the observation there that certainty comes from the game being mechanizable so that a checking program could always be run; the aim of informal proof described as indicating how a proof could be constructed, with major steps given in the knowledge that details could be supplied if doubted; and the correctness-proofs section's remark that the level of detail can be chosen to suit the problem, with the key point about rigorous outlines being that it is clear what would be needed to extend them.
