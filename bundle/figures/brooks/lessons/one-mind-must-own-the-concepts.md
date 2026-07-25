---
type: lesson
title: "Coherence cannot be produced by a committee, so name one mind to own the concepts and give the builders a constraint instead of a vote"
figure: brooks
works: [mythical-man-month]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Coherence cannot be produced by a committee, so name one mind to own the concepts and give the builders a constraint instead of a vote

**Lesson:** A design that presents a single consistent model to whoever uses it has to come from one mind, or from a very small number in genuine agreement. This is not a claim about talent distribution; it is a claim about what coherence is. Consistency across hundreds of small decisions, most of them individually not worth debating, arises only when the same judgment makes all of them, and a system large enough to need many hands is therefore in immediate tension with its own coherence. Resolving that tension is the central organizational problem, and it is resolved by splitting the design task along a boundary rather than by dividing the design authority.

The boundary is between what the thing does, in full user-visible detail, and how it is made to do it. Ownership of the first belongs to one person acting as the user's advocate against every other interest in the room, and it is a full-time job that only the smallest teams can combine with running the project. Everything below the boundary is left deliberately unspecified, which is what makes the arrangement workable rather than tyrannical. Implementation is creative work of the first order, and the product's cost and speed depend on it as much as its usability depends on the design above. On genuinely large systems the same split recurses: the owner partitions the system where the interfaces between parts are smallest and most rigorously statable, and each part gets its own owner reporting upward on concepts.

The objection that this suppresses inventiveness gets the effect backwards. A group handed an external specification stops arguing about what to build and turns immediately on the part nobody has solved, and the inventions start. A group without one spends its thought on the specification and gives construction whatever is left. Constraint concentrates creative attention, which is why a tight budget often produces a better design than a generous one. What the arrangement does require is that the owner of the concepts be able to propose an implementation for anything specified, accept any alternative that meets the objective, and take corrections about cost quietly and continuously, since a boundary defended without that traffic drifts into specifications nobody can build.

**Source:** [The Mythical Man-Month](../works/mythical-man-month.md) — the chapters on coherence of concepts and on the discipline binding designer to builder, including the account of assigning specification work to a large implementation group and the year it cost, plus the retrospective chapter's endorsement of separate design and management roles even on teams of four.
