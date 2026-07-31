---
type: lesson
title: "Export the default and the parts it was assembled from"
figure: wirth
works: [project-oberon]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Export the default and the parts it was assembled from

**Lesson:** A module that offers one complete, working behaviour has answered the common case and forbidden every other one. A module that offers only the pieces has answered nothing and made every client reassemble the common case, badly and differently. The resolution is not a compromise between the two but doing both deliberately: publish the assembled default as the smallest thing a client needs to be useful, and publish, alongside it, the individual operations out of which that default was constructed. The default is then not a wall but a worked example — a client who needs a variant writes their own assembly, substituting the one step that differs and calling the published ones for everything else.

What makes this more than a convenience is the effect on the cost of a variant. Where only the whole is exported, the cheapest way to change one behaviour is to reimplement the whole, which means the variant immediately stops tracking improvements to the original and becomes a second thing to maintain. Where the parts are exported too, a variant costs exactly the part that differs, and everything unchanged stays shared — so the distance between the standard behaviour and a custom one is proportional to how much actually differs, which is the property you want and almost never get by accident. It also disciplines the original: to export the parts at all, they must be separable, individually meaningful, and callable without hidden mutual state, which is a stricter constraint than merely working when run in the fixed order the default happens to use.

The design move that pays for this is upstream of the interface. Write the default behaviour as a dispatch that does nothing itself and calls named operations for each case it recognizes, rather than as a body of inlined logic. Then the parts already exist as named procedures before anyone asks to reuse them, and exporting them is a decision about visibility rather than a refactoring. Aim for the split where each exported part corresponds to one externally recognizable event or one externally meaningful operation, since those are the boundaries a client's variant will actually want to cut on — a client wants to change what happens on one kind of request, not to intervene halfway through one.

**Source:** [Project Oberon](../works/project-oberon.md) — section 5.3, where module TextFrames first exports the minimum needed to use standard text frames (the frame and location types, the standard message handler, the update message, and the two constructors for menu and contents frames), and then additionally exports the set of service procedures — the built-in editor call, character insertion, defocus, neutralize, selection retrieval, copy-over, clone, modify, update, and the four mouse-tracking procedures — stated as being there to support composing custom handlers out of elements of the standard one; together with the preceding presentation of the standard handler itself as a dispatch over message types in which each branch does nothing but call one of those named procedures.
