---
type: lesson
title: "Audit afterward which part of a borrowed theory you actually used"
figure: scott
works: [data-types-as-lattices]
axes: [cognitive-load, primitive-count]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Audit afterward which part of a borrowed theory you actually used

**Lesson:** Work that builds on an existing body of theory almost always announces the dependency in bulk — assumes familiarity with the field, cites the standard text, moves on. Scott does something more useful at the end of the section where the dependency is heaviest: he goes back and asks how much of the presupposed theory the development actually consumed, finds the answer is very little, and writes out the short list. One familiar class of functions with worked examples, one workable definition of the central notion, a handful of easy closure facts about it. That is the whole import bill, and stating it converts the entry price for a reader from "go learn that subject" into a page of preliminaries.

The audit has to be done after the work rather than before, which is precisely why it usually does not get done. Before you start you cannot know which facts you will lean on, so you reach for the whole theory as insurance; afterward you know exactly, but the work is finished and revisiting the front matter feels like tidying. It is not tidying. It is the step that turns a result depending on a field into a result depending on a list, and only the second kind can be checked, reused in a different setting, or ported by someone who does not already live in that field.

The audit also surfaces something the bulk citation hides: parts of the imported theory that turned out to need no importing at all, because the new construction already contains them. In Scott's case the treatment of functions that may fail to produce an answer, normally a substantial separate development in the borrowed theory, needs no separate introduction, since the framework's ordinary objects already behave that way by construction. That is worth generalizing. When your new setting absorbs a chunk of the old theory as a special case rather than as a prerequisite, you have learned something real about the setting — it is doing more work than you credited it with — and you have found a piece of the dependency you can simply delete instead of documenting.

**Source:** [Data Types as Lattices](../works/data-types-as-lattices.md) — the closing paragraph of Section 3, where Scott observes that although knowledge of recursively enumerable set theory was presupposed, analysis shows the required knowledge is slight, then enumerates precisely what a reader needs — primitive recursive functions with standard examples, one of two equivalent working definitions of recursive enumerability, and a few obvious closure properties — and notes that partial functions need no separate introduction because they are naturally incorporated into his multiple-valued setting.
