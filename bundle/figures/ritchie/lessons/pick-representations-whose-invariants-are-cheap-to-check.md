---
type: lesson
title: "Pick the representation whose global invariant is cheap to check, not the one that reads best"
figure: ritchie
works: [unix-time-sharing-system]
axes: [verifiability, primitive-count, hardware-affinity]
subdomains: [operating-systems-and-systems-programming, databases-and-data-management]
tags: [lesson]
---
# Pick the representation whose global invariant is cheap to check, not the one that reads best

**Lesson:** Ritchie and Thompson split naming from identity: a directory entry holds only a name and a small integer, and everything that actually describes a file — owner, permissions, size, block addresses, reference count — lives in a flat table indexed by that integer. The hierarchy people navigate is therefore a convenience laid over a linear array, and the two can be reasoned about separately. Ritchie singles out the consequence he cares about most, and it is not elegance: because the descriptive table is linearly organized, the check that storage accounting is consistent — that the occupied regions and the free regions are disjoint and together exhaust the device — can be done by a sweep that never looks at the directory tree at all. Recovering confidence in the system after a crash does not require traversing the structure that users think they are using.

The general principle is that a data layout has two audiences: the humans reading it and the machinery that must certify it is not corrupt. Those audiences want different things, and when they conflict the certifier should usually win, because a representation whose consistency you cannot cheaply establish is one you will eventually be unable to trust. Note also what the design gives up to buy this. Symmetric links mean a file belongs to no directory in particular, which makes ownership and storage accounting genuinely ambiguous — Ritchie says so plainly and offers only a rough allocation rule. And directories are constrained to a tree, not because trees are pretty, but because arbitrary links among them would make "is this region still reachable from the root?" an expensive question, which is the same checkability concern showing up as a restriction on expressiveness.

A programmer who believes this asks, while choosing a schema or an on-disk format, what the repair tool will have to do. If the answer involves following pointers through user-visible structure, they look for an indirection that lets the audit run over a dense, independently scannable index instead. They also accept deliberate restrictions on what users may express when the alternative is an invariant nobody can afford to verify, and they say out loud which anomalies the choice introduces rather than pretending the design is free.

**Source:** [The UNIX Time-Sharing System](../works/unix-time-sharing-system.md) — the file-system implementation section on i-numbers and the i-list, its explicit remarks on consistency checking and on the accounting oddities that symmetric links create, plus the earlier justification for constraining the directory graph to a rooted tree.
