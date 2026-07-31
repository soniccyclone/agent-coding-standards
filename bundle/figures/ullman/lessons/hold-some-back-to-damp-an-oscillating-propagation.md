---
type: lesson
title: "Hold some back to damp an oscillating propagation"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, verifiability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Hold some back to damp an oscillating propagation

**Lesson:** A propagation rule that moves everything it is given at each step is the obvious rule and is not always the fast one. When the underlying structure has a layered or alternating character — every neighbour of a thing is on the other side of some divide — full forwarding makes the quantity slosh: all of it on one side, then all of it on the other, then back, converging only through whatever leakage the process happens to have. Convergence is measured by how quickly the outstanding amount decays, and a rule that keeps handing the whole amount around leaves a large outstanding amount alive for many more steps than necessary.

Forwarding only a fraction and retaining the rest breaks the alternation. Some of the quantity stays put while the rest advances, so after a couple of steps it is spread across both sides rather than concentrated on one, and the peaks that were bouncing get smeared into a decaying profile. The step is smaller but the number of steps drops by more, and the total work goes down. This is worth noticing because the intuition runs the other way: moving less per step feels strictly slower, and it is strictly slower on structures that were never going to oscillate. The retained fraction is insurance against a structural property of the input that you may not have inspected.

Whether the damping is needed is a property of the data, not of the algorithm, which is why it belongs in the default. On a structure with no alternating character the retention is close to free, costing a modest constant. On an alternating structure it is the difference between rapid convergence and prolonged ringing. Since you generally do not know which you have — and real inputs are mixtures — paying the small constant unconditionally is the right default, and stripping it out is an optimisation to be justified by knowing your structure, not the other way round.

The underlying idea is standard wherever an iteration is driven to a fixed point: taking a partial step toward what the update rule suggests, rather than the whole step, trades a little per-iteration progress for immunity to overshoot and oscillation. It shows up as under-relaxation in numerical solvers, as learning rates below one, as gradual rollout rather than instant cutover in traffic shifting. In every case the retained fraction is a stability knob, and its value is that it makes the procedure's behaviour depend much less on the shape of the input.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the explanation in the approximate-Simrank section of why only half of a node's untaxed residual is distributed to neighbours: the text notes that pushing the entire residual is fine on some graphs, but on a bipartite graph the residuals bounce back and forth between the two sides, keeping at least one large residual alive longer than the halved version does.
