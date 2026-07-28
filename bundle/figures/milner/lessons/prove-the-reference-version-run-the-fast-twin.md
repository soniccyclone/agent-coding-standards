---
type: lesson
title: "Prove the reference version, run the fast twin, connect them by simulation"
figure: milner
works: [a-theory-of-type-polymorphism-in-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Prove the reference version, run the fast twin, connect them by simulation

**Lesson:** An algorithm optimized for speed and an algorithm optimized for provability are usually not the same program, and trying to make one artifact serve both roles ends with either a slow deliverable or an unproven one. The structure adopted here is to write two. The first is deliberately inefficient — it rebuilds and re-applies its accumulated substitutions far more often than necessary — and exists solely because its recursive shape lines up with the inductive proof of correctness. The second threads a single accumulated substitution through mutable state, applies it only when forced, and computes just the one result callers actually want rather than the full annotation of every subterm. The correctness of the second is then established not by re-proving it but by a stated simulation relation: it succeeds exactly when the first does, and its output, once the pending substitution is applied, is exactly the first's output.

This is worth more than a proof-engineering trick. It says the specification and the implementation should be allowed to have different shapes, and that the bridge between them is its own artifact with its own statement. That bridge is what makes the optimizations reviewable. Composing substitutions instead of applying them, holding state globally instead of passing it, discarding intermediate results — each is an aggressive change, and each is checkable against the relation rather than against intuition. Without the reference version there is nothing to check against, and "it seemed equivalent" is the only argument available.

There is a corollary about what to record when you cannot prove everything. The paper proves soundness — acceptance implies a genuine correct assignment exists — and explicitly declines to prove completeness, saying only that it is probably true and that two years of production use in a real proof assistant's metalanguage is the available evidence. That asymmetry is the right one. Soundness is what downstream consumers build on, so it must be a theorem; completeness governs how annoying the tool is to use, so field evidence is an acceptable substitute. Knowing which of your properties admits empirical support and which does not is a large part of shipping verified things at all.

A programmer working this way keeps the obviously-correct implementation around after writing the fast one, and states in writing what makes them the same. It becomes the differential test, the documentation of every optimization, and the thing that makes the next optimization safe to attempt.

**Source:** [A Theory of Type Polymorphism in Programming](../works/a-theory-of-type-polymorphism-in-programming.md) — the pairing of the inference algorithm formulated to support the soundness proof with the simplified imperative variant presented afterward, and the proposition asserting their step-for-step correspondence.
