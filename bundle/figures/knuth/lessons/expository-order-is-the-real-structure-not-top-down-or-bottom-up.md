---
type: lesson
title: "The order a program should be presented in is a discoverable property of the problem, not a choice between top-down and bottom-up"
figure: knuth
works: [literate-programming]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# The order a program should be presented in is a discoverable property of the problem, not a choice between top-down and bottom-up

**Lesson:** Knuth set out to build a system for stepwise refinement and reports arriving somewhere else. He had assumed the two available methodologies were rivals — descend from a top-level statement, or accumulate capability from the bottom — and that one was suited to explaining programs while the other was suited to producing them. Working with fragments he could name and place anywhere dissolved the question. Hierarchy is present in a program, but it is not the whole of the structure; the structure is a set of small parts plus the relations between neighbouring parts, and no single traversal of that graph is privileged. Both methodologies had been arguments about which traversal to force, and the argument only looked important because the compiler's required sequence was the only sequence available.

The evidence he offers for the ordering being real rather than a matter of taste is worth more than the theory. When he discards a first attempt and starts a program over, the second attempt reaches for the same things in nearly the same sequence. That is the signature of something being found rather than invented. He also reports the strong pull, mid-construction, toward settling a major data structure before he can bear to continue — an ordering constraint coming from the material, not from a methodology. And he claims the reader's needs coincide: someone encountering a program for the first time is served best by roughly the sequence in which it was built, because that sequence is the one in which each part's motivation is already available when the part arrives.

His diagnosis of what each pure discipline costs is precise, and both costs are costs in working memory. Descending from the top gives you direction but obliges you to hold a growing stack of unfulfilled intentions, with nothing concluded until the end. Building upward gives you a steadily more capable vocabulary but defers the shape of the whole until so late that you can wander. The mixed order is not a compromise between them; it is what you get when the sequence is chosen against the reader's capacity instead of against a rule.

The habit this recommends is to treat presentation sequence as a design decision with a defensible answer, and to notice which orderings your tools force on you. Declaration-before-use, file layout, initialization order, import structure: each of these imposes a reading sequence that was chosen by a compiler writer for reasons having nothing to do with comprehension. You will not always be able to override them, but knowing which parts of your code's arrangement are load-bearing and which are compiler tribute is the difference between organizing a program and inheriting its organization.

**Source:** [Literate Programming](../works/literate-programming.md) — the section arguing that a program is better regarded as a web than a tree, including the observation about redrafting reproducing the original ordering and the paired critique of what top-down and bottom-up each demand of the programmer.
