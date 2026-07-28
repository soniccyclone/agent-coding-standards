---
type: lesson
title: "An invisible step is not an absent step"
figure: milner
works: [algebraic-laws-for-nondeterminism-and-concurrency]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# An invisible step is not an absent step

**Lesson:** Declare an action internal and it stops being something an outsider can watch. The tempting conclusion is that it may therefore be deleted from any account of what the system does — that internal steps are noise, erasable, semantically free. This paper shows the conclusion is wrong, and the reason is precise: an internal step can consume a choice. A system that internally advances past a branch point has, without emitting anything, given up options it previously had, and an outside party who tries to exercise one of the abandoned options finds itself stuck. Deadlock is observable. So the unobservable step is observable in its consequences, and no equivalence that erases it can be correct.

The analysis that follows is careful about exactly how much erasure is legitimate. An observation is redefined to absorb any run of internal steps before and after the visible action, which is the right generosity — nobody can count them. But the resulting relation turns out not to survive being placed in a larger program: a lone internal step followed by termination is equivalent to termination on its own, and yet becomes distinguishable the moment it is offered as one branch of a choice, because in that position it can pre-empt the other branch. Two laws are then identified that capture precisely which internal steps may be removed, and completeness is proved for them, so the boundary between erasable and load-bearing internal behavior is drawn exactly rather than guessed at.

The practical content is that hidden asynchrony is not free. An internal retry, a buffering hop, a background flush, a lazily initialized resource, an await that yields the scheduler — each is invisible in the sense that it appears in no interface and emits no output, and each can change whether the system remains willing to do what a client is about to ask. Systems get built on the assumption that adding an internal step is a refactoring, and the resulting failures are hangs and lost liveness rather than wrong answers, which is why they are found late and blamed on load.

Someone who has absorbed this treats "this happens internally, so it does not affect the contract" as a claim requiring proof rather than an obvious simplification. The question to ask is not whether anyone can see the step but whether the step forecloses anything: if it commits to a branch, resolves a race, or consumes a token, it is part of the observable behavior no matter how quiet it is.

**Source:** [Algebraic Laws for Nondeterminism and Concurrency](../works/algebraic-laws-for-nondeterminism-and-concurrency.md) — the section introducing an unobservable action, its opening example of two programs distinguished only by an internal step, the observation that the resulting equivalence fails to be preserved by choice contexts, and the two additional axioms shown to complete the axiomatization.
