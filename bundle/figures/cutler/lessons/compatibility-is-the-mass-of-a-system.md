---
type: lesson
title: "Compatibility with what already runs is the mass of a system, and the only way to carry it is at a boundary you design on purpose"
figure: cutler
works: [oral-history-of-david-cutler, decwest-sdt-agenda-prism-vs-mips]
axes: [cognitive-load, expressiveness, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# Compatibility with what already runs is the mass of a system, and the only way to carry it is at a boundary you design on purpose

**Lesson:** The instinct that a codebase has grown too tangled and should be replaced is usually correct about the tangle and usually wrong about the conclusion, because it prices the code and forgets the obligations. What makes a mature system expensive to replace is not the volume of its source but the volume of software written against it that must keep working. That obligation does not disappear when you start over; it transfers unchanged onto the new thing, and it is the dominant term. This is why the size of the effort to build a broadly compatible operating system today is out of reach of almost any organization, and why systems that appear to be replaced are almost always evolutions of the same lineage under a new name.

The design move that makes the obligation survivable is to make compatibility an explicit boundary rather than a property smeared through the implementation. Old interfaces get served by a layer whose entire job is to present the older world faithfully on top of the new mechanisms, and the new system's internals never learn that the older world exists. Multiple such layers can coexist, each presenting a different environment over one core, and each can be reasoned about, tested, and eventually retired independently. The alternative — accreting old behavior into the core as special cases — makes every subsequent change in the core an exercise in remembering which historical caller depended on which accident.

The same logic explains why a family of machines lives or dies on the compatibility of its architecture rather than the merits of any one implementation. Customers do not buy a chip; they buy the assurance that the software they are writing now will run on the machines they will buy later. An architecture that would require the software to be rebuilt, or worse, adjusted, for each new implementation offers no such assurance, and a vendor who abandons the migration path from what customers already own has not made a technical decision but a decision to hand the installed base to somebody else. Divergence, once permitted, is also the mechanism by which a shared platform fragments into mutually incompatible variants, each vendor adding value in a way that subtracts it from everyone.

**Source:** [Oral History of David Cutler](../works/oral-history-of-david-cutler.md) — the subsystem-personality architecture built so one kernel could present several different operating environments, the migration executives used to keep older binaries running across an architecture change, and the closing argument that a genuinely new operating system is now impractical because the compatibility obligation cannot be discarded. Also [DECwest/SDT Agenda: PRISM vs. MIPS](../works/decwest-sdt-agenda-prism-vs-mips.md) — the assumptions and conclusions slides, which weigh an architecture primarily by whether it preserves the existing customer base's migration path.
