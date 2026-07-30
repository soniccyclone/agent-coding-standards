---
type: lesson
title: "Read your own programs for bookkeeping: text that is not about the problem is an indictment of the language"
figure: ingalls
works: [design-principles-behind-smalltalk]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Read your own programs for bookkeeping: text that is not about the problem is an indictment of the language

**Lesson:** There is a cheap and surprisingly sharp test for whether a language fits the problems people write in it: look at typical programs and ask whether they visibly appear to be doing what they are in fact doing. If the statements on the page are mostly about the subject matter, the model underneath is aligned with the model in the author's head. If they are interleaved with instructions about the machinery — allocating, releasing, declaring who owns what, announcing when something is finished with — then the author is being made to think two things at once, and only one of them is the problem. The test works because it does not require you to know what a good language looks like in the abstract; it only requires you to notice the ratio of subject to overhead in text you already have.

The particular case that makes the criterion vivid is manual storage management, and the reason it fails the test is worth stating in general form: human communication carries no such obligations. Nobody prepares a listener before mentioning a thing, or notifies them afterward that it may now be forgotten. When a computational model demands that kind of accompanying ritual, the mismatch is not a quirk of programming, it is evidence that the model was chosen for the convenience of the implementation rather than of the person. The fix is to move the obligation into the system — automatic reclamation, in that case — so the ritual disappears from every program at once rather than being written correctly a million times.

Applied as a habit, this reframes a large class of complaints. Boilerplate is not a stylistic annoyance to be suppressed with better editors or code generation; it is a measurement, and what it measures is the distance between the language's model and the problem's. The productive response to noticing recurring bookkeeping is to identify the obligation it discharges and ask which layer should be discharging it instead, because any obligation that appears in every program is one the system could have taken on itself.

**Source:** [Design Principles Behind Smalltalk](../works/design-principles-behind-smalltalk.md) — the Storage Management principle, its stated test of whether programs look like they are doing what they are doing, and the analogy to the absence of any such preparation-and-release ritual in ordinary human conversation.
