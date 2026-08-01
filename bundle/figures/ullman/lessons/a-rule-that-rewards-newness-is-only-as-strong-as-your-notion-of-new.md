---
type: lesson
title: "A rule that rewards newness is only as strong as your notion of new"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# A rule that rewards newness is only as strong as your notion of new

**Lesson:** Ordering a queue of submissions by recency is the fairest-looking rule available. It requires no judgement, no scoring model, and no privileged information, and it gives every participant the same treatment. It is also trivially defeated, and the defeat does not involve falsifying anything. The timestamp stays honest. The participant simply resubmits a slightly altered copy at intervals, and each copy is genuinely new by the only test the rule applies. The rule allocates a scarce position per submitted object, so the question that decides whether it works is not how the ordering is computed but what it costs to bring a fresh object into existence.

That question is the one to ask of any per-entity policy, and it is asked far too rarely because the entity usually feels like a given. Free trials per account, rate limits per key, first-post visibility per thread, reputation bootstrapping per identity, quota per project: each of these is a benefit attached to an identity, and each is worth exactly the cost of minting a new identity. When that cost is near zero the policy is not a constraint, it is a faucet with an extra step. The corollary is that hardening such a policy almost never means changing the allocation rule. It means raising the price of identity, or defining identity by something more expensive to vary than the fields the submitter controls.

The chapter's answer is the second of those, and the mechanism it reaches for is instructive: define sameness by content similarity rather than by record identity, using the near-duplicate detection machinery already developed for an entirely different purpose earlier in the book. The defence is not a new subsystem invented for this abuse. It is an existing capability pointed at the identity question, which is a recurring shape because "are these two things really the same thing" is a question many parts of a system need answered and few of them phrase it that way.

The general move is to separate two things that get conflated when a fairness rule is written down: the ordering, which is the part everyone argues about, and the individuation, which is the part nobody specifies and which determines whether the ordering means anything. Write the individuation criterion explicitly, then estimate what it costs an adversary to produce one more unit under it. If that number is small, the ordering rule is decoration.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 8's discussion of ranking directly placed ads, which offers most-recent-first as an equitable strategy and immediately notes that it is subject to abuse by advertisers posting small variations of their ads at frequent intervals, pointing at the earlier chapter's similar-item detection as the countermeasure.
