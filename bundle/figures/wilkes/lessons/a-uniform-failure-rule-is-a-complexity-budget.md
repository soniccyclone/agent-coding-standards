---
type: lesson
title: "A uniform rule about failure doubles as a complexity budget you did not have to argue for"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A uniform rule about failure doubles as a complexity budget you did not have to argue for

**Lesson:** Commit as a matter of policy that every operation you offer can be safely reattempted from its beginning after any failure partway through, and something happens beyond the recovery guarantee: the policy silently caps how elaborate any operation is allowed to be. An operation whose intermediate effects cannot be reconstructed or discarded simply cannot be built under the rule, so it is never proposed. The limit is a consequence of a property you wanted anyway, which makes it much easier to hold than a limit derived from taste — nobody has to argue that a feature is too complicated, only that it cannot be made restartable.

The value of a limit with that provenance is that it survives pressure. Complexity budgets grounded in judgement erode, because each individual excess is defensible and the person objecting has only an aesthetic to appeal to. A budget that falls out of a stated safety property does not erode, since exceeding it means abandoning the property, and abandoning the property is a visible decision affecting everything rather than an invisible one affecting a single feature. This is a general technique: when you want a bound on elaborateness, look for a property whose enforcement implies the bound, and adopt the property.

The rule needs one honest concession to remain workable. A few operations are long enough that restarting from the beginning is wasteful rather than merely inelegant, and for those the discipline is relaxed to resuming from a recorded point — an explicit, enumerated exception, not a general licence. Naming the exceptions keeps the rule meaningful; letting each operation decide for itself how it recovers is how the budget stops existing.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 2's statement that all instructions are as a matter of policy implemented to be restartable from the beginning if a trap occurs on any memory access, with block-move instructions arranged to resume where they left off, followed by the observation that adherence to this policy imposed a practical upper limit on the complexity of the special instructions that could be implemented.
