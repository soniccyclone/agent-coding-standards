---
type: lesson
title: "Partitioning the channel is a proxy for knowing the requester"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Partitioning the channel is a proxy for knowing the requester

**Lesson:** A great deal of structure in long-lived systems exists only because, at the time it was built, the individual could not be identified at the moment of the request. So the medium itself was split into compartments, each stocked for a presumed audience: sections, categories, tiers, regional editions, specialised channels. The compartment was never the goal; it was a way of inferring who was on the other end from where they happened to be standing. That inference is coarse, it costs real money to maintain a separate compartment per audience, and the number of compartments is limited by the cost of running them, so the segmentation is always much less precise than the population it approximates.

The moment per-request identity becomes available, the compartments stop being the mechanism and become overhead. The right thing to serve can be selected from what is known about the requester, regardless of which compartment they arrived through, which means one undifferentiated channel outperforms a carefully engineered set of specialised ones. Recognising this early prevents an expensive and very common mistake: continuing to invest in refining a partition that was only ever a substitute for information you now possess. The tell is that the partition's categories are proxies for attributes of the user rather than properties of the content, and that the team keeps proposing to add more of them.

The inverse direction matters just as much, because you will not always have the identity. If per-request knowledge is unavailable, unreliable, or forbidden, then partitioning the channel is not a legacy hack — it is the correct and possibly the only mechanism, and its coarseness is the honest limit of what can be known. Systems should be designed so that the compartment-based path and the identity-based path are both expressible, because privacy regimes, anonymous traffic, and cold starts all push you back onto the coarse path at exactly the times you cannot afford to have deleted it.

The general habit is to look at any static partitioning of a system's resources and ask what unknown it was standing in for. Sharding by geography for latency is a partition standing in for network distance, which is now measurable directly. Tiered pricing plans are a partition standing in for willingness to pay. Each such structure is a frozen guess, and each becomes obsolete the moment the thing it guessed at becomes observable.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the advertising chapter's discussion of display advertising, which explains special-interest publications as the traditional medium's answer to lack of focus, notes the order-of-magnitude gain from placing an ad where the interested audience already gathers, and observes that the web can instead select on what is known about the individual regardless of which page they are viewing.
