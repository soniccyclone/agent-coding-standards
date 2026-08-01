---
type: lesson
title: "A later stage's statistic only describes what earlier stages let through"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A later stage's statistic only describes what earlier stages let through

**Lesson:** Build a cascade in which each stage both filters and measures, and a plausible simplification presents itself almost immediately: since stage two only ever saw the items stage one approved, anything stage two approves must already have passed stage one, so the final admission check can drop the stage-one condition and test only the most recent one. The reasoning has a satisfying economy to it and it is wrong, in a way that is worth understanding precisely rather than just memorising, because the same shape appears in caches, in access control, in progressive validation, and in any pipeline where a downstream summary is built from an upstream-filtered population.

The error is a confusion between two different questions. "Did this candidate pass stage two?" is a question about the candidate. "Is the bucket, or the group, or the aggregate that this candidate belongs to above threshold at stage two?" is a question about a population, and stage two's verdict is a property of the population, not of any individual in it. A candidate that stage one rejected was never fed into stage two, so it contributed nothing to any stage-two aggregate — but it still *has* a stage-two aggregate, the one belonging to whatever group it would have joined, and that aggregate can easily be above threshold on the strength of entirely different members. Evaluating the candidate against stage two after the fact therefore produces a pass, with nothing anywhere in the system recording that stage one had already said no. The pipeline silently readmits what it had correctly excluded.

The general statement is that a filter's decision is only recoverable from later state if the later state was keyed by individual, and aggregate filters are not. Any stage that summarises groups rather than marking members destroys the identity of what it rejected, and once identity is gone there is no reconstruction from downstream evidence. Practically this means every condition a cascade imposes has to be carried forward and rechecked at the point of final admission, all of them, in full — the conditions are conjunctive and none of them implies any other. The cost is the retained state, which is precisely why people try to eliminate it, and it is the price of the cascade rather than an overhead you can optimise away.

The failure mode this produces is quiet. Nothing crashes, results are not obviously wrong, and the extra admissions look exactly like legitimate ones; the system merely does more work than its design promised and, if the stages were also functioning as correctness constraints rather than only as performance filters, admits things that violate a rule nobody can see being violated. The defence is a habit: when you are about to argue that one check subsumes another, state explicitly what population each check was computed over. If those populations differ, the subsumption is false regardless of how the ordering feels.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 6's boxed warning about a subtle error in the Multistage algorithm, which describes implementations dropping the first hash table's condition on the counting pass, on the false reasoning that an unhashed pair could not have affected a second-pass bucket, and points out that such a pair may still hash to a frequent second-pass bucket, so all conditions must be checked together.
