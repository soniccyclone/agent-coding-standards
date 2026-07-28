---
type: lesson
title: "A dependency is a claim about correctness, not a record of who calls whom"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# A dependency is a claim about correctness, not a record of who calls whom

The graph most programmers reason about is the call graph, because it is the one the tools can extract. Parnas insists on a different relation entirely: one component depends on another when the second one being both present and correct is a precondition for the first one meeting its own specification. That definition cuts the call graph in both directions. A component can invoke another without depending on it — if its own specification only obliges it to issue a well-formed request, it has discharged its duty whether or not anything at the far end works. And a component can depend on another it never invokes at all; almost every program in a machine silently assumes that whatever handles interrupts will leave the processor in a state it can survive.

The reason this distinction has teeth is that dependency is where all the interesting structural properties live, and the call graph is only an accident of implementation. Whether a subset of the system can run, whether a correctness argument closes, whether a change can be contained — all of these follow the correctness-precondition relation, not the invocation relation. And you cannot read the relation off either artifact alone: deciding whether one component depends on another requires looking at that component's implementation *and* its specification together, because the question is which of its assumptions are load-bearing for the promises it made.

A programmer who takes this seriously stops treating the import list or the profiler's caller tree as the architecture. Before adding a call, they ask a different question than "does this function exist": does my correctness now rest on that code, or only on my sending it a legal request? The two answers produce very different systems, because the second lets a component be absent without breaking anything above it. They also go hunting for dependencies with no syntactic trace at all — the shared scheduler, the assumed initialization order, the error handler everyone quietly relies on — because those are precisely the ones no dependency-analysis tool will ever show them.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — Developed in the section defining the "uses" relation, including its two explicit divergences from invocation and the observation that settling the question requires both the implementation and the specification of the depending component.
