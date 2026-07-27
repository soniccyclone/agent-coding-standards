---
type: lesson
title: "When unrelated wishes turn out to be one condition, keep every form of it"
figure: fagin
works: [on-the-desirability-of-acyclic-database-schemes]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [databases-and-data-management, algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# When unrelated wishes turn out to be one condition, keep every form of it

**Lesson:** Three communities had been chasing different things. People studying schema structure wanted local agreement between tables to guarantee that the tables are all slices of one coherent whole. People studying constraints wanted a hard-to-check global constraint to reduce to a set of easy-to-check pairwise ones. People building distributed query engines wanted a message-cheap pruning program that leaves only rows which survive the final combination, and an evaluation order whose intermediate results never balloon past the answer. None of these groups was working on the other's problem. The paper proves all of it is the same condition, stated twelve ways: some purely combinatorial, some about constraints, some about execution.

The first inference to draw is about the condition rather than the theorem. A property that can be reached from that many independent motivations is not a convenient hypothesis somebody chose; it is a seam in the subject. Fagin and his coauthors say so directly, arguing the class is natural and important precisely because so many characterizations land on it, and that a general theory becomes cleaner if you confine attention to it because the pathologies that make the general case ugly cannot occur inside it.

The second inference is the practical one, and it is the reason not to pick a favorite formulation. Each face of the condition is good at a different job. One is a rewriting procedure that repeatedly strips columns appearing in only one place and discards tables contained in others; it terminates iff the condition holds, so it is the version you implement as a test. Another is an ordering property saying each table's overlap with everything before it sits inside a single earlier table; that one is the version you reach for when proving further theorems, because induction runs along the ordering. A tree whose edges are labelled by shared columns is the version you hand to a query planner, since it dictates the evaluation order directly. A chordality-plus-conformality statement about the induced graph is the version that connects to existing graph theory and its linear-time algorithms.

A programmer who internalizes this stops collapsing equivalent characterizations down to a single canonical one for tidiness. The equivalences are the asset: the cheap test certifies the expensive guarantee, the inductive form powers the proofs, the constructive form drives the implementation, and each is derivable from the others once. The habit is to notice when several apparently unrelated things you want all hold or all fail together, and to suspect a single underlying structural condition rather than a coincidence, then to hunt for the formulation of it that fits the task in front of you.

**Source:** [On the Desirability of Acyclic Database Schemes](../works/on-the-desirability-of-acyclic-database-schemes.md) — the main equivalence theorem listing twelve conditions, the introduction explaining that the conditions arose in three unconnected research areas, and the section on significance that assigns each condition its distinct practical role.
