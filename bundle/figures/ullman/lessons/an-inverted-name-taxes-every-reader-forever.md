---
type: lesson
title: "An inverted name taxes every reader forever"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# An inverted name taxes every reader forever

**Lesson:** A name whose polarity runs opposite to its value is a small, permanent tax on everyone downstream. Call something a suppression control and then let its high value mean "keep," and every person who reads the code has to perform a mental negation at every site, every time, forever. The error rate of that negation is not zero, and it is highest exactly where you would want it lowest: in unfamiliar code, under time pressure, during an incident. Nothing about this is subtle or arguable, which is what makes it worth being strict about — it is one of the very few naming questions with an objectively correct answer, namely that the name should be true when the value is true.

The reason these names survive is more interesting than the mistake itself. A misnomer that enters a field early gets embedded in papers, tutorials, library APIs and interview questions, and by the time anyone notices, the cost of fixing it exceeds the cost of tolerating it: a corrected name is now inconsistent with everything a newcomer will read elsewhere, so a local fix imports a translation problem to replace an inversion problem. That is a real argument, and it usually wins, and the outcome is that a whole field pays a small tax indefinitely because of a word chosen casually by somebody who did not expect to be defining vocabulary.

Which yields the actual prescriptions, and they are asymmetric in time. When you are the one introducing a term, spend the extra minute — you are choosing on behalf of everyone who will ever read the thing, and your leverage is at its maximum before anyone has adopted it. When you inherit an inverted term, the right move is usually not to rename it in defiance of the field, but to state the inversion explicitly and prominently at every place someone will meet it, so that a reader's correction is prompted rather than remembered.

The general principle underneath is that vocabulary is interface, and interfaces are the expensive thing to change. The internal representation behind a badly named quantity can be replaced in an afternoon. The name cannot, because it has escaped into other people's heads and other people's code. That asymmetry is a reason to treat naming as a design decision with the same weight as a data structure choice rather than as the cosmetic step at the end.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the footnotes in the long-short-term-memory section of the recurrent-networks chapter, which point out that a one in the so-called forget gate causes the corresponding memory entry to be retained so it should really be a remember gate, that the input gate would be better named the save gate, and that the output gate would be better named the focus gate — while stating that the text nevertheless follows the naming convention established in the literature.
