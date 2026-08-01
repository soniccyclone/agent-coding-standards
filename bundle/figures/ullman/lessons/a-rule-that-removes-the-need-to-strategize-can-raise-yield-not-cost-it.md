---
type: lesson
title: "A rule that removes the need to strategize can raise yield, not cost it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# A rule that removes the need to strategize can raise yield, not cost it

**Lesson:** The assumed shape of any anti-manipulation measure is a tax: you give up some throughput, some revenue, or some user convenience in exchange for resistance to abuse, and the design question is how much to give up. An aside in the chapter records a case where that shape does not hold. The deployed pricing rule charges a winner not what they offered but roughly what the next participant offered, and it is reported both to be harder to manipulate than the obvious rule and to produce more revenue for the operator. Both properties, from one change, with no tradeoff to tune.

The mechanism behind the coincidence is worth extracting because it recurs. Under the obvious rule, a participant who states their true valuation and wins has overpaid relative to what would have sufficed, so the rational move is to guess how much lower they can go, and every participant shades downward by whatever margin their guessing tolerates. That shading is a loss to the operator on every transaction, not only on the manipulated ones, and it is caused entirely by the participant's uncertainty about how others will behave. Removing the payoff to shading removes the shading, and what looked like a fraud control turns out to have been an uncertainty control that was suppressing honest participation.

The generalisation is a question to ask before accepting an abuse-versus-yield tradeoff as given: is the manipulation being prevented, or is the incentive to manipulate being removed? Those two have different economics. Prevention is subtractive, since it operates by restricting or rejecting things, and it lands on honest participants as friction. Incentive removal is a change to what the rule rewards, and honest participants experience it as a simplification, since the strategy they had been forced to compute stops mattering. Only the first kind is inherently a tax. Treating both as taxes leads teams to under-invest in exactly the interventions that would have paid for themselves.

The corollary for anyone stating such a rule publicly: the guarantee that honest behaviour is optimal is itself the product. It is what lets a participant stop modelling everyone else, and the cost of that modelling, paid in hedging and in refusal to participate at all, is usually invisible in the metrics precisely because it shows up as things that did not happen.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the boxed aside in chapter 8 on aspects of the real Adwords system not in the model, which notes that search engines charge approximately the bid of the advertiser placed immediately behind the winner and that such second-price auctions are both less susceptible to gaming and higher-revenue than first-price auctions.
