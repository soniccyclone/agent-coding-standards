---
type: lesson
title: "Put the effort-saving tricks in a layer where they cannot change which answers are found"
figure: floyd
works: [nondeterministic-algorithms]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Put the effort-saving tricks in a layer where they cannot change which answers are found

**Lesson:** Most of what makes a search program fast is knowledge about the problem that has nothing to do with what the problem *is*: this partial arrangement can never be completed, that direction is a dead end, this branch already costs more than the best result so far. In hand-written search code such knowledge gets tangled into the traversal machinery, where every added shortcut is also a chance to lose a solution, and where nobody can tell by inspection whether the pruning changed the answer or merely the runtime. Separate the statement of what counts as a solution from the effort spent avoiding hopeless work, and pruning becomes an additive, local act: a test whose failing branch leads to rejection, inserted at a point in the specification, removed just as easily.

The property that earns this is that a prune is expressed in the same vocabulary as the acceptance condition rather than in the vocabulary of the traversal. Adding a reachability test to a cycle search does not touch any stack, any restore step, or any ordering; it narrows the set of partial states worth extending, and it is checkable on its own terms against the problem's definition. Because the transformation down to real machinery is uniform, the corresponding change in the executable version is equally local. Knowledge about the domain accumulates in the layer that is easy to reason about, and the layer that is tedious and error-prone stays untouched.

The second half of the lesson is that whether a given prune pays is an empirical question about the inputs, not a property of the prune. A test that eliminates enormous swathes of a graph rich in dead ends and one-way streets may, on a differently shaped graph, do nothing but consume time on every step. This is exactly why the prune should be a thing you can add and drop cheaply: the decision is instance-dependent and must be settled by measurement, so the design should make the experiment cheap rather than make the guess permanent. Deliberate leaks are admissible on the same footing — letting the best cost found so far survive across otherwise independent attempts is what turns an exhaustive search into a bounded one — but a leak is a considered exception to the isolation, which is only meaningful because the isolation was the default.

A programmer holding this distinction refuses to accept "it got faster" as evidence of anything until it is clear that the change could not have altered the result. The reflex is to ask which layer an optimization lives in: one that constrains what is looked for, or one that reorganizes how the looking is done. The two are debugged differently, and code that mixes them yields performance improvements nobody can safely revert.

**Source:** [Nondeterministic Algorithms](../works/nondeterministic-algorithms.md) — the discussion of making a search more selective by inserting tests that branch to failure, the note that such tests may pay handsomely on some networks and merely cost time on others, that they are inserted and removed by local changes to both versions, and the proposed assignment form whose effect deliberately survives backtracking so a running minimum cost can prune later attempts.
