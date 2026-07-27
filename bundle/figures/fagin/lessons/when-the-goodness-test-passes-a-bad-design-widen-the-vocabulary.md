---
type: lesson
title: "When the goodness test passes a bad design, widen the vocabulary rather than the rulebook"
figure: fagin
works: [multivalued-dependencies-and-a-new-normal-form-for-relational-databases]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# When the goodness test passes a bad design, widen the vocabulary rather than the rulebook

**Lesson:** There is a specific and recurring situation worth learning to recognize: a design passes every formal quality check you own, and yet anyone looking at it can see something is wrong. Fagin's starting point is exactly that. A schema in which an employee's whole salary history is repeated once per child satisfied the strongest normal form then available, because that form was built out of one kind of constraint — the single-valued determination — and the redundancy on display was not of that kind. The tempting responses are to add a heuristic ("also split when it feels repetitive"), to appeal to semantics ("the designer should just know"), or to declare the criterion good enough. All three leave the criterion blind in the same place forever.

The productive response is to treat the blind spot as evidence that the constraint language is impoverished, and to go find the missing primitive. Fagin generalized determination so that the right-hand side could be a *set* of values fixed by the left-hand side and orthogonal to everything else in the row; the older notion falls out as the degenerate case where that set has at most one element. With the richer primitive in hand, the goodness criterion could be restated in exactly the same shape as before — every constraint traces back to a key — and it now saw the defect it had previously waved through. Nothing was bolted on; the definition got shorter relative to what it could express.

The other half of the lesson is about notation. The same content could have been phrased purely operationally, as "this table splits into two without loss," but Fagin deliberately introduced a directional arrow between attribute sets instead, because that framing exposes properties the operational phrasing hides — transitivity, in particular, is visible as a composition law between named relations and invisible when you only ever talk about decompositions performed. How you name a concept determines which of its laws you will notice.

A programmer who has internalized this stops patching a linter, a type system, or a review checklist with special cases when it lets something obviously bad through. The question becomes: what property does the tool have no word for? Then: can that word be chosen so the existing rule, restated over the larger vocabulary, subsumes both the old cases and the new one? A criterion that grows by exceptions decays; a criterion that grows by generalizing its primitives gets stronger and stays short.

**Source:** [Multivalued Dependencies and a New Normal Form for Relational Databases](../works/multivalued-dependencies-and-a-new-normal-form-for-relational-databases.md) — the introduction's worked example of a schema that is all-key and therefore passes the prior normal form while still repeating information, and the parallel construction of the new normal form over the generalized dependency. The remark on arrow notation versus decomposition talk appears in the section on transitivity.
