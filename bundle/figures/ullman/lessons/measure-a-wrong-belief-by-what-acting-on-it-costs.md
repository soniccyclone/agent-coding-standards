---
type: lesson
title: "Measure a wrong belief by what acting on it costs"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Measure a wrong belief by what acting on it costs

**Lesson:** When you need a number for how wrong an estimate is, the tempting route is to write down a formula with the right shape — something non-negative that vanishes when the estimate is right and grows as it drifts — and then defend the formula on grounds of convenience. There is a better route that produces a formula you do not have to defend. Pick a concrete task that consumes the estimate, work out what that task costs when performed on the estimate, and compare it against what the same task would have cost performed on the truth. The gap is the error measure. It arrives already justified, already in units that mean something, and with the property that improving it is guaranteed to improve something a user actually experiences, which no formula chosen for its derivative can promise.

Constructing the measure this way also settles questions that are otherwise argued in the abstract. Symmetry, for instance: a measure derived from a cost is symmetric only if the situation is, and when the two arguments play different roles — one is what is true, the other is what you guessed — there is no reason to expect or want symmetry, and demanding it would mean discarding the derivation that made the measure meaningful. The complaint that such a measure is not a proper distance is then not a defect but a correct report about the asymmetry of the setting.

The construction hands you a second thing, less obvious and more useful: a decomposition. The cost of the task under your estimate splits into the cost that would have been paid even with perfect knowledge and the excess attributable to being wrong. The first part is a property of the problem, fixed before you arrived, and no effort will reduce it. Only the second is yours. This has an immediate consequence for reporting. The total is not readable as a score, because its floor is unknown and problem-dependent, so a total of a given size means nothing in isolation and nothing across two different problems. Only differences in the total, or the excess on its own if you can compute it, are interpretable.

It also has a consequence for optimisation that runs the other way. Since the irreducible part does not move when your estimate moves, minimising the total and minimising the excess are the same problem, and the total is usually the cheaper of the two to compute because it does not require knowing the floor. So the right arrangement is often to optimise the quantity that is not interpretable and report the one that is, which is a perfectly respectable split as long as it is explicit. The confusion to avoid is quoting the optimised quantity as though it were a measure of quality — a habit that produces long arguments about numbers whose baseline nobody has established.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 13's derivation of the classification loss, which introduces the average bits per symbol under an optimal code for the true distribution, asks what the average becomes when the code was designed for a different believed distribution, identifies the shortfall between the two as the divergence, defends the asymmetry on the grounds that one argument is ground truth and the other the model's output, and observes that the entropy term depends only on the input so minimising the divergence and minimising the cross entropy are the same optimisation.
