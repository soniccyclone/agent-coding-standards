---
type: lesson
title: "Delete the privileged default so the general path is the only path"
figure: thompson
works: [plan-9-from-bell-labs]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Delete the privileged default so the general path is the only path

A system that supports many configurations almost always has one it treats as normal: the machine you are sitting at, the architecture you compiled on, the byte order you happen to use. Everything else is reached through a path labeled cross-, remote-, or foreign-, and that path rots, because the people maintaining the system do not travel it. Plan 9's response is to abolish the privileged case rather than to test it more carefully. There is no unqualified compiler command; each target's toolchain is named for its target and the intermediate files carry the target in their names, so from the compiler's own point of view every compilation is a cross-compilation and the concept of building for the local machine does not exist as a distinct mode.

The same move recurs everywhere in the system. Data moves between programs as text where at all practical, so byte order is not a property anyone can accidentally depend on; where volume forces a binary encoding, structures are never handed over as memory images but taken apart into fields, transmitted in a defined order, and rebuilt — so the layout an individual compiler chose can never leak into an interchange format. State that a conventional kernel would expose as packed flags is presented as text through the same interface used for everything else, which means the tool that reports on local processes reports on a remote machine's processes with no code path of its own.

The principle underneath is about which paths get exercised, not about elegance. Correctness of a rarely taken branch decays at a rate set by how rarely it is taken, and the reliable way to keep the general case working is to make it the case everyone is in. This costs something visible up front: names get longer, the easy local shortcut is unavailable, and the common operation pays a little of the general operation's overhead. That cost is the premium on never discovering, six months in, that the portable path was never really portable.

A programmer who believes this becomes suspicious of any convenience that exists only for the situation the authors happen to be in. They will look for the default that lets the general mechanism go untested and remove it, accepting the small tax, rather than adding tests to defend a branch that most contributors will never run. The related instinct: when a fast local case must be kept for performance, keep it as an implementation of the general interface rather than as a second interface — the paper is candid that where it failed to do this, it was left with a dichotomy it describes as an accident of history rather than a design.

**Source:** [Plan 9 from Bell Labs](../works/plan-9-from-bell-labs.md) — the portability and compilation section, where target-specific tool names make every build a cross-build and interchange is defined to be byte-order-independent, reinforced by the portability discussion of representing process state as text.
