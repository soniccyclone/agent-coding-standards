---
type: lesson
title: "Make the awkward question unaskable rather than answering it carefully: drop time, keep order"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [verifiability, expressiveness, parallelizability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# Make the awkward question unaskable rather than answering it carefully: drop time, keep order

**Lesson:** There is a difference between building a model that answers a hard question correctly and building one in which the question cannot be posed. The second is usually the better engineering. Timing is the standard case: a model that records when each thing happened must then be interrogated about whether two things happened at the same instant, and every answer it gives is either arbitrary or a commitment to a particular machine speed. Drop the clock and keep only the order of occurrences, and the question of simultaneity has no expression in the language at all. Nothing in the model can depend on it, because nothing in the model can say it — which is a far stronger guarantee than a rule telling designers not to rely on timing.

The move is not a loss of expressiveness if you carry two encodings with you. Where simultaneity genuinely matters, because two parties must act together or not at all, represent the joint occurrence as a single indivisible happening with one name; the togetherness is then structural rather than coincidental, and cannot be broken by scheduling. Where it does not matter, permit the two occurrences to be recorded in either order and refuse to prefer one, which is exactly the statement that the difference is unobservable. Between them these cover the cases, and each says something definite about the design rather than deferring to whatever the hardware does.

The same trick applies to duration. Rather than giving an occurrence a length — which reintroduces the clock — treat every occurrence as indivisible and represent an extended activity by two of them, its beginning and its end. Overlap between two activities then has a precise meaning in terms of order alone: each began before the other ended. So concurrency of long-running work is fully expressible without any notion of elapsed time, and the resulting descriptions hold for systems of any speed, which is what lets the logical design be settled first and performance treated as a separate concern afterwards. Generalize the habit: whenever a modelling question keeps producing arbitrary answers, the fix is usually to remove the ability to ask it and to name explicitly the few cases where the underlying distinction really was doing work.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the introduction to the chapter on processes, which treats each event occurrence as instantaneous and atomic, represents a time-consuming action by separate start and finish events so that overlap is defined by each start preceding the other's finish, deliberately ignores exact timing so that designs apply to systems of any speed and timing concerns can be treated independently of logical correctness, and refuses to ask whether two events occur simultaneously — representing genuine simultaneity as a single event occurrence and otherwise allowing two potentially simultaneous occurrences to be recorded in either order.
