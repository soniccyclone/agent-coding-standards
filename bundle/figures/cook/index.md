---
type: figure
title: Stephen A. Cook
description: b. 1939, Toronto. Proved the Cook-Levin theorem establishing NP-completeness, founding the formal theory of computational intractability.
status: accepted
layer: implementation-mapping
subdomains: [algorithms-and-complexity]
tags: [figure, accepted]
---

# Stephen A. Cook

**Dates:** b. 1939. American-Canadian computer scientist and mathematician, University of Toronto.

## Why a candidate
Proved the Cook-Levin theorem establishing NP-completeness (SAT), founding the formal theory of computational intractability that this subdomain is built on.

## Top 10 most influential works
1. "The Complexity of Theorem Proving Procedures" (1971, STOC) — `uncertain` (widely mirrored on course/scanned sites, no confirmed authorized open copy)
2. "Feasibly Constructive Proofs and the Propositional Calculus" (1975) — `paywalled`/`uncertain`
3. "The Relative Efficiency of Propositional Proof Systems" (1979, with Reckhow) — `paywalled`
4. "Time-Bounded Random Access Machines" (1973, with Reckhow) — `paywalled`
5. "Characterizations of Pushdown Machines in Terms of Time-Bounded Computers" (1971, JACM) — `paywalled`
6. "An Overview of Computational Complexity" (1983 Turing lecture) — `uncertain`

## Lessons rollup
Cook's work teaches one habit above all: a capability claim means nothing until a cost is attached to it, and the cost has to be built into the concept rather than measured afterward. That runs from the machine level up. Price each primitive at what real hardware would pay, or the analysis credits work nobody performs ([charge for real work](lessons/charge-for-the-work-the-machine-actually-does.md)); demand that a high-level notation lower predictably enough to read cost off the source, and treat a concept as objective only across the translations that provably preserve it ([cost-preserving abstraction](lessons/an-abstraction-worth-reasoning-in-preserves-its-cost.md)); make the budget part of what a definition means, and where possible arrange the formation rules so nothing over budget can even be written ([bounds inside definitions](lessons/a-method-without-a-resource-bound-is-not-a-method.md), [invariant by construction](lessons/make-the-cost-class-an-invariant-of-well-formedness.md)). The second thread is what to do when the absolute question is unanswerable, which it usually is. Give up on measuring difficulty and measure the cheap translations between problems instead, so unknown costs bind to each other into an ordering ([translation over measurement](lessons/compare-difficulty-by-translation-not-measurement.md)); characterize a hard task by the cheap test that recognizes a good answer, since that is where the specification actually lives and the difficulty is exactly the gap between checking and finding ([the recognizer](lessons/the-recognizer-is-the-real-specification.md)); reify a whole execution as one static constraint object so tools that cannot touch running programs can attack it ([reify the run](lessons/turn-a-computation-into-a-static-object-you-can-solve.md)). The third thread is discipline about instruments. Pick the model for what it lets you prove and count every arbitrary clause in a specification as a place no theorem can live ([model selection first](lessons/pick-the-model-that-admits-proofs-not-just-programs.md)); audit whether your method can even discriminate the case you are chasing before spending more effort on it ([check the method's reach](lessons/audit-whether-your-technique-can-reach-the-conclusion.md)); rank competing implementations by a cost measure parameterized on what actually drives the work, not by how they do on the examples someone picked ([measures over benchmarks](lessons/benchmarks-cannot-rank-implementations-a-cost-measure-can.md)). And two structural findings that fall out of taking abstraction seriously: strip a family of artifacts down to its one checkable property and cheap translation will tell you which of your design knobs were ever load-bearing ([abstract to the property](lessons/define-the-family-by-its-checkable-property.md)) — the surviving knob being the right to name an intermediate result, which is worth an exponential in size and nothing at all in step count ([naming is compression](lessons/the-power-to-name-is-the-power-to-compress.md)).
