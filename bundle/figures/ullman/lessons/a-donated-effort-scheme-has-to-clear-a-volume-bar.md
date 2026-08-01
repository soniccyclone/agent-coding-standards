---
type: lesson
title: "A scheme that runs on donated effort has to clear a volume bar, not a cleverness bar"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, databases-and-data-management]
tags: [lesson]
---
# A scheme that runs on donated effort has to clear a volume bar, not a cleverness bar

**Lesson:** Some inputs to a system cannot be computed and have to come from people: descriptions of what an image shows, judgements of whether two things are the same, categories that only make sense to a human. Designs for eliciting that work are frequently ingenious, and ingenuity is the wrong axis on which to evaluate them. The question is arithmetic. How much of this input does the system need to function, at what rate must it arrive to keep pace with new material, and how many willing participants at what throughput does that imply? A mechanism can be elegant, genuinely fun, and still off by two orders of magnitude from the volume required, in which case it is a demonstration rather than a supply.

The elicitation design also has to survive the fact that contributors are careless and occasionally wrong, which is usually handled by redundancy: enough independent contributions that a few bad ones cannot move the aggregate. Note that redundancy raises the volume requirement, so the quality mechanism and the throughput mechanism are coupled and must be sized together. One quality mechanism deserves attention on its own merits, because it produces trustworthy output without anyone checking it. Pair two participants who cannot communicate and reward them only for producing the same answer at the same time. Neither can be verified individually, and neither needs to be, since blind concurrence on an open-ended answer is hard to achieve except by both describing the same obvious truth. That is verification by construction of the incentive rather than by inspection of the result, which is the move to remember whenever the correct answer is subjective and an inspector would have no better basis for judging than the contributors did.

Both halves point at the same discipline: when a design depends on people doing something voluntarily, write down the required rate before you admire the mechanism. If the numbers do not close, the options are to shrink the requirement, to attach the work to an activity people were already going to perform for their own reasons, or to pay. Concluding that public enthusiasm will materialise at the needed scale is a forecast, and it should be labelled as one.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's discussion of obtaining item features from tags, including the sidebar on the tagging game in which two players independently propose a tag for an image and win only by agreeing, and the authors' own doubt that enough public interest can be generated to produce the volume of free work such data requires, together with the adjacent note that tagging works only if there are enough tags for occasional wrong ones not to bias the system.
