---
type: work
title: "Using Branching Time Temporal Logic to Synthesize Synchronization Skeletons"
figure: emerson
description: The expanded journal treatment of the 1981 workshop paper, working out the model-checking algorithm for branching-time (CTL) formulas over finite-state programs in full detail, including its complexity and worked examples of synthesizing correct synchronization skeletons directly from a temporal-logic specification. Functions as the fuller technical reference for the same founding model-checking idea, aimed at a broader readership than the earlier workshop version. Cited alongside the 1981 paper as the canonical original source for algorithmic (as opposed to deductive) verification of concurrent programs.
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
year: 1982
url: https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/UsingBranchingTimeTemporalLogicToSynthesizeSynchronizationSkeletons.pdf
access: public
host: self-archived
tags: [work]
---

# Using Branching Time Temporal Logic to Synthesize Synchronization Skeletons

**Author(s):** with Edmund M. Clarke
**Venue/year:** Science of Computer Programming 2(3), 1982, pp. 241-266.
**Source:** https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/UsingBranchingTimeTemporalLogicToSynthesizeSynchronizationSkeletons.pdf — self-archived PDF on co-author Edmund Clarke's own CMU faculty page, live and directly downloadable (HTTP 200). Previously flagged `uncertain`; resolved.

## Lessons
- [Requirements can contradict each other, so make the contradiction detectable before implementation](../lessons/an-impossible-specification-is-a-result-worth-having-early.md)
- [What you call the specification is the small part; the bulk of it is structure you assumed from a diagram](../lessons/most-of-your-specification-is-the-part-you-never-wrote-down.md)
- [Specify what must remain possible, or a generator will hand you the least capable thing that qualifies](../lessons/demand-possibility-or-be-handed-the-least-capable-thing.md)
- [Treat global behavior as primary and each component as a projection of it; shared state is the price of projecting](../lessons/local-processes-are-projections-of-a-global-behavior.md)
- [Pick the abstraction from the property you intend to check, then own the claim that it is faithful](../lessons/the-abstraction-you-check-is-a-claim-about-the-real-artifact.md)
