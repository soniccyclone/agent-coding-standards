---
type: lesson
title: "Choose a measure for what it refuses to distinguish, not for its accuracy"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Choose a measure for what it refuses to distinguish, not for its accuracy

**Lesson:** A measure of resource growth that treats a cost of n², a cost of a thousand times n², and a cost of 3n² plus 10n plus 17 as the same thing looks like a measure that has thrown away most of what you wanted to know. It has, deliberately. What survives is the answer to one question — how does the requirement change when the problem gets bigger — and the constants are discarded precisely because they do not affect that answer while varying with machine, implementation and mood.

The habit worth taking is to choose a measure by what it is designed to be blind to. Every measure is an equivalence relation on situations, declaring some differences irrelevant; its value comes from that declaration matching the decision you are making. Doubling the input size doubles a linear cost and squares nothing about it — that is a statement you can act on when choosing between designs, and it is true regardless of the constants you do not know. Ask instead what a program costs in absolute terms and you get a number that is precise, real, and worthless the moment anything about the deployment changes.

The corresponding discipline is to notice when the blindness stops being appropriate. Growth order says nothing about which of two same-order implementations to ship, and at fixed realistic input sizes the constants it discards can dominate entirely. Using it to make that decision is not a miscalculation but a misapplication — the measure answered the question it was built for and was asked a different one.

The authors are candid that even their own analysis rests on simplifications that can fail: counting operations assumes an operation's cost is independent of the size of the values involved, which stops being true for large enough numbers. So the analysis of a process, like its design, happens at a chosen level of abstraction, and the level is a decision with consequences rather than a neutral backdrop. State which one you are working at, because a claim about resources is only meaningful relative to it.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.2.3 on orders of growth, which defines the notation, notes that processes requiring n², 1000n² and 3n²+10n+17 steps all share the same order, argues that this crude description nonetheless usefully indicates how behaviour changes as problem size changes, and carries the footnote conceding that these statements mask oversimplification — counting machine operations assumes multiplication cost is independent of operand size, which is false for sufficiently large numbers, so the analysis of a process can be carried out at various levels of abstraction.
