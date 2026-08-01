---
type: lesson
title: "Anchor features on whatever marks payload apart from packaging"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Anchor features on whatever marks payload apart from packaging

**Lesson:** When you compare two composite artifacts, you are rarely asking about the whole artifact. A page carries the thing you care about surrounded by material you do not — navigation, boilerplate, advertising, generated headers — and a uniform feature extraction weights all of it by length, so two pages sharing a template can score higher against each other than two pages sharing the actual content. Turning up the threshold does not fix this; it fails in both directions at once. The fix is upstream, in what you extract: find a property that the payload has and the packaging does not, and define your features so they can only anchor on that property. The extraction then produces many features from the part you care about and few or none from the rest, and ordinary similarity over those features gives you the comparison you actually wanted.

The instructive part is which property does the work. Prose is written in a register that boilerplate is not: it is full of the connective, contentless words that every text-processing pipeline strips out first as noise. Anchoring each feature at one of those words and taking what follows produces a dense harvest from running prose and almost nothing from a caption or a slogan. So the signal is precisely the material a different question had taught you to discard. That is the reusable observation — "noise" is a judgement relative to one question, and the tokens that carry no topical information can be excellent markers of *genre*, which is a different axis and sometimes the one you need. Before building a classifier to separate content from chrome, look for a cheap syntactic marker that already correlates with the split.

Two cautions keep this honest. The marker is a proxy, so state what it would take to fool it — payload written in the wrong register goes unseen, and packaging that happens to contain prose gets counted — and decide whether that failure mode is acceptable in your data rather than assuming it away. And a biased extractor makes the similarity score no longer comparable to one computed uniformly, so the threshold has to be recalibrated for the new features rather than carried over.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the word-shingle section of the similar-items chapter, which defines a shingle as a stop word plus the two words following it, on the grounds that news prose is dense in stop words while surrounding advertisements, logos and link lists are not, so pages carrying the same article score as similar even when their surroundings differ and pages sharing only their surroundings do not; with the worked contrast between a short advertisement yielding no shingles and a comparable sentence of prose yielding nine.
