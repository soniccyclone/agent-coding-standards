---
type: lesson
title: "Design the search so every step permanently retires part of the input, and the cost bound becomes a census instead of a trace"
figure: karp
works: [an-n-5-2-algorithm-for-maximum-matchings-in-bipartite-graphs]
axes: [verifiability, cognitive-load, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Design the search so every step permanently retires part of the input, and the cost bound becomes a census instead of a trace

**Lesson:** The hard half of Hopcroft and Karp's result is not the claim that the work divides into few passes, it is making one pass cost no more than looking at the data once. Their traversal achieves this by a single structural commitment: whenever it examines a connection, that examination settles the connection's fate forever. Either the connection joins the route currently being built, or no acceptable route can ever use it — and in both cases it is removed from consideration and never revisited. The same holds for the vertices on the working stack, which are never re-entered after being abandoned. Because every unit of work consumes a distinct, non-renewable item, the total cost cannot exceed the number of items, whatever the control flow does in between.

That is a different species of reasoning about cost than programmers usually reach for. The instinctive way to estimate a traversal's expense is to trace the execution: how deep can the recursion go, how many times might the outer loop reset, what happens when a partial route fails and the search backs up. That kind of reasoning is fragile, hard to complete honestly, and it is exactly what produces confident wrong answers about backtracking code, which can look like it visits a few things while actually revisiting them combinatorially. The alternative is to stop analyzing the execution and instead find a decreasing supply — a stock of items that only ever shrinks and that every step must draw from. Then the cost bound is arithmetic on the size of the input, and it holds no matter how convoluted the path through the code becomes.

The claim only works if the retirement is genuinely irrevocable, and that is a design obligation rather than an observation about code you already wrote. It requires arranging the problem so that a local failure carries global information: here, the search is run on a structure prepared in advance so that the only routes worth finding are the ones the traversal will consider, which is what licenses the conclusion that a rejected connection is permanently useless rather than merely unhelpful right now. Retrofitting this onto an existing search almost never works, because most searches abandon options for reasons that are true only of the current attempt.

A programmer who has internalized this asks a specific question of any expensive search, cache, retry loop, or reconciliation pass: what does each step use up, and can it come back? If nothing is consumed, there is no bound and the code is one adversarial input away from running far longer than anyone believes. If something is consumed but can be replenished — a marked node that gets unmarked, a cleared flag that gets set again — the bound is the number of replenishments, not the number of items, and that number is usually the thing nobody has thought about. Making the consumption permanent is often a small change to the data structures and turns an unbounded-in-principle procedure into one whose worst case you can state without simulating it.

**Source:** [An n^5/2 Algorithm for Maximum Matchings in Bipartite Graphs](../works/an-n-5-2-algorithm-for-maximum-matchings-in-bipartite-graphs.md) — the third section's depth-first procedure for extracting a maximal disjoint family of routes from the prepared layered structure, together with the closing cost argument that counts deletions and stack removals rather than following the search's execution.
