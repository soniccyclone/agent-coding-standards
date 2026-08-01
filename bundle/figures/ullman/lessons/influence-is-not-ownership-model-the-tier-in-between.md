---
type: lesson
title: "Influence is not ownership: model the tier in between"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Influence is not ownership: model the tier in between

**Lesson:** Reasoning about what an adversary can do almost always starts from a two-way split: the assets they control and the assets they do not. That split is comforting and wrong, and its wrongness is structural rather than incidental. Between the two sits a third category — resources the adversary does not own, cannot read, cannot administer, and yet can write into, because somebody deliberately built an affordance for third-party contribution. Comment fields, public issue trackers, wikis, upload endpoints, reviews, webhooks, forwarded headers, user-supplied display names that appear in someone else's page. Every one of these was added as a feature, is owned by a party with no relationship to the attacker, and is nonetheless a place where attacker-chosen bytes end up living under someone else's name.

The middle tier matters disproportionately because attacks tend to need exactly what it provides. A construct built purely from owned assets is usually inert: it can be arbitrarily elaborate and still have no effect, because nothing outside it points in, so nothing outside it will ever discover or evaluate it. The whole apparatus is dormant until it acquires a single edge from the part of the world the attacker does not own, and that edge has to come from the influenceable tier, since the truly inaccessible tier by definition will not supply one. That asymmetry is a gift to the defender: the elaborate owned structure is the visible part and the tempting thing to hunt, but the scarce, load-bearing resource is the small number of write-affordances that connect it to everything else.

It also explains a category of trust judgement that looks inconsistent until you see the tiers. An organisation whose own content is impeccable is not thereby a source you can trust, if its platform accepts contributions from anyone. The reliability of the operator and the reliability of the bytes served under the operator's name are different properties, and conflating them is how a reputation-based allowlist acquires an attacker-controlled entry without anybody making a mistake. The correct unit of trust is not the site, the domain, or the organisation. It is the narrower thing: content produced through a path that only the owner can write.

The practical exercise is short and rarely done. Take your system's inventory and label every store, field, and channel with who may write to it, not who owns it, and note where those two answers differ. The rows where they differ are the middle tier. Then, for each defence that assumes an adversary is confined to their own assets, check whether the middle tier breaks that assumption. This normally reveals both an over-trusted allowlist and a place where a cheap restriction — rate limiting the contribution path, refusing to propagate authority through it, marking its output as a distinct provenance class — removes the attacker's only bridge at a cost the legitimate contributors barely notice.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 5's architecture of a spam farm, which divides the Web from the spammer's perspective into inaccessible, accessible and owned pages, remarks that it may seem surprising one can affect a page without owning it and points to blogs and news sites that invite comments, notes that without links from outside the farm would not even be crawled, and later warns that a site offering comment facilities cannot be treated as trustworthy even when its own content is entirely reliable.
