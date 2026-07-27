---
type: figure
title: Ronald Fagin
description: b. 1945, IBM Research. Formalized dependency theory beyond Codd's original normal forms (4NF, DK/NF).
status: accepted
layer: design-thought
subdomains: [databases-and-data-management]
tags: [figure, accepted]
---

# Ronald Fagin

**Dates:** b. 1945. IBM Research (San Jose/Almaden); works across database theory, finite model theory, epistemic logic.

## Why a candidate
Formalized dependency theory beyond Codd's original normal forms (4NF, DK/NF) — exactly the kind of "reason from the dependency structure itself" work the vetting standard favors over ad hoc schema design rules. One of the strongest primitive-grounded candidates in this subdomain.

## Top 10 most influential works
1. "Multivalued Dependencies and a New Normal Form for Relational Databases" (1977, 4NF) — `public` (self-archived on researcher.ibm.com)
2. "Functional Dependencies in a Relational Database and Propositional Logic" (1977, IBM J. Res. Dev.) — `public` (IBM Research self-archived)
3. "A Normal Form for Relational Databases That Is Based on Domains and Keys" (1981, DK/NF) — `uncertain`
4. "Horn Clauses and Database Dependencies" (1982, JACM) — `paywalled`
5. "Degrees of Acyclicity for Hypergraphs and Relational Database Schemes" (1983, JACM) — `paywalled`
6. "On the Semantics of Updates in Databases" (1983, with Ullman, Vardi) — `paywalled`

## Lessons

Fagin's body of work treats definitions, not systems, as the thing being engineered, and it teaches a working method for engineering them. The recurring diagnostic is that a design vocabulary can only expose defects it is capable of expressing, so when a formal quality standard blesses a structure everyone can see is bad, the correct response is to enlarge the vocabulary rather than bolt heuristics onto the rulebook, and when a distinction in that vocabulary looks arbitrary, the arbitrariness is a fact about the vocabulary and not about the world. The feedback loop is adversarial and self-directed: state the criterion, then try to satisfy it degenerately and see what theory of permitted moves you forgot to supply; write the even-handed definition, prove it collapses, and let the collapse choose the asymmetric one; notice when a proof only goes through by case-bashing or refuses to survive a slight widening of its hypothesis, and go back to the decomposition rather than write the argument more carefully. Equivalence is the currency he trades in, handled with unusual discipline. A proved reduction licenses importing a neighbouring field's entire apparatus; a condition that turns out to have a dozen equivalent statements is worth keeping in all twelve, because the combinatorial form is what you check, the algebraic form is what you reason with, and the operational form is what you optimize against. Equally, an equivalence is only as wide as its proof, so the habits that come with it are probing the obvious next generalization for the counterexample, and testing how a property behaves under the specific operations you intend to apply to it, restriction and projection and the imposition of finiteness among them, since a guarantee established without a bound on size may simply evaporate when you add one. Where these definitions touch machines, the through-line is that static shape decides which execution costs are reachable at all: the point of designing a schema into a particular structural class is that a cheap local check then certifies an otherwise intractable global property for every possible data set, and that no evaluation order can blow up, which converts "a good plan exists" into the far stronger and delegable "no plan is bad." The later update work extends the same instinct from structure to operations, insisting that you settle what a mutation means before building the mechanism: a change arriving through an abstraction is a claim its author is in no position to translate into a state, several equally minimal outcomes constitute knowledge to be represented rather than a request to reject, the difference between what was asserted and what merely follows is load-bearing precisely when something has to be revised, and whatever discretion the general mechanism has left over belongs in declared data owned by whoever understands the domain.
