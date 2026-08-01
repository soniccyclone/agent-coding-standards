---
type: lesson
title: "A feature that did not help also indicts the path that delivered it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# A feature that did not help also indicts the path that delivered it

**Lesson:** When an added signal fails to improve a system, the natural conclusion is that the signal carries no information. That conclusion is unsupported, because what was actually tested is the composition of the signal with everything that had to happen to get it into the model. If the signal lived in a separate dataset, something had to match its records against yours, and that matching is a fallible process with its own error rate. A weak matcher delivers a feature that is correct on some rows and scrambled on others, and a scrambled feature is indistinguishable from an uninformative one in the final score. The experiment you ran measured the product of two things and you are attributing the result to one of them.

There is a second, independent explanation that also fits a null result, and it points the opposite way: the information may be genuinely present and genuinely useful, but already recovered by the model from the data it had. A learned low-dimensional representation of behaviour will discover something very close to a category system if the category system is what drives behaviour, so bolting on the human-curated taxonomy adds nothing measurable while confirming that the taxonomy was real. That is a completely different finding from "the taxonomy is irrelevant," and it implies a completely different next move. Under the redundancy explanation you should stop looking for external metadata of that kind. Under the broken-join explanation you should fix the join, because the feature may be worth a lot.

The discipline is to design the negative result so it can be attributed before you run it. Measure the delivery path on its own: sample the joined rows and check by hand what fraction matched correctly, then reason about what a feature with that corruption rate could have shown even if it were perfect. Alternatively test the feature on the subset where the match is certain, where the delivery path contributes no noise. Both cost far less than the ambiguity costs, and the ambiguity is expensive precisely because negative results get filed as settled. A finding recorded as "we tried it, it didn't work" without an attribution is a finding that will be re-derived by someone else in three years, or worse, quietly believed.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's account of the Netflix challenge, where attempts to enrich the ratings data with an external movie database's genre, actor and director information were found not to help, and the authors offer two unresolved explanations: that the learning algorithms had already extracted the relevant structure, and that matching movie titles across the two sources is itself an entity-resolution problem nobody solved exactly.
