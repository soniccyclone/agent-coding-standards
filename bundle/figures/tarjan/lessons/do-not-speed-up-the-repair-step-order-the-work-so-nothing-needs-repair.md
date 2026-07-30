---
type: lesson
title: "Don't make the repair step cheaper; order the work so nothing needs repairing"
figure: tarjan
works: [depth-first-search-and-linear-graph-algorithms]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Don't make the repair step cheaper; order the work so nothing needs repairing

**Lesson:** The algorithms Tarjan was competing with for grouping the mutually-reachable parts of a directed graph all worked by guessing and then correcting. Find a cycle, declare its members a group, continue; when a later discovery reveals that two groups were really one, merge them and relabel everything involved. All of the cost lived in the correcting. The published attempts to improve those algorithms attacked exactly that: better merge structures, cleverer relabeling, and — the paper notes this option explicitly — an off-the-shelf fast list-merging algorithm would improve the bound again. Tarjan declines the whole line of attack. The observation is that a careful reading of what the disciplined traversal actually does to a directed graph yields an algorithm in which a group is never emitted before it is complete, so there is nothing to merge, ever. The merge structure is not optimized; it is deleted.

The distinction to internalize is between *provisional* output and *final* output. An algorithm that publishes answers it may later have to revise has committed to maintaining a correspondence between its published state and its current knowledge, and that correspondence is what costs — in running time, in the data structures it drags along, and in the proof burden, because correctness now has to survive every possible revision path. An algorithm that only publishes when the answer is settled needs no such machinery. What buys the second version is finding an order of discovery in which completeness is detectable at the moment it occurs: here, a test that fires exactly when the traversal is about to leave the topmost vertex of a group, at which instant everything in the group is sitting together on a stack and can be handed off in one motion.

The general habit is to treat a prominent fix-up phase as a symptom rather than a component. Reconciliation passes, cache invalidation sweeps, deduplication jobs, re-derivations that repair earlier partial results — each of them exists because something upstream emitted a guess. Before tuning it, ask what ordering of the upstream work would make each output final on first emission, and whether a cheap local test can certify that finality. Sometimes no such order exists and the fix-up phase is essential. But the possibility deserves to be eliminated before its cost is optimized, because the version with no repair step is smaller, faster, and easier to prove than any tuned version of the one that repairs.

**Source:** [Depth-First Search and Linear Graph Algorithms](../works/depth-first-search-and-linear-graph-algorithms.md) — the strong-connectivity section's critique of prior cycle-finding algorithms whose cost is dominated by collapsing and relabeling components, its remark that a fast list-merging algorithm would lower that bound, and its conclusion that a closer study of depth-first search yields a linear algorithm requiring no merging at all, together with the vertex-stack discipline that emits each component only once its root is identified.
