---
type: lesson
title: "Build the cost guarantee into the formation rules, so a well-formed definition cannot escape its budget"
figure: cook
works: [feasibly-constructive-proofs-and-the-propositional-calculus]
axes: [primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification, foundations-of-computation]
tags: [lesson]
---
# Build the cost guarantee into the formation rules, so a well-formed definition cannot escape its budget

**Lesson:** There are two ways to keep a system inside a resource budget. You can let people write whatever they like and audit the result, or you can arrange the construction rules so that nothing outside the budget can be written in the first place. The second is available far more often than programmers assume, and it depends on a structural fact: the desired cost class must have a small basis and be closed under the operations you expose. Given a handful of starting operations and two closure rules — composing what you already have, and recursing on the digits of an argument under an explicit growth bound — you reach exactly the functions computable within a polynomial budget and nothing else. The class stops being a property you test for and becomes a property every derivation carries by construction.

The design detail that makes this work is where the growth bound is discharged. Admitting a new recursive definition requires a bound on how fast it grows, and asking whether an arbitrary candidate satisfies such a bound is undecidable, so demanding the check as an oracle would sink the whole scheme. Instead the obligation is made a precondition of admission and must be met with a proof inside the same system, phrased in terms of already-admitted functions so it never mentions the function being defined. This is the general shape of a workable discipline: the burden is a proof obligation at the point of introduction, stated over material that already exists, so the well-formedness relation stays decidable and even expressible within the system it governs. A rule that requires knowing something undecidable about the thing you are adding is not a rule.

Two consequences are worth naming for practice. First, the austere core does not have to be the surface you work in. A friendlier layer with richer formula structure can sit on top, and if you prove it derives nothing the core could not, you get convenience without paying for it in trust — the classical conservative-extension bargain, and the correct answer to the tension between ergonomics and minimality. Second, self-certification has a ceiling. A system built to admit only feasible constructions cannot in general certify its own feasibility as a proof mechanism, by the same self-reference that limits consistency proofs. The discipline governs what you build with it, never itself.

A programmer who thinks this way stops writing validators for properties that could have been made unrepresentable. If the invariant that matters is closed under the combinators you offer, the invariant belongs in the type of the combinators, and the audit disappears along with the class of bugs it was chasing.

**Source:** [Feasibly Constructive Proofs and the Propositional Calculus](../works/feasibly-constructive-proofs-and-the-propositional-calculus.md) — the construction of the equational system, resting on the characterization of the polynomial-time functions by a small basis plus substitution and length-bounded recursion, together with the requirement that a growth bound be proved before a function symbol may be introduced, the conservativity result for the more convenient variant system, and the closing self-reference argument.
