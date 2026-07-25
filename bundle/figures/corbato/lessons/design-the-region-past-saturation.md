---
type: lesson
title: "Design the Region Past Saturation"
figure: corbato
works: [an-experimental-time-sharing-system, on-building-systems-that-will-fail]
axes: [verifiability, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, algorithms-and-complexity]
tags: [lesson]
---
# Design the Region Past Saturation

**Lesson:** Every resource policy has a load above which demand exceeds what the hardware can supply. Corbató's point is that what happens in that region is a design decision you either make on purpose or make by accident. The obvious round-robin makes it by accident and makes it badly: past the critical user count, service does not slowly worsen, it collapses, because the cost of moving programs between fast and slow storage suddenly swamps the useful work. So he treats the shape of the curve beyond saturation as part of the specification, and asks for progressive, predictable erosion concentrated on the largest and longest-running jobs rather than an even collapse for everyone.

The technically interesting part is that he gets graceful degradation and provability from the same structure. Because the geometric level scheme guarantees each program runs at least as long as it takes to move it, the efficiency floor is derivable rather than measured. Because the worst case is fully occupied lower levels, a response-time bound follows as a function of the active user count and the largest program size — invertible, so a required response time yields a capacity limit. Because a job's relative movement overhead shrinks as it cascades downward, the asymptotic overhead becomes a tunable percentage. None of these are benchmark results. They are consequences of how the mechanism is built, and that is the reason to prefer this mechanism over one that merely performs well in the comfortable range.

A programmer who takes this seriously writes down the overload behavior next to the nominal behavior, and when choosing between two mechanisms prefers the one whose worst case falls out of its structure. Corbató is careful about the limits, too: he notes that his capacity estimates hinge on distributions of think time and program size that past experience cannot supply, because the distributions themselves will be reshaped by whatever system you build. The bounds are trustworthy; the numbers you plug into them are not.

**Source:** [An Experimental Time-Sharing System](../works/an-experimental-time-sharing-system.md) — the multi-level scheduling algorithm section, from the qualitative saturation argument through the five enumerated performance bounds. The Turing lecture's closing recommendation to anticipate failure modes and develop contingency paths is the same instinct applied beyond resource exhaustion.
