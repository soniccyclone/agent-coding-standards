---
type: lesson
title: "A single-point summary smuggles in an assumption about shape"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A single-point summary smuggles in an assumption about shape

**Lesson:** Summarising a group by one representative value is so routine that the commitment it makes goes unexamined. The commitment is that the group is blob-like around that value — that membership is decided by proximity to a centre, so nearness to the summary means membership and distance means non-membership. Any group whose true extent is not organised around a centre breaks this silently. The extreme illustration is two groups that genuinely differ but share the same central value: one occupying a core, the other a shell around it. Summarised by their centres, they are indistinguishable, and every downstream decision — which group a new item joins, whether two groups should merge, how far apart they are — is wrong while every computation is correct.

The fix is to summarise with several values chosen from the group's periphery rather than one from its middle. A handful of well-spread boundary samples traces the group's actual extent, so distance from a group becomes distance to its nearest representative rather than distance to its centre, and a shell stops being confused with a core. This costs a small constant more storage per group and changes the summary from a claim about where the group is to a claim about where the group reaches. It also changes what the merge criterion means: two groups merge if any pair of their representatives is close, which is a statement about touching rather than about concentricity, and that is the statement you usually intended.

Boundary representatives introduce their own weakness, and the standard remedy is worth learning as a technique in itself. Anything chosen for being extreme is disproportionately likely to be noise, so a summary made of extremes inherits the noise sensitivity that the central summary did not have. Pulling each representative a fixed fraction of the way back toward the centre blunts that without collapsing the shape: outliers get dragged in most, genuine boundary points shift slightly, and the traced extent stays recognisable. That fraction becomes an explicit knob between fidelity to shape and robustness to noise — and, together with the merge distance, it is what actually decides whether nested structures are reported as one thing or two. That decision was always being made; the multi-representative form merely makes it a parameter someone can argue about instead of an accident of the summary's form.

The general habit: for every aggregate your system stores, write down what the aggregate cannot express. A mean cannot express multimodality; a centre cannot express a hole; a range cannot express density. Then ask whether your data can actually exhibit the thing it cannot express. If it can, the aggregate is not a summary, it is a filter.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the CURE sections of the clustering chapter, which motivate multiple representatives with the example of a disc surrounded by a ring sharing one centroid, select the representatives to be mutually distant so they land on the boundary, move them a fixed fraction toward the centroid, and note that this fraction together with the merge distance determines whether the nested structures are treated as one cluster or two.
