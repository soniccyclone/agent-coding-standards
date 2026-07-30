---
type: lesson
title: "Price the generality you add for elegance by asking what the structure would actually change"
figure: wilkes
works: [cambridge-cap-computer-and-its-operating-system]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Price the generality you add for elegance by asking what the structure would actually change

**Lesson:** A recurring pattern in system design is to build a facility to unbounded depth when everyone involved knows that one or at most two levels will ever be used, on the grounds that the general version is more elegant and that an arbitrary cutoff would be inelegant. The cost of that decision is not the extra code. It is that the mechanism now has to be correct for cases nobody will exercise, its invariants have to hold in configurations nobody will build, and every interaction with the rest of the system has to be reasoned about at full generality. Facilities built this way are frequently implemented, documented, and then never used for their intended purpose, which is a complete loss rather than a hedge.

The check that catches this before it is built is to work out, concretely, what would change if the structure were adopted. Not whether it is coherent — elegant structures generally are — but what its net effect would be on the properties you care about. It is common for the honest answer to be an increase in the amount of code that has to be trusted and a lengthening of the paths between clients and the services they use, with no compensating gain. When that is the answer, the elegance is decorative: it improves the diagram and degrades the system. Discovering this requires forcing the abstract proposal into specifics, since at the level of the diagram the arrangement will keep looking better than the flat alternative.

A separate reason for skepticism is that unused generality tends to hide a defect rather than merely waste effort. If a facility has been implemented and left unused, the reason it is unused is worth chasing — in the case that motivated this, the depth was unusable because a fundamental property failed at the boundary between levels, which is exactly the sort of thing that stays hidden as long as the general facility is only exercised in its degenerate one-level form.

**Source:** [The Cambridge CAP Computer and Its Operating System](../works/cambridge-cap-computer-and-its-operating-system.md) — Chapter 5's account of the coordinator hierarchy: implemented to indefinite depth because considerations of elegance and generality dictated it, though one or two levels were known to be all that would ever be needed; the later, more modest plan abandoned once closer examination showed it would only increase the amount of trusted software and lengthen the chains between user processes and system services; and the decision to settle for a single level of coordination.
