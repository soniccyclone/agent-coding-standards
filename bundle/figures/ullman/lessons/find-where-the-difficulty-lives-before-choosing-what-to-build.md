---
type: lesson
title: "Find which half of the problem is hard, because the deployed part is often trivial"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Find which half of the problem is hard, because the deployed part is often trivial

**Lesson:** A working classifier for fraudulent mail can be decomposed into two pieces that could not differ more in difficulty. One piece is a table of weights over words, positive where a word signals fraud and negative where it signals legitimacy. The other is the thing that runs in production: add up the weights of the words present, and call it fraud if the total is positive. The second piece is a sum and a comparison. Essentially all the intellectual content, all the data, and all the risk live in the first.

Naming this split changes how work gets estimated and staffed. The running system is what everyone looks at, so effort gets allocated to it — its architecture, its latency, its deployment — while the artifact it consumes is treated as an input that will show up somehow. Inverting that attention is usually correct: if the algorithm is a sum, then improving the system means improving the weights, and no amount of engineering on the trivial half moves the outcome. It also relocates where correctness has to be established. You cannot test a sum-and-compare into being right; the properties you care about are properties of the table, so that is where validation, provenance and monitoring belong.

The distinction generalizes past classifiers because plenty of problems have no model at all — a similarity-search scheme or a streaming estimator is difficulty embodied directly in the procedure, with nothing separable to consume. So the useful question is not "what is my model" but "where does this problem keep its difficulty," and there are three answers worth distinguishing: in an artifact that is expensive to produce and cheap to apply, in a procedure that is intrinsically clever with no artifact, or split between them. Each implies a different shape of effort, and mistaking one for another is how teams end up with an elegant serving layer and a worthless table, or with a heavily engineered pipeline around an algorithm nobody found the trick for.

The habit to keep: before designing anything, separate the parts of the task by how hard each is to get right, not by which will be visible in the finished system. The visible part is frequently the easy part, and it will absorb attention in proportion to its visibility unless you deliberately spend it elsewhere.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's opening on modeling, which uses phishing detection as its example: a model of weights on words, and then a detection algorithm that merely sums the weights in an email and reports phishing when the sum is positive, with the note that finding the best weights is the difficult problem. The same section observes that the objective of data mining is more generally an algorithm rather than a model — locality-sensitive hashing and the stream-mining algorithms involve no model — while in many applications the hard part is creating the model and the algorithm to use it is then straightforward.
