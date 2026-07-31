---
type: lesson
title: "Your move set, not your objective, decides what you can reach"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Your move set, not your objective, decides what you can reach

**Lesson:** An iterative improvement procedure is usually described by its objective — what it is trying to maximise — and evaluated by how good its answer scores. But the objective is not what determines the outcome. What determines the outcome is the set of edits the procedure is allowed to make from its current position, because that set defines which configurations are neighbours, and therefore which configurations count as locally optimal. Change nothing but the move set and the same objective on the same data terminates somewhere entirely different. Two implementations can agree on every stated design decision and disagree on the answer, with the disagreement traceable to a choice nobody wrote down.

The practical grip this gives you is that a stuck search is often a move-set problem rather than an objective problem or a tuning problem. If every allowed edit is a single small change — add one element, remove one element — then any configuration that would need two coordinated changes to improve is a terminal state, and no amount of restarting or annealing will get you across a gap that requires a move you do not have. Adding a compound move that performs the coordinated change atomically, merging two groups or splitting one, does not make the objective better; it makes previously unreachable regions reachable, which is usually the larger effect.

The same reasoning applies to quantities you thought were fixed before the search began. If the size of the model — how many groups, how many factors, how many partitions — is a constant chosen in advance, then you are optimising within a slice and cannot know whether a neighbouring slice is better. Promoting that constant to something the search can adjust, by trying one more and one fewer and moving in whichever direction improves, folds a hyperparameter into the search rather than leaving it as an assumption. That is the same move as adding a compound edit: enlarging the space of things a step is permitted to change.

None of this yields a global optimum, and the honest framing is that local search returns the best configuration reachable from where it started under the moves it was given. Both of those qualifiers deserve to be reported alongside the result. Random restarts address the first. Only an expanded move set addresses the second, and knowing which of the two is limiting you is the difference between a productive fix and more restarts.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the discrete-optimisation section of the overlapping-communities chapter: hill-climbing on community membership using single insertions and deletions, the explicit warning that the reachable assignment may be far from the globally best one because only those simple changes are allowed, the suggestion to repeat from many random starting assignments, and the extension of the move set to merging communities, adding a community, or hill-climbing on the number of communities itself.
