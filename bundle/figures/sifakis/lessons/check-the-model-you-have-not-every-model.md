---
type: lesson
title: "Ask whether this one structure satisfies the formula, not whether some structure does"
figure: sifakis
works: [turing-lecture-2009]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# Ask whether this one structure satisfies the formula, not whether some structure does

**Lesson:** Logic had spent decades treating satisfiability as the interesting question: given a formula, does any interpretation at all make it true? That question is general, hard, and — for someone holding a specific design in their hands — beside the point. The question that actually gets asked in engineering is whether the artifact in front of you has the property you want. Evaluating truth under one fixed interpretation was always implicit in the standard definition of truth, but nobody had treated it as a computational problem worth attacking, because it looked like a degenerate special case rather than a theorem. Making that narrow question the primary one is what turned verification from a manual craft into a search you could run on a machine.

The general move is to notice when you are solving a harder problem than your situation requires. A universally quantified question — over all inputs, all schedules, all configurations — is often intractable while the instantiated version is merely large. Large is a resource problem you can throw representations and hardware at; undecidable is not. Deliberately weakening the question until it is decidable, then paying for scale, is a different trade than the one most formal work reaches for by reflex, which is to keep the question strong and pay in human ingenuity for each individual answer.

Expect this to read as a category error at first. The narrowed question is neither satisfiability nor validity, and to people whose whole vocabulary is built from those two it registers as confusion rather than as a new problem. Disorientation from the specialists is weak evidence against an idea; it is often just the sound of a question being asked outside the frame that produced the field's existing results.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Emerson's account of the technical formulation of the model checking problem, and his section on the field's early reception, where the method was dismissed precisely because it was neither satisfiability nor validity.
