---
type: lesson
title: "One word, two relations: push the meaning into a parameter"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# One word, two relations: push the meaning into a parameter

**Lesson:** The same everyday word will name unrelated relations in different parts of one system, and the collision is invisible because both usages sound obviously correct. Two documents can be called similar because long stretches of them are identical, which is what you want when detecting copies, and two documents can be called similar because they are about the same subject despite sharing almost no phrasing, which is what you want when suggesting further reading. These relations are not weak and strong versions of each other. A pair can score at the top of one and the bottom of the other. Any conversation that does not disambiguate them will produce agreement between people who mean different things, and the disagreement surfaces later as a system that behaves inexplicably for one of its two audiences.

Having noticed the ambiguity, the productive move is not to pick a winner but to make the meaning a parameter. The expensive machinery in this area, which finds close pairs among huge collections without comparing everything to everything, never actually reads the objects. It consumes a distance function and a way to hash under it, and it works identically no matter which notion of closeness was supplied. So the collision that looked like a definitional problem turns out to be free at the level that costs money: build the search once, and let each application choose what closeness means. That is the payoff for finding the narrowest thing your infrastructure genuinely depends on, which is nearly always narrower than what it appears to be about.

The parameterisation does come with a companion obligation, and skipping it is how this gets botched. Each notion of distance needs its own randomised hashing scheme with the property that near things collide more often than far things, and those schemes are not interchangeable. So the abstraction boundary is not "a distance function" but "a distance function together with a family that is sensitive to it," and a metric for which no such family is known cannot be plugged in no matter how well it captures your intent. Get the boundary right and swapping meanings is a line of configuration. Get it wrong by exposing only the metric and every new notion of similarity becomes an emergency.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 9's sidebar on two kinds of document similarity in the content-based recommendation section, which distinguishes the lexical similarity of shared character sequences used earlier in the book from the recommendation-oriented notion of sharing many important words even with little lexical overlap, and notes that the same locality-sensitive machinery applies once a distance measure is fixed, with minhashing paired to set overlap and random hyperplanes paired to angular distance.
