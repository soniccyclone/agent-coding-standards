---
type: work
title: "Mining of Massive Datasets"
figure: ullman
description: A textbook, built out of Stanford's CS246/CS345A courses, covering the algorithmic side of large-scale data analysis — MapReduce, locality-sensitive hashing, stream algorithms, link analysis (PageRank), recommendation systems, clustering, and (in the 3rd edition) deep learning. Cambridge University Press returned the rights to the authors, who now give the full book away free rather than let it go out of print. It's the same "textbook as the mechanism for shaping how a subfield is taught" pattern as Ullman's earlier database books, just applied to data mining instead of relational/Datalog theory.
subdomains: [databases-and-data-management, algorithms-and-complexity]
year: 2020
url: http://infolab.stanford.edu/~ullman/mmds/book0n.pdf
survey_pages: 603
survey_text_layer: full
survey_fetch_mb: 3
access: public
host: self-archived
tags: [work]
---

# Mining of Massive Datasets

**Author(s):** Jure Leskovec, Anand Rajaraman, Jeffrey D. Ullman
**Venue/year:** 3rd edition, 2020 (1st ed. 2011, published by Cambridge University Press; rights reverted to the authors, who distribute it free by agreement with the publisher).
**Source:** http://infolab.stanford.edu/~ullman/mmds/book0n.pdf — live, self-archived full-book PDF (603 pp.) on Ullman's own Stanford InfoLab page, linked from the book's own site http://www.mmds.org (verified 200 via direct fetch).

## Lessons
- [Compute what randomness alone would hand you, before you trust any discovery](../lessons/compute-what-randomness-alone-would-hand-you.md)
- [Learn only the part of the problem you cannot state yourself](../lessons/learn-only-what-you-cannot-state-yourself.md)
- [Restartability is a shape you keep, not a feature you add](../lessons/restartability-is-a-shape-not-a-feature.md)
- [A cost model is a claim about which resource runs out first](../lessons/a-cost-model-is-a-claim-about-what-runs-out-first.md)
- [The dependency between inputs and outputs bounds what any parallel version can cost](../lessons/what-each-output-needs-bounds-what-parallelism-can-cost.md)
- [Compress so that one question survives exactly, not so the data gets smaller](../lessons/compress-so-that-one-question-survives-exactly.md)
- [Build the error curve you want by composing tests too weak to use alone](../lessons/build-the-error-curve-you-want-from-weak-tests.md)
- [Hold a signal out of the score so it can tell you what the score means](../lessons/hold-back-a-signal-to-calibrate-the-score.md)
- [Sample the entity your question quantifies over, not the records in front of you](../lessons/sample-the-entity-your-question-is-about.md)
- [How you combine independent estimates is part of the estimator, not a formality](../lessons/how-you-combine-estimates-is-part-of-the-estimator.md)
- [When the exact question is provably unaffordable, change the question](../lessons/when-the-exact-question-is-unaffordable-change-the-question.md)

_Coverage note: lessons above are drawn from Chapters 1-4 (pp. 1-174), read in full.
Chapters 5-13 (link analysis, frequent itemsets, clustering, advertising, recommendation,
social-network graphs, dimensionality reduction, large-scale ML, deep learning; pp. 175-568)
are not yet mined, so this work is deliberately left unmarked as fully extracted._
