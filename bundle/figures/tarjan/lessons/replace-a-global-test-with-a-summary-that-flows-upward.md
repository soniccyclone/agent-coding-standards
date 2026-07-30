---
type: lesson
title: "Replace a global test with a per-node summary that flows upward"
figure: tarjan
works: [depth-first-search-and-linear-graph-algorithms]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Replace a global test with a per-node summary that flows upward

**Lesson:** Some properties are stated as global operations. Asking whether a particular vertex is the one holding a graph together is literally a question about what happens to reachability *between every other pair* once that vertex is gone. Taken at face value the definition dictates the algorithm: remove a candidate, re-test connectivity, repeat for every candidate, and pay the product of the two sizes. The prior art did exactly that. Tarjan's alternative is to find a single number attached to each vertex that (a) can be computed from the numbers already computed for its children plus the edges leaving it, and (b) makes the global property a comparison between a child's number and its parent's. The quantity here is how far back toward the root you can still get from inside a subtree using one shortcut edge. If you can't get back past the parent, the parent is the only way out, and that *is* the global property, decided locally.

Two conditions make the trick work, and both are worth naming because you have to check them deliberately. The summary must be *compositional* over the structure the traversal built — a parent's value is a minimum over its children's values and its own outgoing shortcuts, so the whole array is filled in on the way back up a single walk, with no second pass and no lookahead. And the summary must be *sufficient*: the local comparison has to be proved equivalent to the global definition in both directions, or you have a heuristic that happens to agree on your examples. The paper does that proof, and the converse half is the load-bearing one, since it rules out the possibility that some vertex holds the graph together for a reason the number cannot see.

Generalized, this is the standard escape from quadratic re-derivation, and it applies far past graph theory: propagating type information up a syntax tree, summarizing what a subtree of a module graph transitively imports, computing which regions of a dataflow graph can be reordered. When you catch yourself planning to iterate over candidates and re-run an expensive whole-system check on each one, the productive question is not how to make the check faster. It is what finite summary each part could carry that makes its neighbors' answers derivable from it, and whether that summary is provably equivalent to the thing you actually wanted to know.

**Source:** [Depth-First Search and Linear Graph Algorithms](../works/depth-first-search-and-linear-graph-algorithms.md) — the biconnectivity section, where the prior approach of testing each vertex in turn is contrasted with defining a lowest-reachable-vertex value per vertex, proving the articulation-point property equivalent to a local comparison on that value (with its converse), and observing that the values satisfy a recurrence computable during a single search.
