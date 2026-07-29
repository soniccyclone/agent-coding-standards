---
type: lesson
title: "The rate at which you cross a threshold changes the outcome, not just the time it takes to get there"
figure: turing
works: [the-chemical-basis-of-morphogenesis]
axes: [hardware-affinity, verifiability]
subdomains: [foundations-of-computation, operating-systems-and-systems-programming]
tags: [lesson]
---
# The rate at which you cross a threshold changes the outcome, not just the time it takes to get there

**Lesson:** Arguments of the form "eventually the dominant mode wins and everything else is negligible" are correct and nearly useless on their own, because they say nothing about when. A competition between growing modes has a settling time set by how fast the leader pulls ahead of its nearest rival, and if the system is driven past its threshold faster than that settling time, the outcome is a mixture of contenders rather than the clean winner the asymptotic analysis promised. The same rules, the same parameters, the same final state — pushed through the transition quickly you get an irregular blend, pushed through slowly you get the mode the theory predicted. Rate is a parameter of the result.

This holds because the asymptotic claim quietly assumes the system was allowed to run undriven long enough for exponential separation to do its work. Every such claim therefore owes you an estimate of the separation rate, which is usually a difference between the two closest competitors and thus small — much smaller than either growth rate. Small differences mean long settling times, so the window where the asymptotic answer is wrong can be most of the system's actual life.

For a programmer this reframes anything with a convergence story. A cache warms, a load balancer's weights settle, a distributed system's membership stabilizes, an autoscaler finds its level — and each of those "settles to X" claims is only true if you are not changing the input faster than the convergence rate. So when you ramp load, roll a config change, or move a tuning knob, the ramp speed belongs in the design and in the test plan, and the honest version of any equilibrium claim carries a time constant next to it. The habit to build: whenever you write down "eventually", compute the rate that makes "eventually" arrive, then compare it to how fast the world you live in actually moves.

**Source:** [The Chemical Basis of Morphogenesis](../works/the-chemical-basis-of-morphogenesis.md) — the finer-points discussion of how far the fastest-growing component outruns its neighbours, cashed out in the worked numerical example whose two "cooking speeds" yield an irregular pattern versus a clean one from identical chemistry.
