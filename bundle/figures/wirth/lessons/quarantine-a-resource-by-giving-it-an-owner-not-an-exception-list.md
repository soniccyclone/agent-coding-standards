---
type: lesson
title: "Quarantine a resource by giving it an owner, not an exception list"
figure: wirth
works: [project-oberon]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# Quarantine a resource by giving it an owner, not an exception list

**Lesson:** Every allocator eventually meets a unit that must never be handed out again — a physically damaged one, a region reserved by something outside the system, an address that is special for reasons the allocator has no vocabulary for. The obvious response is a second structure: a list of excluded units the allocator consults in addition to whatever it normally consults. That structure is new machinery on the allocation path, it is a second thing that must be persisted and kept correct, and it introduces a case that every future change to allocation must remember.

There is usually a cheaper answer available, because the allocator already has a complete mechanism for expressing "this unit is not available": it belongs to somebody. So create a holder — an ordinary member of whatever population owns units — and give it the excluded ones. Nothing about allocation changes. The occupancy computation, whatever it is, already accounts for units that are owned, so the damaged unit is marked in use for exactly the same reason and by exactly the same code as every other unit in use. The exclusion has been expressed in the vocabulary that already existed rather than beside it, and the amount of new mechanism is one record.

The reason this works, and the condition under which it works, is that ownership in most systems is a claim about reachability rather than about usability. Nothing requires that the owner ever be readable, or that anything ever traverse its contents; it only has to exist and be counted. That is a strong hint about where else the trick applies: whenever you are tempted to add a side-table of exceptions to a mechanism that already tracks membership, ask whether you can instead create a member that absorbs them. The side-table adds a case to every consumer; the absorbing member adds a case to none, and the peculiarity is confined to the one place where the record was created — which is also the place where a human reading the store will find it and understand what happened.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.3's handling of an unrecoverably faulty sector, which is made unreferenceable by appending it to a file called BadSectors, described as inherently unreadable but whose sectors are marked as used by the ordinary construction of the sector reservation table during boot.
