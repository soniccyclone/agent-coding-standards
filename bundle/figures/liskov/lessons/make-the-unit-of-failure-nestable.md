---
type: lesson
title: "Make the unit of failure nestable and failure handling becomes composable"
figure: liskov
works: [guardians-and-actions]
axes: [expressiveness, parallelizability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics, databases-and-data-management]
tags: [lesson]
---
# Make the unit of failure nestable and failure handling becomes composable

**Lesson:** An all-or-nothing unit of work is a fine idea that becomes rigid if it is the only size available. With one flat level, any sub-step that fails destroys the entire effort, so a program that wants to try a peer and fall back to another, or to accept the first of several answers, or to require only most of a set to succeed, has to abandon the mechanism and hand-roll its own bookkeeping — which is where correctness goes to die. Let the units nest, and all of those patterns become ordinary code.

The rules that make nesting work are worth noticing because they are exactly the rules that preserve composability. A nested attempt is all-or-nothing with respect to its siblings, so several can run at once without any additional coordination written by hand. A nested attempt that fails does not condemn its parent; the parent learns of the failure and chooses. A nested attempt that succeeds is only provisionally committed — its parent can still discard it — which is what allows the outermost attempt to keep the guarantee that a caller sees the whole thing or none of it. And durability only happens at the outermost level, so the expensive part is paid once no matter how finely the work was divided.

With that in place, a hedged read is a set of nested attempts started together where the first success cancels the rest; a majority write is a set where the parent commits once enough children have. Neither needs a special construct, and the discarded siblings leave nothing behind. The composability comes precisely from failure being local and recoverable at each level rather than a global event.

The counterpart, which the design is careful about, is that the pattern only holds for effects the system can actually retract. Anything that escapes into the world — a printed document, a dispatched shipment — cannot be undone by discarding a version, so those effects belong in a separate, later unit that runs only after the reversible part has succeeded. A programmer who believes this designs their retryable region to end exactly where irreversibility begins, and treats any irreversible act inside a speculative region as the thing that will eventually require a human to clean up.

**Source:** [Guardians and Actions: Linguistic Support for Robust, Distributed Programs](../works/guardians-and-actions.md) — the nested-actions section with its replicated-database quorum example and its concurrency construct where the first successful branch aborts the rest, plus the remarks on effects that cannot be undone and must be deferred to a separate later action.
