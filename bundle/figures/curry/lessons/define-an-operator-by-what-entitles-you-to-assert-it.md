---
type: lesson
title: "Define an operator by what entitles you to assert it, and its laws stop being a matter of taste"
figure: curry
works: [a-theory-of-formal-deducibility]
axes: [expressiveness, verifiability, primitive-count]
subdomains: [foundations-of-computation, programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Define an operator by what entitles you to assert it, and its laws stop being a matter of taste

There are two ways to pin down what a construct in your system means. You can
list the properties you want it to have and call that list the definition — the
axiomatic habit, and the one everybody reaches for first. Or you can state
exactly the circumstances that license you to produce a thing of that kind, plus
exactly what a consumer is allowed to do with one, and then *derive* the
properties. Curry takes the second road on principle and shows what the first
road costs: when meaning is a wish-list, disputes about which laws belong have
no arbiter. He points at a predecessor who published five competing accounts of
the same connective and admitted he could not tell which one was right. That is
not a failure of cleverness. It is the predictable end state of defining
something by the theorems you hope it satisfies, because a wish-list has no
mechanism for adjudicating between rival wish-lists.

Fix meaning at the point of introduction instead, and the arbitration problem
dissolves. Each operator gets a rule saying what you must already have in hand
to build one, and a matching rule saying what a downstream consumer may extract.
Every law of the operator now has to be *earned* from those two rules, which
makes the law set a consequence rather than a negotiation. The payoff Curry
extracts is striking: the properties that practitioners assume instinctively
turn out to be provable, and the ones that turn out *not* to be provable are
precisely the ones that were smuggling in an extra assumption nobody had
declared. When his construction-based system refuses to validate a plausible
law, that refusal is diagnostic — it tells him the law secretly requires the
underlying system to be complete, i.e. to already know the answer to every
question. The rule set didn't fail; it exposed a hidden premise.

A programmer who believes this designs abstractions from their constructors and
eliminators outward. When someone proposes a new operation, the first question
is not "what should it satisfy" but "what must a caller present to be entitled
to it, and what may a caller do with the result." Interfaces designed that way
have derivable algebras: associativity, distributivity, commutation with other
operators either follow or visibly don't, and when they don't you learn which
unstated assumption you were leaning on. Interfaces designed the wish-list way
accumulate laws by fiat, contradict each other under composition, and produce
exactly the situation of five plausible variants with no way to choose.

The corollary is a discipline about the other direction too. Curry does build
one system purely by formal analogy — he notices an asymmetry, patches it for
symmetry's sake, and admits the result has no justification from meaning at all.
He does not then pretend it does. He proves it consistent with the base system,
carries it along in parallel, and says outright that what it is good for must be
settled after the fact. Symmetry-driven generalization is a legitimate way to
find new constructs; it is just not a way to define them. The honest move is to
mark such a construct as unjustified until you discover what it means, which in
his case turned out to be a truth-functional reading rather than a
derivability reading — a genuinely different notion wearing the same notation.

**Source:** [A Theory of Formal Deducibility](../works/a-theory-of-formal-deducibility.md) — the informal analysis opening the chapter on the finite positive connectives, where each connective is given introduction and consumption conditions, together with the introduction's complaint that earlier modal systems had no objective criterion for choosing among rival law sets, and the chapter's closing comparison of the semantically grounded system with the one built by analogy alone.
