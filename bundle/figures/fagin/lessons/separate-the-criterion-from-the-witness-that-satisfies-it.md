---
type: lesson
title: "Separate the criterion from the witness that satisfies it"
figure: fagin
works: [horn-clauses-and-database-dependencies]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification, databases-and-data-management]
tags: [lesson]
---
# Separate the criterion from the witness that satisfies it

**Lesson:** Fagin wanted a hard, global guarantee: that for any set of stated rules there exists one structure obeying exactly their consequences and nothing more. Instead of proving it directly he proves a three-way equivalence, at a level of abstraction where nothing about databases appears at all. The guarantee holds precisely when there exists some combining operation on structures under which membership in your class of statements is preserved in both directions, and precisely when a disjunction entailed by your rules always has one of its disjuncts entailed. The theorem is stated for an unspecified collection of models, an unspecified collection of sentences, and an unspecified relation of one holding in the other.

The methodological payoff is the explicit split between what is required and what happens to supply it. Fagin says plainly that his interest in the particular combining operation he uses is not because there is anything inherent about that operation; it is because it happens to satisfy the abstract condition, is conceptually simple, and is usually easy to check by hand for a given rule. He then points out that a completely different operation, gluing disjoint copies together, does the job for a narrower class of rules and was in fact how earlier authors got their weaker version of the result. Two unrelated constructions, one criterion. Once the criterion is isolated, the constructions become interchangeable tools and you pick whichever is cheapest to verify in the case at hand.

Stating the theorem where the mechanism has been abstracted away also lets it leave the field. Fagin flags an application in which the models are sets of test data for a program and the sentences are descriptions of what the program computes, where somebody wanted test data carrying no unneeded relationships and got the guarantee for free by checking the disjunction condition. He notes the same theorem explains a long-known fact about free algebras. None of that transfer is possible if the theorem is phrased in terms of tuples and columns, even though the proof would be identical.

For a programmer the discipline runs in two directions. Given a property you want but cannot establish, look for an equivalent condition that is local and mechanically checkable, then prove the bridge once; the awkward global property becomes a corollary of an easy inspection forever after. And when you find yourself proving something about a specific construction, check whether the construction's identity is actually used. If the proof only leans on one closure property, say so, because the version stated in terms of the property covers cases you have not met and callers you have not imagined, while the version stated in terms of the construction covers exactly one.

**Source:** [Horn Clauses and Database Dependencies](../works/horn-clauses-and-database-dependencies.md) — the deliberately domain-neutral statement of the central equivalence theorem, the paragraph disclaiming any special role for the particular product operation used, and the noted applications to program test data and to free algebras.
