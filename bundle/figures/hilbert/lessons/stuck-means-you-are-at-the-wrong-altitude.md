---
type: lesson
title: "Being stuck usually means you are at the wrong altitude, not that you lack cleverness"
figure: hilbert
works: [mathematische-probleme]
axes: [cognitive-load]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Being stuck usually means you are at the wrong altitude, not that you lack cleverness

**Lesson:** Hilbert gives two diagnostic moves for a problem that will not yield, and they point in opposite directions. Going up: the difficulty often comes from seeing the problem in isolation when it is really one member of a family, and finding the vantage point from which the family is visible both makes this instance tractable and hands you a method that covers its siblings. Going down: more often, he says, the real obstacle is that some simpler problem underneath has never been solved properly, and the whole task is to locate that easier problem and solve it with tools clean enough to generalize. Neither move is about trying harder at the level you are already on.

The asymmetry in his advice is the interesting part. He rates the downward move as the more frequently decisive one, which cuts against the instinct to reach immediately for the general framework. The reason is that abstraction built before the small case is understood is abstraction over a shape you have guessed at, and it inherits the confusion instead of removing it. Working the simplest unsolved case first gives you something true to generalize from. He adds a warning about the upward move as well: hunting for general methods with no concrete problem in hand is mostly wasted motion, because the problem is what tells you which generalization is the useful one.

For a programmer these two moves cover most of what looks like being blocked. The upward move is noticing that the awkward special case you keep patching is an instance of a class the system has no representation for, and that introducing the missing concept dissolves a dozen patches at once. The downward move is the discipline of shrinking to the smallest failing case, or of admitting that the reason the caching layer is a nightmare is an unsettled question about identity or lifetime one level below it. Someone practiced at both asks, when stuck, only which direction to move — and defaults downward, since a framework erected on an unresolved simpler question just relocates the problem where it is harder to see.

**Source:** [Mathematische Probleme](../works/mathematische-probleme.md) — the pair of methodological remarks between the general discussion and the numbered problems: first on recognizing a problem as a link in a chain of related problems, then on the greater importance of specialization and of solving the easier problems underneath.
