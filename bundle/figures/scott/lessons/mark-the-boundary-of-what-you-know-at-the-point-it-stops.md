---
type: lesson
title: "Mark the boundary of what you know at the exact point where it stops"
figure: scott
works: [continuous-lattices]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# Mark the boundary of what you know at the exact point where it stops

**Lesson:** A finished piece of technical work contains claims in at least four states: proved, believed but unproved, actively doubted, and not investigated. Writing that collapses these into a uniform confident register is unusable by anyone trying to build on it, because they cannot tell which sentences they may lean on. The cure is to annotate in place, at the point where each gap occurs, and to distinguish the kinds of gap from one another. Scott's habit through this paper is the model: a theorem might generalize but he was unable to see the argument; whether a lemma survives with a weaker hypothesis he does not know and suspects difficulties; a correspondence he very much doubts is continuous, though no counterexample comes to mind; whether a fact about the relationship between two classes of lattice means anything at all he cannot say.

The value is not modesty, it is information density. "I do not know" attached to a specific statement is a research lead someone can pick up, and it costs one clause. "I doubt it but have no counterexample" says something stronger than ignorance — the author has tried and failed to find one, which is evidence about where the truth lies. "I was unable to see the argument" tells a reader the obstacle is likely technical rather than fundamental, so the generalization may be worth another attempt. Each of these steers effort differently, and a text that renders them all as silence steers nothing. The same holds for a codebase: the comment that says which case was never tested is worth more than the one that restates what the function does.

Scope declarations belong in the same family. Scott notes that the whole development could probably be put in a more general categorical setting and that he is not the man to do it, his interests lying in specific applications. That single sentence does more work than an attempt would have: it identifies a direction, declines it explicitly rather than by omission, and prevents a reader from mistaking absence for judgment that the direction is worthless. Declining work out loud, with the reason, is part of describing what you did.

**Source:** [Continuous Lattices](../works/continuous-lattices.md) — the remark after Theorem 3.3 that the result might generalize to arbitrary source spaces but the author was unable to see the argument; the statement after Lemma 3.9 that he does not know whether it holds for retractions and suspects difficulties; the note after Proposition 3.8 doubting the continuity of the maximal-extension operator while admitting no counterexample comes to mind; the open question after Proposition 3.13 about whether other essentially different projection pairs exist; the closing remarks declining the general categorical treatment as work for someone else; and the final bibliographic note's unanswered question about whether every continuous lattice being a retract of an algebraic one means anything.
