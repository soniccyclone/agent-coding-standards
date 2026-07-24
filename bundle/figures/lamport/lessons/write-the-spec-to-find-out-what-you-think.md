---
type: lesson
title: "Write the specification to expose your own sloppy thinking; choosing the abstraction is the design act"
figure: lamport
works: [specifying-systems]
axes: [cognitive-load, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---

# Write the specification to expose your own sloppy thinking; choosing the abstraction is the design act

**Lesson:** The primary product of writing a formal specification is not the document, it is the discovery of what you had not actually thought through. Prose tolerates vagueness; a formal notation refuses it, and each refusal is a design question you were going to answer accidentally in code. This is why specifying is worth doing before building even when no tool will ever check the result: understanding a system before constructing it is the point, and precise writing is the only reliable instrument for finding out whether you understand it. Informal mathematics is not precise enough for this job either — it is precise in the small and sloppy in the large, holding together with prose exactly where system descriptions need rigor.

The hard part is not the notation, which can be taught, but the abstraction, which can only be practiced: choosing what the specification's state consists of and how coarse its steps are. Every detail omitted simplifies the description and simultaneously admits a potential error, because implementers cannot learn from the spec what the spec chose not to say — a timing constraint abstracted away is a constraint someone will violate. So the choices of variables and step granularity are conscious, defensible engineering decisions, and a useful trick for making them honestly is to write out a few concrete sample behaviors first and see what distinctions they force. When several formulations express the same thing, verify they are equivalent and then pick for readability; when they differ, the difference is a real decision you have just been saved from making blindly.

A programmer shaped by this treats the sentence "I'll work it out in the code" as an alarm, budgets design time for writing the behavior down precisely, and evaluates a specification not by completeness but by whether it says exactly the things the system's users and implementers must agree on, at the coarsest granularity that still says them.

**Source:** [Specifying Systems](../works/specifying-systems.md) — the introduction's argument that specifying a system helps you understand it and that writing exposes sloppy thinking, and the asynchronous-interface chapter's discussion of abstraction as the hardest, unteachable part: the deliberate choice to let signals change in one step, the warning that every omitted detail is a potential error source, and the advice to begin from sample behaviors.
