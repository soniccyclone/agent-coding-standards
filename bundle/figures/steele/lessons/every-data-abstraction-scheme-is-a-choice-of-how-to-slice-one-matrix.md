---
type: lesson
title: "Types and operations form one matrix, and every data-abstraction scheme is just a choice of which way to slice it"
figure: steele
works: [lambda-the-ultimate-declarative]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Types and operations form one matrix, and every data-abstraction scheme is just a choice of which way to slice it

**Lesson:** Imagine a grid whose rows are kinds of data and whose columns are operations, each cell holding the sequence of primitive actions that this operation performs on that kind of data. Every program that manipulates more than one kind of value is implementing part of this grid, and no realistic program writes it out cell by cell; the grid is always factored. The decisive design question is the direction of the factoring. Group by column and you get an operation implemented once as a routine that begins by asking what it was handed — adding an operation is then a single new routine, but adding a kind of data means touching every routine. Group by row and you get each value carrying its own behavior and answering requests about itself — adding a kind of data is then self-contained, but adding an operation means visiting every kind of data.

Framing it as one grid with two factorings does something that arguing about paradigms does not: it shows that the two styles are not competing philosophies with a winner, they are dual, and each is easy in exactly the dimension the other is hard. That is a structural fact about the grid, not a deficiency of either technique. It also predicts the failure mode of trying to have both — factoring in both directions at once, one cell per module, is possible and has been tried, and it produces code that is fragmented along whichever axis the reader is currently thinking in.

The practical value is in choosing deliberately rather than by habit or by whatever the language makes easy. Ask which axis of your problem is going to grow. A system that will accumulate new kinds of things with a stable set of operations wants row-wise organization; a system with a fixed set of things and an open-ended set of analyses over them wants column-wise, and forcing the second into a row-wise style produces the familiar pain of adding one method to forty classes. The framing also demystifies dispatch: whether a value's row is selected by a tag, a pointer, or the code of a closure that answers messages is an implementation detail of the same act — indexing the grid — so the choice can be made on cost grounds without pretending it is a semantic difference.

**Source:** [Lambda: The Ultimate Declarative](../works/lambda-the-ultimate-declarative.md) — the procedural-view-of-data-types section, which lays out the operand-by-operation matrix and then compares slicing it by columns as conventional type-dispatching routines against slicing it by rows as self-describing objects.
