---
type: lesson
title: "Let satisfied cases stop pulling"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, hardware-affinity]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Let satisfied cases stop pulling

**Lesson:** When a solution is fitted to many pieces of evidence, the shape of the penalty attached to each piece decides which pieces matter. A penalty that keeps decreasing as a case gets better and better means every case, however comfortably handled, keeps exerting force on the answer — so the answer is pulled around by the mass of easy cases, and adding more easy cases moves it further. A penalty that drops to exactly zero once a case is handled with the required clearance, and grows only for cases that fall short, produces something qualitatively different: cases that are comfortably right contribute nothing at all, and the solution is determined entirely by the ones near the boundary.

That is a large structural consequence dressed as a small choice of function. It means the answer depends on a small, identifiable subset of the evidence — the marginal cases — and that the rest could be deleted without changing it. Which in turn means you can summarise or discard the bulk, that adding more of the easy kind changes nothing, and that the solution is stable against wholesale shifts in the population as long as the boundary region is unchanged. The same property is the warning: the answer is highly sensitive to a handful of cases, so a single mislabelled or corrupted marginal case has influence out of all proportion to its share of the data.

The usual objection to such a penalty is that it is not smooth — it has a kink where it reaches zero, so the slope is undefined at exactly that point. In practice this is a non-issue and worth understanding why: the slope is defined everywhere else, exactly one of two simple expressions applies depending on which side you are on, and gradient-following methods need only a direction, not a derivative that exists everywhere. Rejecting a well-shaped penalty because it is not differentiable at one point trades a real structural benefit for a theoretical tidiness that the algorithm does not require.

The general recognition is that penalty shape is where you encode "when is this good enough." A penalty with no zero region says nothing is ever good enough, which is a strong claim and rarely the one intended. Giving the penalty a flat region says explicitly what suffices, and everything that suffices then stops competing for your attention — in the objective, and in the running time.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the hinge-loss discussion in the support-vector-machine sections, where the penalty is zero once an example is on the correct side by at least the required margin and rises linearly as it falls short, the derivative is given as a two-case expression that is zero for satisfied examples, and the points at the margin are identified as the support vectors that actually constrain the dividing hyperplane.
