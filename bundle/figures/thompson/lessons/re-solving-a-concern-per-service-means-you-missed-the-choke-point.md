---
type: lesson
title: "If a concern has to be re-solved per service, you have not found the choke point"
figure: thompson
works: [plan-9-from-bell-labs]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# If a concern has to be re-solved per service, you have not found the choke point

Some concerns are not features of any one service but conditions on all of them: proving who is asking, deciding what a name refers to, reaching something on another machine. The ordinary outcome is that each service handles these for itself — one story for remote login, another for file transfer, another for the window system — and then a perimeter device is bolted on to police the results, needing its own special-case knowledge of each service in turn. Plan 9's structural bet is that this is a symptom of a missing convergence point, not an inherent cost. Every interaction in the system, local or remote, kernel or user-level, passes through one protocol; naming, access, and authentication are therefore settled once, inside that protocol, and no service can be reached in a way that bypasses them.

The reasoning generalizes past operating systems. A cross-cutting concern implemented n times has n implementations to audit, n places for the treatments to diverge, and n opportunities for a new service to arrive without one. Worse, the per-service approach makes the perimeter the only place with a global view, and a perimeter can only reason about the traffic shapes it was taught. When instead every request traverses a single narrow interface, the concern is enforced by construction: a component that has not satisfied it has not made contact. That is also why the same design lets a compute service act with a user's authority across an untrusted network without any special arrangement — the delegation is expressed in the one mechanism everything already speaks.

The corollary is a diagnostic. Whenever you find yourself writing a policy for the third time, in the third service, do not factor the policy into a shared library and call it done — a library only helps the callers that remember to call it. Ask instead what interface all three services genuinely traverse, and whether the policy can be moved there and made unavoidable. If no such interface exists, that absence is the actual finding: the system has no choke point, and every cross-cutting property it wants will have to be maintained by discipline forever.

Plan 9 pairs this with a matching refusal — it has no super-user. Concentrating the enforcement point is not the same as concentrating authority, and the paper is careful that each server answers for its own resources rather than deferring to one omnipotent identity. Universal mechanism, distributed authority: collapsing those two together is how a single choke point turns into a single catastrophe.

**Source:** [Plan 9 from Bell Labs](../works/plan-9-from-bell-labs.md) — the authentication overview, which contrasts placing authentication in the one protocol against firewalls needing per-service code, together with the discussion section's claim that the protocol centralizes naming, access, and authentication, and the special-users section on the absence of a super-user.
