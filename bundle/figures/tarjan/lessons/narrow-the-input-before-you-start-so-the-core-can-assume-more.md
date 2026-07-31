---
type: lesson
title: "Narrow the input in cheap front passes so the core algorithm may assume more, and the bound simplifies with it"
figure: tarjan
works: [efficient-planarity-testing]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Narrow the input in cheap front passes so the core algorithm may assume more, and the bound simplifies with it

**Lesson:** Before the interesting algorithm runs, two cheap passes reshape what it is allowed to receive. The first counts edges and rejects the input outright once the count passes a threshold that a classical counting argument shows no object with the target property can exceed. The second splits the input into its maximally-connected-in-the-strong-sense parts, which is legitimate because the property holds of the whole exactly when it holds of every part. Neither pass does anything clever. Together they mean the core algorithm never sees a dense input and never sees a weakly connected one, and both of those are assumptions the core's reasoning leans on constantly.

The subtle payoff is in the analysis rather than the runtime, and it is the part worth internalizing. The core algorithm's cost is naturally expressed in two independent parameters, vertices and edges. After the counting guard, one parameter is provably bounded by a constant multiple of the other, so every bound stated in both collapses to a bound in one — which is how a result about a two-parameter cost becomes a clean statement about input size. Without the guard the algorithm would be no slower on the inputs it accepts, but the theorem would be uglier and would have to carry a caveat about dense inputs forever. So an early rejection test is not only a fast path for bad inputs: it is a device for establishing a relationship between your parameters that the rest of the analysis gets to use for free.

The habit generalizes into two questions to ask at the start of any pipeline. What cheap necessary condition does the target property imply, stated in a quantity you can measure in one pass? And is the property compositional over some decomposition, so that the general case reduces to a constrained one? An affirmative answer to the first buys early exit plus a parameter relationship; an affirmative answer to the second buys a stronger precondition for everything downstream, which usually removes whole families of cases from the core logic. The failure mode this prevents is a core routine bloated with defensive handling of inputs a two-line front pass could have excluded — and the diagnostic is to look at your central function's edge cases and ask which of them describe inputs that should never have arrived.

**Source:** [Efficient Planarity Testing](../works/efficient-planarity-testing.md) — the outline section's first step, which counts edges and declares the graph non-planar as soon as the count exceeds the linear threshold implied by the lemma derived from Euler's formula, followed by the division of the graph into biconnected components justified by the cited fact that a graph is planar exactly when all its biconnected components are, with the core test applied per component; together with the final timing lemma, whose argument observes that because the algorithm stops when the edge count exceeds that threshold, each of the counting, searching, sorting, and embedding phases costs time linear in the vertex count alone.
