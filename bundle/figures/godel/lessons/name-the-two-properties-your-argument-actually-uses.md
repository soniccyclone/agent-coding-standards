---
type: lesson
title: "State the minimal properties your argument actually consumes, and it stops being about your artifact"
figure: godel
works: [on-formally-undecidable-propositions, on-undecidable-propositions-of-formal-mathematical-systems]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# State the minimal properties your argument actually consumes, and it stops being about your artifact

**Lesson:** The 1931 argument is carried out against one specific, fully spelled-out system, chosen for convenience, and Gödel is explicit that the choice is convenience only — the Peano-style axioms are there to shorten the work and could be dispensed with. Then comes the move that matters: after the proof is complete, he goes back and enumerates exactly which two features of that system the proof consumed, namely that its axioms and inference relation are mechanically recognizable once the symbols are coded as numbers, and that computable relations are expressible in it. Everything else about the system — its type hierarchy, its particular axiom schemata, the comprehension and extensionality assumptions — turns out to have been scaffolding. With the two conditions named, the result is no longer a fact about one system; it holds of every system meeting them, and he can immediately note that the standard set theories and the standard number theory qualify.

This is the difference between a proof and a reusable proof, and it is also the difference between an implementation and an interface. Doing the work against a concrete artifact is the right way to start — you cannot see what you actually depend on until you have used it. But the artifact then has to be dissolved back into the properties that carried the weight, or the result stays chained to it. The reader benefits twice: a shorter dependency surface is easier to check for soundness, and it is easier to apply, since you test a candidate system against two conditions instead of comparing it feature-by-feature to a reference design.

For the programmer this is the dependency-inversion instinct derived from first principles rather than fashion. When a module's correctness argument runs through a concrete collaborator, ask which of that collaborator's properties the argument used — often it is two or three, none of them the interesting ones — and re-state the module against exactly those. The payoff is not aesthetic. Every property you do not depend on is one that can change without breaking you, and every property you do depend on becomes a thing you can state, check, and require of a replacement. The failure mode this prevents is the common one where an argument, a test, or a design is quietly specific to the first thing it was written against, and nobody knows which parts of that thing are load-bearing.

**Source:** [On Formally Undecidable Propositions of Principia Mathematica and Related Systems I](../works/on-formally-undecidable-propositions.md) — the passage closing Section 2 that lists the only two properties of the concrete system used in the proof, plus the footnote conceding that the concrete system's extra structure served merely to simplify the argument. Also [On Undecidable Propositions of Formal Mathematical Systems](../works/on-undecidable-propositions-of-formal-mathematical-systems.md), which pushes the same discipline further by recasting the whole development as five explicit conditions on an arbitrary system.
