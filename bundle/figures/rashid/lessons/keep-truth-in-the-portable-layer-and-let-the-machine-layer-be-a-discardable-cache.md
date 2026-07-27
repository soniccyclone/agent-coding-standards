---
type: lesson
title: "A portability boundary holds only when the machine-specific side owns no truth and can be thrown away and rebuilt"
figure: rashid
works: [mach-a-new-kernel-foundation-for-unix-development]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A portability boundary holds only when the machine-specific side owns no truth and can be thrown away and rebuilt

**Lesson:** Splitting a system into a portable part and a per-machine part is standard advice, and most attempts at it leak, because the boundary is drawn by subject matter rather than by authority over state. The per-machine part ends up holding facts nobody else holds — which mappings currently exist, what was recently changed, some bookkeeping the hardware structures made convenient — and from that moment the portable part cannot reason about the system without knowing something about the machine, and each new machine forces a renegotiation of the interface. The stronger discipline is to draw the line by who owns the authoritative state: the portable side knows everything, and the machine-specific side is permitted to know nothing except how to obey a handful of imperatives about the hardware's own structures.

The reason this works is that it turns the machine-specific structures into a cache rather than a record. If every fact they encode is derivable from the portable side's data, then they can be discarded at any moment and reconstructed on demand — which is precisely the freedom a hardware-facing layer needs, because different machines make wildly different tradeoffs about what is cheap to keep and what is cheap to rebuild. One architecture's tables are expensive to hold and fine to regenerate; another's are the only representation available. A layer that owns no truth can make that choice locally, per machine, without informing anyone. A layer that owns truth cannot, and so the same interface has to be widened for every new target until it stops being an interface.

The second dividend is that the two sides stop having to agree on units. Because the authoritative side is the only one reasoning about regions, sharing, and provenance, the granularity it works in becomes a matter of its own convenience rather than something the hardware dictates — the hardware's granularity, the portable layer's granularity, and the granularity used by whatever supplies the data can all differ. A design that had let hardware facts propagate upward would have frozen a single number into everything above it.

The general form of the rule: identify what a layer is authoritative about before deciding what it does. A layer that only translates commands and holds regenerable state can be replaced wholesale for each new substrate, and its correctness is checkable in isolation because the small set of imperatives it must honor is the entire contract. A programmer applying this asks, at every abstraction boundary they draw, which side would have to be consulted to answer a question about system state — and if the answer is "both," the boundary is not yet a boundary.

**Source:** [Mach: A New Kernel Foundation for UNIX Development](../works/mach-a-new-kernel-foundation-for-unix-development.md) — the virtual-memory implementation section, where the machine-dependent portion is confined to a narrow validate/invalidate/protect role with no knowledge of the machine-independent structures, permitting it to reclaim its own mapping tables and to work at a different page granularity than the layers above it.
