---
type: lesson
title: "Solve a coarse version first, carry the answer forward, and pay for a repair step you can bound"
figure: karp
works: [theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Solve a coarse version first, carry the answer forward, and pay for a repair step you can bound

**Lesson:** Faced with a problem whose difficulty comes from the precision of its numbers, Karp and Edmonds do something a working engineer should steal wholesale: throw away most of the precision, solve the crude problem that remains, then reintroduce precision one digit at a time, using each stage's answer as the starting point for the next. Two things make this pay. Working at a coarse scale means every step of progress is a large step, so there are far fewer of them. And the answer to the coarse problem is nearly the answer to the finer one, so each stage begins close to where it needs to end rather than from nothing. Cost stops tracking the values in the data and starts tracking how many digits those values occupy.

The part that makes this an honest engineering lesson rather than an appealing sketch is what happens at the seam. Scaling the coarse answer up gives you something valid but not quite correct for the finer problem, off by at most a small amount on any single element. So the method needs a repair procedure, and the repair needs a proof it terminates. What they build is a numeric measure of how far each element is from being correct, plus a step that provably drives the total measure down by at least one whole unit each time it runs. Since the total starts small and cannot go negative, the number of repairs is bounded before you ever run it. That pattern is the reusable part: define a scalar that measures wrongness, make each repair strictly decrease it, and termination stops being a hope.

A programmer with this habit stops treating hard instances as monolithic. Solve at low resolution, warm-start the next resolution from the last one, and keep a bounded reconciliation step at each transition. It is the same structure as a coarse-to-fine numerical solve, an approximate index consulted before an exact one, or a cached plan adjusted rather than recomputed. The failure mode to watch for is the one they were careful about: a warm start you cannot repair with a bounded amount of work is not a shortcut, it is an unbounded correction loop wearing a shortcut's clothes, and the monotone measure is what tells the two apart.

**Source:** [Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems](../works/theoretical-improvements-in-algorithmic-efficiency-for-network-flow-problems.md) — the scaling sections, which state the two features the technique relies on, and the accompanying repair algorithm built around a per-element wrongness count whose total strictly decreases with each application.
