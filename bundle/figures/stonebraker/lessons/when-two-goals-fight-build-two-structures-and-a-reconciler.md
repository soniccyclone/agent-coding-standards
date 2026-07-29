---
type: lesson
title: "When two goals fight, build two structures and a reconciler"
figure: stonebraker
works: [c-store-a-column-oriented-dbms]
axes: [primitive-count, hardware-affinity, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# When two goals fight, build two structures and a reconciler

Some requirement pairs are not tunable against each other; they want opposite structures. A layout sorted for fast retrieval makes arbitrary insertion expensive, and a layout that appends cheaply is in the wrong order for nearly every read. The usual response is to pick a single structure and accept mediocrity on one axis, or to add knobs that let an administrator slide between two bad points. The alternative is to stop pretending one structure can serve both roles: keep a small structure shaped entirely for accepting change and a large structure shaped entirely for being read, and make a background process responsible for migrating from one to the other in bulk.

What makes this a design pattern rather than an evasion is the reconciler's economics. Because it works in batches, it can rewrite whole regions rather than mutating in place — producing a fresh version alongside the old and switching over on completion — which is cheaper precisely when almost everything is changing, and which sidesteps the fragmentation and locking pain of in-place updates to a densely packed structure. The staging area stays small enough that its inefficiency does not matter and its working set stays resident in memory, so the "slow" side of the split is never on the critical path for long. The cost is honest and bounded: the query path must now read both structures and understand their union, and the system needs a visibility rule that says which records in each one count.

Applying this outside storage engines means recognizing the signature. Whenever you find yourself trading write cost against read cost, freshness against aggregation, or flexibility against compactness in one data structure, ask what each side would look like unconstrained, then ask what the migration between them costs in bulk. A programmer who believes this stops looking for the clever single representation that is decent at both, accepts a second representation plus a merge process as the smaller total complexity, and spends the design effort on the union-visibility rule — which is where the real subtlety lives.

**Source:** [C-Store: A Column-oriented DBMS](../works/c-store-a-column-oriented-dbms.md) — the hybrid writeable-store / read-optimized-store architecture and the tuple mover's bulk merge-out, including its replace-rather-than-update-in-place strategy.
