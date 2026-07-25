---
type: lesson
title: "Choose the model for what it lets you prove, and treat every arbitrary detail in a specification as a place no theorem can live"
figure: cook
works: [an-overview-of-computational-complexity, time-bounded-random-access-machines]
axes: [verifiability, primitive-count, parallelizability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Choose the model for what it lets you prove, and treat every arbitrary detail in a specification as a place no theorem can live

**Lesson:** Expressive power is the wrong criterion for picking a model, because the models that can express anything are the ones about which almost nothing can be proved. Establishing that a task cannot be done faster than some bound requires quantifying over all programs, and the more freedom the model grants, the more programs there are to rule out. The observable consequence is stark: for the most general machine models, no interesting lower bound is known for any of the natural problems anyone cares about, while for models restricted to operations appropriate to the problem — comparisons only for sorting, arithmetic only for polynomial work — matching or near-matching bounds fall out. Restriction is what buys provability, and the restrictions worth choosing are the ones that still admit the algorithms people actually write, so the bound says something about real implementations.

The complementary failure is a specification so loaded with arbitrary decisions that no clean statement can be made about it. A shared-memory parallel model has to answer how simultaneous reads and writes to one location are resolved, which operations a processor may perform, and whether reaching common memory is charged. Every one of those answers is a choice with no principled basis, and each one is a joint at which theorems break. A model built instead from acyclic gate networks, where the resources are simply the gate count and the longest path, has almost no arbitrary content, corresponds to how machines are physically constructed, and was already a well-studied mathematical object. It is the better ground even though the shared-memory picture is closer to how people write parallel code.

This inverts a common instinct. Familiarity and convenience of the model are worth less than the absence of arbitrary content in it, because arbitrary content is exactly what blocks general statements. And the choice is not free of consequences for what you can discover: a model with the right primitives can support a finer separation of cost levels than a coarser one supports, so the model determines the resolution of every question you can ask through it. That places model selection before analysis in the order of work, not after.

The practical form of this is a discipline about specifications and interfaces. Every place a specification says behavior is unspecified or implementation-defined is a place where no property can be proved and no test can be justified, and such places should be counted, minimized, and treated as debt. When a component resists reasoning, the productive suspicion is not that the reasoning is too hard but that the component grants freedoms nobody needs.

**Source:** [An Overview of Computational Complexity](../works/an-overview-of-computational-complexity.md) — the lower-bounds section on restricted models and why they yield bounds close to the best known algorithms, together with the parallel-computation section rejecting shared-memory models for the arbitrariness of their specification in favor of uniform families of gate networks. Also [Time-Bounded Random Access Machines](../works/time-bounded-random-access-machines.md) — the abstract and introduction, where the payoff claimed for the model is a finer separation of time levels than was available on tape machines.
