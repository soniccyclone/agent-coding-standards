---
type: lesson
title: "An offline tool is often the online mechanism with a different sink"
figure: wirth
works: [project-oberon]
axes: [primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# An offline tool is often the online mechanism with a different sink

**Lesson:** Systems accumulate pairs of components that do the same intellectual work at different times: the thing that resolves references when a component is brought in, and the thing that resolves references ahead of time to produce a pre-linked image; the thing that renders for a screen and the thing that renders for a printer; the thing that applies a change now and the thing that records it for later. These are usually written twice, by different people, and they drift — not in the interesting part, which both get right, but in the corners, where one handles a case the other silently does not, and the difference shows up as an image that behaves unlike the live system.

Before writing the second one, check whether it differs from the first only in where its output goes. Often it does: the analysis, the ordering, the fixups and the address arithmetic are all identical, and the sole distinction is that one deposits results into freshly obtained storage at addresses discovered as it proceeds, while the other deposits them into one contiguous region whose base is a constant and which is emitted as a unit at the end. That is a difference in a destination, not a difference in an algorithm. Factor the destination out — an abstraction offering "place these bytes at this offset" is usually enough — and the second tool becomes a short program that supplies a different sink and a different start-address policy.

The gain is not the code saved, which is modest, but the guarantee that the two agree. A pre-built image produced by the same logic that would have produced the live arrangement cannot disagree with it about layout, about what a reference means, or about which cases are handled, because there is no second opinion to disagree with. That property is what makes the offline artifact trustworthy enough to sit at the bottom of a boot, where no diagnostic exists to tell you it was wrong. And the discipline is self-checking in a useful way: if the two really do not share an algorithm, the attempt to unify them will show you exactly where the semantics diverge, which is a thing worth knowing whether or not you go on to merge them.

**Source:** [Project Oberon](../works/project-oberon.md) — section 14.2's description of the boot linker, said to be almost identical to the module loader except that object code is not deposited in newly allocated blocks but in a fixed buffer which is finally output to form the boot file, with the load addresses of its blocks given as constants in the tool.
