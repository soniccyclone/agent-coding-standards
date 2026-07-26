---
type: lesson
title: "Knowing what will be needed is not permission to fetch it early"
figure: denning
works: [the-working-set-model-for-program-behavior]
axes: [hardware-affinity]
subdomains: [operating-systems-and-systems-programming]
tags: [lesson]
---
# Knowing what will be needed is not permission to fetch it early

**Lesson:** Having built a model that names precisely the set of information a program is using, the obvious next move is to load that set in advance instead of waiting for faults. Denning declines, and the reason is worth more than the conclusion. The moment when preloading is convenient — when a suspended unit of work becomes runnable again — is precisely the moment its needs are most likely to have changed. A program that paused to interact with the outside world resumes into a different phase of its own structure; the set it favored before the pause is a poor description of the set it will favor after. The trigger for the speculation is correlated with the event that invalidates it.

So the question to ask about any eager fetch is not "how accurate is my prediction on average." It is two other questions: is my trigger independent of whatever makes the prediction stale, and what does a wasted fetch cost me. Where the trigger is anti-correlated with prediction validity and the wasted transfer is expensive in the same currency as the miss it was meant to avoid, waiting for actual demand is the cheaper policy even when you hold an excellent model. Average-case accuracy is the wrong statistic; the conditional accuracy at the instant you would act is the right one.

The same section carries a smaller lesson with wide reach. Once speculation is off the table, the policy no longer needs the membership of the set at all — only its size. The size answers the question that actually gets asked ("is there room for this?"), while the membership would only have been needed for the prefetching he has just rejected. Asking what a decision actually consumes, rather than assembling everything you could know about the subject, often reveals that a scalar is sufficient and the full structure was work you never had to spend.

Concretely, this changes how prefetching, cache warming, connection pre-establishment, and eager initialization get evaluated: by trigger correlation and waste cost, not by hit-rate optimism. And it changes what you instrument — collect the quantity the decision consumes, at the resolution the decision needs, and stop.

**Source:** [The Working Set Model for Program Behavior](../works/the-working-set-model-for-program-behavior.md) — the argument against anticipatory page loading, including the observation that blocking for interaction signals an imminent change of favored pages, and the following passage establishing that working-set size alone suffices for memory allocation.
