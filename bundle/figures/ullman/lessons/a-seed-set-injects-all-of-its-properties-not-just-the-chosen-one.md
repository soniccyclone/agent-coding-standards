---
type: lesson
title: "A seed set injects all of its properties, not just the one you chose it for"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A seed set injects all of its properties, not just the one you chose it for

**Lesson:** Many systems work by picking a small set of items asserted to have some property and letting a propagation rule spread influence outward from them. The set is chosen against one criterion, and the criterion is usually defended carefully. What goes undefended is everything else the set happens to be, because those attributes were never part of the selection reasoning and therefore never appear in the review. They propagate anyway. A rule that spreads influence cannot distinguish the property you selected for from the properties that came along with your selection method, and every correlate of the seed becomes a correlate of the output.

The pattern is most visible when a proxy is used for cheapness. Choosing membership-controlled domains as a stand-in for trustworthiness is sound on the criterion: getting a page into such a domain really is hard, so the proxy tracks the property. But those specific domains are also overwhelmingly from one country, and nothing in the propagation knows that the nationality was incidental and the gatekeeping was the point. Everything downstream inherits a geographic tilt that no line of code expresses and no parameter controls, and it will be observed later as a puzzling quality difference between regions rather than as a consequence of a sourcing decision made once, early, for unrelated reasons.

Two things follow. The first is a check that takes minutes: after choosing a seed set by a criterion, describe the set by several attributes you did not select on — origin, age, size, language, format, the era it was produced in, which team produced it — and ask for each whether it is uniform in a way the general population is not. Uniformity there is a leak. It does not necessarily mean the seed is wrong, but it means you now know the direction in which the output will be skewed, which is the difference between a stated limitation and an unexplained anomaly. The second is that the remedy is usually not a cleverer criterion but a deliberately heterogeneous set assembled from several independent sources satisfying the same criterion differently. Diversity of sourcing method is what breaks the correlation, because the correlates of one method are unlikely to be the correlates of another.

The reasoning applies wherever a small curated input governs a large derived output: trust anchors, training seeds, canonical examples, style exemplars, allowlists, the reference corpus a threshold is calibrated against. In every case the curation effort concentrates on the intended property because that is what the review is about, and in every case the propagation is indifferent to intent. Writing down the incidental attributes of a seed set is cheap, it is the only moment at which the skew is easy to see, and it converts a permanent invisible bias into a documented one that someone can later decide to fix.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 5's discussion of assembling a TrustRank teleport set, which proposes picking domains whose membership is controlled on the grounds that spammers cannot get pages into them, then immediately observes that the domains named are almost exclusively United States sites and that analogous domains from other countries must be included to obtain a good distribution of trustworthy pages.
