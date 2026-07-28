---
type: lesson
title: "A program can be entirely correct and still have decayed into worthlessness"
figure: parnas
works: [software-aging]
axes: [verifiability, hardware-affinity]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A program can be entirely correct and still have decayed into worthlessness

**Lesson:** There is a comfortable argument that software cannot deteriorate: it
is a mathematical object, and mathematical truths do not rot, so a program that
satisfies its specification today satisfies it forever. The argument is sound and
almost useless. Correctness is a relation between a program and a statement of
what was wanted; usefulness is a relation between a program and a world that
keeps moving. Nothing in the first relation protects the second. A program left
completely untouched, with no defect introduced and no line edited, can slide
from indispensable to unusable purely because the machines, the interfaces people
expect, and the surrounding systems it was fitted to have all moved on without
it. The artifact did not change; its fit did.

This matters because it tells you where verification stops paying. Proving a
component correct fixes it against one description of its obligations, and that
description was itself written against assumptions about hardware, users, and
neighbouring systems that have their own expiry dates. So the frozen, proven,
never-touched component is not the safe one — it is merely the one whose decay is
invisible, since no commit history records it. Treating "we haven't had to change
it in years" as evidence of health inverts the truth: it is often evidence that
nobody has checked whether it still fits.

The practical consequence is that fitness needs its own periodic re-examination,
separate from testing. A programmer who believes this asks about a stable
component not "does it still pass?" but "are the assumptions it was built
against still true?" — what it presumes about its platform, its callers, and the
expectations of the people who use it. Change is then not something inflicted on
a healthy system from outside; it is the cost of remaining fitted to a world that
did not consult you. Refusing it does not preserve the system's value, it just
converts the loss from a maintenance line item into a silent one.

**Source:** [Software Aging](../works/software-aging.md) — the opening rebuttal
to the "mathematics does not decay" objection and the first of the two named
causes of aging, illustrated by Parnas's recollection of an early program of his
own that would still execute flawlessly and that nobody would now consent to use.
