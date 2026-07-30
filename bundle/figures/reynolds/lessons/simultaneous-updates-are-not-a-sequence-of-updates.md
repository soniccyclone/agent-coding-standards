---
type: lesson
title: "A set of simultaneous updates is not the same as performing them one at a time"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# A set of simultaneous updates is not the same as performing them one at a time

**Lesson:** When you have several changes to make and each of them reads values the others are about to destroy, the collection of changes is a single operation and not a sequence. Doing them in some order does not implement it. The smallest instance is a pair of variables that must each take on a function of both old values: assign to the first and the second's new value has lost its input; assign to the second and the first's has. Neither order is right, and there is no third order. What the situation demands is either a stated simultaneous update or a staging step that captures the old values somewhere out of harm's way before any of them is overwritten. The same phenomenon appears wherever names are being replaced rather than values: replacing one name with another and then the second with the first, one after the other, does not swap them — it collapses them both onto one — whereas the simultaneous replacement does swap them.

The reason this bites so often is that most notations make the sequential reading the default and give the simultaneous one no syntax at all, so the difference lives entirely in the programmer's head. That makes it a class of bug you cannot find by looking for a mistake, because each individual step is correct; only the composition is wrong. The reliable defense is a habit at the point of writing: before ordering a group of updates, ask which of them read state that another one writes. If none do, the order is genuinely free and you should stop worrying. If any do, the group is atomic in the sense that matters here, and you owe it either a real simultaneous form or an explicit snapshot of the pre-state.

The habit scales past variables and covers most of the places multi-part changes go wrong. A rename that shuffles several identifiers, a migration that moves data between columns, a configuration merge, a set of mutually-referencing rows being repointed, a batch of file moves — all are read-write tangles wearing different clothes, and all fail in the same way when executed serially without staging. Notice too that the staging variable is not clutter to be optimized away; it is the visible record of the fact that the group is simultaneous. When someone later "simplifies" it out and the order suddenly matters, the deleted variable was the documentation.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 1.3.6's Fibonacci development, where updating each of the two accumulators requires the other's previous value so that either order loses information and a temporary variable is introduced; together with Section 2.2.6's closing observation that simultaneous substitution can produce a different result than repeated substitution, illustrated by the two-name exchange.
