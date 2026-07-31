---
type: lesson
title: "Spend from the deepest reserve, so the future still has someone who can serve it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [parallelizability, cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
tags: [lesson]
---
# Spend from the deepest reserve, so the future still has someone who can serve it

**Lesson:** When requests arrive one at a time and each must be assigned to some provider that holds a finite budget, the obvious rule is to pick whichever provider scores best on this request. That rule systematically destroys capacity it did not have to destroy. The providers that score well tend to be the ones that also cover a wide range of future requests, so serving the current request from them drains exactly the reserve that would have absorbed requests nobody else can handle. The narrow provider, which can only ever be used for a small slice of the stream, sits full while the general-purpose one empties, and when the slice arrives there is nothing left to serve it. Nothing about this is visible at the moment of the decision; each individual choice looks locally correct.

The corrective rule is to weight the decision by how much reserve each candidate still holds and to prefer the fullest. It reads as perverse — you are deliberately declining the candidate that looks best — but it is buying an option. Depleting the deepest reserve leaves the maximum number of viable options for whatever arrives next, and it keeps every provider alive rather than exhausting them in order of usefulness. In allocation problems of this shape the improvement is not marginal: it moves the guaranteed fraction of what an omniscient allocator could have achieved substantially upward, and it does so with a rule that is no more expensive to evaluate than the naive one.

Two details decide whether the rule works in practice. Remaining capacity must be expressed as a fraction of each provider's own budget rather than as an absolute quantity, because absolute remainders are not comparable across providers of different sizes and comparing them lets a large, useless provider dominate a small, valuable one forever. And the preference must be graded rather than absolute: rather than always choosing the fullest, discount each candidate's value by a smooth function of how depleted it is, so a much more valuable candidate can still win while a nearly-exhausted one is progressively demoted without ever being categorically excluded.

The pattern recurs anywhere finite per-party allowances meet an unpredictable stream — rate-limit budgets, connection pools, retry allowances, spare capacity across replicas, on-call rotation. The general instruction is to make preserving future feasibility an explicit term in the objective, rather than trusting that a sequence of locally optimal choices adds up to a globally sensible allocation. It does not.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the advertising chapter's Balance algorithm and its analysis, where assigning to the bidder with the largest remaining budget raises the guaranteed fraction over the naive highest-bidder rule, and the generalisation that switches to fractional remaining budget with a smooth discount to handle unequal bids and budgets.
