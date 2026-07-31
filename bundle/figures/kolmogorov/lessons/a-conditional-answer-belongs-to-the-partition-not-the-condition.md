---
type: lesson
title: "A \"given that\" answer is fixed by the family the condition came from, not by the condition"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, databases-and-data-management]
tags: [lesson]
---
# A "given that" answer is fixed by the family the condition came from, not by the condition

**Lesson:** Take a point distributed uniformly over a sphere and ask for the distribution of its latitude given that it lies on one particular meridian circle. The question sounds well posed and it has an obvious intuitive answer, uniform along the circle. Kolmogorov computes the actual distribution and it is not uniform; insisting on uniformity produces a flat contradiction. His diagnosis is sharper than "the intuition was wrong": conditioning on an isolated hypothesis of probability zero is *inadmissible*. There is no distribution along that circle at all until you regard the circle as one member of a decomposition of the whole sphere — here, the family of meridians through a chosen pair of poles. Fix a different family containing the very same circle and the conditional distribution changes.

So what conditioning consumes is not the condition, it is the partition. Kolmogorov makes this exact rather than rhetorical: the conditional probability given a function depends only on the partition that function induces, and two functions related by a one-to-one relabeling of their values yield literally the same conditional probability. The function was over-specified input; the partition is the real argument. The consequence for whoever poses the question is that naming a single case does not determine an answer — you must also name the family the case was drawn from. This is very often the hidden cause when a query looks unambiguous yet two competent derivations produce different numbers: each derivation quietly supplied a different family, and the disagreement is not arithmetic.

The pattern recurs wherever a conditional number is computed over a slice thin enough to be effectively measure-zero. Ask for the failure rate given a single value of a continuous or high-cardinality field and the answer is a property of your bucketing, which the question never mentioned. Condition an experiment's analysis on a quantity determined after treatment and the same ambiguity appears in a costlier form. Route or cache by "requests like this one" without defining the similarity classes and you have specified nothing. The discipline is to make the partition an explicit parameter — of the API, of the report, of the question — and to decline conditional queries that have not supplied one. When two teams disagree about a conditional figure, compare their partitions before you compare their computations.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — Chapter V, §2's resolution of the Borel paradox, computing the non-uniform latitude distribution on a meridian and concluding that conditional probability with respect to an isolated hypothesis of probability zero is inadmissible because the distribution exists only relative to a decomposition of the sphere into meridians; together with §1's demonstration that conditional probability depends only on the induced partition and is unchanged by a one-to-one relabeling of the conditioning function's values.
