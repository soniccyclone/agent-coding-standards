---
type: lesson
title: "Define a measure as the cheapest route, and its axioms come free"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness, primitive-count]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# Define a measure as the cheapest route, and its axioms come free

**Lesson:** Most of the axioms people want from a notion of closeness are cheap to obtain, and one of them is not. Non-negativity, zero exactly at identity, and symmetry can usually be arranged by inspection. The triangle inequality is the one that takes work, and the work is unnecessary if the measure was constructed in the right shape to begin with. Define the quantity as the minimum cost over all sequences of primitive moves that carry one object to the other, and the inequality is immediate: going by way of a third object is a particular sequence of moves, so its cost cannot be less than the cheapest sequence. There is nothing to prove beyond the observation that concatenating two routes yields a route.

Reading the axiom this way also tells you what it means rather than what it says. It is the statement that being forced to pass through a specified intermediate can never help you, which is exactly what makes a measure behave like a shortest path and exactly what every algorithm that prunes with the inequality is relying on. Once that is visible, the same one-line argument covers cases that look unrelated: counting the insertions and deletions that convert one string to another, measuring the rotation that carries one direction onto another, or any measure whose primitive moves compose. Whenever the moves compose and their costs add, you have the axiom, and when they do not compose, no amount of algebra will supply it.

The design consequence is that the definition is the place to spend your effort. Faced with a new kind of object and a need to say how far apart two of them are, the productive question is what the primitive edits are and what each one costs, rather than what formula to write. A definition assembled as a minimum over compositions arrives with the metric properties attached, is usually more faithful to the domain because the primitive edits are things practitioners already talk about, and gives you a knob — the cost assigned to each kind of edit — that can be tuned against real cases without endangering any of the axioms.

A related discipline applies when the measure was not built that way. Then the profitable move is to find an alternative characterisation of the same number under which the property is obvious, rather than to attack the original formula. An expression in terms of set sizes can be re-read as the probability of a certain event; the inequality then becomes a claim about when events can and cannot co-occur, and it falls out of a sentence about which of three outcomes can hold simultaneously. Neither route is a trick. Both are the same recognition that a quantity has several equivalent presentations and that its properties are trivial in one of them.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 3's section on distance measures, which glosses the triangle inequality as the impossibility of benefiting from a forced detour, verifies it for edit distance by concatenating the edits from one string to a third and onward, argues it for the angle between vectors by composing two rotations, and proves it for Jaccard distance by recasting the quantity as the probability that a random minhash separates two sets.
