---
type: lesson
title: "Hoist one kind of operation to the front and re-encode the interleaving as a constraint"
figure: tarjan
works: [efficiency-of-a-good-but-not-linear-set-union-algorithm]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Hoist one kind of operation to the front and re-encode the interleaving as a constraint

**Lesson:** What makes this cost analysis hard is not either operation but their interleaving. Queries walk a structure whose shape depends on which merges have already happened, and merges land on a structure whose shape depends on which queries have already flattened parts of it. Reasoning about the cost of the tenth query requires knowing the state, and the state is the accumulated history. Tarjan's reframing removes the interleaving entirely: imagine all the merges performed first, yielding one fixed final structure, and then re-express every original query as a walk in *that* structure — but truncated, stopping at the highest point that had actually been merged in by the time the query originally ran. The chronology has not been discarded; it has been converted from a property of the process into a per-query bound on how far up the fixed structure the walk may go. What was a moving target becomes a static object plus a side condition, and only then does the counting argument become available.

The technique generalizes to any analysis of a system where two kinds of event mutate and observe shared state. Reasoning about interleavings directly means reasoning about a combinatorially large set of histories. Reasoning about the final state means reasoning about one object. If you can hoist the mutations, describe the terminal structure they produce, and then re-express each observation as a restricted view of that structure — restricted by exactly the ordering information you gave up — you have traded a dynamic problem for a static one at no loss of generality. That exchange is worth looking for on purpose, and its two halves have to be done together: hoisting without recovering the ordering constraint proves something about a different, easier problem, which is the way this move goes wrong.

The same pattern shows up whenever it is easier to reason about a finished artifact than an evolving one. Analyzing what a build produces rather than the order in which it produced it; reasoning about the eventual contents of a replicated store plus a happens-before restriction on what each reader could have seen; verifying a migration by its end state plus a constraint on which intermediate states were observable. In each case the trick is not simplification by approximation — nothing is dropped — it is finding the reformulation in which the difficult dimension appears as data rather than as sequencing. A good sign you have found it: quantities that were previously only definable relative to a moment in time become plain functions of the fixed structure, and the argument can then treat them as such.

**Source:** [Efficiency of a Good But Not Linear Set Union Algorithm](../works/efficiency-of-a-good-but-not-linear-set-union-algorithm.md) — the opening of the upper-bound section, which proposes thinking about the algorithm by performing all the unions first to obtain a single final tree and reinterpreting each original find as a partial find in that tree, bounded by the furthest ancestor whose union preceded that find in the original sequence, and the subsequent analysis conducted entirely on the fixed tree.
