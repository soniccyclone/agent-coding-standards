---
type: lesson
title: "Express robustness as the exact assumption your design needs, not as a probability that hides it"
figure: schneider
works: [implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial]
axes: [verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Express robustness as the exact assumption your design needs, not as a probability that hides it

There are two ways to say how much abuse a system survives. One is statistical: expected time between failures, probability of surviving an interval. The other is structural: a count of simultaneously broken components below which the specification still holds. Both are true statements, but only the second one tells a reader what the design is assuming, and therefore only the second one can be checked, argued with, or violated in a way anyone notices. A statistical claim is a property of the parts you happened to buy. A structural claim is a property of the arrangement, and it stays true when you swap the parts.

The direction of derivation settles which one is primary. From a structural claim plus reliability figures for the components, the statistics follow — you compute the chance of exceeding the tolerated count. The reverse derivation does not exist: no headline reliability number tells you how many concurrent failures the arrangement absorbs. So the statistical figure is a downstream summary, and quoting it as the specification silently discards the assumption that generated it. Systems fail in production when an assumption nobody wrote down turns out to be false; a specification whose form cannot express assumptions is a specification that guarantees this.

The same demand for explicitness applies to the failure model itself. "Fails by stopping in a way others can detect" and "behaves arbitrarily, possibly maliciously" are different assumptions with sharply different costs, and the choice between them is a design decision to be made deliberately rather than a detail to be left ambient. Assuming less about how components misbehave buys robustness and costs replication; assuming more is cheaper and stakes the system on the assumption holding. Neither is wrong. Failing to state which one you picked is.

There is a trap on the other side, worth keeping in view. A specification consisting only of safety properties — only of things that must never happen — is trivially satisfiable by a component that does nothing at all. A failure detector that never reports anything never wrongly evicts a healthy node and never admits a broken one; it satisfies its safety obligations perfectly and contributes nothing. The useful content of such a specification lives entirely in the progress obligations and the rate bounds: how fast repairs must occur relative to failures for the system to survive indefinitely. A programmer who has absorbed this writes down, for every resilience mechanism, both what it must never do and how quickly it must act — and treats a spec with only the first half as unfinished.

**Source:** [Implementing Fault-Tolerant Services Using the State Machine Approach: A Tutorial](../works/implementing-fault-tolerant-services-using-the-state-machine-approach-a-tutorial.md) — the section introducing failure terminology, which argues for counted tolerance over statistical measures, and the later reconfiguration section where the do-nothing reconfigurator is observed to satisfy the safety conditions while achieving nothing.
