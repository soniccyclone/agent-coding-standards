---
type: lesson
title: "Structure derived from what things are outlives structure derived by repair"
figure: chen
works: [the-entity-relationship-model-toward-a-unified-view-of-data]
axes: [expressiveness, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Structure derived from what things are outlives structure derived by repair

**Lesson:** There are two routes to a well-shaped schema and Chen sets them side by side. One begins with whatever grouping of fields you happen to have inherited and repairs it: inspect which fields determine which others, split wherever a determination is misplaced, repeat until the known defects are gone. The other begins by asking what the domain's things and associations are, and lays data out along those seams. For a fixed set of assumptions the two routes land in nearly the same place, which is why the disagreement looks academic — until an assumption moves. Chen's demonstration is small and decisive: permit an undertaking to have more than one person in charge, and the repaired schema is defective again and must be split a second time, while the schema drawn from the domain's categories needs no change at all, because the association already had its own home instead of having been folded into a thing's description on the strength of a cardinality that happened to hold.

The general point is about the provenance of a design's information. A bottom-up repair bakes contingent facts into the shape — which determinations hold right now, at the traffic and cardinalities of today. A top-down derivation bakes in categories: this is a kind of thing, this is an association among things. Categories are far more stable than the cardinalities hanging off them, so the cost of future change tracks how contingent the facts were that decided the structure. Repair reaches correctness for the present without ever recording why the present shape is right, so the reasoning cannot be replayed when conditions shift; derivation from categories leaves that reasoning visible in the shape itself.

A programmer who takes this seriously treats mechanical restructuring rules as a diagnostic rather than a design method. Before applying them, sketch what the structure would be if it were drawn from the domain's own categories, and treat any gap between the two as the interesting finding — the gap is usually a place where a contingent fact got promoted to structure. It also argues for giving an association its own home even when today's multiplicity permits collapsing it into one of the participants, since collapsing is a bet that the multiplicity will never change, and that bet is placed silently and lost expensively.

**Source:** [The Entity-Relationship Model — Toward a Unified View of Data](../works/the-entity-relationship-model-toward-a-unified-view-of-data.md) — the comparison of normalized relations against entity and relationship relations, including the worked case where a changed multiplicity assumption forces further decomposition on one route and nothing on the other, and the closing characterization of the two routes as bottom-up versus top-down.
