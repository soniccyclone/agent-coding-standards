---
type: lesson
title: "A taxonomy of failures is worth what it makes you look for, not whether its boxes are disjoint"
figure: parnas
works: [active-design-reviews-principles-and-practices]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A taxonomy of failures is worth what it makes you look for, not whether its boxes are disjoint

**Lesson:** Engineers who classify things carry over a mathematician's instinct: a good classification partitions, categories are mutually exclusive, and an item belonging to two boxes means the scheme is defective. That instinct is misapplied when the classification's job is to direct a search. A list of the kinds of way a design can be wrong — it contradicts itself, it forces its users into waste, it can be read two ways, it cannot absorb the change that is coming — is not a filing system for defects already found. It is a generator of distinct search strategies, each of which sweeps the artifact along a different axis. Overlap between two such sweeps costs almost nothing; a gap between them costs you an entire class of defect, permanently and invisibly.

This reframes how you should evaluate any such scheme. Do not ask whether the categories are clean, or argue about which box a given item belongs in — that argument consumes real effort and yields nothing detectable. Ask instead whether each category, held in someone's mind while they read, causes them to notice something the other categories would not have surfaced. A category that induces no distinct looking is dead weight regardless of how neatly it partitions; two categories that overlap heavily but each catch things the other misses are both earning their place. The purpose is coverage of the search space, and the currency is attention directed, not items sorted.

The same logic explains why one entry on such a list will look like it does not belong. Inflexibility — a design that cannot accommodate a change it will be asked to accommodate — is not a defect in the same sense as a contradiction; it may be evidence that a requirement was misunderstood upstream rather than that this design is internally wrong. Keeping it on the list anyway is correct, because it directs a reader toward exactly the errors that were made before this document was written and were never caught. A reviewer who only hunts for errors introduced at this step will confirm faithful execution of a mistaken premise. The most valuable thing a review finds is often not in the thing being reviewed.

**Source:** [Active Design Reviews: Principles and Practices](../works/active-design-reviews-principles-and-practices.md) — the error-classification section, which introduces its four categories and then explicitly disclaims any intent that a defect fall into exactly one of them, stating the point is to shape reviews that find as many defects as possible; the surrounding discussion of reviews needing to catch errors made earlier is the companion argument.
