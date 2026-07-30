---
type: lesson
title: "A case split in a basic law is a prediction of where the bugs will be"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, formal-methods-and-verification]
tags: [lesson]
---
# A case split in a basic law is a prediction of where the bugs will be

**Lesson:** When you write down the most elementary fact about a representation and find you cannot state it without a conditional, treat that conditional as a forecast. It is telling you that programs over this representation come in two flavours, that the two flavours behave differently, and that some of your code will handle one and not the other. The size of a range described by its two endpoints is the example: for endpoints in the expected relation the size is their difference, and otherwise it is zero, because a set cannot have a negative size. That single "otherwise" is the seed of an entire class of defects, and noticing it at the moment you define the notion is far cheaper than discovering it later as a program that loops forever on empty input.

The underlying cause is almost always redundancy in the representation: one abstract value has several encodings. Here only the empty range has the anomalous encodings — but it also has ordinary ones, which is exactly what makes the situation treacherous, since testing with an empty range does not reliably exercise the anomalous form. The productive response is to name the two classes and then keep the distinction visible. Once you can say that an encoding is well-formed or degenerate, you can state which of your operations require well-formedness, which tolerate degeneracy, and which produce it; the vocabulary turns a lurking case analysis into something you can quantify over and check. Without the vocabulary you are left with a hazard nobody can talk about.

Three follow-through habits make the diagnosis pay off. Enumerate the classes explicitly and completely, since the count is usually larger than expected — a range's endpoint difference can be positive, zero, or negative, and the middle case is well-formed-but-empty, which is neither of the two you had in mind. Then, for each operation, decide deliberately whether it should reject degenerate input, normalize it, or handle it correctly, and write that decision down; the failure mode is not choosing wrongly but different parts of the system choosing differently. Finally, if you get to design the representation, spend real effort eliminating the redundancy at the source, because a representation in which every abstract value has exactly one encoding lets every law be stated without a conditional, and then there is no forecast of bugs to act on.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 2.2.2's treatment of interval size, which observes that needing a conditional expression to describe a fundamental property of intervals is a clear portent of a source of programming errors because a program may be correct for one case and not the other, introduces the regular and irregular representations to name the distinction, and tabulates the three cases showing that only the empty set has irregular representations while it also has regular ones.
