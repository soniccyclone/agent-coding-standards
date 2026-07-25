---
type: lesson
title: "Indirection is a debt, and only demonstrated recurrence pays it off"
figure: gang-of-four
works: [design-patterns-abstraction-and-reuse-of-object-oriented-design]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Indirection is a debt, and only demonstrated recurrence pays it off

**Lesson:** The most easily ignored passage in this paper is the one that undercuts its own enthusiasm. The authors state that the flexibility their catalog offers is purchased with additional layers of indirection, that indirection makes a design harder rather than easier, and that a structure should therefore be introduced only when the specific freedom it provides is genuinely wanted. This is not modesty. It is the claim that flexibility has a unit price, denominated in what a reader must hold in mind to follow a path through the code. A design that can vary along six axes has six forwarding layers a maintainer must traverse, and if only one of those axes ever moves, five of them are pure cost — a larger set of parts buying no additional reachable behavior.

The same skepticism gets applied to their own subject matter one paragraph later, and this is where it becomes a rule of thought rather than a caveat. They anticipate that people will start labeling any clever trick a pattern, and set a bar against it: a genuine one is non-trivial and has demonstrably been applied more than once. Elsewhere they describe how the catalog was screened — entries had to have seen real use, most of them more than twice, ideally either found independently by different people or exercised across unrelated domains. That is an empirical admission criterion, and it is doing epistemic work. Recurrence across independent contexts is evidence that a structure is a real feature of the problem space rather than an artifact of one system's history or one author's taste. Without it, you cannot distinguish a discovered structure from an invented one, and inventions generalize badly.

Both halves point the same way, and the second is what makes the first actionable. Abstraction is justified by observed repetition, never by anticipated repetition. You are allowed to generalize from cases you have in hand; you are not allowed to generalize from cases you expect to have, because the expectation is unfalsifiable at the time it is most tempting. It is worth noticing that the authors themselves report applying these structures after a first implementation existed rather than designing them in from the start — the recurrence had to show up before the abstraction was warranted.

A programmer who takes this seriously waits for the second and third instance before factoring, treats a proposed abstraction with exactly one user as a hypothesis rather than a design, and asks of every layer of indirection what variation it exists to permit and whether that variation has ever actually occurred. They read speculative generality as a defect of the same family as duplication, not as its cure.

**Source:** [Design Patterns: Abstraction and Reuse of Object-Oriented Design](../works/design-patterns-abstraction-and-reuse-of-object-oriented-design.md) — the caveats closing the conclusion, together with the introduction's account of the screening criteria used to admit entries into the catalog and the observation that patterns were frequently applied only after an initial implementation.
