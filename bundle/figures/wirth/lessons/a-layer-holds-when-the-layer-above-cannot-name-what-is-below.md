---
type: lesson
title: "A layer holds when the layer above never names the vocabulary below"
figure: wirth
works: [project-oberon]
axes: [cognitive-load, primitive-count, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A layer holds when the layer above never names the vocabulary below

**Lesson:** Everyone claims their design is layered, and the claim is nearly unfalsifiable as usually stated, since any pile of modules can be drawn with some of them above others. There is a sharp test available, and it is about vocabulary rather than about structure. List the terms in which the lower layer's job is stated — the units it manipulates, the concepts it exists to hide. Then read the layer above and see whether any of those terms appear. If the upper layer speaks only of the things the lower one produces, and never of the material the lower one produces them from, the abstraction is real. If those terms leak upward, even occasionally, there is no boundary there, only an arrangement of files.

Stated this way the test can actually be applied, and it is worth applying to each candidate boundary separately rather than to the design as a whole. The most valuable abstractions are usually the ones where the two vocabularies are genuinely different in kind — where the lower layer's units are small and numerous and the upper layer's are structured and few — because that is where the reduction in what must be held in mind is largest. It is also where leaks are most tempting: some case is awkward to express in the upper vocabulary, and reaching one level down solves it immediately, at the cost of the property that made the layer worth having. The right response to such a case is to extend the upper vocabulary, not to peek beneath it.

The same criterion applies to representations, where it is easier to enforce and just as often neglected. If exactly one component knows how a stored or transmitted form is laid out, and every other component obtains what it needs by asking that one, then the layout is genuinely changeable — the claim can be tested by searching for anyone else who assumes anything about the arrangement. If two components know, the format is frozen no matter what the documentation says, because changing it now requires a coordinated edit that nobody will risk. Sole knowledge of a representation is therefore a property to be checked deliberately and defended, and the check is mechanical: who else would have to change if this layout changed. If the answer is "only that module", you have a layer. If it is a list, you have a convention.

**Source:** [Project Oberon](../works/project-oberon.md) — section 12.1's account of the scanner, which reads as many characters as needed to recognise the next symbol and is described as implementing the abstraction of symbols, with the note that the scanner alone reflects the definition of symbols in terms of characters while the parser is based on the notion of symbols only; together with the same section's statement about symbol files, which are written and read by the table-handling module and of whose structure no other module relies on any information.
