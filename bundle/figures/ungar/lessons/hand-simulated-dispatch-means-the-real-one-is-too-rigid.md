---
type: lesson
title: "Code that hand-simulates a mechanism the system already has is evidence the mechanism is too rigid, not that the code is sloppy"
figure: ungar
works: [organizing-programs-without-classes]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
tags: [lesson]
---
# Code that hand-simulates a mechanism the system already has is evidence the mechanism is too rigid, not that the code is sloppy

A recurring shape in real programs: a field records which of several modes an entity is currently in, and every operation that depends on the mode opens with a test on that field. The usual reading is that this is undisciplined code. The more useful reading is that it is a faithful, manual re-implementation of selection-by-kind — the exact service the system's own dispatch already provides — and that the programmer resorted to building it by hand because the built-in version cannot do the one thing this situation requires: change which kind an entity is, while the entity is alive.

Once you see it that way, the pathologies are predictable rather than incidental, and they are the same pathologies that motivated dispatch in the first place: adding a mode means editing every site that tests the flag, any single mode's logic is scattered through code belonging to other modes, and the compiler cannot help because the branching is data, not structure. The fix is not to write the conditionals more neatly. It is to make the real mechanism mutable — to let the thing that determines an entity's behavior be an ordinary assignable reference rather than a fixed property stamped in at creation. Then switching modes is one store, each mode's logic sits in its own place, and adding one touches nothing existing.

This inverts a common intuition about run-time mutability. Letting an object change what it inherits sounds like an invitation to chaos, and it can be; but the alternative, in practice, is not discipline — it is the same variability re-encoded as conditional logic where it is far less visible and far harder to extend. Used in the narrow, stylized way of selecting among a small fixed set of behavior sets, the dynamic version makes the structure of the program *more* apparent, because each mode is a nameable, browsable thing rather than a value that some conditionals happen to compare against.

The transferable habit is to treat every hand-rolled dispatcher as a design report. A lookup table of function pointers keyed by type tag, a chain of type tests, a switch on an enum that mirrors a class hierarchy — each is a programmer routing around a mechanism whose parameters were frozen at the wrong time. Before optimizing or tidying such code, ask what the built-in mechanism refuses to let vary, and whether that thing could safely become variable. Often the entire structure collapses into a single assignment.

**Source:** [Organizing Programs Without Classes](../works/organizing-programs-without-classes.md) — the section on dynamic behavior changes, which explicitly likens mode-flag testing to simulating method dispatch by hand and then locates the blockage in the fixed binding between an entity and the source of its behavior.
