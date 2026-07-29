---
type: lesson
title: "Build tools to run in the direction reasoning runs, which is backward from symptom to cause"
figure: ungar
works: [debugging-and-the-experience-of-immediacy]
axes: [cognitive-load, verifiability]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Build tools to run in the direction reasoning runs, which is backward from symptom to cause

**Lesson:** Programs execute forward, so tools get built forward: step forward, run to the next breakpoint, print as you go. But nobody debugs forward. Debugging starts from an observed wrong outcome and works backward, asking what produced this value, and what produced that one. A tool that only moves forward forces the programmer to guess where the interesting moment was, restart, and try to arrive there again — repeatedly, since each guess is usually wrong. The mismatch is not a missing convenience feature; it is a tool oriented against the grain of the only task it exists to serve.

Once you accept that inference runs backward, the design consequences are large and specific. State has to be retained rather than overwritten, because the question "what was it before" must be answerable at all. Every view the programmer consults — the code position, the current value, the call stack, whatever the program drew on the screen — has to move together, or moving backward in one view leaves the others describing a different moment and the programmer has to reconcile them by hand. And the granularity of stepping has to be chosen by relevance rather than by whatever unit the machine happens to advance in: stepping to the next thing that appeared on screen is the right move when the symptom is visual, even though it is not a unit the language defines.

The generalization beyond debuggers: for any diagnostic system, identify the direction in which someone will actually interrogate it, then build for that direction even when the underlying process runs the other way. Logs written in emission order and searched in causal order, traces that record forward and get read backward from the failure, metrics stored per-event but questioned per-incident — all the same shape. A programmer who has internalized this asks, before building any observability surface, what question will arrive first, and makes that question the cheap one.

**Source:** [Debugging and the Experience of Immediacy](../works/debugging-and-the-experience-of-immediacy.md) — the treatment of temporal immediacy, which argues that closeness backward in time matters at least as much as closeness forward, and the accompanying discussion of a reversible stepper that keeps code, values, stack, and graphical output consistent in either direction.
