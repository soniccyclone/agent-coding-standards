---
type: lesson
title: "While operations are in flight, an object's meaning is a set of possible values, not a value"
figure: herlihy
works: [linearizability-a-correctness-condition-for-concurrent-objects]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---

# While operations are in flight, an object's meaning is a set of possible values, not a value

**Lesson:** Sequential reasoning about a data structure rests on two conveniences that concurrency destroys. The first is that the representation is only required to make sense between operations, so an invariant may be broken mid-operation and restored before anyone looks. The second is that at any sensible moment the representation denotes one abstract value. In a structure whose operations genuinely overlap, there may be no moment when nothing is in progress, so any invariant that only holds between operations holds never; the invariant must be preserved by every individual step, and the interpretation of the representation must be defined at every step too.

The second convenience fails more interestingly. It is tempting to keep a single-valued interpretation and simply identify, within each operation, the one step at which it takes effect. That is provably impossible for genuinely concurrent implementations. When two insertions have each claimed a slot but only one has filled it, the order in which they will appear to have happened is not yet determined by anything in the representation — it depends on a race that has not occurred, between a later fill and a reader's inspection of that slot. Every candidate single value is refuted by some continuation, and the refutations are mutually exclusive, so no such interpretation exists. The honest model maps the representation to the whole set of abstract values still consistent with what has happened, and correctness becomes containment: every value the representation could denote must be one the abstract contract still permits. This was not an aesthetic preference; a well-known single-valued verification technique could not handle such an implementation, and had to be extended with the ability to talk about future choices in response.

For a programmer, the lesson generalizes past proofs. Concurrent state is inherently partially ordered and partially decided, and asking "what is the current value" of a structure with operations in flight is asking a question that has no answer. Debuggers, monitors, invariant checks, and mental models that assume a single current value will produce confident nonsense at exactly the moments that matter. Two practical corollaries: the useful invariants are the ones that survive every intermediate step, not the ones true at rest; and when a step's meaning lives in a participant's program counter or local variables rather than in the shared representation, you must make that hidden state explicit — as auxiliary data recorded alongside the real thing — before you can say what the object means. Reasoning is only possible about state you have made visible.

**Source:** [Linearizability: A Correctness Condition for Concurrent Objects](../works/linearizability-a-correctness-condition-for-concurrent-objects.md) — the section reworking representation invariants and abstraction functions for the concurrent case, the explicit contradiction argument showing no single-valued interpretation works for the highly concurrent queue, the resulting set-valued abstraction function with the subset correctness criterion, and the auxiliary-data treatment of an implementation whose state hides in a critical section.
