---
type: lesson
title: "Give a value one representation for processing and another for transport, and make the conversion an explicit phase"
figure: hoare
works: [notes-on-data-structuring]
axes: [hardware-affinity, cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Give a value one representation for processing and another for transport, and make the conversion an explicit phase

**Lesson:** A structure that is convenient to walk around in is not the structure that should leave the machine, and trying to make one form serve both jobs means doing both badly. The form built for processing scatters its parts and connects them by addresses, because that is what makes any component reachable from any other in one step, and what lets several structures share a common part. The form built for transport lays everything out end to end and recovers the structure from position and from the marks the values carry, because that is what makes it compact and what makes it meaningful somewhere else. The two are not competing candidates for a single decision. They are answers to different questions, and the honest design keeps both and converts between them at the boundary.

The reason the transport form cannot simply be the processing form written out is that an address means nothing outside the space it came from. Anything that has to survive being written down and read back — sent over a link, filed away, handed to the next stage — must have had its internal references re-expressed as something intrinsic to the data, and re-expressing them is real work with real decisions in it. When that work is not made a phase of its own, it gets improvised at each site that needs it, and every one of those sites gets to invent its own answer to the same question. The compactness argument reinforces the same conclusion from the other side: dropping the addresses and packing the components can shrink a structure by an order of magnitude, which is worth having on any path where the volume is what costs.

So expect a long-lived system to translate between representations repeatedly — read in, expand into the working form, process, collapse for the next stage, and again. That looks wasteful until you notice the alternative: one compromise representation that is slow to traverse and awkward to move, chosen so nobody has to write the converters. Building the converters is the cheaper trade, and it has a second benefit worth naming, which is that the transported form becomes the interface between phases. Once it exists as a written-down thing rather than a memory layout, phases can be replaced independently.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the representation section of the chapter on recursive data structures, which contrasts the pointer-based tree form (favoured when the structure is being processed, and permitting shared branches) with the linear bitstream form (avoiding pointers, roughly an order of magnitude more compact, and preferred whenever the structure must be output and later re-input because it sidesteps the difficulty of representing pointers on backing store), and notes that a structure passing through several phases of processing and input-output is commonly translated between the two at each phase, as in a multipass language translator.
