---
type: lesson
title: "Make cost depend on the instance in front of you, and pick a representation that keeps its structure visible"
figure: stearns
works: [an-algebraic-model-for-combinatorial-problems]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Make cost depend on the instance in front of you, and pick a representation that keeps its structure visible

**Lesson:** Framing a problem as membership in a set of strings makes the instance an undifferentiated blob. It is a perfectly good frame for asking which problems are hard, and it is close to useless for asking whether this particular input is hard, because the representation has already discarded the only thing that could answer that: which parts of the instance interact with which. Represent an instance instead as a collection of variables together with a collection of relations over them, and the interaction pattern is right there in the representation. That pattern is the entire exploitable structure. Everything downstream — organising the instance into a shape that displays which subproblems are independent, and bounding cost by a parameter of that shape rather than by the input's total size — is available only because the representation kept the pattern.

The consequence is that cost stops being a property of the problem and becomes a property of the instance. Two inputs to the same notoriously hard problem, of the same size, can differ enormously in what they cost, according to a structural parameter each of them individually possesses. Worst-case class membership is a statement about the least structured member of a family; the input on your desk is a particular member, and it is entitled to its own answer. So the move when told a problem is intractable is not to accept it but to ask two questions in order: did my representation destroy the structure I would need, and if not, what is the structural parameter of this instance, and what does the cost look like as a function of it?

A detail of the arrangement is worth extracting on its own. The structural analysis here depends only on which variables occur in which relations — purely on incidence, never on what the relations mean. That independence is what makes the analysis reusable: it can be done once, by someone who knows nothing about the semantics, and applies to every interpretation of the same skeleton. When you are carving a system into parts, look for a cut that separates a purely combinatorial layer from an interpretive one, because a combinatorial layer is analysable in isolation and its results are shared by everything above it. A cut that leaves meaning smeared across both sides gives you two things to study instead of one, and the results of neither generalise.

**Source:** [An Algebraic Model for Combinatorial Problems](../works/an-algebraic-model-for-combinatorial-problems.md) — the introduction and abstract, which contrast the language-recognition framing with a representation as variables and terms and give as the model's first stated advantage that one can discuss the structure of individual instances, with cost governed by a parameter of that instance's organisation; and the remark closing the first half of the structure-trees section that the structural concepts depend only on which variables occur in which terms and are therefore independent of the terms' interpretation, so structural analysis can be carried out orthogonally to meaning.
