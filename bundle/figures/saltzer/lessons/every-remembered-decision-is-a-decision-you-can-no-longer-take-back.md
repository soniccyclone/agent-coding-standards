---
type: lesson
title: "Every remembered decision is a decision you can no longer take back"
figure: saltzer
works: [the-protection-of-information-in-computer-systems]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Every remembered decision is a decision you can no longer take back

**Lesson:** The moment a system converts the outcome of a decision into a durable
artifact — a token, a handle, a cached answer, a copied pointer — it has performed a
binding, and it has thereby given up the ability to change its mind unless it planned
otherwise in advance. This is the underlying mechanic behind the comparison of two
protection architectures that looks at first like a mere implementation choice. Hand
out unforgeable tokens and each access is fast, because holding the token *is* the
proof; but the token now exists somewhere you cannot see, can be duplicated without
your knowledge, and cannot be recalled. Re-consult a list at the moment of each use
and every access costs a lookup, but the decision is never frozen: change the list
and the change takes effect, and you can also answer the question of who currently
has access, which the token scheme cannot answer without searching the entire world.

The general form is a tradeoff between when a decision is bound and how much control
you retain over it, and the currency of that tradeoff is indirection. Reversibility
requires a place where the decision is re-made, or at least re-checked, on the path to
the thing. If no such place exists, no amount of later effort creates one; the only
remedy is destroying the underlying object, which harms parties who did nothing wrong.
So the question "where in this path is the decision actually re-evaluated?" is worth
asking of any design, early, because the answer is very expensive to change afterward.

This lands hardest on performance shortcuts, which is where it is least expected. Any
optimization that remembers the result of a check has quietly converted a live
decision into a stored one, and has created an invalidation obligation that usually
goes unwritten. That is the same defect as an uncontrollable token, arrived at by
accident rather than by design. The honest version of the shortcut keeps both
properties by making the fast path an explicitly derived copy of the slow path's
answer, with a defined way to clear it — accepting a bounded window of staleness that
you can name, rather than an unbounded one you cannot.

A programmer holding this idea reads their own system for bindings: every place a
derived fact outlives the decision that produced it. For each one they can say how it
gets invalidated and how long the stale window is, or they knowingly accept that this
particular grant is permanent. The failure mode this prevents is the common one where
revocation is discovered to be impossible long after someone has promised a customer
it exists.

**Source:** [The Protection of Information in Computer Systems](../works/the-protection-of-information-in-computer-systems.md)
— Section II's contrast between capability and access-control-list organizations,
particularly the treatment of revocation, propagation, and review of access, the
observation that reversing a binding requires indirection, and the shadow-register
scheme that buys speed back at a stated cost in immediacy of revocation.
