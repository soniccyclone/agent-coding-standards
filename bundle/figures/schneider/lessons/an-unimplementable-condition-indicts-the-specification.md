---
type: lesson
title: "When a technique cannot express a requirement, suspect the requirement: use the failure as a probe"
figure: schneider
works: [synchronization-in-distributed-programs]
axes: [verifiability, expressiveness]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# When a technique cannot express a requirement, suspect the requirement: use the failure as a probe

Running into a wall while implementing something is normally read as a fact about the implementer: not clever enough, wrong technique, try again. But if the technique you are using is confined to a well-characterized class — say, decision rules that no later information can falsify — then failing to express a requirement inside that class is a *measurement*. It says the requirement lies outside the class, and if the class was chosen to be exactly the timing-independent decisions, the requirement is timing-dependent. That may be news to the person who wrote it.

The classic shape is a requirement that reads innocently and hides an impossibility. "Do this only while that other participant is in a particular state" mentions no clocks, no delays, no timeouts. It sounds like a constraint on states. But no participant can know another's *current* state in a system without shared memory — anything it learns is a report about the past — so honoring the requirement requires assuming a bound on how long the report took and how long the state persists. The timing assumption was in the requirement from the beginning. The attempted implementation did not introduce it; it exposed it.

This is why a restricted technique is worth more than a universal one. A method that can implement anything tells you nothing when it succeeds and nothing when it struggles. A method with a sharp boundary partitions requirements into two kinds and tells you which kind you have — and the answer is frequently the useful deliverable, more useful than the implementation would have been. Discovering that a requirement is time-dependent lets you go back and negotiate it, or accept the timing assumption explicitly with the bound written down, instead of implementing something that silently depends on a network's current mood.

The habit: when implementation resistance appears, before reaching for a more powerful tool, check whether your current tool is refusing for a principled reason. Name the class it works within, and ask whether what you were asked for is inside that class. When it is not, the correct output of the work is not a cleverer implementation but a statement back to whoever wrote the requirement about the assumption they did not know they were making.

**Source:** [Synchronization in Distributed Programs](../works/synchronization-in-distributed-programs.md) — the two-process counterexample given immediately after the requirements on phase transition predicates are stated, where the inability to construct a suitable predicate is used to conclude that the problem statement itself was time dependent.
