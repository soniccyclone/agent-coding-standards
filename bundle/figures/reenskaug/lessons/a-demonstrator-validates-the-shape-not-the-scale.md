---
type: lesson
title: "A demonstrator validates the shape of an answer, not its scale — so enumerate what it left out"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# A demonstrator validates the shape of an answer, not its scale — so enumerate what it left out

**Lesson:** A proposal for how an entire industry might organize its software production was demonstrated with a running system of eighteen objects. The author's own description of it is that in terms of the actual domain it is ridiculously simple, and that it was sufficient to illustrate the one thing it was built to illustrate: how actors and technologies match up across the layers. Both halves of that sentence are load-bearing. The system was not a small version of the real thing, and it was not offered as evidence that the real thing would work at size. It was evidence about the *structure* of the proposal — that each layer has a coherent job, that the handoffs between them are expressible, that every technology has a place.

Being clear about which claim a demonstrator supports is what keeps it honest, and the failure in both directions is common. Present a small system as proof of feasibility and you have overclaimed, since almost nothing that breaks at scale is visible at eighteen objects. Dismiss it as a toy and you have missed that structural claims are genuinely testable small: a decomposition that cannot be made to work at all in miniature will not be rescued by more of it, and finding that out cheaply is exactly what the exercise is for.

What makes this instance exemplary is the accompanying inventory of omissions, stated at each point rather than gathered into a caveat nobody reads. An entire layer was left out to keep things simple, and the reader is told which figure it is therefore missing from. Two functions were bundled into one module that a real system would factor apart for reuse. The contract document is said to need more work before it could serve a real sales operation. The module structure is said to require careful construction and many more modules at real size. And the whole thing is quantified — a table of class count, method count, line count — so nobody has to guess what "simple" meant. That inventory is the deliverable that makes the demonstrator trustworthy, because it converts the gap between the demo and reality from something a reader must estimate into something the author has already measured.

The reflex to take: before building a demonstrator, write down which claim it will support, and while building it keep a running list of every simplification made. Publish the list next to the result. A prototype without its list of omissions is not modest, it is unreadable — a reader cannot tell what was solved from what was skipped, so they must either trust everything or nothing.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — chapter 12's account of the TINA-93 demonstration: the running system consisted of 18 objects, "ridiculously simple in terms of telecommunications technology, but sufficient to illustrate how we match actors and technology in the IN value chain"; section 12.3's note that Subscribers were omitted to keep the initial system simple and so do not appear in figure 12.3; section 12.4's admission that more work is needed before the contract document could be used in a real marketing operation; section 12.6's note that in a full size system two bundled functions would be factored into separate modules for reuse, that scaling up will require organizing constituents into a large number of modules assigned to well-defined sublayers, and the program statistics table giving 38 application-specific classes, 314 methods and 988 lines.
