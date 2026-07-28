---
type: lesson
title: "Publish a ladder of models at increasing fidelity, and state which one is allowed to answer which question"
figure: mccarthy
works: [lisp-1.5-programmers-manual]
axes: [verifiability, cognitive-load]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Publish a ladder of models at increasing fidelity, and state which one is allowed to answer which question

**Lesson:** Documentation usually pretends to be a single description of a single thing, and that pretence is where it starts lying. The manual for LISP 1.5 refuses the pretence. It describes the evaluator three times over. The opening section gives a compact recursive definition you can read in a few minutes and trace by hand. An appendix gives a longer version written in a mixture of the same formal notation and plain prose. The machine holds the third version, in assembly, and nobody claims the prose is it. What makes this a design decision rather than sloppiness is that each description carries an explicit statement of its own standing: the short one is named a teaching device and disclaimed as not being the function actually running; the appendix is nominated as the thing to consult when you need to settle how the system really behaves; and even the appendix warns that its notation should not be read too literally, because where it shows a recursion the real code often does a store and a jump.

The value of the arrangement is that it separates two questions that get conflated and that want different answers. "What does this construct mean?" is best answered by the smallest model that gets the meaning right, because a model you can hold entirely in your head is a model whose consequences you can actually derive. "Why did my program do that?" is a question about the artifact, and only a description faithful to the artifact can answer it. A single document tuned for one of these is wrong for the other. Tuned for both, it becomes long enough that nobody reads it whole and precise enough that nobody trusts it, which is the worst of the available outcomes. Two documents, each labelled with its jurisdiction, dominate one document trying to serve both.

The discipline that keeps a ladder honest is direction of deference. Every rung must name the rung below it as the authority for anything it simplifies away. Once that is written down, a discrepancy between the teaching model and the implementation is no longer a contradiction the reader must adjudicate — it is a known, bounded simplification, and the reader knows where to go. Without the statement, the same discrepancy is a trap: the reader reasons confidently from the clean model and gets a result the machine disagrees with, and there is nothing in the text to tell them which side was wrong.

A programmer who works this way stops treating "the docs are out of sync with the code" as a documentation failure to be fixed by rewriting, and starts treating it as a missing declaration of jurisdiction. They ship a small conceptual model for reasoning, keep a faithful description for debugging, and label both. They resist the urge to make the small model more accurate, because accuracy is not its job and every increment of it costs the property that made the small model useful. And they consider it a serious defect when a system has only the faithful description, because then every question, however conceptual, has to be answered by reading the implementation.

**Source:** [LISP 1.5 Programmer's Manual](../works/lisp-1.5-programmers-manual.md) — the closing remarks of the first section, which label the compact evaluator definition a pedagogical device, deny that it is the function in the running system, and direct the reader to the interpreter appendix for questions about actual behaviour; and that appendix's own opening caveat that its notation approximates a machine program whose control structure differs.
