---
type: lesson
title: "Keep facts about your mechanism separate from facts about your subject matter, and give them exactly one joint"
figure: reynolds
works: [the-craft-of-programming]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Keep facts about your mechanism separate from facts about your subject matter, and give them exactly one joint

**Lesson:** Any argument that a program does what you want mixes two utterly different species of knowledge. One species concerns the machinery: what sequencing does, what assignment does, what a loop guarantees. These facts hold no matter what the program computes, and they are the same for a payroll system as for a graph algorithm. The other species concerns the subject matter: that a remainder shrinks when you subtract the divisor, that a particular recurrence holds, that these two accounts always sum to a constant. These facts are indifferent to whether anyone ever writes a program. The reason to notice the split is that the rules governing the first species can be applied blindly, whereas the second species is where all the real thinking lives, and mixing them means you cannot tell which of the two you are currently doing.

The structural move is to allow the two to meet at one designated place and nowhere else. In the rules for reasoning about statements, that place is the pair of steps that let you replace a requirement by a stronger one or a guarantee by a weaker one. Those two rules look so obvious as to be not worth stating — of course you may demand more than you need, of course you may promise less than you achieved — but they are the entire channel through which knowledge about integers, sets, graphs or money enters an argument otherwise composed of language mechanics. Everything else in the proof is bookkeeping. When a step fails, you immediately know its character: either you got the machinery wrong, or the domain fact you needed is not true.

Carry the discipline into ordinary construction and it shows up as a rule about where cleverness is allowed to live. A layer that manipulates data should know the mechanics of manipulation and nothing about what the data means; the meaning enters through one explicit narrowing or widening at the boundary — a validation, a conversion, a stated assumption — rather than being smuggled in as an unremarked assumption at fifty scattered points. The payoff is diagnostic rather than aesthetic. Code whose domain assumptions are all concentrated at named joints can be checked against a changed domain by inspecting those joints; code that has interleaved them with its mechanics has to be re-derived from scratch every time the world changes.

**Source:** [The Craft of Programming](../works/the-craft-of-programming.md) — Section 1.4.2's remark that the rules for strengthening precedents and weakening consequents seem too obvious to mention yet are the essential mechanism by which static mathematical facts enter a correctness proof, illustrated by contrasting a specification that depends only on assignment and sequencing with implications that depend only on properties of the integers.
