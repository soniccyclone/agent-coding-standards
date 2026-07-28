---
type: lesson
title: "A consistency guarantee ends where information flow leaves your interface"
figure: liskov
works: [providing-high-availability-using-lazy-replication]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [distributed-systems-and-concurrency, databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A consistency guarantee ends where information flow leaves your interface

**Lesson:** It is tempting to define the ordering a service promises in terms of the calls the service saw. That definition is wrong in a way that produces real, confusing bugs, because the reason one action depends on another is that somebody learned something — and learning can happen along paths the service knows nothing about. One party reads a value and then mentions it to another party directly; that second party now issues a request whose sensibility depends on an earlier effect it never observed through the service. Nothing in the service's own record of calls reveals the connection.

So the scope of the guarantee is set by the scope of information flow, not by the boundary of the interface. Making the guarantee real means capturing the out-of-band paths: dependency information has to ride along on party-to-party communication as well as on service calls, which in practice means placing a component on the client side that observes both and merges what it learns. That component is doing something conceptually larger than a client library — it is tracking what its party could possibly know, so the service can be told.

Two consequences fall out. First, this kind of tracking is necessarily conservative: it assumes that any contact between parties transferred everything either of them knew, which manufactures dependencies that do not really exist and yields an order stronger than required. That over-approximation is the correct default, since the alternative is missing a real dependency, and a party that genuinely knows better can be given the means to state its dependencies precisely. Second, the cost of the tracking scales with how many independent guarantee scopes a party participates in, which turns out to be an argument for keeping services small and mutually unrelated: when a subsystem's use of a service is fully encapsulated, its dependency information never has to travel with anybody else's.

A programmer who believes this maps the information paths before designing the ordering guarantee, and treats any channel between components that bypasses the system as either inside the guarantee — and therefore instrumented — or explicitly outside it and documented as such. Undocumented side channels are how consistency promises get broken by code that never touched the system, and no amount of internal rigor detects it.

**Source:** [Providing High Availability Using Lazy Replication](../works/providing-high-availability-using-lazy-replication.md) — the discussion of how the front end guarantees causality by intercepting client-to-client messages as well as service calls, its note that the resulting order may be stronger than needed, and the scalability section's treatment of encapsulated, mutually unrelated services.
