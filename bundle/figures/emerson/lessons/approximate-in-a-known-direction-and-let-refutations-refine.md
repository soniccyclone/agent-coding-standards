---
type: lesson
title: "Approximate in a direction whose error you can name, then let each false alarm tell you where to sharpen"
figure: emerson
works: [model-checking-algorithmic-verification-and-debugging]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Approximate in a direction whose error you can name, then let each false alarm tell you where to sharpen

**Lesson:** Any tractable analysis of a real system is an approximation, and the useful question is not how accurate it is but which way it is allowed to be wrong. Collapse a system's states by forgetting some distinctions and you get a smaller system that can do everything the original could do and possibly more. That containment has a precise consequence: a property asserting that all behaviors are acceptable, if it survives on the coarse system, must hold on the real one, because the real one's behaviors are a subset. The implication runs one way only. A failure on the coarse system proves nothing, since the offending behavior may be an artifact of what you chose to forget. Knowing the direction of the error converts an approximation from a heuristic into a sound instrument: positive results transfer, negative results are merely inconclusive.

That asymmetry is what makes the second half work. When the coarse analysis reports a violation, examine the reported behavior against the real system. If it is genuine, you have found a real defect and you are finished. If it cannot be reproduced, the report was an artifact, and the artifact is diagnostic: it identifies the distinction you erased that mattered. Restore that distinction, producing a slightly less coarse system, and repeat. The loop consumes its own false alarms as the signal that guides where to spend precision, so the analysis is only as detailed as the property under examination forces it to be, and each iteration is driven by evidence rather than by guesswork about which details matter.

This is a general pattern for building anything that must reason about a system too large to reason about exactly, and it applies well beyond verification. Static analyses, type systems, cache and index summaries, sampled telemetry, simplified models used for capacity planning: each is an approximation, and the design question is always the same. Which way can it lie, is that direction the safe one for the decisions I will make from it, and when it raises a false alarm do I have a mechanism that turns the alarm into a targeted improvement instead of into noise the team learns to ignore? An approximation with an unknown error direction is not conservative, it is just wrong at unpredictable times.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/model-checking-algorithmic-verification-and-debugging.md) — Clarke's section on abstraction refinement: the definition of an abstraction mapping and the simulation conditions it must satisfy, the property-preservation theorem covering universally quantified properties in one direction only, the counterexample that holds concretely but fails abstractly, and the refinement loop driven by spurious counterexamples.
