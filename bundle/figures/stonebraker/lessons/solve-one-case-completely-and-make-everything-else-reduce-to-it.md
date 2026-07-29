---
type: lesson
title: "Solve one case completely and make everything else reduce to it"
figure: stonebraker
works: [the-design-and-implementation-of-ingres]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Solve one case completely and make everything else reduce to it

Faced with requests that may reference any number of interrelated collections at once, the tempting design is a general engine that handles the general case. The alternative is to pick the narrowest case you can execute really well — one collection, one set of conditions, one pass — build a single component that does only that, and then make the entire remaining problem a matter of rewriting arbitrary requests into sequences of that one case. Everything hard moves into the reduction, and the reduction is a rewriting problem rather than an execution problem, which is a much better place to have your difficulty concentrated.

This pays off in ways that a general engine does not. The narrow solver is small enough to optimize aggressively, because it has only a handful of situations to distinguish and can rank them by expected cost. The reduction layer, freed from any execution concern, can spend real effort on the choices that matter — which reference to eliminate first, which intermediate result to build, how to organize an intermediate so the next round of the narrow case runs against a favorable layout. It can even undo its own earlier guesses when new information arrives, reorganizing a temporary it created a moment ago, because reorganizing costs one pass while a badly organized inner loop costs one pass per iteration. And when the reduction terminates in a case the solver handles by construction, correctness of the whole rests on correctness of a component you can hold in your head.

The discipline is to identify the case whose solution you actually trust before designing anything above it, and to insist that every other case be a rewriting into it rather than a new branch inside it. A programmer who works this way ends up with two artifacts of very different character — an execution kernel that is boring and fast, and a planning layer that is where all the cleverness and all the future improvement live — and can improve either one without touching the other. The failure this prevents is the general engine that grows a special case per workload until nobody can predict what it will do, because there is no longer any single case to reason from.

**Source:** [The Design and Implementation of INGRES](../works/the-design-and-implementation-of-ingres.md) — the decomposition process described in the query-processing section, which reduces multi-variable requests to one-variable requests by detachment and substitution and hands each resulting single-variable request to a dedicated processor.
