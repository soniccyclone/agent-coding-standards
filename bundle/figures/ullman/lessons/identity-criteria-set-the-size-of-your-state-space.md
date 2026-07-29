---
type: lesson
title: "What you decide counts as 'the same thing' sets the size of your state space"
figure: ullman
works: [a-comparison-between-deductive-and-object-oriented-database-systems]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [databases-and-data-management, programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# What you decide counts as 'the same thing' sets the size of your state space

Deciding when two pieces of data are the same thing looks like a modelling nicety
and is actually a decision about whether your computation finishes. Ullman's
transitive-closure argument makes this sharp: under a value discipline, where two
derived facts that look alike *are* alike, the closure of a finite graph is finite
and computing it terminates by construction. Give every derivation its own
identity instead, so that the same conclusion reached two ways counts as two
things, and the identical rules now denote an infinite object as soon as the graph
has a cycle. Nothing about the rules changed. The only thing that changed was the
equality test, and it moved the answer from finite to unbounded.

The reason is that a value discipline is what collapses the search space. Merging
indistinguishable results is the mechanism by which iteration reaches a fixed
point at all; a fact already derived contributes nothing new, so progress is
monotone and bounded. Identity refuses that merge on principle — it insists on
remembering provenance — and provenance grows with the number of paths rather
than the number of conclusions. Any system that closes over its own output, be it
a query engine, a rule engine, a constraint solver, an incremental build graph or
a memoizing cache, lives or dies on this choice. And identity is not something
you can bolt on afterward: it can always be encoded, by carrying the derivation
history along as extra structure, which is exactly why bolting it on costs you
termination.

The programmer who has internalized this treats the equality predicate as a
load-bearing design decision made early and deliberately, not a detail deferred
to whatever the language's default happens to be. Faced with unbounded growth in
a derived collection, the first place to look is not the algorithm but the
question of what distinctions are being preserved that need not be. And where
some provenance really is needed, the useful move is to bound how much gets
remembered — distinguishing derivations by a fixed, finite feature rather than by
their whole history — restoring termination while keeping the distinction that
mattered.

**Source:** [A Comparison Between Deductive and Object-Oriented Database Systems](../works/a-comparison-between-deductive-and-object-oriented-database-systems.md) — the section arguing that deductive and object-oriented approaches do not mix, where the two-rule path definition is evaluated first under value semantics and then under object identity, plus the follow-on discussion of encoding identity via extra derivation-tracking arguments and of limiting it to a finite distinction.
