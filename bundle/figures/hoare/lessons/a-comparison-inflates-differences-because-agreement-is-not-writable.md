---
type: lesson
title: "Any comparison inflates differences, because agreement gives you nothing to write; end it by stating what both sides share"
figure: hoare
works: [communicating-sequential-processes-book]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# Any comparison inflates differences, because agreement gives you nothing to write

**Lesson:** Set two approaches side by side and write down what you find, and the result will overstate how far apart they are. This is a property of the exercise rather than of the writer's fairness. Where the two agree there is nothing to say — the shared assumption is invisible precisely because neither side contests it — while every divergence yields a paragraph, an example, and often a diagram. The output is therefore a catalogue of disagreements presented against an unstated background of agreement that never gets counted. Readers, seeing only the catalogue, come away with a picture in which the two things are nearly opposites, and then reason from that picture when choosing between them.

The correction is small and belongs at the end, where it can be checked against everything above it: say plainly that the treatment has emphasized differences, name the property both approaches share, and be specific about which of your own claims were pushed further than the evidence supports. Doing this is not modesty and it is not hedging. It restores the reader's ability to weigh the differences you documented, because a disagreement about which operators to take as primitive means something quite different when both parties are agreed on having a rigorous basis for reasoning about designs and implementations at all. Without the shared ground stated, that same disagreement reads as a choice between incompatible worldviews.

There is a practical filter in this for anyone doing the choosing rather than the writing. When you read a comparison — of two libraries, two architectures, two methodologies — try to reconstruct what the document never argues about, since that is usually the part that determines whether either option will work for you. The advertised differences are typically decidable later, cheaply, or by preference; the unmentioned common assumption is the one that will be load-bearing and the one you cannot change afterwards. And when you write the comparison yourself, notice that you have unusual access to that background, because you are the person for whom it was too obvious to mention.

**Source:** [Communicating Sequential Processes](../works/communicating-sequential-processes-book.md) — the closing paragraph of the discussion chapter's mathematical-models section, in which Hoare states that his description has overemphasised the differences of CCS and overstated the case for the practical application of his own approach, and that the two share their most important characteristic — a sound mathematical basis for reasoning about specifications, designs and implementations — either being usable for both theoretical investigation and practical application.
