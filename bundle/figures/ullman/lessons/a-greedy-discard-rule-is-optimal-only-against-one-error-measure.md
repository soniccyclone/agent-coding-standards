---
type: lesson
title: "A greedy discard rule is optimal only against one error measure"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# A greedy discard rule is optimal only against one error measure

**Lesson:** "Throw away the smallest components" is so natural a rule that it usually goes unexamined. It is worth examining, because it is not self-evidently right — it is right relative to a particular way of measuring how wrong the truncated version is, and the connection has to be established rather than assumed. The argument that establishes it has a recognisable shape: show that the total error decomposes into independent per-component contributions, show that each contribution is a monotone function of that component's magnitude alone, and conclude that discarding the smallest ones minimises the total under a fixed budget of survivors. Each of those steps is a real condition, and each can fail.

Where it fails is instructive. If the error measure penalises the largest single deviation rather than the aggregate, the components do not contribute independently and the smallest-first rule loses its justification. If components interact — if dropping one changes what another contributes — the decomposition step fails outright. And if the consumer cares about something other than aggregate reconstruction error, such as preserving the ordering between a few particular entries, then a component with small magnitude can be the one carrying the distinction that matters, and dropping it is precisely wrong while being optimal by the stated criterion. The criterion is doing the work, and it should be named before the rule is adopted.

The same reasoning applies to the companion question of how many components to keep, where the honest answer is that the data does not contain one. What the decomposition provides is an accounting: each component's share of the total, sorted. A rule such as "retain enough to account for most of the total" converts an unanswerable modelling question into a budget on a measurable quantity, which is a genuine improvement in that it is explicit and comparable across datasets — but it is a convention, not a discovery, and the threshold in it is a judgement about how much distortion the downstream use tolerates. Presenting it as though the data chose it is the mistake.

The practical residue: whenever you truncate, compress, prune, or sample by discarding the least of something, write down what error you are minimising and check that your discard order actually minimises it. It usually does. When it does not, you find out at design time rather than from a user reporting that the one thing they cared about disappeared.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the section on why zeroing low singular values works in the dimensionality-reduction chapter, which reduces the Frobenius norm of a decomposed matrix to the sum of squares of its diagonal factor by exploiting orthonormality, concludes that the error of a truncation equals the sum of squares of the discarded values and is therefore minimised by discarding the smallest, together with the accompanying rule-of-thumb box on retaining ninety percent of the energy.
