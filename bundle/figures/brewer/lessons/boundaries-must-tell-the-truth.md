---
type: lesson
title: "A boundary that hides where it really is will fail where you cannot see"
figure: brewer
works: [towards-robust-distributed-systems]
axes: [cognitive-load, expressiveness]
subdomains: [distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# A boundary that hides where it really is will fail where you cannot see

**Lesson:** The interface between two modules changes character depending on what physically separates them: same address space, different address spaces, different machines, different owners. Each step outward adds concerns the previous step did not have — argument copying, trust and validation, independent partial failure, resource reclamation when the other side vanishes, independent versioning and upgrade. Brewer's diagnosis of fragile distributed systems is that the field spent decades papering over these differences, dressing remote interactions up as local procedure calls. The disguise does not remove the new failure modes; it removes the programmer's ability to see them, which is strictly worse. The reader of a call site that looks local must nonetheless mentally track timeouts, absent peers, and stale references the syntax gives no hint of.

The supporting evidence is an asymmetry worth remembering: wire protocols have historically outlived and outperformed distributed APIs, precisely because a protocol is forced to be honest. It passes values rather than pretending references travel, it is designed around partial failure from the start, and its explicit state machine gives every abnormal transition a visible place to live, where a call/return shape has nowhere natural to put them. When the notation matches the true structure of the interaction, the hard cases become expressible instead of exceptional.

A programmer who absorbs this treats every boundary crossing as a design site rather than a syntax detail: they ask who trusts whom across this line, which side can disappear mid-conversation, how the two sides will ever be upgraded independently, and whether the abstraction in use lets those questions be answered in the code or only in comments. They become suspicious of any technology whose sales pitch is that the distributed case looks just like the local one.

**Source:** [Towards Robust Distributed Systems](../works/towards-robust-distributed-systems.md) — the "understanding boundaries" arc of the keynote, which walks the boundary outward from procedure call to inter-machine protocol, indicts false transparency as the root cause of fragility, and contrasts protocols with APIs.
