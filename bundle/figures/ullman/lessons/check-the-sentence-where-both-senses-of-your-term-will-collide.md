---
type: lesson
title: "Check the sentence where both senses of your term will collide"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Check the sentence where both senses of your term will collide

**Lesson:** A borrowed technical term and a domain term can be perfectly clear in isolation and unusable together. The test that catches this is concrete rather than abstract: write down the phrase in which both senses will inevitably stand next to each other, and see whether it parses. Algorithms for a certain class of decision-under-uncertainty carry one name; the network on which the application runs carries the same name; the sentence that has to be written is about algorithms of the first kind applied to advertising of the second kind, and it reads as nonsense to anyone who has not been warned. The same book flags a second instance a chapter earlier, where a grouping of similar data points and a grouping of cooperating machines share a word, and the unavoidable phrase is about computing the first on the second.

The reason this class of collision is worth a specific check is that ordinary review does not surface it. Each term was introduced in its own context, by someone competent, and each is standard in its own literature. The defect only exists at the intersection, and the intersection is exactly where your work lives, because importing a technique from one field into another is what put the two vocabularies in the same document. So the risk is highest precisely in the interdisciplinary work that is otherwise most valuable, and it will not be caught by anyone who reads only one of the two fields.

Since both terms are usually established elsewhere, unilateral renaming is generally the wrong move, and both instances in the book resolve the same way: keep both words and disambiguate at the point of collision, prominently, on first use. That is a cheap and durable fix, and it has a property renaming lacks, which is that it stays compatible with everything the reader will encounter outside your document. The mistake is to assume context will disambiguate. It will, for the author, who knows which sense was meant, and not for the reader, who is doing the disambiguation from a standing start while also trying to follow the argument.

Where you genuinely do control the naming, run the collision test before adopting the term rather than after. Writing the worst sentence you will ever have to write with the new name takes a few seconds and is a far better test than judging the name in isolation, which is how names are almost always judged.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the footnote in chapter 8 warning that "on-line" as a property of an algorithm must not be confused with "on-line" meaning on the Internet, citing the parallel case from the clustering chapter of algorithms for computing clusters on computer clusters.
