---
type: lesson
title: "Give observations tiers of commitment instead of forcing one decision"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Give observations tiers of commitment instead of forcing one decision

**Lesson:** A single-pass process that must dispose of each item as it arrives faces a false dilemma: commit the item to a decision it may not deserve, or keep it in full and run out of room. The resolution is to stop treating disposal as binary and introduce intermediate states of commitment, each with its own representation. Items you are confident about get folded into a summary and their individuality is released. Items you cannot place yet, but which clearly resemble each other, get grouped into a provisional summary that has the same shape as a confident one but is not yet attached to any conclusion. Items you can say nothing about are kept verbatim, because they are few and because throwing them away would be a decision you have no basis for.

The tiers are doing distinct jobs, which is why collapsing them hurts. The confident tier is what makes the process affordable, since it converts unbounded data into fixed-size state. The provisional tier is what makes the process correct, since it lets evidence accumulate about a group before anything irreversible happens to it, and groups in that tier can later merge with each other or attach to a conclusion when enough arrives. The verbatim tier is the honesty valve: it holds the things the model does not yet explain, keeps them available for later reconsideration, and — importantly — its size is a live signal about whether the model fits. A verbatim tier that keeps growing is telling you the summaries are wrong, and that diagnostic simply does not exist in a design that forces every item into a bucket immediately.

Making the provisional and confident tiers share one representation is the detail that makes this practical rather than fussy. When a provisional group is described exactly as a confident one is, promoting it costs nothing, merging two of them costs nothing, and the code paths do not fork. That is worth designing for deliberately: pick the summary form first, then define the tiers as different *uses* of the same form rather than as different data structures.

The end of the stream forces the deferred decisions, and the design should name that policy explicitly rather than letting it fall out of the implementation. Leftover provisional groups and verbatim items can be attached to their nearest conclusion, or they can be reported as things that did not fit. Both are defensible, and they mean very different things to whoever consumes the output — one claims full coverage, the other admits residue. Choosing silently is the only wrong answer.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the Bradley-Fayyad-Reina sections of the clustering chapter, which partition in-memory state into cluster summaries whose points are released, summaries of provisional groups not yet attached to any cluster, and individually retained points, and which discuss the end-of-input options of treating the residue as outliers or assigning it to nearest clusters.
