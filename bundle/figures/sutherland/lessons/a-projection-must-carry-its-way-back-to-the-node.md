---
type: lesson
title: "A projection is only usable if it carries the way back to the node that made it"
figure: sutherland
works: [the-ultimate-display]
axes: [expressiveness, cognitive-load, hardware-affinity]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# A projection is only usable if it carries the way back to the node that made it

Anything a program shows a person is a projection: a structured, nested, richly typed thing in memory gets flattened onto a surface with no notion of parenthood or type. Sutherland's sharpest practical observation is that pointing at that surface is not a graphics problem at all, it is an identity problem, and the flattening is what makes it hard. Two dimensions admit no useful ordering by neighborhood, so recovering "which thing is this" from a coordinate afterwards means searching, and the search gets worse as the structure gets richer. The fix he describes is not a cleverer search — it is arranging for the act of drawing to hand back the address of whatever it drew. The inverse map has to be produced by the forward pass, because it cannot be reconstructed cheaply once the forward pass has thrown its context away.

The part that generalizes beyond displays is his complaint that even an address is not enough. What the program needs is not the coordinate, not the identity of the leaf, but which subpart of which part the person meant — the position in the hierarchy, several levels of nesting deep. Selecting the line is a different act from selecting the figure the line belongs to, and from selecting the instance of that figure. Any layer that emits a flat stream of leaves has silently decided that only one of those selections is expressible. This is the recurring failure mode of log lines, stack traces, error messages, generated code and compiled output: the artifact reaches the person with its ancestry stripped, and every question worth asking is about the ancestry.

He then notes something worth taking as a general warning. A newer display technology, one with an analog store, would be better on the axis its builders were optimizing and would lose the pointing ability altogether. Substrate changes are usually evaluated by what they add, because that is what the people who built them are proud of. The affordance that quietly disappears is not on anyone's comparison table, and it is often the one that made the whole interaction possible.

A programmer who takes this seriously designs the return path at the same moment as the output path. Every rendering, serialization, diagnostic or transformation stage gets asked one question before it ships: given a thing a person or a tool picks out of my output, can I name the exact node at the exact level of nesting that produced it, without a search? If the answer is no, the correction belongs in the emitting stage — thread the provenance through — and not in a downstream heuristic that guesses at what was thrown away.

**Source:** [The Ultimate Display](../works/the-ultimate-display.md) — the middle section on pointing, where he moves from coordinate-to-object conversion, to light-pen interrupts returning an address, to needing depth of recursion, and closes on analog-memory displays forfeiting pointing.
