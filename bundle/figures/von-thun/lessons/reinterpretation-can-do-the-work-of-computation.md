---
type: lesson
title: "Reinterpretation can do the work of computation — at a cost in generality"
figure: von-thun
works: [some-simple-programming-in-joy]
axes: [expressiveness, primitive-count]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# Reinterpretation can do the work of computation — at a cost in generality

Reversing a sequence is a computation: you write a loop or a recursion that moves elements one at a time onto an accumulator. Von Thun gives that version, then gives another one and admits to being surprised by it. Since a list of values, when executed, pushes each of its values in turn, and since there is an operator that runs a program using some other list as the working area, a list executed against an empty area lands with its elements in opposite order — reversal, with no reversing code. He points out that this is possible only because the identification of program with data extends to the working store as well, and notes that the reinterpretation is also the faster of the two.

That is the general shape worth carrying: before writing an algorithm, check whether some existing mechanism already performs the operation under a different reading of the same structure. When one representation serves several roles — code, data, storage — every operation defined for one role is silently available to the others, and some of them are the operation you were about to implement. This is where the largest simplifications live, because the alternative is not a shorter algorithm but no algorithm.

Von Thun does not oversell it, and the caveat is the more useful half of the lesson. The reinterpretation trick depends on the specific structure being executable, so it works for lists and not for the other sequence type. His polymorphic reversal therefore keeps the ordinary accumulator version and adds a type test to supply the right kind of empty accumulator — the slower, duller implementation wins on the interface that has to serve every case. So the reinterpretation is not simply better; it is cheaper and narrower, and which you want depends on whether the operation is a leaf you can specialise or a general contract you must honour. Recognising a free reinterpretation is one skill; recognising when its narrowness disqualifies it is the other, and the second is the one people skip.

**Source:** [Some Simple Programming in Joy](../works/some-simple-programming-in-joy.md) — the utility-operators section, where reversal is first written with an accumulating parameter and then obtained by executing the sequence against an empty working list, followed by the polymorphic version that reverts to the accumulator approach.
