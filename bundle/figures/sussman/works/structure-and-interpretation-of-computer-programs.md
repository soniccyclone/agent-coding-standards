---
type: work
title: "Structure and Interpretation of Computer Programs"
figure: sussman
description: The textbook for MIT's introductory computer science course (6.001), built around the idea that a programming language is best understood by building an evaluator for it and that most of "design" is choosing the right abstraction barriers between layers. It works through procedural and data abstraction, generic operations and message-passing object systems, streams and lazy evaluation, explicit state and its costs, and finally a metacircular Scheme evaluator and a small register-machine compiler. Enormously influential as a way of teaching computing as applied abstraction-building rather than syntax memorization.
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
year: 1985
url: https://web.mit.edu/6.001/6.037/sicp.pdf
survey_pages: 883
survey_text_layer: full
survey_fetch_mb: 7
access: public
host: institutional
tags: [work]
---

# Structure and Interpretation of Computer Programs

**Author(s):** Harold Abelson and Gerald Jay Sussman, with Julie Sussman
**Venue/year:** MIT Press, 1st edition 1985 (2nd edition 1996); MIT released the full text free.
**Source:** https://web.mit.edu/6.001/6.037/sicp.pdf — live PDF hosted on MIT's own web.mit.edu domain under the 6.001/6.037 course materials.

## Lessons
- [Judge a system by its primitives, its means of combination, and its means of abstraction](../lessons/judge-a-system-by-its-three-mechanisms-not-its-features.md)
- [A definition that lets you recognize the answer is not one that produces it](../lessons/a-definition-that-identifies-is-not-a-definition-that-produces.md)
- [Adopt a model you have already decided to outgrow, and say where it will break](../lessons/adopt-a-model-you-have-already-decided-to-outgrow.md)
- [An abstraction boundary is a claim that a whole class of implementations is interchangeable](../lessons/an-abstraction-boundary-is-a-claim-about-an-equivalence-class.md)
- [What you may freely rename is exactly what you do not depend on](../lessons/what-you-may-rename-is-exactly-what-you-do-not-depend-on.md)
- [Scope exists so that strangers can both use the obvious name](../lessons/scope-exists-so-strangers-can-both-use-the-obvious-name.md)
- [Ask whether you could stop and resume from the named state; that is the test for whether the state is complete](../lessons/resumability-is-the-test-for-whether-your-state-is-complete.md)
- [A construct that looks essential may only be compensating for an implementation defect](../lessons/a-feature-that-looks-essential-may-be-compensating-for-a-defect.md)
- [Choose a measure for what it refuses to distinguish, not for its accuracy](../lessons/a-crude-measure-is-useful-because-of-what-it-refuses-to-see.md)
- [Distinguish a cost you incurred by transcribing the definition from a cost the problem actually has](../lessons/distinguish-naive-transcription-from-inherent-difficulty.md)
- [Compare your algorithm's error rate against the machine's, not against zero](../lessons/compare-your-error-rate-against-the-substrate-not-against-zero.md)
- [Repeating a test buys confidence only if you have proved the failures are independent](../lessons/repetition-buys-confidence-only-if-failures-are-independent.md)

- [Being able to compute a thing and being able to express the concept are different powers](../lessons/computing-a-thing-and-expressing-the-concept-are-different-powers.md)
- [When you see the same shape three times, write the template and turn its holes into parameters](../lessons/let-repetition-hand-you-the-abstraction-by-templating-it.md)
- [When an iteration oscillates instead of converging, damp the step rather than abandoning the formulation](../lessons/when-an-iteration-oscillates-damp-it-toward-the-previous-value.md)
- [First-class status is a checklist you can audit, not a compliment](../lessons/first-class-is-a-checklist-not-a-compliment.md)
- [Abstraction has an optimum, not a maximum](../lessons/abstraction-has-an-optimum-not-a-maximum.md)

- [Name the interface you wish you had, build everything on it, and decide the representation last](../lessons/name-the-interface-you-wish-you-had-and-build-on-it-first.md)
- [An interface without its laws is not a specification](../lessons/an-interface-without-its-laws-is-not-a-specification.md)
- [Algebraically equivalent formulas stop being equivalent once the values carry uncertainty](../lessons/rearranging-a-formula-is-not-safe-when-values-carry-uncertainty.md)
- [A means of combination that cannot consume its own output cannot build hierarchy](../lessons/a-combiner-that-cannot-consume-its-own-output-cannot-build-hierarchy.md)
- [An abstraction that changes nothing about execution can still be the whole point](../lessons/an-abstraction-can-change-nothing-about-execution-and-still-be-the-point.md)

- [Two programs can share a deep structure that neither one exhibits](../lessons/the-shared-structure-may-be-real-and-still-absent-from-the-text.md)
- [Modularity comes from agreeing on one interchange representation, not from splitting code into modules](../lessons/modularity-comes-from-agreeing-on-one-interchange-representation.md)

_EXTRACTION IN PROGRESS — 883 pages, hand-read in the main loop. Source text:
`scratchpad/sicp/sicp.txt` (30,343 lines). Body starts at line 784. Chapter
offsets: ch1 784, ch2 4662, ch3 10939, ch4 17804, ch5 23936, index ~29990.

**Read so far: all of chapter 1, plus chapter 2 through the end of 2.2.3 (lines
784-6781)** — data abstraction, what data means, interval arithmetic, closure,
sequences, hierarchical structures and sequences as conventional interfaces. Next
unread line is **6782** (section 2.2.4, the picture language). `extraction: complete` withheld until all five chapters are read._
