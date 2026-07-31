---
type: lesson
title: "Adopt a model you have already decided to outgrow, and say where it will break"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# Adopt a model you have already decided to outgrow, and say where it will break

**Lesson:** Introducing a rule for how procedure application works, the authors do something unusual with it immediately: they say it is not what the implementation does, that it exists to help the reader think, and that a later chapter will break it deliberately by introducing mutable state, at which point a more complicated model replaces it. The simplification is not a regrettable compromise disclosed in a footnote — it is announced with its own expiry conditions attached.

The practice worth extracting has three parts, and the third is the one usually skipped. Commit to a model simple enough to reason with. State plainly that it is a model rather than a description of the machinery. And name the specific circumstance under which it stops being true. That last part converts a teaching lie into an engineering instrument, because a reader who knows the boundary can use the model confidently inside it and knows to distrust it at the edge — where without the warning they would carry a false intuition into exactly the situation that punishes it.

The general pattern is a sequence of increasingly elaborate models rather than a single accurate one, which mirrors how modelling works in every technical field: begin with something incomplete, discover where it fails, replace it. Stating this up front changes the reader's stance from believing the model to using it, and those are different mental postures with different failure modes.

For anyone documenting a system, this is the useful discipline. Simplified mental models get written all the time — the retry story, the caching story, the consistency story — and they are almost always presented as simply true, so the first engineer to hit the boundary experiences it as the documentation lying. Naming the boundary costs one sentence and converts that experience into a recognized transition. The test of whether you understand your own abstraction is whether you can say precisely what would have to happen for your simplified account to stop holding.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) — chapter 1 section 1.1.5's presentation of the substitution model, which stresses that its purpose is to help us think about procedure application rather than to describe how the interpreter really works, that typical interpreters use local environments instead, and that the book will present a sequence of increasingly elaborate models culminating in a full implementation — with the explicit warning that the substitution model breaks down once procedures with mutable data are introduced.
