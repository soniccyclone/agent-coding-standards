---
type: lesson
title: "Two representations that are provably equivalent can diverge the moment you extend the system"
figure: hartmanis
works: [relativization-a-revisionistic-retrospective]
axes: [primitive-count, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Two representations that are provably equivalent can diverge the moment you extend the system

**Lesson:** The same computational class can often be described in more than one way — as what a resource-bounded machine can decide, or as what a prover can convince a skeptical verifier of. Inside the original system those descriptions pick out exactly the same set, and it becomes natural to treat them as interchangeable names for one thing. Extend the system by giving every participant access to some external source of answers and the descriptions come apart, because they consume that source at wildly different rates: a machine sweeping through a huge space can consult it an enormous number of times, while a single line of an interactive exchange can consult it only sparingly. The extension does not act on the class; it acts on each machine formulation separately, and different formulations were only ever equal with respect to their outputs, never with respect to how they get them. Reading the extended results as facts about classes rather than about machines is the error that made a whole framework look sturdier than it was.

The general principle: extensional equality of two designs is not structural equality, and only structural equality survives extension. Whenever you prove that two implementations, two APIs, two data models, or two specifications are equivalent, that proof is scoped to the operations you had in mind. Add a capability — a hook, an escape hatch, a side channel, an observer, a new query mode — and the equivalence must be re-established, because the new capability is not a passive addition. It is a lens that magnifies exactly the structural differences the equivalence proof was allowed to ignore.

This is what makes leaky abstractions leak on schedule. Two libraries interchangeable under normal use diverge under cancellation, or under introspection, or when something needs to observe intermediate state. Two storage layers with identical query semantics diverge the moment transactions, replication, or a change feed enters the picture. The disagreement is not a bug in either one; it is the previously invisible structural difference becoming visible, on the axis the new feature happens to expose.

The practical discipline is to write down, for each equivalence you rely on, what set of operations it was proven over — and to treat any proposal that widens that set as invalidating it until re-argued. Then, when comparing two designs, prefer knowing where they differ structurally to knowing that they currently behave the same, since the structural differences are the complete list of ways the future can break the equivalence.

**Source:** [Relativization: A Revisionistic Retrospective](../works/relativization-a-revisionistic-retrospective.md) — the argument that relativized separations and collapses trade on mismatched oracle access mechanisms between machine-based and protocol-based characterizations of the same class, concluding that oracles relativize machines rather than classes; also the earlier discussion of positive relativizations, where equalizing the access mechanisms removes the effect.
