---
type: lesson
title: "State what you want and surrender the plan"
figure: stonebraker
works: [what-goes-around-comes-around]
axes: [expressiveness, cognitive-load, parallelizability]
subdomains: [databases-and-data-management, programming-languages-and-semantics]
tags: [lesson]
---
# State what you want and surrender the plan

When an interface hands back one item at a time, the caller is forced to author the strategy: which entry point to start from, which path to follow, when to stop. That authorship looks like control and is actually a tax, because the right strategy depends on facts the caller cannot see — how many records there are, how they are distributed, what indexes exist today — and those facts change under the program without notifying it. The survey's illustration is that two hand-written traversals answering the same question invert in cost depending on the population of the data, so the programmer is not choosing between a good and a bad algorithm but gambling on statistics they were never given.

The move that resolves this is to raise the interface until the request describes the desired result and contains no procedure at all. Then a planner that can read the current statistics chooses the strategy on every execution, and the strategy is free to change as the data changes. The empirical claim the survey defends is stronger than "this is more convenient": an automatic planner beats all but the very best hand optimizers, which means giving up manual control is usually a performance *win*, not a performance concession made for the sake of tidiness. It is also the enabling condition for anything else the engine wants to do behind the request — parallelize it, reorder it, rewrite it against a different physical layout — none of which is legal when the request is a recipe.

This principle generalizes well past query languages, and the way to apply it is to notice where your API is asking the caller to encode a plan. Any interface where the caller loops, positions a cursor, or chains steps has moved optimization into the least informed place in the system. A programmer who believes this designs for a declarative boundary even at the cost of building a planner, because the planner is written once and improves for every caller, while hand-tuned traversals are written many times and rot individually.

**Source:** [What Goes Around Comes Around](../works/what-goes-around-comes-around.md) — from the survey's comparison of record-at-a-time navigation in the pre-relational languages against set-at-a-time languages, and its lesson about optimizers versus hand-written access strategies.
