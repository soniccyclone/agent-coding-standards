---
type: lesson
title: "A law is only valid relative to the contexts your language can build"
figure: milner
works: [algebraic-laws-for-nondeterminism-and-concurrency]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# A law is only valid relative to the contexts your language can build

**Lesson:** An equation between program fragments feels like a fact about the fragments. It is not. It is a fact about the fragments together with the set of surroundings they might be placed in, because interchangeability means no surrounding can tell them apart, and the surroundings are exactly what the language lets you write. Add an operator and you have added new surroundings, some of which may be more discerning than anything expressible before — and previously sound equations can become false without either side changing at all. This paper exhibits it concretely: a law about absorbing internal steps is established and proved complete for a sequential fragment, and then, once parallel composition is added to the signature, a specific instance of that law is shown false, because a concurrent partner can offer an interaction that resolves a choice at a moment the sequential contexts could not observe.

The response is instructive. The law is not patched or hedged; it is replaced by two strictly weaker laws, each of which survives the richer setting, and it is verified that the weaker pair is derivable from the old one — so nothing was gained that was not there before, only claims that overreached were withdrawn. The authors then go further and conjecture that this same weakening is what any operator representing concurrent activity will demand, whatever its details. Having discovered which of their laws was contingent on a poverty of contexts, they treat the surviving pair as the more fundamental statement.

The mechanism generalizes past process calculi and is worth naming plainly. Every refactoring identity a codebase relies on — this cache is transparent, these two orderings are equivalent, this retry is unobservable — is implicitly quantified over the ways the surrounding system may observe. Introduce a new observer and the quantifier's range grows: a metrics endpoint, a debug log, a second consumer of a queue, an API that exposes intermediate state, a client sensitive to latency. None of these change the code that was refactored, and all of them can retroactively falsify the equivalence that justified the refactoring. The failure mode is silent, because nothing near the new observer looks wrong.

So the discipline is to record what the equivalence assumed, and to treat every new externally-visible capability as a re-validation event for the identities that assumed it away. When you find that an identity has to be weakened to survive a new observer, resist the urge to special-case it: the weakened form was probably the true statement, and the strong form was an accident of what you had not yet built.

**Source:** [Algebraic Laws for Nondeterminism and Concurrency](../works/algebraic-laws-for-nondeterminism-and-concurrency.md) — the section extending the signature with a composition operator, where a previously complete axiom is refuted by a concrete concurrent context and replaced by two weaker axioms, with the conjecture that any concurrency operator forces the same replacement; the paper's summary table records which axioms hold for which signature.
