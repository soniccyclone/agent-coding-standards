---
type: lesson
title: "Audit the machine model a language commits you to before comparing its features"
figure: backus
works: [can-programming-be-liberated-from-the-von-neumann-style, the-history-of-fortran-i-ii-and-iii]
axes: [hardware-affinity, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Audit the machine model a language commits you to before comparing its features

**Lesson:** Every notation for computing carries an implicit answer to three questions: what counts as state, how state changes, and how big the smallest change is. Those answers are usually not chosen; they are inherited from whatever machine the notation grew up next to. When storage cells become variables, fetch-store-arithmetic becomes assignment, and branch-and-test becomes control structure, the language is a dialect of the machine rather than of the problem. Two such languages can differ enormously in surface vocabulary while agreeing on all three answers, which makes a feature-by-feature comparison between them a comparison of accents.

This matters because the model, not the feature list, sets the ceiling. If the unit of change is one word moving between a processor and a store, then any substantial change to a data structure has to be re-expressed as a schedule of small changes, and the programmer's attention is consumed by designing the schedule rather than stating the change. The consequences are structural and they compound: since every detail of execution touches state, every construct's meaning has to be spelled out as an effect on state, which is why languages built this way grow bulky faster than they grow strong. Familiarity hides all of this. The model feels like the nature of computing rather than one choice about it, so alternatives read as eccentric rather than as competitors.

A programmer who takes this seriously evaluates a language by interrogating its model first. What is the state? How tightly is each construct coupled to it — does every step touch it, or only a few? What is the smallest thing that can be changed in one act, and what is the largest? Is the same kind of reasoning valid throughout the language, or does it split into a region where algebra works and a region where it does not? The answers predict what will be awkward before any code is written, and they explain why decades of effort spent enriching a model can produce very little additional power.

**Source:** [Can Programming Be Liberated from the von Neumann Style?](../works/can-programming-be-liberated-from-the-von-neumann-style.md) — the opening survey classifying computing models by their foundations, storage, and semantics, and the following sections deriving the shape of conventional languages from the structure of the machine underneath them. Also [The History of FORTRAN I, II, and III](../works/the-history-of-fortran-i-ii-and-iii.md) — the closing retrospective, where the author reclassifies his own language and its descendants as elaborations of one machine's programming style.
