---
type: lesson
title: "Earn parallelism from the structure of the program itself, and treat every synchronization point as a visible defect in that structure"
figure: girard
works: [linear-logic]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Earn parallelism from the structure of the program itself, and treat every synchronization point as a visible defect in that structure

**Lesson:** There are two ways to make concurrency trustworthy. The common one bolts an external description onto the program — a temporal or modal commentary that reasons *about* the program's interleavings from outside it. The other insists that the program's own well-formedness is what makes its concurrent execution safe, so that nothing needs to be said from outside at all. The second is the harder standard and the one worth holding. Under it, a program that is structurally sound composes concurrently by construction; there is no separate proof obligation about races, because there is nothing in the representation for two workers to contend over.

The striking empirical fact is how far this actually goes. In the fragment where the resource discipline is total — nothing duplicated, nothing discarded, no branching — independent rewrites can proceed in any order, all at once, with not a single synchronization concern, and the whole computation still converges. That is not a scheduling achievement; it is a consequence of there being no shared identity to coordinate. And the converse is just as informative: the places where synchronization becomes necessary are exactly the places where the formalism has to introduce an opaque enclosure — a region that must be treated as a unit and entered only through its designated door. Choice points need one, because until the branch is decided you cannot know which of the superposed alternatives matters. Reusable values need one, because duplication is a genuinely sequential act.

That correspondence is the design tool. If every enclosure is a synchronization point and every synchronization point is an enclosure, then the parallel structure of a program becomes something you can read off its notation rather than something you discover by profiling or by debugging a race. Reducing enclosures becomes an explicit, well-posed engineering goal, with a known floor: some of them are removable with effort, and at least one — the one that licenses reuse — is irreducible and should simply be written down honestly rather than wished away. Enclosures also license laziness on principled grounds: a branch enclosure need not be opened until something demands its result, and the waiting time is real time available for other work.

For a working programmer this inverts the usual habit. Instead of writing sequential code and then hunting for parallelizable regions, you ask what discipline the representation would have to satisfy for concurrency to be structurally impossible to get wrong, then treat each place you must break that discipline as a documented, deliberate cost. The list of those places *is* your concurrency design.

**Source:** [Linear Logic](../works/linear-logic.md) — the proof-net material and its computer-science commentary: the argument that concurrency should hold for internal reasons rather than by external annotation, the observation that the fully resource-disciplined fragment normalizes with no synchronization problem whatsoever, and the treatment of proof-boxes as synchronization marks whose number should be minimized.
