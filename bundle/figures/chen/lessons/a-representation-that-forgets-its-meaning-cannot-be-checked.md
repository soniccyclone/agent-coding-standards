---
type: lesson
title: "A representation that discards its own meaning cannot police itself"
figure: chen
works: [the-entity-relationship-model-toward-a-unified-view-of-data]
axes: [verifiability, expressiveness]
subdomains: [databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# A representation that discards its own meaning cannot police itself

**Lesson:** Chen's sharpest objection to a purely structural view of data is a nonsense operation that no rule forbids. Two columns can be perfectly compatible in type — both counts of years — while measuring utterly different things, the age of a person and the age of a vessel. A formalism that records only the shape of the columns will combine them on request and hand back an answer, and it will be right to, because it was never told which population each number described. The defect is not an error in the algebra; it is an omission in what the algebra was given to work with. Retain the missing fact — model a field as a named mapping out of a specific category of thing, not merely as a column drawn from a pool of values — and the check that was previously a matter of user vigilance becomes something the system can perform, or at minimum warn about.

That is the dependency worth internalizing: expressiveness is upstream of verifiability. Nothing can be validated that was never stated. The corollary is a real test for any representation, stricter than whether it can hold the data: does it have a distinct home for every distinct kind of meaning the domain contains? Chen presses that test on a case the flat view handles badly. The share of a worker's time committed to a particular assignment is a fact about the pairing and about nothing else — it is not a property of the worker, not a property of the assignment. A vocabulary that only lets things carry properties forces such a fact into an arbitrary owner, and everything downstream that reasons about what determines what then reasons from a false premise about where the fact lives.

A programmer who believes this stops treating meaning as documentation. Units, provenance, and which population a value was drawn from get encoded where the machine can see them, because the alternative is a system that cannot distinguish a legitimate combination from a category error and therefore cannot help. And before adding a field, they ask whether it describes a thing or describes a relation between things, on the grounds that putting it in the wrong place is not a tidiness problem — it corrupts every later inference about dependency and ownership.

**Source:** [The Entity-Relationship Model — Toward a Unified View of Data](../works/the-entity-relationship-model-toward-a-unified-view-of-data.md) — the critique of semantic ambiguity in combining structurally compatible columns, and the earlier treatment of properties belonging to an association rather than to either participant.
