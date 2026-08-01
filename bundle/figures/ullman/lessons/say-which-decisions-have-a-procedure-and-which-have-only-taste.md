---
type: lesson
title: "Say which decisions have a procedure and which have only taste"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability, primitive-count]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Say which decisions have a procedure and which have only taste

**Lesson:** Any substantial design contains two populations of decisions that feel alike from the inside and behave nothing alike. One population has been handed to a procedure: there is an algorithm that takes the inputs and returns the choice, and the choice will be as good as the algorithm is. The other population has no procedure at all. It is settled by accumulated experience, by what worked last time, by taste. Writing down which decisions are in which population is a small piece of bookkeeping with a large payoff, and it is skipped almost universally because the taste decisions do not announce themselves — they are made confidently, early, and with the same tone of voice as the ones that were computed.

The payoff is that effort and scepticism can be aimed. Effort should go where there is no procedure, because that is where a person is genuinely deciding and where more thought changes the outcome; the decisions with a procedure will not improve from staring at them. Scepticism should go the same way, because a taste decision presented as settled will otherwise be inherited unexamined through every subsequent version of the system. And the count of taste decisions is itself a design metric: an approach that leaves a dozen of them exposed is worse, at equal performance, than one that leaves three, since each is an independent opportunity for the design to be wrong in a way nobody will catch.

The two populations also demand different treatment of the choices themselves. Where a procedure exists, the interesting artefact is the procedure, and the specific values it produced are derived data that nobody should be reading or copying. Where no procedure exists, the specific values are the artefact, and they should be recorded along with whatever reasoning was available, because the next person has nothing else to go on. Conflating these produces the familiar failure where someone copies a set of computed values into a new context as though they were considered choices, or reargues a considered choice as though it would be recomputed.

The boundary between the populations moves, and watching it move is how a field's practice matures. What is judgement today becomes a rule of thumb once enough people have tried enough variants and reported what happened, and becomes an algorithm once someone can say what is being optimised. Rules of thumb are the interesting middle state: they are real information, cheaply transmitted, and they are also unexplained, so they should be treated as defaults to be departed from with reason rather than as constraints. Recording a rule of thumb as a rule of thumb, rather than promoting it into a principle, is what keeps the eventual explanation possible.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 13's repeated separation of the art of neural-net design from the science of training: the list of decisions that must be made before training begins, covering layer count, node counts per layer and interconnection pattern; the statement that the computational part, choosing the weights, is the part that is science; and the later observation that architecture design remains more art than science though a handful of empirical rules of thumb about depth, filter size, stride and where size reduction should happen have emerged from practice.
