---
type: lesson
title: "Vary the route, not only the starting point"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Vary the route, not only the starting point

**Lesson:** When a procedure gets stuck in local optima, the standard remedy is to run it many times from different initial states and keep the best result. That is only half the available variation. The path a local search takes is determined by the starting state *and* by the order in which it considers its moves, and those are independent knobs. Fixing the start and shuffling the visiting order produces genuinely different trajectories that land in genuinely different optima, which means a multi-start budget can be spent along two axes rather than one. If the initial state is expensive to construct, or if the interesting behaviour of your system lives in the traversal rather than the configuration, the second axis is the cheaper source of diversity.

The choice of how to shuffle is itself a design decision with a coverage property attached. Picking the next element to work on uniformly at random gives an unbiased path but no guarantee that every element gets attention within a bounded window, so some parameters may go a long time untouched while others are revisited repeatedly. Drawing a fresh permutation each round and following it gives the same diversity across rounds while guaranteeing that each element is considered exactly once per round. That is a small distinction with real consequences: the permutation version has a coverage invariant you can state and rely on when reasoning about progress, and the with-replacement version does not. Prefer the randomisation that still lets you say something true about what happened.

The wider point is that stochastic search has more than one place to inject randomness, and people habitually reach for the most visible one. Initial values, traversal order, which subset of the data a step consults, which subset of moves are even considered: each is a lever, each produces a different correlation structure between runs, and levers that decorrelate runs more strongly give better value per run when you are keeping only the best. Before adding another restart, ask whether the runs you already have were meaningfully different from each other, and if they were not, ask what else in the procedure could have been shuffled.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's initialization and optimization-ordering discussion in the UV-decomposition section, which observes that randomness is essential given many local minima, that one can vary the initial matrices or the way the optimum is sought or both, and which contrasts round-robin visiting, picking the element to optimize at random, and following a fresh permutation of the elements each round.
