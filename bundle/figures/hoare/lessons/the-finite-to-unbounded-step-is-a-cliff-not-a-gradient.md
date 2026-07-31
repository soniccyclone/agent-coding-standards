---
type: lesson
title: "Going from bounded to unbounded is a cliff, not a gradient: stay on the cheap side until the application forces you off"
figure: hoare
works: [notes-on-data-structuring]
axes: [hardware-affinity, cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Going from bounded to unbounded is a cliff, not a gradient: stay on the cheap side until the application forces you off

**Lesson:** Descriptions of data divide into two classes that look adjacent and behave nothing alike. On one side, everything a description can denote has a size you can compute from the description itself; on the other, the description admits arbitrarily many possibilities and the size is known only while running, and changes while running. Crossing that line is not a small increase in generality. It changes four things at once: storage can no longer be reserved from the declaration, so an allocator with its own failure modes joins the design; efficient work must be done by modifying pieces in place rather than by producing whole new values; the pieces get connected by addresses, which brings both reclamation and the fact that an address means nothing outside the space it came from; and the choice of representation stops being obvious and starts depending on knowing the relative frequency of the operations, which is precisely the thing you do not know yet.

Because all four arrive together, the sane default is to stay bounded and treat unboundedness as something the problem must demand. A collection with a real ceiling should be described with the ceiling in it; a value with a natural maximum size should be given that maximum. This is not timidity about generality, it is refusing to pay a fixed, large cost for a generality nobody requested. Notice that most of the discipline that makes bounded structures pleasant — predictable size, stack or static placement, transfer between storage levels by plain copying, cheap uniform operations — is lost wholesale the moment one component becomes unbounded, and it is lost for the whole containing structure, not just for that component.

The corollary for design order is that this is one of the decisions worth making early and deliberately, because it is the one that cannot be quietly reversed later. It also tells you what to look for when a system is unexpectedly slow or unexpectedly fragile: find the place where something bounded was generalized to something unbounded for a reason that no longer applies, and see what the four costs bought. Where the unboundedness is genuinely required, take it — but take it knowingly, and confine it, so that the structures above and below the unbounded one keep their static shape.

**Source:** [Notes on Data Structuring](../works/notes-on-data-structuring.md) — the opening of the sequence chapter, which contrasts elementary structures (finite cardinality, storage determinable from the declaration, no pointers, primitive operations of comparable efficiency across representations) with advanced ones (size known only at run time and varying during it, dynamic allocation and reclamation, pointer-linked units that complicate transfer to backing store, representation choice critically dependent on operation frequencies), and advises confining oneself to the elementary case except where the application forces otherwise.
