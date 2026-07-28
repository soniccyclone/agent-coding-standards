---
type: lesson
title: "Split every decision into an expensive search you do not have to trust and a cheap check you do, then let the untrusted half fail only in the safe direction"
figure: lampson
works: [authentication-in-distributed-systems-theory-and-practice]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, formal-methods-and-verification]
tags: [lesson]
---
# Split every decision into an expensive search you do not have to trust and a cheap check you do, then let the untrusted half fail only in the safe direction

**Lesson:** Deciding anything in a large system usually requires gathering evidence from many places: databases, remote services, caches, files written long ago by parties you no longer talk to. If the correctness of the decision depends on all of that machinery behaving, then all of it is part of the part you must get right, and the part you must get right is now unbounded. The way out is to notice that assembling the evidence and confirming that the evidence entails the conclusion are two different jobs with wildly different costs. Assembly is a search — slow, distributed, heuristic, allowed to be wrong. Confirmation is a proof check — small, local, mechanical, total. Only the confirmer needs to be trusted, provided the evidence is self-authenticating, so that a lie or a corruption in transit is detectable rather than believed.

This reframing pays twice. First, it shrinks the set of components whose failure can produce a wrong answer down to something a person can actually read and reason about, which is the only kind of trust boundary that means anything. Second, it frees the search to be as opportunistic as you like: evidence can be cached anywhere, forwarded by anyone, stored in a plainly insecure place, fetched by whichever side of a conversation happens to have better locality, or produced years before the decision was contemplated. The party that gathers the evidence and the party that relies on it need not even be the same, because a checkable artifact carries its own warrant wherever it goes.

The second half of the discipline is directionality. It is not true that untrusted components can fail with no consequence — a missing record, an unreachable service, an expired cache entry all change outcomes. What must be true is that every such failure biases the outcome toward refusal rather than toward permission. That in turn dictates how facts are represented: affirmative evidence may be believed only when presented, so its absence is treated as absence of authority, while restrictive evidence must be believed on sight, because failing to find it must never widen what is allowed. A builder who has internalized this asks two questions of every new piece of infrastructure: is the thing it hands me self-checking, and if it hands me nothing at all, does the system get more permissive or less? Anything that answers "no" to the first or "more permissive" to the second has silently joined the part you must get right.

**Source:** [Authentication in Distributed Systems: Theory and Practice](../works/authentication-in-distributed-systems-theory-and-practice.md) — the discussion of the trusted computing base and fail-secure behavior in the concepts section, carried through to the access-decision section's asymmetric treatment of affirmative versus restrictive evidence and to the observation that every decision leaves behind a checkable proof suitable for audit.
