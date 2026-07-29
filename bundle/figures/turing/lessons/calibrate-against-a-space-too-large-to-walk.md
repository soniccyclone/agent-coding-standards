---
type: lesson
title: "Calibrate against the whole space by computing its summary in closed form, never by walking it"
figure: turing
works: [paper-on-the-statistics-of-repetitions]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Calibrate against the whole space by computing its summary in closed form, never by walking it

**Lesson:** A statistical decision procedure is only as good as the baseline it scores against, and the honest baseline is usually defined over a set of possibilities far too large to enumerate. The naive reading of that is a dead end: you cannot generate every candidate alignment of every pair of messages, so you fall back to a small sample and inherit its bias. The move worth learning is to notice that you never needed the individual candidates, only aggregate counts over them, and aggregate counts over a regularly structured space are frequently available as a formula. Laying the material out as one cycle against a copy of itself makes the entire family of relative offsets a single geometric object, and the total overlap across all of them, plus the expected repeat counts, then follow from a closed-form expression — with the degenerate offsets and the symmetry between an offset and its mirror handled by subtracting named terms rather than by filtering a generated list.

The reason this is not a trick but a habit is that the structure making the space large is usually the same structure making it regular. Combinatorial blowup comes from repeated uniform choice, and uniformity is exactly what lets a sum be evaluated instead of accumulated. So the size of the space is weak evidence that enumeration is required; it is often better evidence that enumeration is unnecessary. The discipline is to write down what you want as a sum over the space first, then attack the sum, rather than reaching for sampling the moment the cardinality looks bad.

The programmer who works this way treats "we'll estimate it from a sample" as a fallback that needs justification, not a default. Before generating candidates they ask what functional of the candidate set the algorithm actually consumes, because the answer is often a handful of moments or counts. This shows up in choosing an analytic null distribution over a permutation test, in deriving an expected collision count from parameters instead of measuring one, and in computing a cost-model estimate over a plan space rather than materialising plans. It also has a verification payoff: a closed-form baseline is a thing you can differentiate, sanity-check at limits, and disagree with precisely, in a way a sampled baseline never is.

**Source:** [Paper on Statistics of Repetitions](../works/paper-on-the-statistics-of-repetitions.md) — the passage constructing the complete set of comparisons as two concentric cycles of the material, arguing the aggregate repeat statistics follow without any comparison actually being performed, and correcting for the unrotated and half-turn cases by adjusting the formula.
