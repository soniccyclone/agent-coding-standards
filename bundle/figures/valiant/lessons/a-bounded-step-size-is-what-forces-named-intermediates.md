---
type: lesson
title: "A bound on what one step can span is what forces named intermediates, and it sets their granularity"
figure: valiant
works: [a-theory-of-the-learnable]
axes: [cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# A bound on what one step can span is what forces named intermediates, and it sets their granularity

**Lesson:** Layered abstraction usually gets defended on aesthetic grounds — tidiness, separation of concerns, taste. There is a harder argument available. If the mechanism that acquires new capability can only span a bounded gap in a single unaided step, then anything beyond that gap is unreachable except by constructing a chain of intermediates, each within reach of the one before. Naming and ordering those intermediates is not a stylistic contribution; it is the only route to the far end. Whoever does that work — a teacher, a library author, a designer of a curriculum or an API — is performing an act structurally identical to programming, and the reason the work is necessary is a complexity bound rather than a preference.

The sharper consequence is that the bound is quantitative, so the granularity of the intermediates is not up for negotiation either. A theory of what can be acquired in one step tells you the maximum size of a rung: too coarse and the step is genuinely impossible, so the chain breaks; too fine and you have paid for structure that bought nothing. This turns a question normally settled by argument — how big should a module, a lesson, a layer be? — into something you could in principle compute from what the acquiring mechanism can do. Even without the exact number, the framing changes how the question is asked, from "does this decomposition feel right" to "can each step actually be taken from the one below it."

The reason chains work at all is that a named intermediate becomes an ordinary primitive for everything built afterwards, indistinguishable from something given at the start. What was expensively acquired becomes cheap vocabulary, and the next step's difficulty is measured against the new vocabulary rather than the old. That is why the ordering matters so much: a chain is only as good as its worst gap, and a well-chosen intermediate is exactly the one that shortens the longest remaining stretch.

**Source:** [A Theory of the Learnable](../works/a-theory-of-the-learnable.md) — the introduction's conclusion that a severely limited learnable class implies complex concepts must be built from simple ones by a teacher who identifies, names and sequences the intermediates as a programmer would, with the theory setting the maximum granularity of any single unprogrammed step; together with the earlier observation that previously acquired concepts subsequently serve as available variables.
