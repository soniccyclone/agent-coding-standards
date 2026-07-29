---
type: lesson
title: "Count the primitives you never wrote down, or your minimality is bookkeeping"
figure: curry
works: [grundlagen-der-kombinatorischen-logik]
axes: [primitive-count, cognitive-load, verifiability]
subdomains: [foundations-of-computation, programming-languages-and-semantics]
tags: [lesson]
---
# Count the primitives you never wrote down, or your minimality is bookkeeping

**Lesson:** Any formal apparatus rests on a layer of machinery its author never states: which sorts of thing exist, which ways of putting two things together are legitimate, when two different ways of putting things together land in the same place, and what sort of thing comes out. Curry names this presupposed layer and treats it as an object of study rather than as background, and the immediate consequence is deflationary. If that layer already carries an unbounded stock of notions and rules, then eliminating two or three of the notions you happened to list buys nothing. You have not reduced the system; you have reduced the part of the system you were willing to write down. Worse, some celebrated reductions are paid for out of generality, completeness, or plain correctness — a definition clever enough to remove a listed primitive can quietly leave the theory unable to distinguish two claims it ought to distinguish.

The reason this holds is that a count is only meaningful relative to a boundary, and the boundary is a choice. Whatever sits below it is not free; it is unaudited. It gets exercised on every use, and it is exactly the region where mistakes are invisible because nothing there was ever stated precisely enough to contradict. So the honest form of "simplify the foundations" is not "shorten the axiom list" but "push the boundary down until the substrate itself is small and stated" — and then a genuine claim becomes available: the whole apparatus has finitely many parts, and its rules are no more intricate than the one inference step everyone already accepts.

A programmer who believes this stops treating primitive count as a scoreboard for the visible layer. Given a language with seven keywords sitting on a runtime with an unstated object model, unstated coercion rules, and unstated equality, they see a large system, not a small one. Given two designs where one has more named operations but a substrate you can write down completely, they prefer it. And when asked to shrink an interface, their first move is to ask what the interface is currently assuming about its callers and its host, because that is where the real inventory is, and it is the part that never appears in the comparison table.

**Source:** [Grundlagen der kombinatorischen Logik](../works/grundlagen-der-kombinatorischen-logik.md) — Chapter I's opening discussion, where the presupposed categories, combining operations and their properties are named as a body of prior doctrine, and the first of the two problems posed there is argued to be unreachable unless that substrate is simplified first.
