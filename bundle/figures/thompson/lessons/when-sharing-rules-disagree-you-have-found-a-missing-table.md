---
type: lesson
title: "When two sharing rules disagree about where a piece of state lives, you have found a missing layer"
figure: thompson
works: [unix-implementation]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# When two sharing rules disagree about where a piece of state lives, you have found a missing layer

**Lesson:** Put a piece of mutable state in the wrong structure and the symptom is never "wrong place" — it is a pair of requirements that both look reasonable and cannot both be met. Some clients must see the state change together; others must see their own copy. Attach it to the shared, long-lived object and the independent clients collide. Attach it to each client and the ones meant to move in lockstep drift apart. The reflex at that point is to add a flag, or a special case for the lockstep clients, or a rule about who is allowed to update what. All of those encode the conflict rather than resolving it.

The resolution is to read the conflict as a measurement. Two irreconcilable placements mean the state's lifetime and sharing pattern match neither of the structures you already have, which means there is a level of indirection your model does not yet contain. Give that state its own structure whose only job is to hold it, and let the disagreeing parties differ in whether they share an instance of it. The new structure is not gratuitous — it is exactly the distinction the two requirements were pointing at, and once it exists both requirements become statements about which clients share which handle, rather than exceptions carved into existing objects.

The general principle is that the correct unit of sharing is discovered, not chosen up front. Objects in a design usually get their boundaries from what they represent, and that is a fine first cut; but the axis along which a system actually needs to alias and diverge is a separate axis, visible only once concurrent users show up. Where those two axes fail to line up, an object has to split. The tell is always the same: a field that some callers need shared and others need private.

Someone who has internalised this treats "both of these constraints are legitimate and they contradict" as good news, because it localises the design error precisely. Instead of arbitrating between the constraints or making one of them a configuration option, they ask what entity would have to exist for both to be plainly true, and add it — accepting one more structure in exchange for deleting a special case, which is nearly always the trade to take.

**Source:** [UNIX Implementation](../works/unix-implementation.md) — the file system implementation's account of why the read/write position could live neither in the per-file structure nor in the per-process list of open files, and why a separate table was introduced whose sole purpose was to hold it.
