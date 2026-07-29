---
type: lesson
title: "Let stages negotiate locally instead of scheduling them globally"
figure: sutherland
works: [a-head-mounted-three-dimensional-display]
axes: [parallelizability, hardware-affinity, verifiability]
subdomains: [programming-environments-and-object-systems, concurrency-and-distribution]
tags: [lesson]
---
# Let stages negotiate locally instead of scheduling them globally

**Lesson:** The display path in Sutherland's system is a chain of separate units, each doing one transformation and handing the result along. The interesting choice is that no central authority sequences them. Each unit knows only two things: whether its input has arrived, and whether its output has been taken. It waits on the first, signals the second, and the signal it raises is precisely the signal its successor waits on. Composition is achieved by wiring adjacent pairs together, not by writing down a schedule that mentions all of them. The consequence is that the whole assembly runs at whatever rate its current bottleneck permits, and the bottleneck is allowed to move around as the data changes — one unit's cost varies with what it is asked to clip, another's varies with the length of the line, and none of them needs to know that.

This works because a global schedule requires global knowledge of timing, and timing is the thing most likely to be data-dependent, most likely to change when any single component is improved, and least likely to be knowable in advance. A local handshake requires only that each pair of neighbors agree on readiness, which is knowledge each of them actually has. It is the difference between a system whose correctness depends on a worst-case timing estimate holding, and one whose correctness depends only on a protocol that cannot be wrong about whether a value is present.

There is a second payoff that the paper is explicit about, and it is the one people skip: because each unit synchronizes for itself, each unit can also be driven on its own or bypassed entirely. That was what made the thing debuggable at all. A pipeline whose stages are only reachable by running the entire pipeline gives you one experiment; a pipeline whose stages are separately addressable gives you one experiment per stage, and the ability to answer "which stage is lying" by direct measurement rather than by inference.

The programmer who takes this seriously builds concurrent systems out of components that block on their own inputs and announce their own completions, rather than out of components a coordinator calls in a fixed order at times it computes. They also insist that every stage be runnable alone, with a real input and an inspectable output, and they treat inability to do so as a design defect rather than a testing inconvenience.

**Source:** [A Head-Mounted Three Dimensional Display](../works/a-head-mounted-three-dimensional-display.md) — this is the section describing how the transformation, clipping, and line-drawing units are interlocked by input and output flags, including the remark about configuring or bypassing individual units.
