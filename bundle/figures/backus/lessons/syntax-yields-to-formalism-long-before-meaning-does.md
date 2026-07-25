---
type: lesson
title: "Formalizing what is well formed is far easier than formalizing what it means, and the attempt is itself a design test"
figure: backus
works: [syntax-and-semantics-of-the-proposed-international-algebraic-language]
axes: [verifiability, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# Formalizing what is well formed is far easier than formalizing what it means, and the attempt is itself a design test

**Lesson:** A paper that set out to give both a complete account of which texts are legal and a complete account of what they do delivered the first and postponed the second, saying so plainly. Both halves had been declared necessary in the same document a page earlier, so this was not a change of ambition. It is an honest report of asymmetric difficulty: the shape of admissible utterances submits to a compact generative description, and their behavior does not submit nearly as easily. Anyone who has a grammar and believes they have specified a language is confusing the tractable half for the whole, and the confusion is easy because the grammar looks complete on its own terms and mechanically settles every question it is capable of asking.

The more useful observation is what the incomplete attempt produced anyway. Working toward a formal account of meaning revealed that the language itself would need changes to make such an account possible — modifications significant enough to require going back to the committees that had approved the design. Formalization is not a transcription step performed after design is finished. It is an instrument that finds places where the design cannot be given a coherent meaning, and it finds them by failing on them. Features that resist precise definition are usually features that are also ambiguous to users and awkward to implement, and the resistance is the signal.

Two habits follow. Distinguish, in any specification effort, between having pinned down the form and having pinned down the behavior, and never let progress on the first stand in for the second. And treat the attempt at formal semantics as a design review with teeth: begin it while the design can still be changed, expect it to demand changes, and read every construct that will not sit still under formalization as a candidate for revision rather than as a hard problem in specification technique.

**Source:** [The Syntax and Semantics of the Proposed International Algebraic Language](../works/syntax-and-semantics-of-the-proposed-international-algebraic-language.md) — the general part of the formal description, which states both precision requirements, then reports that only the account of legal programs was finished, that the semantic treatment is deferred, and that the work already done on it indicated the language would need modification.
