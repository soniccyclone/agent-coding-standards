---
type: lesson
title: "Move the computation into the arithmetic the machine is good at"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, primitive-count]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Move the computation into the arithmetic the machine is good at

**Lesson:** A problem stated mathematically comes with an implied numeric domain, and that domain is a property of the statement rather than of the answer. A shape defined by an equation over the reals suggests real arithmetic; but the thing actually wanted is a sequence of positions on a discrete grid, every one of which is an integer, and every one of which is close to its predecessor. Two facts follow that the equation does not advertise: the outputs live in a cheaper domain than the equation does, and consecutive outputs differ by a small, bounded amount. Together they license a reformulation in which nothing but integers is ever computed — you never evaluate the defining relation at all, you carry a quantity that records how far the current position has drifted from the ideal, and each step consults its sign to decide which of a small number of neighbours to take next.

The transferable move is to stop treating the numeric domain as given and to ask instead what domain the answers occupy and what domain the *differences between successive answers* occupy. Those are often both cheaper than the domain the specification is written in, because a specification describes the whole object at once while an algorithm produces it one step at a time, and a step is a much smaller thing than a value. Wherever a computation walks through adjacent cases, look for a running quantity whose update is a few additions and whose sign answers the question the expensive evaluation was being asked. When you find one, the cost per step collapses to what the machine does in a cycle, and the loss of the general formulation costs nothing because you were only ever going to ask it about adjacent points.

The discipline generalises past graphics: fixed-point instead of floating-point where the range is known, integer ratios instead of division, differences instead of absolute recomputation, comparison of squares instead of taking roots. Each is the same trade — accept a formulation that is less faithful to the mathematics and exactly as faithful to the required outputs. The check that keeps this honest is to state up front which properties of the answer must hold exactly, because a cheaper domain is only free when the answers it produces are the same answers, not merely close ones.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.9.2's account of module Curves, which draws oblique lines, circles and ellipses using Bresenham algorithms specifically in order to avoid computations involving floating-point numbers and to increase efficiency.
