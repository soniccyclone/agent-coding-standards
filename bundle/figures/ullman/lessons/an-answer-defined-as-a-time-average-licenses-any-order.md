---
type: lesson
title: "An answer defined as a time average licenses any processing order"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, verifiability]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# An answer defined as a time average licenses any processing order

**Lesson:** Whether a computation may be reordered, run asynchronously, or spread across machines is usually treated as a question about the algorithm. It is better treated as a question about the definition of the answer. If what you are computing is the value of the system after exactly k synchronised rounds, then rounds are part of the specification and any asynchrony changes the result. If what you are computing is a long-run average — the fraction of time the system spends in each configuration, the expected value under a stationary regime — then no particular schedule appears in the definition at all, and any schedule that visits everything often enough converges to the same thing. Reordering freedom is not something you win by argument; it is a property you either wrote into the specification or did not.

That framing makes the design decision clear and moves it earlier. Before optimising, ask what your target quantity is actually defined as, and if the definition mentions a global step counter, ask whether it needs to. Very often the synchronised formulation was chosen because it is easy to write down and reason about, while the quantity of interest is genuinely a steady-state average that the synchronisation is merely one way of reaching. Restating the target as an average over time rather than a snapshot after a fixed schedule costs nothing in fidelity and removes the coordination barrier that was making the computation expensive to distribute.

The argument that an asynchronous schedule computes the right thing then has a specific shape, worth being able to reproduce. Committing a portion of each element's pending amount at moments determined by an arbitrary selection order is equivalent to observing the process at arbitrary times; a long-run average is by definition what you see when you observe at an arbitrary time; so the accumulated observations approximate the average. What the argument requires is that the selection be unbiased with respect to the quantity being measured — a schedule that systematically favours certain elements at certain phases would sample the process non-uniformly and skew the result. Fairness of the schedule, not its determinism, is the condition.

The residue of this is a habit: when synchronisation is the bottleneck, examine whether it is load-bearing for correctness or only for the convenience of the specification. The cases where you can drop it are exactly the cases where the answer was a statistic over time rather than a state at a time, and those are far more common than the synchronous formulation makes them look.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the section on why approximate Simrank works, which argues that walkers moving asynchronously still distribute themselves as they would under a synchronous walk, and that selecting nodes in an arbitrary order to commit their residual amounts to observing each walker at a random time, which is precisely the definition of the probability that a walker is at a given node.
