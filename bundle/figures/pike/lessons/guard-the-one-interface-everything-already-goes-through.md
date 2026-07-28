---
type: lesson
title: "Guard the one interface everything already goes through"
figure: pike
works: [plan-9-from-bell-labs]
axes: [verifiability, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# Guard the one interface everything already goes through

Perimeter security has a structural flaw that is easy to state and easy to
forget: a wall only works if nothing passes through it, and everything useful
passes through it. So every service that needs to reach across the boundary gets
its own hole and its own special-purpose code to police that hole, and the
security of the whole arrangement is the security of the least careful of those
holes. This work takes the other route, which only becomes available because
every resource is reached through one protocol: identity is established once, at
the point where a client attaches to a service, and every service inherits that
check without writing any security code at all.

The consequences ripple further than authentication. Because the check is
attached to attachment rather than to a network location, a remote session over
an untrusted network is not a special case needing a tunnel — it is the ordinary
case. Because the mechanism is about which user an action speaks for, delegation
becomes expressible: a compute server can act with a client's authority by
proving it is permitted to speak for that user, rather than by holding
god-powers. And because access is mediated by what is visible in a namespace,
confining an untrusted party is a matter of building them a sparse namespace
rather than trusting a wrapper program to refuse the wrong requests. Not being
able to name a thing is a stronger guarantee than being asked not to touch it.

The general principle is that trust checks want to live at chokepoints, and a
system that already funnels all access through one interface has a chokepoint
worth using. Conversely, if you find yourself writing authorization logic in
many places, that is evidence about your architecture and not merely about your
security posture: the access paths have not been unified, and no amount of
diligence in each path will give you a property you can state about the whole.
A programmer who believes this designs for a narrow waist first and gets
enforceable security as a consequence, rather than trying to bolt a boundary
around a system with many front doors.

**Source:** [Plan 9 from Bell Labs](../works/plan-9-from-bell-labs.md) — the authentication sections, particularly the argument against firewalls in favor of a single protocol-level check, the delegated "speaks for" relation used by the remote-CPU mechanism, and the restricted namespace used to cage guest users.
