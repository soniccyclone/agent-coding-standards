---
type: lesson
title: "Bridge heterogeneous representations through one semantic center, never pairwise"
figure: bachman
works: [oral-history-charles-bachman]
axes: [primitive-count, cognitive-load]
subdomains: [databases-and-data-management, distributed-systems-and-concurrency, software-engineering-and-architecture]
tags: [lesson]
---
# Bridge heterogeneous representations through one semantic center, never pairwise

**Lesson:** The problem Bachman calls data independence recurs everywhere systems built by different hands must exchange information: the same facts encoded in different formats, character sets, units, and names. The naive response is a hand-written translator per pair of systems, which grows quadratically and buries the shared meaning inside each bridge. The three-schema answer he helped shape inverts this: define one conceptual schema — a description of the information itself, stripped of every implementation and optimization detail — and map each concrete representation to it exactly once. Any two representations can then be bridged through the center, and because the maps carry enough information, a *direct* translator between any pair can be generated mechanically from its two maps. The count of hand-built artifacts drops from quadratic to linear, and the semantics live in one inspectable place instead of being smeared across every bridge.

Bachman applied the identical move to communications: what became the OSI presentation layer is the three-schema idea inserted into a protocol stack, a designated place where format disagreement between endpoints is resolved (and which costs nothing when the endpoints already agree). His insistence that the architecture be open — no privileged node at the root, anyone who follows the layered rules may connect, each layer replaceable so long as it preserves its upper and lower interfaces — is the same instinct at the system level: interoperation among unlike parties comes from agreed meeting points, not from one party's format winning.

A programmer who thinks this way, on meeting the second incompatible representation of the same information, does not write the second converter. They ask what the information *is* independent of any encoding, write that down as the canonical model, and express every format as a mapping to it. They also learn the failure mode Bachman reports from his later Constellar years: the whole scheme stands or falls on the teams actually agreeing on the center's definitions, and deferring that agreement is fatal, because the canonical middle is exactly the part that cannot be reconciled later.

**Source:** [Oral History: Charles Bachman](../works/oral-history-charles-bachman.md) — the ANSI/SPARC three-schema account in the Honeywell section, the presentation-layer reasoning against SNA in the OSI discussion, and the Constellar Hub post-mortem near the end.
