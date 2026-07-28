---
type: lesson
title: "Track which assumption buys which capability, and prove one is needed by exhibiting the world where it fails"
figure: church
works: [a-formulation-of-the-simple-theory-of-types]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Track which assumption buys which capability, and prove one is needed by exhibiting the world where it fails

Church does not present his axioms as an undifferentiated pile that the system rests on. He tiers them by yield: one group gets you propositional reasoning, adding the next gets the functional calculus, adding a further group gets elementary arithmetic, and only with two more groups does real analysis become available. The reader can therefore see, for any capability, the exact assumption budget that capability costs — and can work inside a cheaper tier on purpose. He also keeps assumptions he acknowledges are redundant, stating plainly that he wants them present so the consequences of the smaller system can be studied without the stronger extensionality and choice principles in play.

The technique that makes this stratification real rather than decorative is how he argues an assumption is load-bearing. He does not assert necessity; he builds a reading of the symbols in which the assumption is false and everything else still holds — a universe with exactly one individual, or with finitely many — and the assumption's independence follows. This is the general shape of showing a dependency is genuine: construct the concrete world where the thing is absent and watch what stops working. It is the same reasoning as removing a component to find out whether anything actually needed it, done in a setting where the removal can be carried out rigorously instead of guessed at.

The honesty extends to what he cannot settle. He records that one independence question remains open, notes that the familiar techniques do not apply to it, and credits a proof by someone else that partially replaces the assumption in question. An assumption ledger is only useful if unresolved entries stay visibly unresolved; a system whose documentation claims every axiom is necessary, without the constructions to back it, is a system nobody can safely shrink.

A programmer who thinks this way refuses to let a codebase's requirements — a dependency, a global invariant, a configuration flag, a schema constraint — accumulate as an undifferentiated list of things that must be true. They map each one to the specific behavior it enables, then test necessity by actually constructing the reduced configuration and seeing what breaks. Two consequences follow: the system can be deployed in genuinely smaller variants, and the "we can't remove that, something probably needs it" class of permanent complexity never gets established.

**Source:** [A Formulation of the Simple Theory of Types](../works/a-formulation-of-the-simple-theory-of-types.md) — the section on formal axioms, where the axiom groups are mapped onto the theories they suffice for, independence is established by exhibiting interpretations with restricted domains of individuals, and one independence question is left explicitly open.
