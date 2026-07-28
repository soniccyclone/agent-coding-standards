---
type: lesson
title: "An annoyance now beats a decision deferred forever"
figure: pike
works: [go-at-google]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# An annoyance now beats a decision deferred forever

**Lesson:** Systems accumulate their worst structural problems out of postponement, not out of ignorance. Nobody chooses to entangle two components; the tool simply permits the entangling reference today, so the question of where the boundary belongs is never forced, and by the time the cost is visible the answer is expensive. The same shape appears when an interface can absorb one more optional parameter: the design flaw that should have prompted a second, differently named operation gets patched over instead, and the patch is cheaper than thinking every single time it is offered.

The corrective is to make the tool refuse at the moment the shortcut is taken, and to accept that this refusal will be experienced as friction. A rejected mutual reference forces someone to decide what the boundary between two components actually is, while that decision is still cheap. An error rather than a warning for a stale declaration means the recorded structure cannot drift from the real structure, so anything computed from it is trustworthy without an audit. The friction is small, immediate, and localized; the deferral it prevents is diffuse, delayed, and global. That asymmetry is why the trade is nearly always worth making even though it always feels backwards in the moment.

Note the difference between this and mere strictness. The point is not that constraints are virtuous — it is that constraints are how you buy the timing of a decision. Prohibition placed at the right point converts a question that would have been answered by accretion into one answered by a person, at a moment when the answer is still revisable. A designer who has internalized this evaluates a proposed relaxation by asking which decision it lets people skip, and treats "this would be convenient" as an incomplete argument until that is answered.

There is a companion move: prohibition works far better as a machine-checked property than as documented practice. A convention that depends on everyone remembering it holds only as long as the group is small and attentive; the identical rule enforced by the compiler holds under scale, turnover, and deadline pressure, and its guarantee can be relied on by every downstream tool.

**Source:** [Go at Google: Language Design in the Service of Software Engineering](../works/go-at-google.md) — the dependency discussion's treatment of unused imports as compile errors and the ban on cyclic imports, together with the argument against defaulted function arguments.
