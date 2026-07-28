---
type: lesson
title: "A specification small enough to be read whole beats a reference large enough to be looked things up in — provided you name what you left out"
figure: mccarthy
works: [a-micro-manual-for-lisp]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# A specification small enough to be read whole beats a reference large enough to be looked things up in — provided you name what you left out

**Lesson:** There are two ways to document a language and they are not the same artifact serving different audiences. A reference manual is something you consult: it is indexed, it is comprehensive, and nobody ever holds all of it at once, so nobody ever notices when two of its corners disagree. A core specification is something you read from beginning to end in one sitting: it is short by construction, and its shortness is what makes it *checkable* — a reader who has the whole thing in working memory can spot an inconsistency, and can verify for themselves that the derived vocabulary really does follow from the base rules rather than taking it on trust. The micro-manual is an argument that the second artifact is worth producing separately, not as an abridgement of the first but as its own thing with its own job.

Getting there requires a discipline the title makes explicit: you must partition the language into the part that is definitional and the part that is convenience, and you must say out loud which omissions you made. The evaluation rules come first as the actual semantics; the abbreviations follow, each one presented as an expansion into those rules rather than as new capability; and the things genuinely absent — functional arguments, property lists, I/O, sequential control — are enumerated rather than quietly skipped. That last move is what keeps the compression honest. A short document that pretends to completeness is a lie; a short document that states its boundary is a load-bearing specification, because a reader knows precisely where its guarantees stop.

The self-application requirement is what makes the partition rigorous rather than editorial. Writing the evaluator in the very subset being specified forces every convenience out of the core: the auxiliary routines get folded inline, awkwardly and admittedly at a cost to readability, because using the cleaner factoring would have pulled in machinery the core does not contain. That constraint acts as an automatic auditor. Anything the evaluator needs is genuinely primitive; anything it can be written without is genuinely sugar, and no amount of arguing about it changes the answer.

A programmer who works this way ships two documents for any nontrivial system: the small one that defines what the thing *is*, and the large one that describes everything it currently does. They resist the pressure to merge them, because the merge destroys the property that made the small one valuable. And when they cannot make the small one small, they read that as a finding about the system rather than about their writing.

**Source:** [A Micro-Manual for Lisp — Not the Whole Truth](../works/a-micro-manual-for-lisp.md) — the structure of the piece itself: a short numbered set of evaluation rules, a separately labelled abbreviations section presented as expansions, an explicit list of what the core does not cover, and the closing self-applicable evaluator whose inline-auxiliary awkwardness is acknowledged as the price of staying inside the core.
