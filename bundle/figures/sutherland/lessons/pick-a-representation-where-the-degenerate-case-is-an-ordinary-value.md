---
type: lesson
title: "Pick a representation where the degenerate case is an ordinary value"
figure: sutherland
works: [a-head-mounted-three-dimensional-display]
axes: [expressiveness, primitive-count, verifiability]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
tags: [lesson]
---
# Pick a representation where the degenerate case is an ordinary value

**Lesson:** A geometry system has to cope with points that are arbitrarily near and points that are effectively at infinity, and with the fact that translation and rotation are different kinds of operation. The naive representation makes each of those a separate problem: a special branch for the far case, a divide-by-zero to guard, two composition rules to keep straight. Sutherland's system instead carries an extra scale component alongside each coordinate, and the awkward cases stop being cases at all — the infinitely distant point is just a particular value of that component, and translation and rotation collapse into a single uniform multiply. Nothing in the hardware has to know that anything unusual happened.

The principle is that the shape of your representation decides how many exceptions your code must contain. Special cases are not intrinsic to a problem; they are artifacts of a coordinate system that cannot express certain states as interior points of its own domain. Enlarge the representation slightly, in the right direction, and states that had to be handled by branching become states that are handled by the ordinary path. This is also why the choice pays off in hardware: a uniform operation with no data-dependent branching is exactly what a fixed pipeline can execute at constant cost.

What the programmer does differently is treat a proliferating pile of edge-case branches as evidence against the representation, not as work to be done. When the third guard clause appears, the question is not "what else must I check" but "what value am I unable to name." A missing element, an unbounded interval, an empty selection, a not-yet-known timestamp, an identity transform: if the type can hold each of these as a legitimate value, the branches disappear along with the class of bugs that comes from forgetting one. The cost is a representation slightly larger and slightly less obvious than the naive one, which is a real price and usually a bargain, because the number of paths through the code is what actually has to be reasoned about and tested.

**Source:** [A Head-Mounted Three Dimensional Display](../works/a-head-mounted-three-dimensional-display.md) — the argument is in the description of how drawing data is stored in the room coordinate system, where the extra scale component absorbs both distance extremes and lets one matrix operation cover both kinds of transform.
