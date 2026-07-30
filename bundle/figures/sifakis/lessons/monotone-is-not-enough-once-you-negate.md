---
type: lesson
title: "Monotonicity carries an approximation through composition; only non-contradiction carries it through negation"
figure: sifakis
works: [property-preserving-abstractions-1995]
axes: [verifiability, primitive-count]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Monotonicity carries an approximation through composition; only non-contradiction carries it through negation

**Lesson:** An approximation that maps a fine-grained description onto a coarse one earns its transfer theorems from order-preservation: if the map never turns a stronger fact into a weaker one, then whatever you build by composing operators that are themselves order-preserving inherits the guarantee, and the argument goes through by structural induction with no further conditions. That is why almost every conservative analysis is stated in terms of monotone functions. But order-preservation says nothing about what happens to a claim and its complement. Nothing in it prevents the coarse view from placing a state in the image of a proposition and simultaneously in the image of that proposition's negation — each mapping was individually order-preserving, and the collision is invisible from inside either one.

Sifakis and co-authors therefore name a separate requirement and prove it separately: for the abstraction to be usable on a specification that mentions negated facts, the images of a proposition and of its negation must not overlap. Without it, the abstraction can be made to endorse both a claim and its opposite, and a checker running on it produces answers that are not merely imprecise but incoherent. The requirement is also stated at exactly the granularity where it costs the least — it is demanded per atomic proposition, not of the abstraction as a whole, and only for the propositions that appear un-negated in the specification, because a proposition that appears only under a negation is being evaluated against a strictly stronger claim anyway and so is safe for free.

The transferable content is a two-part checklist for any approximation you intend to reason with. Ask first whether it preserves the ordering that makes composition sound, and second, separately, whether it can ever assert a thing and its complement about the same object. Analyses that only ever conclude in one polarity need only the first. The moment negation, complement, difference, or "absence of" enters the query language, the second becomes load-bearing and it will not be implied by the first. Then look for the smallest scope on which to demand it — per predicate rather than globally, per query rather than per system — because a non-contradiction condition demanded everywhere is usually the condition that makes the abstraction impossible to build.

**Source:** [Property Preserving Abstractions for the Verification of Concurrent Systems](../works/property-preserving-abstractions-1995.md) — section 6.2's definition of consistency between an abstraction function and an interpretation as disjointness of the images of a proposition and its negation, the lemma characterizing it, and the verification method's observation that consistency is only needed for propositions occurring non-negated in the formula.
