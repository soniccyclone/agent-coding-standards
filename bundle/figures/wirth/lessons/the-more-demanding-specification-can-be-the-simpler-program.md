---
type: lesson
title: "The more demanding specification can be the simpler program"
figure: wirth
works: [algorithms-and-data-structures]
axes: [cognitive-load, expressiveness, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# The more demanding specification can be the simpler program

**Lesson:** Asking for less is not reliably cheaper to build, and when a program is fighting you it is worth testing the opposite direction: what would it look like if it produced everything rather than the first acceptable answer? The case where this pays is easy to recognize once you have seen it. A search that must stop at the first success has to know, at every level, whether the levels below it succeeded; that knowledge has to be reported upward, so every step acquires a result to return, the loop that tries alternatives acquires a compound termination condition combining exhaustion with success, and each step's undo has to be conditional on the outcome. A search that must report every success needs none of that. It visits each candidate, records, descends, unrecords, and moves on unconditionally; there is nothing to report because there is nothing to decide. The whole success-propagation apparatus was overhead imposed by the weaker specification, not by the problem.

What makes the exhaustive version correct is a property the first-answer version also needed but could leave implicit: candidates must be generated systematically enough that no candidate is produced twice and none is skipped, which is the same as saying the space of partial solutions is walked with each node visited exactly once. Once that property is established, continuing after a success is simply the next step of the walk, and the ability to stop early was never carrying the argument. Establishing the systematic-generation property explicitly is therefore the real work, and it is worth doing whichever version you end up shipping.

Two extensions follow cheaply from the simpler version and would have been painful additions to the other. Selecting an optimal solution is the exhaustive program with the recording step replaced by a comparison against the best seen so far. And once a bound on what is still achievable is available, the search regains its ability to stop — not at the first answer, but at every branch that provably cannot beat the current best — which restores the pruning without restoring the plumbing. The general habit: when a program's complexity seems to be concentrated in reporting, deciding and unwinding rather than in the problem, suspect that the specification asked for a special case, and check what the general case costs. Sometimes it costs less.

**Source:** [Algorithms and Data Structures](../works/algorithms-and-data-structures.md) — section 3.5's extension of the eight queens program from finding one solution to finding all of them, where the success-reporting function is folded into the loop body, the Boolean result becomes unnecessary, and the text records the surprise that the search for all solutions is realized by a simpler program than the search for a single one, together with the accompanying requirement that candidate generation be systematic so that every node of the candidate tree is visited exactly once; and section 3.7, where the same schema is extended to optimal selection by replacing the recording step with a comparison and adding an acceptability test based on the still-achievable value, described as a branch and bound algorithm.
