---
type: lesson
title: "Give each attribute one legal direction of inquiry, and forbid the other"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Give each attribute one legal direction of inquiry, and forbid the other

**Lesson:** In any containment hierarchy there are two obvious questions about size and placement: how much room does this part want, and how much room did it actually get. The naive design lets anyone ask either question of anyone. That design deadlocks or loops, and it does so for a reason worth understanding rather than patching: the two questions have opposite owners. What a part wants is something the part alone can answer, so the query must travel from container down to part. What a part got is something only the container knows, since allocation happens above, so that query must travel from part up to container. Wire either question in the wrong direction and the answer either does not exist or is a request for the answer you are in the middle of computing.

The discipline that falls out is stronger than a convention: for each attribute, name the single direction in which it may be asked, and state the reverse query as prohibited. Two things come free. Termination becomes structural instead of accidental — a query that only ever moves one way through a tree cannot cycle, so recursion is bounded without a depth counter, a visited set, or a lock. And storage becomes decidable: if a part may ask upward at any time, the part need not remember the answer, which removes a cache and every staleness bug that a cache brings. The prohibition is also the more useful half of the rule to write down, because a permitted query is discovered naturally by anyone who needs it, while a forbidden one is discovered only by the person who tries it and gets a hang.

The reason to state the reverse case as *meaningless* rather than merely unsupported is that it prevents the sympathetic-sounding extension. A container asking its parts what they were allocated is not a missing feature; it is the container asking someone else to recite a fact the container itself authored, and any value that comes back is either a copy of what the container knows or a lie. Treating it as meaningless closes the request permanently; treating it as unimplemented invites someone to implement it.

Generalize past layout and the shape is the same wherever a hierarchy carries derived facts: requests and desires flow one way, allocations and grants flow the other, and the whole class of circular-dependency bugs comes from letting a value be interrogated from both ends. The design question for each field becomes not "who stores this" but "who is entitled to be asked."

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 9 section 9.6, which defines virtualBounds as the area a visual part requires (a container may ask its components; a component is explicitly prohibited from asking its container, to avoid infinite recursion) against actualBounds as the area a container allocates (a component may ask its container at any time and therefore need not remember it, while a container asking its components is called dangerous and meaningless).
