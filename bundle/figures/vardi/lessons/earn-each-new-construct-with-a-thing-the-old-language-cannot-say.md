---
type: lesson
title: "Earn each new construct with a thing the old language cannot say, and price it before adding it"
figure: vardi
works: [the-complexity-of-relational-query-languages]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# Earn each new construct with a thing the old language cannot say, and price it before adding it

**Lesson:** The disciplined way to grow a language is one rung at a time, where every rung is justified by a specific request the current language provably cannot honour and is immediately priced in the currency of evaluation cost. Reachability along a relation of unbounded length cannot be phrased with a fixed number of quantifiers, so a closure construct is admitted — and the cost of the cheapest possible query jumps from deterministic to nondeterministic. Closure still cannot carry a parameter that must stay constant along the whole chain, so least-fixpoint recursion is admitted — and the price moves again. Parity of a set resists even fixpoint recursion, so quantification over unknown relations is admitted, and the price rises once more. Each step is a purchase with a receipt: here is the sentence you could not previously write, and here is what it now costs to answer anything at all.

The counterexample-driven half of that discipline is what keeps a language from bloating. It is easy to add a construct because it feels expressive, or because a competing system has one; it is hard, and much more informative, to be required to exhibit something genuinely unsayable first. An inexpressibility result is what turns "would be nice" into "is necessary", and it also bounds the addition: knowing exactly which gap the construct closes tells you when you have added enough and can stop. The pricing half is what keeps the language honest, because expressive power acquired without noting its cost is how systems end up with a feature that is cheap to type and unaffordable to run.

What generalizes is the shape of the ledger. Ranking constructs by what they add and what they charge produces a chain in which power and cost rise together, and that chain becomes the tool you use to place a new requirement: find the lowest rung that can express what you actually need, and refuse to climb further. Most design regret in query interfaces, configuration languages, and rule engines comes from starting at the top of such a chain out of caution, then paying its cost forever on workloads that only ever needed the bottom.

**Source:** [The Complexity of Relational Query Languages](../works/the-complexity-of-relational-query-languages.md) — the section on logical languages, where each extension (transitive closure, then least fixpoint, then second-order existential quantification) is introduced by exhibiting a concrete flight-network query unexpressible in the previous language, and each is then given data- and expression-complexity completeness results that step up in lockstep.
