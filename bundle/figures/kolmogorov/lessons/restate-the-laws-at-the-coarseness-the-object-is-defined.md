---
type: lesson
title: "When an object is only defined up to an equivalence, restate every law about it at that coarseness"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# When an object is only defined up to an equivalence, restate every law about it at that coarseness

**Lesson:** Extending conditional probability from finitely many cases to arbitrary partitions costs something specific, and Kolmogorov names the cost instead of absorbing it. The generalized object is no longer a number but a random variable, and it is pinned down only up to equivalence: two candidates differing on a set of probability zero are both correct answers. Consequently the two properties that characterize ordinary probability — lying between zero and one, and being additive over countable decompositions — survive only in almost-sure form. He proves them in exactly that form, and then warns the reader not to forget that for a fixed event the conditional probability is determined uniquely only to within equivalence.

The discipline generalizes cleanly. When you extend a construction, first determine at what granularity the extended object is actually determined, then restate every inherited law at precisely that granularity and never at the old one. Asserting a pointwise property of something defined only up to a null set is not a harmless simplification; it is a false statement, and it is the worst kind of false statement because it will hold in every case you happen to examine and fail in the case that matters. The compensating good news is that honest restatement is what makes the inheritance work: because the characterizing properties do survive in almost-sure form, essentially the whole body of results about the original object carries over to the extension. Coarsening the laws is the mechanism of transfer, not an obstacle to it.

Software is full of objects defined up to an equivalence and code that forgets it. A computed value determined only up to rounding: every predicate about it has to be stated at a tolerance, and an equality comparison is a defect even though it will usually pass. A collection with unspecified iteration order: every downstream property must be order-invariant, and the one place that accidentally depends on order works fine until a library version changes. A replicated value defined up to its merge relation, an identifier defined up to normalization, a key defined up to collision. The procedure is identical each time — identify the equivalence at which your object is genuinely determined, then audit every assertion, test, and invariant for whether it respects that equivalence. The ones that do not are your latent bugs, and this audit finds them by inspection rather than by waiting for the unlucky run.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — Chapter V, §1, where conditional probability with respect to an arbitrary function is constructed as a random variable unique only up to equivalence, its two fundamental properties (bounds and countable additivity) are proved to hold almost surely rather than pointwise, and the text notes that these almost-sure analogues are what allow the basic properties of absolute probability to be carried over.
