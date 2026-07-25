---
type: lesson
title: "A proof establishes internal consistency and nothing about whether you wanted this system, so intent needs its own artifact and its own check"
figure: abrial
works: [faultless-systems-yes-we-can, formal-methods-in-industry-achievements-problems-future]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A proof establishes internal consistency and nothing about whether you wanted this system, so intent needs its own artifact and its own check

**Lesson:** Discharging every obligation establishes that a model is coherent with itself. It says nothing whatever about whether the model describes the system anybody wanted, because the properties proved were transcribed from a statement of intent that was written in prose by people, and prose written by people is wrong. This is the bitter part of the discipline: enormous care goes into stating precisely what must be proved, and success then raises the possibility that what was stated was not what was needed. No amount of additional proof closes that gap, since the gap is between the formalism and the world outside it.

So intent has to be treated as a first-class artifact with its own structure. The useful shape is borrowed from mathematical writing: two texts interleaved but cleanly separable, one explaining and motivating for a reader meeting the problem for the first time, the other consisting of labeled, individually numbered, self-contained statements that constitute the sole reference against which correctness is judged. Explanation must never be load-bearing. Classify the reference statements twice over, once by kind — function, equipment, safety, units, degraded modes, error behavior — and once by abstraction, general down to specific, so that a model's refinement steps can draw from the hierarchy in order and the coverage of the document can be audited. Then get the stakeholders to sign it. The traceability that everyone wants is a consequence of this arrangement rather than an activity performed later.

And because that document is still fallible, keep at least one channel to intent that does not run through the proofs. Animate the model — execute the very thing you proved, even though executing something proved feels like a contradiction, because the point is not to check the mathematics but to let people look at behavior and recognize that it is or is not what they meant. Do it during the earliest, most abstract steps, where changing your mind is nearly free, rather than after implementation, where discovering the same mismatch is ruinous. Staff an inspection team independent of the developers whose only job is to judge the model against the requirements document. Aim whatever system-level testing survives at the requirements rather than at modules. Each of these is deliberately outside the proof loop, which is precisely what makes them worth having.

**Source:** [Faultless Systems: Yes We Can!](../works/faultless-systems-yes-we-can.md) — the opening prescription for a definitions-and-requirements document structured like a mathematics text along two classification axes, and the later argument for animating a model that has already been proved. Also [Formal Methods in Industry: Achievements, Problems, Future](../works/formal-methods-in-industry-achievements-problems-future.md) — the analysis of requirement-document weakness as the residual risk, with the independent validation team and the redirection of global testing toward the document itself.
