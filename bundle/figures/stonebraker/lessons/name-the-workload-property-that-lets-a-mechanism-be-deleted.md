---
type: lesson
title: "Name the workload property that lets a mechanism be deleted"
figure: stonebraker
works: [the-end-of-an-architectural-era]
axes: [verifiability, primitive-count, parallelizability]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
tags: [lesson]
---
# Name the workload property that lets a mechanism be deleted

Most defensive machinery in a system exists because the system does not know what it will be asked to do. A general engine cannot know whether the next request will touch one partition or twenty, whether it will need to undo half its work, or whether it will interleave badly with something already running, so it carries apparatus that copes with all of those possibilities at all times. The interesting inversion is to stop treating that ignorance as inevitable and start treating it as a design parameter. If the set of things the system will be asked to do is registered ahead of time, each piece of defensive apparatus can be re-examined against a specific question: what property would the workload have to possess for this mechanism to be provably unnecessary?

The discipline that makes this productive is naming the properties precisely and separately, rather than reaching for one vague notion of "simple workload." Whether every step of a request lands on a single partition is one property. Whether a request can be decomposed into independent pieces that need no intermediate exchange is another. Whether a request does all its potential aborting before it does any of its mutating is a third. Whether two request kinds can be interleaved in any order and land in the same final state is a fourth. Each one, held alone, discharges a different mechanism — distributed coordination, cross-node data flow, rollback bookkeeping, concurrency control respectively — and each is checkable against the code of the request rather than guessed at runtime. Naming them separately also tells you which cheap schema surgery buys which deletion: replicating the tables nobody writes, or splitting off the columns nobody updates, can move a workload across one of these lines without changing what it computes.

This is a different move from relaxing a guarantee. Nothing about correctness is being surrendered; the guarantees still hold, but they are discharged by a static argument about the shape of the workload instead of by runtime enforcement. The cost is real and should be stated plainly: the system now demands its workload up front and refuses to serve arbitrary late-arriving requests, and pushing a real workload across those property lines took human insight that no tool could have supplied. That is the trade. Generality is being sold, and the price it fetches is the wholesale removal of subsystems.

A programmer who internalizes this stops asking "how do I make the locking faster" and starts asking "under what conditions would I need no locking." That question has a very different answer surface. It sends you to the schema, to the request boundaries, and to the application's own structure rather than to the mechanism's internals — and it frequently finds that the workload already nearly has the property, and that a small deliberate restriction on the interface gets it the rest of the way.

**Source:** [The End of an Architectural Era (It's Time for a Complete Rewrite)](../works/the-end-of-an-architectural-era.md) — the section defining the transaction and schema characteristics the prototype relies on, and the walk through the standard benchmark showing which restructurings move each request class across those lines.
