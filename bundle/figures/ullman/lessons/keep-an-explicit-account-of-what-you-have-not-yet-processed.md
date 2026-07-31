---
type: lesson
title: "Keep an explicit account of what you have not yet processed"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, parallelizability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Keep an explicit account of what you have not yet processed

**Lesson:** The standard shape of an iterative computation is a sweep: touch every element, update it from its neighbours, repeat until nothing moves much. The cost of that shape is the size of the domain multiplied by the number of sweeps, and it is paid whether or not most elements had anything to contribute. An alternative shape is to maintain, alongside the answer, a second quantity representing what has been discovered but not yet propagated. Work is then drawn from wherever that pending quantity is largest, a little of it is committed to the answer, and the rest is pushed to neighbours. Elements with nothing pending are never visited at all.

The pending quantity is the load-bearing idea, and it is more than a work queue. Because it is a conserved account — everything is either committed or pending, and the total is fixed — it is simultaneously a schedule and an error bound. Stopping while the pending total is below some level is not a heuristic cutoff; it is a statement that at most that much of the answer is unaccounted for. This converts termination from a judgement call into arithmetic, and it lets you derive a bound on the number of steps directly: each step commits at least a fixed minimum, the total is fixed, so the step count cannot exceed their ratio — a bound depending only on your tolerance and not on the size of the input at all.

The consequence worth internalising is that the computation's cost decouples from the size of the domain and attaches instead to the size of the answer. For a query whose true answer is concentrated in a small region, most of the structure is never examined, never loaded, never allocated for — which is what makes a per-source computation feasible on a system far too large to sweep even once. Selecting the largest pending item efficiently needs a priority structure, and the threshold should be scaled by how many neighbours an element would push to, so that the comparison is about what any single neighbour would receive rather than the raw pending total.

The pattern transfers to anything with the shape "propagate an effect through a structure until it settles": invalidation, constraint propagation, incremental recomputation, dataflow. In each case, keeping the not-yet-propagated amount as a first-class value rather than implicit in a queue of dirty flags buys you priority ordering, a principled early stop, and a bound on the residual error — three things that a plain dirty-set gives you none of.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the approximate-Simrank algorithm in the social-network chapter, which maintains a committed vector and a residual vector, repeatedly selects a node whose residual exceeds a tolerance scaled by its degree, commits the taxed fraction and pushes the rest to neighbours, and the accompanying argument that since the two vectors always sum to one and each step commits at least a fixed amount, the number of rounds is bounded by a constant independent of the graph size.
