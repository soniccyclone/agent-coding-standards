---
type: lesson
title: "Go back and refit the earlier decisions to the principle you only discovered halfway through"
figure: strachey
works: [the-main-features-of-cpl]
axes: [cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Go back and refit the earlier decisions to the principle you only discovered halfway through

**Lesson:** Design principles are usually presented as inputs, chosen at the start and then applied. In practice the good ones emerge during the work, as the recognition of something several decisions already had in common. What separates a coherent design from a pile of features is what happens next: either the principle is noted and applied to whatever is designed from that point on, leaving the earlier parts as they were, or the earlier parts are revisited and brought into line with it. Only the second produces a structure someone can learn as a whole, because a principle that governs half a system is not a principle, it is a regional convention with a good story attached.

The reason this is hard is that refitting means reopening decisions that already work, on the strength of an argument about uniformity rather than about function. That is exactly the kind of argument teams refuse in the ordinary course of business, and it needs a measurable justification to survive. The measure available is the count of special cases the refit removes: a genuine principle, applied retroactively, eliminates rules that previously had to be stated separately and remembered separately. If a newly found principle does not reduce that count, it is a description of the design rather than a constraint on it, and refitting to it buys nothing.

So the practical procedure is to keep a running list of the rules a user would have to be told that do not follow from anything, treat that list as the design's outstanding debt, and use each newly recognized principle as an opportunity to shorten it. This also gives an honest completion criterion for a design's structure, distinct from its functionality: not that everything is implemented, but that the number of things which must simply be memorized has stopped falling.

**Source:** [The Main Features of CPL](../works/the-main-features-of-cpl.md) — the introduction's account of how general principles evolved during the language's development and, as each was recognized, the language was refined to conform to it, with the stated result of a coherent unified structure containing a minimum of ad hoc rules.
