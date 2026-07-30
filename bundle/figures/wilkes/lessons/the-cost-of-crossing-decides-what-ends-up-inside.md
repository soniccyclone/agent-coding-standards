---
type: lesson
title: "The cost of crossing a boundary decides how much ends up inside it"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [primitive-count, hardware-affinity, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# The cost of crossing a boundary decides how much ends up inside it

**Lesson:** If invoking a trusted core is expensive, its clients will avoid invoking it, and the way they avoid it is by asking for larger, more compound operations that accomplish in one crossing what would otherwise take many. Those compound operations get implemented inside the core. So the core grows, its internal complexity grows, and the probability that it contains an error grows with it — all driven by the crossing cost, not by anyone's design intent. The chain is worth stating explicitly because each link looks like a local optimization: expensive primitives, fewer calls, richer calls, bigger trusted base, more defects in the one place defects are least affordable.

The lever, then, is the crossing cost itself. Make a boundary cheap to cross and the pressure to move functionality across it disappears, which is what keeps the inside small. This inverts the usual framing where efficiency and minimality are traded against each other: here the efficiency of the boundary is the *mechanism* by which minimality is achieved, and the two are the same objective. Where a crossing is intrinsically expensive because it is emulated by software over a substrate that does not support it, the productive response is to move the boundary's implementation into the substrate rather than to make peace with a large core.

The corollary for anyone publishing a component is to state the cost of your primitives as a ratio against the cheapest operation available, because that ratio is what determines how programs above you will be structured. A facility priced at a few times the baseline will be called freely and in fine grain; one priced at a thousand times will be routed around, batched, and cached, and the shape of every client will be distorted accordingly. The number is a design constraint you are imposing on everyone downstream, so it belongs in the specification rather than in a footnote about performance.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Appendix 1's opening analysis, which observes that software emulation of protection operations is orders of magnitude slower than a hardware procedure call, that the resulting inefficiency of kernel primitives encourages implementing complex compound functions inside the kernel to reduce the number of calls, and that this increases kernel complexity and correspondingly the probability of errors; together with the appendix's measured costs of each primitive expressed as multiples of a simple load instruction.
