---
type: lesson
title: "Build the richer mechanism on top of the plainer one, never inside it"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [primitive-count, cognitive-load, hardware-affinity]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Build the richer mechanism on top of the plainer one, never inside it

There is a specific reasoning error that produces components nobody can afterwards take apart, and its distinguishing feature is that it does not feel like a shortcut at the time. Two capabilities are related, both are small, and separating them looks like ceremony out of proportion to their size — so they go into one component. Often there is even a quality argument for the merge: doing them together is safer, or more consistent, than allowing them to be done independently. The cost lands much later, when someone needs one of the two capabilities in a context where the other one is expensive or meaningless, and finds there is no route to it. The pairing that seemed too trivial to be worth a boundary has become a permanent constraint on every configuration.

What makes the error avoidable is that a better arrangement was available and cost nothing extra. The richer, safer, more disciplined mechanism can almost always be constructed as a separate thing that rests on the plain mechanism, rather than as a plain mechanism with the extra behavior welded into it. Same functionality when you want it, plus the plain one still standing on its own for the cases where it suffices. The irony Parnas draws out is that it is the more powerful facility whose separate existence is being sacrificed by the merge — the extra strength gets bought at the price of making the weaker version unobtainable, when the layered arrangement would have delivered both.

Generalizing, treat any argument of the form "these are too simple to separate" as a claim about implementation effort masquerading as a claim about design, and answer it with the configuration question instead: is there a plausible system that wants one of these and not the other. Where a safety property is what motivates the fusion, ask whether the property can be established outside the mechanism rather than enforced inside it — a check that some clients can discharge earlier and more cheaply than at the point of use is exactly the sort of thing that should live above the mechanism, not within it, so those clients can decline to pay. Component size is no defense here. The number of configurations a merge forecloses is unrelated to how much code the merge saved.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the discussion of components that perform more than one function, with its example of synchronization fused with message sending and acknowledgment, its example of run-time type checking built into the basic call mechanism, and its closing observation that the more powerful mechanism could have been built separately from but using the simpler one.
