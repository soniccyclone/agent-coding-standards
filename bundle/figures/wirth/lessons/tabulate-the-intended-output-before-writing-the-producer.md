---
type: lesson
title: "Tabulate the intended output before writing the thing that produces it"
figure: wirth
works: [project-oberon]
axes: [verifiability, cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Tabulate the intended output before writing the thing that produces it

**Lesson:** For any component whose job is to turn one form into another, there are two things to work out: what the result should be, and how to get there. They are almost always tackled together, with the target form emerging as a by-product of writing the machinery, and this is the wrong order. Deciding what the output should look like is a design activity with its own criteria — economy, regularity, exploiting what the destination does well — and doing it inside the loop of writing a producer means those criteria are being applied incidentally, case by case, under the pressure of whatever the code needs next.

Settling the destination first turns the producer into a much smaller problem. Take each kind of input construct in turn and write down, concretely, the result it should yield, with a worked instance rather than a description. The collection of these is the specification, and it has several properties a prose description does not. It is complete in a checkable way — you can see whether every construct has an entry. It is directly comparable against reality, since you can run the thing and compare. It makes the quality of the output visible while it is still cheap to change, which is when you notice that some construct's result is clumsy and that a different choice would serve every use of it. And it makes the producer's own structure obvious, because once each construct's output is fixed, the code that emits it has almost nothing left to decide.

This is only possible when the correspondence is local — when each construct's output depends on that construct and the attributes of its immediate parts, not on the surrounding context. That property is worth checking early, and worth preserving, precisely because it is what makes the table-of-patterns approach available at all. Where it holds, the specification can be written construct by construct in any order and reviewed by someone who never reads the implementation. Where it fails, you have not merely lost a convenience; you have a component whose behaviour cannot be described in pieces, and the exceptions should be identified and confined so that the tabulated part stays tabulated.

**Source:** [Project Oberon](../works/project-oberon.md) — the opening of section 12.2, which states that before it is possible to understand how code is generated one needs to know which code is generated, that the goal must be known before the way leading to it can be found, and that a concise description of the goal is possible because of the structure of the language: since semantics are attached to each individual syntactic construct independent of context, it suffices to list the expected code for each construct instead of an abstract semantic rule; followed by the section's presentation of that listing as small worked programs shown beside the instructions they produce.
