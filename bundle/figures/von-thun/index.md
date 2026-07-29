---
type: figure
title: Manfred von Thun
description: La Trobe University, Melbourne. Created Joy - deliberately built on combinatory logic, explicitly citing Curry. The direct descendant Forth never claimed to be.
status: accepted
layer: design-thought
subdomains: [programming-languages-and-semantics]
tags: [figure, accepted]
---

# Manfred von Thun

**Dates:** Philosopher and computer scientist, La Trobe University, Melbourne, Australia. Began exploring function-composition alternatives to lambda calculus in the early 1980s; first Joy papers ~1994, C implementation 1995, public debut at EuroForth 2001. Birth/death dates not confirmed in this research pass — flagging rather than guessing.

## Why a candidate
Explicitly designed Joy as a programming language grounded in combinatory logic, deliberately citing Curry — the direct, deliberate descendant of Schönfinkel/Curry's combinator lineage (see [schonfinkel](../schonfinkel/index.md), [curry](../curry/index.md)) that Chuck Moore's Forth (see [chuck-moore](../chuck-moore/index.md)) never claimed to be. Where Forth is convergent invention, Joy is conscious formal derivation — a useful contrast pair for the primitive-count axis.

## Top 10 most influential works
Nearly entire bibliography self-archived and mirrored — one of the most accessible candidates in the set, alongside Lamport and McCarthy:
1. "Joy: Forth's Functional Cousin" — `public` (mirrored at kevinalbrecht.com/code/joy-mirror/forth-joy.html)
2. "Mathematical foundations of Joy" — `public` (kevinalbrecht.com/code/joy-mirror)
3. "An informal tutorial on Joy" (2001 EuroForth tutorial, Joy's public debut) — `public` (kevinalbrecht.com/code/joy-mirror/j01tut.html)
4. "Some Simple Programming in Joy" — `public` (kevinalbrecht.com/code/joy-mirror/j06prg.html)
5. "The prototype implementation of Joy" — `public` (kevinalbrecht.com/code/joy-mirror/j09imp.html)
6. "A Joy interpreter written in Joy" — `public` (kevinalbrecht.com/code/joy-mirror/jp-joyjoy.html)
7. "Recursion Theory and Joy" — `public` (kevinalbrecht.com/code/joy-mirror)

Original site is offline; all of the above survive via Kevin Albrecht's mirror — worth a Wayback Machine cross-check in Phase 3 per the standing rule, in case the mirror itself ever goes down too.

## Lessons

Von Thun's body of work is a sustained argument that the notation you compute in determines which thoughts are cheap, and that most of what we experience as intrinsic difficulty is the cost of an inherited representation. Joy exists to make one identity hold literally — program text concatenated is function composition, so the algebra of the notation is the algebra of its meaning — and von Thun then spends seven papers cashing that in. Because there are no formal parameters, there is no substitution, which removes scoping machinery, removes evaluation-order pathologies at their root rather than trading one strategy for another, and turns program construction into derivation: state the law a combinator must satisfy, rewrite until only primitives remain, and the result is correct because every line equalled its neighbour. Because programs are ordinary data, the classical results of computability theory that normally require arithmetic encodings of syntax reduce to a few lines of algebra, and self-reference becomes constructive — including a self-interpreting kernel that turns "how small should the core be" from a matter of taste into a fixed point you can run. Recursion is abstracted by its shape rather than its values, so a family of combinators replaces named recursive definitions; variation nobody can enumerate in advance is accepted as an editable program fragment rather than a hook; and a well-fitted control abstraction is one where informal pseudocode transcribes into it slot for slot with the plumbing having no representation at all. The counterweight, and the reason he is more than a formalist, is that he repeatedly declines his own machinery: duplication left unfactored because the reader would suffer, an efficient trick abandoned because it cannot be made polymorphic, a delegating fall-through built into an incomplete model so it stays useful and made loud so the gap reports itself. The through-line for a programmer is a habit of suspicion toward ceremony — count the invisible machines your semantics needs, measure a mechanism by what it costs to invoke rather than whether it is definable, enumerate every way your system can be wrong as a readout of how many independent mechanisms it really has, and treat a name, once nothing forces you to introduce one, as a message to a human rather than structural residue.
