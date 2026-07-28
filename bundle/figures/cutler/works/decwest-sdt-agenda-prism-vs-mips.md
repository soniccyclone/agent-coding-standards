---
type: work
title: "DECwest/SDT Agenda: PRISM vs. MIPS"
figure: cutler
description: An internal DEC strategy slide deck Cutler personally wrote and presented to lay out the choice DEC faced in mid-1988 - keep funding the in-house PRISM RISC architecture his DECwest team was building, or switch entry-level workstation products to the commercially available MIPS microprocessor. It states the problem, the market pressure, and several concrete alternative strategies without pretending the answer is obvious. Read against what happened next, it's effectively the internal argument that immediately preceded PRISM's cancellation a few weeks later and Cutler's departure to Microsoft to build Windows NT.
subdomains: [operating-systems-and-systems-programming]
year: 1988
url: https://bitsavers.org/pdf/dec/prism/memos/880530_Cutler_PRISM_vs_MIPS.pdf
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# DECwest/SDT Agenda: PRISM vs. MIPS

**Venue/year:** Internal Digital Equipment Corporation memo/slide deck, DECwest Engineering, May 30, 1988. Author initials "dnc" (David N. Cutler) appear on every page footer.
**Source:** https://bitsavers.org/pdf/dec/prism/memos/880530_Cutler_PRISM_vs_MIPS.pdf — verified live (HTTP 200), page-checked directly. Part of bitsavers.org's "prism/memos" collection, a preservation archive of original DECwest emails and presentations from the late 1980s.
**Host:** third-party-rehost — bitsavers.org is a long-running, well-established computing-history preservation archive, not DEC's or Cutler's own site, but a legitimate host for scanned original internal documents.

## Lessons
- [An interface is a promise about every future implementation, so whatever it leaves unsaid is where incompatibility will grow](../lessons/an-architecture-is-a-promise-across-implementations.md)
- [Enumerate the mechanisms your abstraction silently requires from the layer beneath it, then price their absence as recurring](../lessons/inventory-what-your-abstraction-demands-from-below.md)
- [Any behavior you put in shared implicit state serializes every operation that reads it; encode it in the operation instead](../lessons/implicit-mode-state-serializes-what-touches-it.md)
- [A technical recommendation earns its authority by containing the strongest available argument against itself](../lessons/state-the-case-against-your-own-recommendation.md)
- [A decision repeatedly revisited costs more than a mediocre one held, because stability of the target is itself an engineering resource](../lessons/re-deciding-costs-more-than-deciding-wrong.md)
- [As a system's defects thin out, the survivors are almost all synchronization, so design for concurrency at the start or not at all](../lessons/synchronization-is-where-the-residual-bugs-live.md)
- [Compatibility with what already runs is the mass of a system, and the only way to carry it is at a boundary you design on purpose](../lessons/compatibility-is-the-mass-of-a-system.md)
- [Portability comes from naming the seam where the machine shows through, not from hiding the machine](../lessons/name-the-seam-where-the-machine-shows-through.md)
