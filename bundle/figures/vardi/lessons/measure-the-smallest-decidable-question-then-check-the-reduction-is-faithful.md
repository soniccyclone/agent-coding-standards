---
type: lesson
title: "Measure the smallest yes-or-no question, then check the reduction back is faithful"
figure: vardi
works: [the-complexity-of-relational-query-languages]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, databases-and-data-management]
tags: [lesson]
---
# Measure the smallest yes-or-no question, then check the reduction back is faithful

**Lesson:** Comparing things that produce outputs is awkward, because output size confounds the comparison and every result class needs its own accounting. Comparing decisions is clean, and the tools for it are sharp. So the productive move when you want to grade a family of output-producing mechanisms is to replace each one by a yes-or-no question — does this particular candidate belong to the output? — and grade those instead. The whole output is recoverable by asking the question of every candidate, so nothing is lost in principle, and the space of decision problems comes with an established ladder of classes and completeness notions you can locate each mechanism on.

The step that makes this legitimate rather than convenient is the check that follows: for the mechanisms you actually care about, is producing the full output really no harder than deciding membership in it? Where the answer is yes, the substitution is free and every conclusion about the decision question transfers. Where it is not, the substitution has hidden the interesting part of the cost, and a paper full of tight bounds is measuring the wrong object. Stating that check explicitly, rather than assuming it, is what separates a reframing from a sleight of hand.

Generalize it as a habit for any hard-to-measure quantity: look for a simpler proxy that your existing instruments handle well, then spend real effort establishing the gap between proxy and target before trusting any number. The payoff is not just tractability but comparability, since once every member of a family has been mapped onto the same kind of question, differences between them become differences on one scale instead of incommensurable descriptions. The risk is that a proxy adopted for convenience quietly becomes the definition, and nobody rechecks the gap when the family grows a new member.

**Source:** [The Complexity of Relational Query Languages](../works/the-complexity-of-relational-query-languages.md) — the definitions section, which converts the study of queries-as-functions into the study of recognizing whether a tuple belongs to a query's result, notes that the full result can be obtained by testing all candidate tuples, and states explicitly that for most of the languages considered the computation cost equals the recognition cost.
