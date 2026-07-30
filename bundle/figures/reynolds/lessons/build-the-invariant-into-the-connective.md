---
type: lesson
title: "If your specifications grow quadratically as you mention more things, the fix is a new connective, not more clauses"
figure: reynolds
works: [separation-logic-a-logic-for-shared-mutable-data-structures]
axes: [cognitive-load, verifiability, expressiveness]
subdomains: [formal-methods-and-verification, programming-languages-and-semantics]
tags: [lesson]
---
# If your specifications grow quadratically as you mention more things, the fix is a new connective, not more clauses

**Lesson:** Watch what happens to a description when you add one more object to it. Stating that a program in-place reverses a linked structure is short, until you notice the program misbehaves if the two structures overlap, so you add a clause saying nothing is jointly reachable from both. Then a third structure appears that the program must leave alone, and you add clauses pairing it against each of the first two. Nothing in this is subtle or wrong; the description is simply growing as the square of the number of things mentioned, and every clause restates the same idea. That growth curve is the diagnostic. When the bookkeeping in a specification scales with the number of participants rather than with the difficulty of the program, the notation is at fault, not the programmer.

The remedy is to move the repeated content out of the clauses and into the meaning of a combining operator. Instead of joining two descriptions with ordinary conjunction and then separately forbidding them to overlap, introduce a way of joining them that asserts they describe disjoint portions of the resource in the first place. The prohibition is then discharged by the act of composition, and the quadratic pile of pairwise clauses vanishes: describing three independent structures costs three descriptions and two uses of the operator. The pattern generalizes past storage — anything that behaves like a divisible resource admits the same treatment — and so does the diagnostic step that finds it: identify the property you keep restating between every pair of things you mention, then look for the composition operator that has that property built in.

Two consequences are worth anticipating. First, an operator like this cannot be a definitional convenience layered over what you had; joining descriptions of disjoint resources is not expressible by the ordinary connectives, and the logic that results genuinely lacks structural rules you are used to — a description no longer implies two copies of itself, and joining a fact onto a description no longer lets you drop it again. Expect familiar reasoning steps to stop working, and treat that as the price of the scaling you bought. Second, the payoff extends past brevity into what becomes provable at all: once separateness is carried by the notation, the fact that a program leaves some structure alone can be *derived* from the observation that its specification never mentions that structure, rather than proved case by case.

**Source:** [Separation Logic: A Logic for Shared Mutable Data Structures](../works/separation-logic-a-logic-for-shared-mutable-data-structures.md) — the introduction's worked degradation of the list-reversal invariant as non-sharing constraints are added for a second and then a third structure, the replacement of those constraints by separating conjunction, and section 3's observation that contraction and weakening are unsound in the resulting substructural logic.
