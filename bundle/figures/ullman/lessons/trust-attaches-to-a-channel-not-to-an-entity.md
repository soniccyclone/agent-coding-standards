---
type: lesson
title: "Trust attaches to a channel, not to the entity that owns it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Trust attaches to a channel, not to the entity that owns it

**Lesson:** Reputation is usually modelled as a property of a party — this source is reliable, that one is not — and the model is wrong in a way that gets exploited constantly. What is actually reliable is a particular path by which content arrives, and a single party normally operates several paths with wildly different guarantees. An organisation whose own output is scrupulously produced may simultaneously run an open submission channel that anyone can write to. Content arriving by the second path carries the organisation's name and none of its diligence. Any system that grants standing per party rather than per path will accept the unvetted content at the vetted content's rating, and an adversary only has to find one delegated write path behind a respected name.

Getting this right means the unit of trust in your data model has to be finer than the entity. Ask, for each inbound path, who can cause content to travel it, and rate the path by that population rather than by the owner's reputation. The practical consequence is often uncomfortable: an obviously respectable source has to be excluded from your trusted set, not because you doubt its editorial standards but because it hosts a path you cannot distinguish from the outside. Being willing to exclude on that basis is the whole discipline, and the instinct to make an exception for a source you personally trust is exactly the instinct being exploited.

The same reasoning applies to how you assemble a trusted set in the first place. Any cheap proxy for trustworthiness — membership in a namespace that is hard to enter, or being at the top of some existing ranking — works by making entry expensive, which is a legitimate mechanism. But every such proxy also selects a population, and the selection is rarely the one you intended. A namespace with controlled membership may be controlled by one jurisdiction, one industry, or one era, and seeding from it does not merely reduce coverage: it systematically biases every downstream score toward whatever that population happens to talk about. Fixing this requires deliberately assembling analogous sets from the populations the first proxy excluded, which is manual work nobody enjoys and which no amount of algorithmic sophistication substitutes for.

So there are two questions to ask about any trusted set, and both are about populations rather than algorithms: who can write into each thing I am trusting, and who is missing from the set because of how I chose it. Neither has a technical answer, and both determine whether the technical machinery downstream produces anything worth having.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the trust-propagation section of the link-analysis chapter, which excludes reputable sites that accept reader comments from the trusted seed set, and notes that seeding from controlled domains skews the result toward one country's institutions unless equivalent foreign domains are added.
