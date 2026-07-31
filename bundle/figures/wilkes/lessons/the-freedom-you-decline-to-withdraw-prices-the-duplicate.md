---
type: lesson
title: "What a transparent duplicate of state really costs is the set of freedoms you decline to withdraw from its clients"
figure: wilkes
works: [slave-memories-and-dynamic-storage-allocation]
axes: [verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# What a transparent duplicate of state really costs is the set of freedoms you decline to withdraw from its clients

**Lesson:** Any fast copy of slower state carries one obligation: it must not survive a change to the original that it did not see. The size of that obligation is fixed not by the copy's design but by what clients are still permitted to do. Decide that a class of data cannot be modified after it is published, and the duplicate needs no invalidation machinery whatever — there is nothing to miss. Decline to remove that permission, and every route by which the original can change becomes a route that has to consult the duplicate first, including routes whose authors have no idea the duplicate exists. So the first question is not how to keep the copy fresh. It is which capability you are unwilling to take away, because the answer determines the whole bill.

Stated that way, the invalidation cost stops looking like an implementation detail and starts looking like a consequence of a policy decision made somewhere else, usually by someone defending a client's freedom rather than costing it. That reframing also tells you where the bugs will be. Not in the lookup path, which runs constantly and fails loudly, but in the seldom-exercised mutation paths nobody remembered to route through the check — the administrative tool, the migration script, the recovery path. The honest precondition for calling a duplicate transparent is an enumeration of every way the original can change. If you cannot produce that list, you have not built a transparent cache; you have built one that is correct on the paths you happened to think of.

Two moves follow. Where you can restrict, restrict and write down that you did: converting an ongoing consistency obligation into a one-time constraint is a real gain, because a constraint is checked at one place at one moment while an obligation must be honoured forever by everyone. Where you cannot restrict — because the freedom is genuinely load-bearing — force every mutation through a single chokepoint, so that the number of places obliged to remember the duplicate is one rather than however many callers exist now and will exist later. The same reasoning governs every kind of derived state, not just caches: secondary indexes, denormalized fields, materialized views, generated artifacts.

**Source:** [Slave Memories and Dynamic Storage Allocation](../works/slave-memories-and-dynamic-storage-allocation.md) — the passage on the instruction slave which observes that keeping the programmer's freedom to modify instructions forces the slave to be examined on every write, and the word updated in both places when it is found there; and the large-slave scheme, where the fast copy is instead made authoritative while resident, so reads and writes alike are satisfied without touching the slow memory.
