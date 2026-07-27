---
type: lesson
title: "Optimize against the machine's real cost hierarchy, not the operation you can see"
figure: torvalds
works: [linux-kernel-coding-style]
axes: [hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming]
tags: [lesson]
---
# Optimize against the machine's real cost hierarchy, not the operation you can see

**Lesson:** The style guide's treatment of inlining is a compact lesson in how performance intuition goes wrong. The intuitive model is local and additive: each call eliminated saves a call, therefore eliminating more calls is monotonically better. The document dismantles this by changing the unit of accounting. Duplicated bodies inflate the total size of the resident code, which worsens instruction-cache behaviour and, more brutally, leaves less memory for cached file data — and a single extra fetch from rotating storage costs more time than an enormous number of instructions. The local saving is real and the global loss dwarfs it by orders of magnitude. Nothing about the reasoning is specific to that one keyword; it is a demonstration that a change's cost must be evaluated at the level where the scarce resource actually lives.

The same pattern recurs elsewhere in the document with different resources. A convenient boolean type is endorsed for readability but forbidden in structures whose layout matters, because its size and alignment are not fixed across targets and layout decisions are made against cache lines, not against source readability. Many independent flags are better packed into bits than stored as separate values. Hand-written assembly is neither romanticized nor banned: use it when the hardware genuinely requires it, keep it out of places where compiled code does the job, and factor recurring fragments into helpers instead of scattering variants — and be aware that pinning a fragment down to stop the compiler discarding it also stops the compiler improving it. Each of these is a judgment that only makes sense once you know which physical resource is the binding constraint.

The most useful part is the epistemic humility about the compiler. The advice is to stop supplying hints for decisions the compiler already makes correctly, both because the hint is redundant and because it becomes a maintenance obligation that will be forgotten when circumstances change. A person's model of a modern optimizer is worse than the optimizer, and the places where human knowledge genuinely beats it are narrow and identifiable — chiefly where you know something about a value at compile time that the compiler's analysis cannot see.

A programmer who believes this stops reasoning about speed in units of source-level operations. Before changing anything for performance, they name the resource under pressure — cache footprint, memory bandwidth, a device round trip — and estimate the change's effect in that currency. They also treat every manual hint to the toolchain as a claim they must be able to defend, and delete the ones they cannot.

**Source:** [Linux Kernel Coding Style](../works/linux-kernel-coding-style.md) — the chapter on inlining, which reprices the local call-elimination win against instruction-cache and page-cache pressure and against storage latency; the boolean chapter's carve-out for structures where size and alignment matter; and the inline-assembly chapter's guidance on when hardware access genuinely demands it.
