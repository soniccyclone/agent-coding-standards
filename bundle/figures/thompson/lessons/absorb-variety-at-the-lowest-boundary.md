---
type: lesson
title: "Absorb hardware variety at the lowest boundary so nothing above it has to know"
figure: thompson
works: [the-unix-time-sharing-system]
axes: [primitive-count, cognitive-load, hardware-affinity, expressiveness]
subdomains: [operating-systems-and-systems-programming]
tags: [lesson]
---
# Absorb hardware variety at the lowest boundary so nothing above it has to know

**Lesson:** Every system that touches real devices faces the same question: where does the diversity of the hardware get handled? The usual answer is that each program learns about each device, either by linking in the code to drive it or by asking at runtime which kind of thing it is talking to. Thompson and Ritchie took the opposite position, that the diversity should be flattened once, at the very bottom, and that everything above should see a single shape. A device gets a name in the same namespace as stored data, obeys the same access-control rules, and answers the same handful of calls. Sequential and random access stop being separate categories. No record structure is imposed, so no program has to negotiate one.

The reason this holds is an argument about where cost accumulates rather than about elegance. If distinctions survive upward, every program pays for them, and it pays repeatedly, because each new device multiplies the number of program-device pairs someone has to get right. Flattening at the boundary costs once. The paper makes this trade explicit when it considers the alternatives to putting device knowledge in the kernel: carry per-device code in every program, or resolve it dynamically, and both are worse in space or in overhead. The choice also buys a property nobody asked for at design time, which is that a program written to consume stored data can be handed a device instead and simply works, because the argument it accepts was never a kind of thing but a name.

A programmer who believes this stops asking what capabilities each caller needs and starts asking what the narrowest uniform shape is that all the underlying variety can be squeezed into. When the variety refuses to squeeze, that refusal is treated as information about the abstraction being wrong rather than as a reason to leak a type tag upward. The practical tell is a function whose behavior branches on what kind of source it was given: that branch belongs one layer down, written once, not replicated in every caller.

**Source:** [The UNIX Time-Sharing System](../works/the-unix-time-sharing-system.md) — this thinking lives in the treatment of special files as ordinary members of the hierarchy and in the retrospective section's accounting of why device knowledge was pushed into the kernel rather than into programs.
