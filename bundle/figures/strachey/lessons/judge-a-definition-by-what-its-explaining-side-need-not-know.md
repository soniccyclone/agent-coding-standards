---
type: lesson
title: "Judge a definition by what its explaining side need not know"
figure: strachey
works: [toward-a-mathematical-semantics-for-computer-languages]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Judge a definition by what its explaining side need not know

Write down what a numeral means by recursion on how numerals are built and the result looks embarrassing: each clause seems to say that a numeral means the number it obviously means. Scott and Strachey anticipate the objection and answer it with a test that is worth stealing, because it applies to every definition anyone writes. Take an inventory of the vocabulary the explaining side actually draws on. Here it needs the idea of a quantity, the two smallest ones, and two ways of combining quantities — and nothing else. It never needs to have heard of writing a quantity as a string of digits, nor of the trick where position within the string carries weight. That trick is precisely what was being explained, and it is absent from the explanation. So the definition has content after all, and the content is exactly the reduction of a notational device to concepts that are indifferent to it.

The general test, then, is not whether the same words appear on both sides — they often must — but whether the explaining side presupposes the mechanism you claim to be explaining. If it does, you have relabelled rather than defined, and no amount of formality will rescue it. If it does not, the definition is doing work, and the inventory tells you both what the work was and what it cost: these are the notions I had to assume in order to account for that one. Enumerating the assumed notions is itself a result, since a reduction to fewer or more elementary ideas is a better reduction, and you cannot compare two accounts on that basis unless each has stated its assumptions.

A second thing falls out of the same inventory, and it is the more interesting one. The trick being explained does not belong to the subject matter at all. Nothing about quantity implies place-value notation; someone had to invent that, and it was an invention in language, not a discovery about numbers. Separating the two matters because systems are full of features whose air of necessity comes from the notation rather than the problem — and the way to spot them is that they vanish from the explaining vocabulary while the problem's real notions remain. Programming languages, on this reading, are largely collections of such inventions, and knowing which of your concepts are artifacts of how you write things down is what lets you tell an essential constraint from an inherited convention.

The habit to build is to stop asking "is this definition circular?" and start asking "what does the right-hand side need to know?" A reference implementation expressed in terms of the abstractions it purports to define explains nothing to anyone. One expressed in terms of strictly more elementary operations explains something specific, and the list of those operations is the honest statement of what the explanation assumes.

**Source:** [Toward a Mathematical Semantics for Computer Languages](../works/toward-a-mathematical-semantics-for-computer-languages.md) — the introduction's defence of the recursive evaluation equations for binary numerals against the charge of circularity or vacuity, resting on the observation that the metalanguage needs arithmetic notions but need never have encountered positional notation, which is characterised there as a discovery in language rather than a fact about number.
