---
type: lesson
title: "A simple strategy is valid because of a structural property, not because the problem resembles one it worked on, so name the property before reusing it"
figure: edmonds
works: [optimum-branchings]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A simple strategy is valid because of a structural property, not because the problem resembles one it worked on, so name the property before reusing it

**Lesson:** Edmonds sets up the branching problem by first describing its near neighbour. Drop one condition and you have the spanning-tree problem, for which the crude strategy of repeatedly grabbing the heaviest element that keeps the partial answer admissible is both cheap and correct. Restore the condition — each selected edge must point at a distinct node — and the same strategy is no longer correct. The change to the problem statement is a single clause. The change to the strategy's validity is total, and he shows it with a worked example whose greedy answer is measurably worse than the optimum. The lesson is not that greed is unreliable; it is that greed's correctness was never a property of greed. It was a property of the family of admissible sets, and he points at the abstract characterization of exactly which families admit it under every weighting.

This reframes what "similar problem" means. Surface similarity — same objects, almost the same constraint, obviously the same shape of answer — carries no information about which techniques transfer. What transfers is whatever the technique's correctness proof actually used, so the reusable artifact is the property, not the code. Before applying a known method to a new problem, the work is to recover the proof obligation the method imposes and check it, which is usually much faster than discovering by benchmark that the answers are subtly worse than optimal.

The paper supplies a second, sharper demonstration in its worked examples, and it is the kind of thing that would pass code review unnoticed. Adding a constant to every weight leaves the best spanning arborescence unchanged, because every candidate has the same number of edges and so absorbs the shift identically. Apply the same shift when the answer is allowed to have fewer edges and the optimum changes completely, even though all the weights in the original answer stayed positive and even though that answer is still the best arborescence. An invariance that holds for one formulation fails for its close relative for a reason visible only in the proof. Assume invariances at your peril; the cheap ones to check are exactly the ones people skip.

**Source:** [Optimum Branchings](../works/optimum-branchings.md) — the section contrasting the spanning-tree problem with the branching problem and noting that the bucket-filling strategy is valid for one and not the other, with the abstract characterization of admissible families cited to a companion paper; and the closing discussion of the figures, where a uniform shift of all weights preserves the optimum arborescence but produces two entirely different optimum branchings.
