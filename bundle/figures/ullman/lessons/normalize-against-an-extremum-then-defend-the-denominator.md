---
type: lesson
title: "Normalize against an extremum, then go defend the denominator"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, algorithms-and-complexity]
tags: [lesson]
---
# Normalize against an extremum, then go defend the denominator

**Lesson:** When raw counts have to be compared across containers of wildly different sizes, the obvious denominator is the container's total, and there is a better one available: the largest count inside that same container. Dividing by the local maximum puts every container's strongest member at exactly one and everything else on a fraction of it, which makes the score answer a question about standing within its own context rather than about absolute magnitude. That is often what you actually wanted, and it comes with two properties a total-based ratio does not have — a guaranteed upper bound, so downstream thresholds and combinations are on known ground, and insensitivity to how much irrelevant filler the container carries, since filler inflates a total but does not touch a maximum.

The cost is that you have moved the entire scale onto one observation, and one observation is the least robust statistic there is. Everything downstream is now hostage to whichever member happened to be largest. If a member can be large for reasons unrelated to what you are measuring — a structural element that appears in every container, a boilerplate artifact, a sentinel, a systematically duplicated record — it will win the maximum in nearly every container, and every score in the system becomes a ratio against that thing. The measure keeps functioning and quietly stops discriminating, because the denominator now varies with the wrong quantity.

So an extremum normalizer is not finished when you write it down. It comes with an obligation to state which members are eligible to be the maximum and to exclude the ones that are large for uninteresting reasons — the same exclusion list you would apply to the signal itself, applied a second time to the denominator, which is the step people forget because the denominator does not look like part of the measurement. It also comes with an obligation to think about the degenerate cases the extremum creates and the total does not: a container whose members are all equal, or a container with a single member, both score one and carry no information, and whether that is acceptable depends on whether such containers exist in your data.

The general shape is worth carrying past this instance. Any normalization is a claim about what the score should be invariant to, and the choice of denominator is where that claim lives — divide by a total and you have said scale should not matter, divide by a maximum and you have said only relative standing should matter, divide by a spread and you have said only surprise should matter. These are different measures that will rank the same data differently, and the decision belongs upstream with the question rather than downstream as a formatting detail. Pick the denominator from what you want the score to mean, then audit the population that denominator is computed over as carefully as you audited the numerator.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 1's definition of TF.IDF, whose term-frequency factor divides a term's count in a document by the maximum count of any term in that same document, so the document's most frequent term receives a value of one and all others a fraction, with the parenthetical instruction that the maximum should perhaps be taken after excluding stop words — the same stop-word removal the chapter earlier prescribes for the documents themselves.
