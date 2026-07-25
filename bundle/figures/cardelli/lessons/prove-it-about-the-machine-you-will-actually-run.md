---
type: lesson
title: "State the semantics over the mechanism you will actually run, so the theorem covers the thing you ship"
figure: cardelli
works: [an-imperative-object-calculus, the-functional-abstract-machine]
axes: [verifiability, hardware-affinity]
subdomains: [formal-methods-and-verification, operating-systems-and-systems-programming]
tags: [lesson]
---
# State the semantics over the mechanism you will actually run, so the theorem covers the thing you ship

**Lesson:** A formal account of a language can be written over idealized machinery that no implementation uses, most commonly by defining evaluation as textual replacement of names by terms. Such an account is easier to write and yields theorems about a system nobody runs, leaving a gap that has to be closed by an unwritten argument that the real implementation, with its frames, environments, and mutable store, agrees. The alternative is to build the model out of the mechanisms the implementation actually has: a stack that binds names to results, closures pairing code with the bindings it needs, and a store mapping locations to contents. The rules get longer and the proof gets more bookkeeping, and in exchange the soundness result is about a realistic execution strategy, so the gap is closed rather than assumed away.

The same instinct produces a design artefact rather than just a proof convenience. An execution machine can be specified as a transition relation over a state that is literally a handful of pointers into real stacks and a heap, where each instruction is a rule saying how that state changes and where absence of a rule marks an inconsistent state whose behaviour is undefined. That specification is a formal object you can reason about and an implementation blueprint at the same time, precise enough to argue with and concrete enough that the register allocation and stack discipline are visible in it. Failure behaviour, ordering of evaluation, and the exact points at which state changes all become stated rather than emergent.

There is a real cost. Choosing the concrete model commits you to details, some of which are arbitrary, and it makes the semantics longer and less pretty. The judgement is about which gap you would rather have: a clean theory sitting a translation away from the artefact, or a heavier theory that talks about the artefact. When the properties at stake concern state and ordering, the heavier one is generally the honest choice, because those are exactly the properties an idealized model abstracts away.

**Source:** [An Imperative Object Calculus](../works/an-imperative-object-calculus.md) — the introduction's statement that the soundness argument avoids formal substitutions in favour of stacks and closures precisely to yield a manageable proof for a realistic implementation strategy, together with the store-based operational rules and typings over stores. Also [The Functional Abstract Machine](../works/the-functional-abstract-machine.md) — the state and operational semantics sections, where the machine state is a tuple of the pointers a real implementation maintains and every instruction is given as a transition over it, including the treatment of failure and of states with no transition.
