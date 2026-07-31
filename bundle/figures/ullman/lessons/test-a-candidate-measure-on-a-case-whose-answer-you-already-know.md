---
type: lesson
title: "Test a candidate measure on a tiny case whose answer you already know"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Test a candidate measure on a tiny case whose answer you already know

**Lesson:** Choosing how to compare two things is usually treated as a matter of taste or of what the library provides, and the choice is then validated — if at all — by looking at aggregate output on real data, where nobody can tell whether it is right. The stronger method costs almost nothing: construct an example small enough to hold in your head, in which you are certain what the answer ought to be, and run every candidate against it. A measure that disagrees with an unambiguous case is disqualified regardless of how principled it looks, and you learn this in minutes instead of after a quarter of production behaviour that seemed vaguely disappointing.

The example has to be built to discriminate, which is the skill worth practising. A useless probe is one where all candidates agree. A good probe isolates the specific way candidates differ: two parties who evaluated the same two things and reached opposite conclusions must come out far apart, and any measure that instead reports them as close because they happened to engage with the same things has confused participation with agreement. That single case eliminates a whole family of set-overlap measures, and it does so with numbers you can compute by hand and check.

The failures such a probe exposes are structural, not numerical, which is why staring at real output would not have found them. A measure defined over which entries exist discards the values entirely, so it cannot distinguish agreement from disagreement in principle. A measure that reads unobserved entries as the bottom of the scale treats the enormous absent mass as evidence of dislike, so it reports similarity dominated by what neither party has touched. Each of these is a sentence-long argument once you have the case in front of you, and nearly invisible without it.

Generalise past distance functions. Any component whose job is to make a judgment — a ranking function, a conflict resolver, a scheduler's priority rule, a diff algorithm — should be checked against a handful of hand-built situations where a competent person's expected answer is not in doubt. These probes are cheap to write, they survive every refactor because they encode intent rather than implementation, and their real value is diagnostic: when one fails you usually learn something about the representation, not just about the function.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the similarity-measure section of the collaborative-filtering part of the recommendation-systems chapter, where a deliberately tiny ratings table containing one pair of raters with opposite opinions on the two items they both rated is used to reject set-overlap similarity and to expose what treating blanks as the lowest value does to the cosine measure.
