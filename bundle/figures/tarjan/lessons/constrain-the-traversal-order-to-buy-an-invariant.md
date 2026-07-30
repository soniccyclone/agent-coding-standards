---
type: lesson
title: "Constrain the order you explore in and you buy an invariant, not just a search"
figure: tarjan
works: [depth-first-search-and-linear-graph-algorithms]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Constrain the order you explore in and you buy an invariant, not just a search

**Lesson:** Backtracking had been in wide use for years as a way of walking a possibility space, and nobody had bothered to analyze what it guaranteed. Tarjan's move is to stop treating the walk as the interesting object and treat the *choice rule* as the interesting object. Any exploration of a graph eventually crosses every edge; what distinguishes one exploration from another is only how the next step is picked. Commit to the rule that you always continue from the most recently reached place that still has unexplored options, and the residue the walk leaves behind — a tree of the edges that discovered something new, plus everything else — is no longer arbitrary. Every non-discovering edge is forced to point from a vertex back to one of its own ancestors in that tree. Nothing connects two unrelated branches. The rule is proved equivalent to the shape in both directions: any structure with that property is the output of some run of the search. Discipline on order and structural guarantee are the same fact stated two ways.

The reason this matters beyond graphs is that it inverts where the value of a technique lives. An exploration procedure feels like control flow, something you write and run; a structural guarantee is a static object you can quantify over and prove things about. Buying the second with the first is nearly free — the constraint costs a stack — and the return is that every problem downstream gets attacked on the structure rather than on the traversal. The strength of such a technique is measured by what it *forbids*, not by what it visits: here, the forbidden thing is a cross-branch connection, and the two linear-time algorithms in the paper are both built out of that prohibition. A weaker rule that visits the same vertices in a different order forbids nothing and is worth nothing to a proof.

The habit to take away is to look for the ordering freedom you are currently spending at random. Processing order is usually treated as an implementation detail settled by whatever is convenient — a queue was handy, the list came in that sequence. Ask instead what property of the finished state a stricter rule would make impossible to violate, then decide whether that property is the one your later reasoning needs. Names help here too: once the invariant has a name, later work quotes the name instead of re-deriving the traversal, and the layer boundary between "how we walked it" and "what we may now assume" holds.

**Source:** [Depth-First Search and Linear Graph Algorithms](../works/depth-first-search-and-linear-graph-algorithms.md) — the section deriving depth-first search as a specific choice rule over general graph search, and the theorem (with its converse) establishing that the directed structure such a search generates is exactly the class of structures in which every non-tree edge joins a vertex to an ancestor.
