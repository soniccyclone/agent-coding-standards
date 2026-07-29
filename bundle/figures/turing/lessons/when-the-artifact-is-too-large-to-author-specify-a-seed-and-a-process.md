---
type: lesson
title: "When the artifact is too large to author, specify a small seed plus the process that grows it"
figure: turing
works: [computing-machinery-and-intelligence]
axes: [cognitive-load, primitive-count, expressiveness]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# When the artifact is too large to author, specify a small seed plus the process that grows it

Estimate your own authoring rate against the size of the thing you have been asked to write, and sometimes the arithmetic says the direct approach cannot be completed by any team you could assemble in any time you have. That estimate is not a reason to give up on the goal; it is a reason to reject the shape of the plan. The alternative shape is to write something much smaller — an initial configuration with very little structure and a great deal of unwritten capacity — and then write the feedback process that drives it toward the target. The problem has been split in two, and the two halves are coupled: a seed is only good relative to a training regime, and a regime only works against a seed that can absorb it.

Two properties make the split pay. First, the process can be steered, which a blind search cannot: when a weakness has a traceable cause, the next variation is chosen rather than sampled, and directed variation beats undirected variation by a factor that grows with how well you can diagnose. Second, undirected sampling is still the right primitive at the innermost level, because when acceptable solutions are plentiful and the space contains long barren stretches, drawing at random avoids both the bookkeeping of exhaustive enumeration and the risk of enumerating a region that happens to contain nothing. Notice the asymmetry: randomness where you have no information, direction where you do.

There is a price, and it must be accepted up front rather than discovered later. The person who builds a system this way gives up the clear mental picture of internal state that ordinary construction affords. You may be able to predict the thing's behaviour without being able to say what it is doing, and the correspondence between what you wrote and what runs becomes statistical rather than structural. The apparent paradox of a system whose rules change is dissolved by stratifying them: the outer rules governing how change happens are fixed and are what you actually authored, while the inner rules are provisional, hold only until revised, and were never yours.

A programmer who thinks this way asks, before writing a large body of hand-specified behaviour, whether the specification could instead be a small kernel plus a corpus plus a scoring function. The same reflex applies far from machine learning: configuration generated from a policy rather than enumerated by hand, test cases produced by a generator plus properties rather than written one by one, schemas derived from a description rather than transcribed. In each case the artifact you maintain is the seed and the process, and the large thing is downstream output you never edit directly.

**Source:** [Computing Machinery and Intelligence](../works/computing-machinery-and-intelligence.md) — the constructive final section, which begins from an explicit arithmetic of how long hand-programming would take, proposes the child-machine-plus-education split instead, and then works through steering, randomness, and the teacher's necessary ignorance of the pupil's internals.
