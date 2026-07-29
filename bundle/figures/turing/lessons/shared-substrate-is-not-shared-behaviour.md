---
type: lesson
title: "Shared implementation medium is not evidence of shared behaviour; only functional correspondence is"
figure: turing
works: [computing-machinery-and-intelligence]
axes: [hardware-affinity, cognitive-load]
subdomains: [foundations-of-computation, operating-systems-and-systems-programming]
tags: [lesson]
---
# Shared implementation medium is not evidence of shared behaviour; only functional correspondence is

When two systems are built out of the same physical stuff, it is tempting to read that coincidence as a deep kinship and to expect their behaviours to correspond. The temptation should be resisted, and there is a clean argument for why. If a class of machines is behaviourally interchangeable regardless of the medium they are realized in — one member of the class built out of gears, another out of switching circuits, another out of pressure waves in a delay line — then the medium cannot be carrying any of the theoretically significant content. It is selected on engineering grounds, typically speed, and it drops out of every statement about what the class can compute. A similarity that is invisible to the theory is a similarity that explains nothing.

What does carry content is correspondence of function: two systems are alike to the degree that a mapping exists between their states and transitions such that the behaviour of one predicts the behaviour of the other. That is a demanding relation and it has to be exhibited, not assumed from a shared parts list. The failure mode is expensive in both directions. Reasoning from a shared substrate to a shared capability yields a conclusion the substrate does not license. Reasoning from a different substrate to a different capability is worse, because it rules out an equivalence that actually holds — the same behaviour reached through an unfamiliar realization looks like a different kind of thing when it is only a different implementation of the same kind.

For a working programmer this is the discipline of judging systems by their observable state-transition behaviour rather than by their family resemblance. Two services written in the same language on the same runtime are not thereby comparable; two written in different languages on different hardware are not thereby incomparable. It also disarms a common category of architectural argument, the kind that infers suitability from resemblance — this workload is graph-shaped so it wants a graph database, this problem is neural-looking so it wants a neural substrate. The honest form of that argument names the functional correspondence and the performance property it buys, and admits that the resemblance itself was never the reason.

**Source:** [Computing Machinery and Intelligence](../works/computing-machinery-and-intelligence.md) — the aside on why the electrical nature of modern machines is not the reason they resemble nervous systems, developed from the observation that an entirely mechanical predecessor belongs to the same equivalence class.
