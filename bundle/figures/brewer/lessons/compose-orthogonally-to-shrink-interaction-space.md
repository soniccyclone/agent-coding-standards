---
type: lesson
title: "Robustness comes from mechanisms that cannot interact"
figure: brewer
works: [harvest-yield-and-scalable-tolerant-systems]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Robustness comes from mechanisms that cannot interact

**Lesson:** Most failures in complex systems come from unexpected interactions between components, not from bugs inside them, so the number of possible interactions is the quantity a robustness-minded designer should minimize. Layering helps, but Brewer and Fox push one step further: prefer mechanisms that are orthogonal, meaning they share essentially no runtime interface with the rest of the system at all. A guard timer, a sandbox, a periodic restart, an out-of-band security handshake — each does its job without the application knowing it exists, which means it cannot participate in the combinatorial explosion of cross-component states. Since interaction complexity grows roughly with the square of the moving parts, every mechanism removed from the interaction graph pays quadratic dividends.

The same reasoning drives the decomposition strategy: split an application along its state-management fault lines, so that only the subsystems that genuinely need strong guarantees carry the machinery for them, and the failure of any one subsystem subtracts a feature instead of the service. This is a different cut than the usual functional decomposition; the question is not "what does this module do" but "what happens to the whole when this module dies, and what state discipline does it actually require."

A programmer who believes this reaches for small-state-space mechanisms whose entire behavior can be held in the head and audited (a timeout has very few behaviors; a distributed lock manager has very many), accepts seemingly harsh constraints like arbitrary restartability because they purchase simple recovery machinery, and treats soft, refreshable state as attractive precisely because it collapses the recovery path into the normal path. The instinct being trained is subtractive: robustness is bought by removing possible couplings, not by adding defensive code.

**Source:** [Harvest, Yield, and Scalable Tolerant Systems](../works/harvest-yield-and-scalable-tolerant-systems.md) — the second strategy and its discussion, where decomposition by state requirements, orthogonal mechanisms, and the quadratic argument for less machinery are developed with deployed cluster systems as evidence.
