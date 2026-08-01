---
type: lesson
title: "Establish credibility on the surface you do not monetize"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# Establish credibility on the surface you do not monetize

**Lesson:** The same mechanism, built twice by different companies a few years apart, failed the first time and worked the second, and the difference had nothing to do with the mechanism. The first version answered every query with a ranked list of whoever paid most. It served the small fraction of users who arrived already intending to buy and was worthless to everyone else, so everyone else left, and the paying users had no reason to arrive because nobody used the thing for anything. The second version kept a merit-ranked list of results computed from criteria no advertiser could purchase, and put the paid list beside it rather than inside it. Same auction, same bidding, same ad selection problem. It worked because the unpaid surface had already been running long enough that people believed what it told them.

The transferable point is a dependency between two parts of a system that looks like an ordering constraint on features but is actually a precondition on trust. The monetized surface derives its entire value from an audience that showed up for the unmonetized one, and that audience's willingness to show up is a stock accumulated slowly and spent quickly. A design that lets paid placement contaminate the merit ranking is not making a small quality tradeoff; it is drawing down the asset that makes the paid placement worth anything. This applies well outside advertising. Any system with a free tier feeding a paid tier, a recommendation feed carrying sponsored slots, a package registry with promoted entries, or an API whose rate limits can be bought has the same structure.

Two design consequences follow. First, the separation should be structural rather than a policy someone maintains. Compute the merit ranking from inputs that have no path from the payment system at all, so that the claim "you cannot buy your way up this list" is a property of the data flow and not a promise anyone has to keep. Second, sequence matters: the credibility has to exist before the monetization is switched on, which means the earlier product must be allowed to run unprofitable for as long as it takes. A team that reads the failed first version as a failed idea rather than as a premature one will build the same thing again and conclude the idea does not work.

The general habit is to ask, of any revenue mechanism, what the users' reason for being present is, and whether the mechanism consumes that reason. When it does, the revenue curve rises first and then the audience curve falls, and the two are separated by enough time that nobody connects them.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 8's history of search advertising, contrasting the earlier keyword-auction search that ordered all results by bid and was useless to anyone seeking information, with the later system that kept the objectively ranked results separate from the ad list and could rely on an already-established reputation to make people willing to trust the ads.
