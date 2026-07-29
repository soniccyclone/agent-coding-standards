---
type: lesson
title: "Design interfaces so the data outlives the programs that touch it"
figure: stonebraker
works: [what-goes-around-comes-around]
axes: [expressiveness, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# Design interfaces so the data outlives the programs that touch it

The observation that organizes the whole survey is a lifetime mismatch: the data an organization keeps outlives the programs written against it, often by decades, and it certainly outlives whatever tuning decision looked right the year the first program was written. Every access path, storage layout, index choice, and partitioning scheme is a guess about a workload that has not finished arriving. If programs are written against those guesses, then every later retuning is a program-rewriting event, and the cost of adapting the system grows with the number of programs that exist rather than staying proportional to the change itself.

The countermeasure is to make the program's contract be with an abstract description of the data and never with its realization — so that layout can be re-decided freely, and so that the abstract description can itself be re-projected as the underlying structure grows new pieces. The early hierarchical and network systems show both halves of the failure: languages whose semantics were defined in terms of the physical traversal order pinned the storage organization in place, and the workarounds that restored flexibility were intricate enough that a decade later they blocked their own vendor from bolting a cleaner interface on top. Complexity in a compatibility layer is not merely ugly; it forecloses future migrations that the simpler design would have permitted.

What follows practically is that independence is worth buying early, at real cost, before you know which changes you will need — because you buy it by choosing a simple model and a non-navigational interface, and neither choice can be retrofitted. A programmer who believes this treats "can I change the physical representation without touching callers?" and "can I add to the schema without breaking existing readers?" as acceptance criteria on the interface itself, not as pleasant properties to discover later. The corollary bites too: interfaces that expose iteration order, pointer identity, or storage adjacency are selling the future for present convenience.

**Source:** [What Goes Around Comes Around](../works/what-goes-around-comes-around.md) — drawn from the survey's treatment of physical and logical data independence across the hierarchical and network eras, including why a relational front end could not be retrofitted onto the older engine.
