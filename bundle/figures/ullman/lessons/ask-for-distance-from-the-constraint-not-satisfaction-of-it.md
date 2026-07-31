---
type: lesson
title: "Ask for distance from the constraint, not satisfaction of it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Ask for distance from the constraint, not satisfaction of it

**Lesson:** A search that halts as soon as its constraints are satisfied returns a solution sitting right against the constraint surface, because that is where the search first arrived. Every requirement is met and every one of them is met by nothing — which is fine if the requirements are exact and permanent, and wrong whenever they are a sample of a larger set you will be judged against later. The solution has been fitted to the evidence's boundary, so any new case falling marginally outside that boundary is handled incorrectly, and marginal cases are exactly the ones that keep arriving.

The correction is to stop asking whether the constraints hold and start asking by how much. Replace "find something feasible" with "find the feasible thing that is furthest from infeasible," and the arbitrary answer becomes a determinate one. Two useful properties come with the change. The solution stops depending on incidental details of the search — the order the evidence arrived in, the starting point — because the objective now has a unique optimum rather than a large plateau of acceptable answers. And the solution acquires a stated tolerance: it is not merely correct on what you tested, it is correct with a specific amount of room, which is a claim about how much the world can move before it breaks.

Real evidence is usually contradictory, so the strict version must be softened, and how it is softened is itself a design decision. Rather than a binary of satisfied or violated, score each case by how far it falls short of the required clearance — outright violations penalised heavily, cases that are technically correct but uncomfortably close penalised proportionally less. That produces a smooth objective you can actually optimise, and it encodes the belief that a barely correct case is nearly as worrying as a wrong one. The trade-off between total shortfall and the amount of clearance demanded needs an explicit constant: turn it one way and you tolerate no mistakes on the evidence at hand while leaving almost no room; turn it the other way and you accept some mistakes in exchange for generous room on everything else. That constant is a statement about how much you trust your evidence to represent the world.

Read generally, this is the difference between a specification met and a specification met with margin, and it applies well beyond classifiers — to capacity planning, timing budgets, thresholds of every kind. Whenever a search terminates on a predicate, ask what the corresponding quantity is, and whether you would rather maximise it.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the problems-with-perceptrons section, which notes that training stops as soon as no point is misclassified so the resulting boundary just barely accommodates the last examples and is biased toward one class, together with the support-vector-machine sections that instead maximise the margin, and the soft-margin objective which penalises misclassified points and correctly classified points that are too close, traded against the margin by an explicit regularisation constant.
