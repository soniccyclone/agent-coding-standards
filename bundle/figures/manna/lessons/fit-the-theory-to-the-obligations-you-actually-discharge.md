---
type: lesson
title: "Fit the theory to the obligations you actually discharge, not to the space of obligations that exists"
figure: manna
works: [a-temporal-proof-methodology-for-reactive-systems]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Fit the theory to the obligations you actually discharge, not to the space of obligations that exists

**Lesson:** Manna and Pnueli owned a general, complete proof system for temporal properties, and when they set out to teach practitioners how to verify concurrent programs they deliberately declined to present it. Their stated reason is a diagnosis of how theory fails to reach use: once the accumulated results about what a specification language can express and how complete its proof theory is grow past a certain mass, a newcomer reasonably infers that all of it is prerequisite to doing anything at all, and the perceived cost of entry keeps the methodology on the shelf. So they invert the presentation. They name the small number of claim shapes a working verifier spends actual time on, hand each shape its own compact rule set, and cite the general theory only as something a reader may consult later.

What makes this discipline rather than corner-cutting is the word complete. The specialized rule sets are not heuristic subsets of the general machinery that happen to work on the examples; each one is claimed to be sufficient for every property in its class. Restricting scope therefore costs nothing inside the scope, and the boundary of the scope is stated out loud rather than left for the user to discover by failing. The general theory remains the thing that justifies the restriction — you need it to know your specialized tool loses nothing — but it does not need to be in the user's head. A newcomer learns three claim shapes and a handful of local checks, and can prove real mutual-exclusion algorithms correct.

The trade being made is between primitive count in the user's toolkit and the generality of any single primitive. A general rule that subsumes several special cases looks like the economical choice, and by one measure it is. But a general rule forces every user to re-derive their case from it, whereas several sharply-shaped rules dispatch on recognition: identify which kind of claim you are making and the applicable rule is already the right shape, its premises already matching the situation. The cost is a few more rules to know. Manna and Pnueli judge that cost worth paying, and the frequency distribution of real obligations is what decides it — the shapes they specialize for are the ones that come up constantly.

Someone who thinks this way builds interfaces and abstractions against the measured distribution of what callers actually do rather than the closure of what they could conceivably do. They will ship three specialized operations whose preconditions match three common situations before one universal operation that every caller must adapt to, and they will justify it by pointing at usage, not taste. The complementary obligation is honesty about scope: the specialized offering must state what falls outside it, and there must exist a general story the specialization is provably a shadow of, or the restriction is just an unexamined guess about what users need.

**Source:** [A Temporal Proof Methodology for Reactive Systems](../works/a-temporal-proof-methodology-for-reactive-systems.md) — the introduction's argument for circumventing the general theory of temporal logic in favor of rules tailored to the frequently-verified classes, and the paper's resulting organization as one small, class-complete rule set per claim shape rather than a single general system.
