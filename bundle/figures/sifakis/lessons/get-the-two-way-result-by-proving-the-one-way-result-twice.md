---
type: lesson
title: "Before assuming a two-way result needs the strongest relation, try proving the one-way result twice in opposite directions"
figure: sifakis
works: [property-preserving-abstractions-1995]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [formal-methods-and-verification, foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Before assuming a two-way result needs the strongest relation, try proving the one-way result twice in opposite directions

**Lesson:** There is a standard pairing in this kind of theory: a weak correspondence between two models transfers answers one way, and if you want answers to transfer both ways — a "yes" on the small model meaning yes on the large one *and* a "no" meaning no — you are told you need the strong correspondence, the one where each model can mimic the other move for move with a single relation serving both directions. That folklore is expensive, because the strong correspondence is exactly what a state-collapsing scheme is least likely to satisfy; the whole point of collapsing was to be lossy. Sifakis and co-authors do not accept the pairing. They prove a general lemma saying that one-way transfer from the first model to the second, plus one-way transfer from the second back to the first, plus a modest algebraic side condition on the maps, yields two-way transfer — and then obtain their two-way results by invoking it, never by establishing the strong correspondence at all.

What this buys is concrete: two-way preservation of the universal and existential fragments now holds under *mutual* one-way correspondence, where the two directions may be witnessed by different relations chosen independently. That is strictly easier to arrange than a single relation working both ways, and it decomposes the work: each direction is a separate obligation, provable with separate machinery, discharged by whoever can discharge it. The strong correspondence is still needed for the full logic including its negations, and the paper says so. But the fragments people actually write specifications in fall out of the cheaper hypothesis.

The habit generalizes past logic to any place where a bidirectional claim seems to demand a heavy structure. Round-tripping a data format, showing two implementations are interchangeable, showing a cache agrees with its backing store, showing a refactor changed nothing observable — the instinct is to look for one relation or one invariant strong enough to carry the whole equivalence. Try instead to state the two implications as separate one-way claims, prove each on its own terms, and look for the smallest extra condition that lets them be composed into the equivalence. Often the composing condition is something you already have and never named. When two directions genuinely need different arguments, forcing them through a single symmetric structure is not rigor; it is a self-imposed obstacle that hides which half of the claim is the hard one.

**Source:** [Property Preserving Abstractions for the Verification of Concurrent Systems](../works/property-preserving-abstractions-1995.md) — section 5's theorem deriving strong preservation from preservation in each direction under an idempotence and an identity-below condition on the two maps, and section 6.2's observation that whereas strong preservation of the whole mu-calculus is known to require bisimulation, applying that theorem yields strong preservation of the box and diamond fragments under the weaker hypothesis of simulations existing in both directions.
