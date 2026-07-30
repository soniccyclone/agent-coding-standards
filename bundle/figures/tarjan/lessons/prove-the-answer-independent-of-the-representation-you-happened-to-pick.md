---
type: lesson
title: "Separate the canonical answer from the representation artifact, then prove the answer indifferent to it"
figure: tarjan
works: [depth-first-search-and-linear-graph-algorithms]
axes: [verifiability]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Separate the canonical answer from the representation artifact, then prove the answer indifferent to it

**Lesson:** Feeding a graph to a program requires choosing how to lay it out, and one graph admits many layouts — every way of ordering the edges around each vertex is a different one. The traversal is sensitive to that choice: a different layout produces a different tree, different numbering, different intermediate values. The property being computed is not sensitive to it at all; the groups a graph decomposes into are a fact about the graph. Tarjan states this explicitly as a proof obligation rather than letting it pass: because the search performed depends on the layout supplied, correctness must be established for *every* layout, not for the one an example happened to use. Which halves of your output are canonical and which are artifacts of encoding is a question worth asking out loud, because the two are usually tangled together in the same run and only one of them is the answer.

Getting this wrong is a common and quiet failure. A procedure validated against a handful of inputs is really validated against a handful of (input, encoding) pairs, and the encodings in a test suite tend to share accidental regularities — insertion order, sortedness, the direction a file was read. A result that silently depends on one of those regularities passes every test and then differs on a machine where a hash iterated differently. The defense is not more examples; it is identifying the degrees of freedom the representation leaves open and arguing the result invariant across all of them. That argument also pays back as a design constraint: if you cannot show indifference to the encoding, either the specification was underdetermined — in which case say so and pick a canonical form deliberately — or the algorithm is reading information out of the encoding that the problem never put there.

The correctness argument itself has a shape worth copying, because it lines up with what the algorithm produces rather than with the algorithm's control flow. Induction runs on the size of the input, and the inductive step uses the algorithm's own decomposition: the first group it emits, and everything left when that group is removed. The claim is that the run on the whole input behaves exactly as the runs on the two pieces would, which is what licenses applying the hypothesis. When a procedure's job is to decompose something, look for a proof organized around the decomposition it emits — it tends to be far shorter than an argument that tracks the procedure step by step, and it forces you to state precisely why the pieces don't interfere.

**Source:** [Depth-First Search and Linear Graph Algorithms](../works/depth-first-search-and-linear-graph-algorithms.md) — the remark that a single graph admits many adjacency structures, one per edge ordering, each producing a different search; the explicit statement opening the biconnectivity correctness theorem that the proof must cover all adjacency structures; and that proof's induction on edge count via the algorithm's own split into the first component emitted and the remainder.
