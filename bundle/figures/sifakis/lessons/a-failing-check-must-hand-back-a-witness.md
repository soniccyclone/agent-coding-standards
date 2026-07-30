---
type: lesson
title: "Make the negative answer carry evidence: an analysis that only says no is half a tool"
figure: sifakis
works: [turing-lecture-2009]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Make the negative answer carry evidence: an analysis that only says no is half a tool

**Lesson:** The first automatic checkers reported that a property failed without showing how. Adding a concrete execution trace that walks from the initial state to the violation changed what the tool was for. Practitioners started running it not to certify designs but to find defects, and many used it for nothing else. A bare verdict puts the entire diagnostic burden back on the engineer, who must reconstruct the failure from a design too large to hold in mind — which is why the design needed the tool in the first place. The witness collapses that work: it is a specific, replayable story that either exposes a real defect or exposes a flaw in what you asked for.

This reframes what a verification method is competing on. Since most programs under analysis are in fact wrong, the common case is the negative answer, and a method's practical value is dominated by how useful it is in that case rather than by the strength of its guarantee in the rare positive one. Deductive approaches carry a stronger positive result but, when the proof simply fails to go through, give you almost nothing to act on. That asymmetry, more than any complexity bound, explains their slower uptake in industry.

The design rule generalizes past verification. Any analysis that reduces a rich state to a boolean should be asked what it returns on failure. A type checker that names the term, a constraint solver that returns the conflicting core, a test framework that shrinks to a minimal failing input — each is the same discipline. Build the search so that the path it took to reach the counterexample is a first-class output, not an artifact discarded when the answer is computed.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Clarke's section on model checkers and debugging, on the addition of counterexample generation and its consequences, together with Emerson's remarks on bug detection as a driver of industrial adoption.
