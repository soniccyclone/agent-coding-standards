---
type: lesson
title: "Component-wise invariants don't certify the composition"
figure: boyce
works: [recent-investigations-in-relational-data-base-systems]
axes: [verifiability]
subdomains: [databases-and-data-management, formal-methods-and-verification]
tags: [lesson]
---
# Component-wise invariants don't certify the composition

**Lesson:** A property checked piece-by-piece can hold on every piece and still fail for the whole. In schema design the concrete case is stark: every relation in a collection can individually satisfy the strictest normal form, yet a dependency that only becomes visible when two relations are joined can mean the collection as a whole admits a cleaner decomposition. The verification obligation therefore has two layers — the constraints inside each component, and the constraints that emerge across the lossless combinations of components — and discharging only the first layer produces a false sense of being done.

The transferable habit is to ask, after any modular check passes, what statements about the assembled system the per-module checks were silent on. Interfaces, joins, and compositions are where hidden coupling lives precisely because no single component owns it; a discipline that only ever inspects one unit at a time is structurally blind there. This does not argue against modular reasoning — per-component checks are what make the global question tractable at all — it argues for knowing exactly which global properties the local ones do and do not entail, and for naming the residue as its own verification task rather than assuming it away.

**Source:** [Recent Investigations in Relational Data Base Systems](../works/recent-investigations-in-relational-data-base-systems.md) — the close of the normalization section, where a two-relation example shows a collection of individually normalized relations that is nonetheless not optimally decomposed, motivating analysis of dependencies across non-loss joins.
