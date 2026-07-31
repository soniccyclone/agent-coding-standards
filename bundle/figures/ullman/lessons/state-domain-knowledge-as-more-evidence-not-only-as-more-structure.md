---
type: lesson
title: "State domain knowledge as more evidence, not only as more structure"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# State domain knowledge as more evidence, not only as more structure

**Lesson:** When you know something about a problem that the evidence alone would not reveal — that a certain kind of change to an input leaves its correct answer unchanged — you have two places to put that knowledge, and they are genuinely different engineering decisions. You can build it into the structure of the system, so that the invariance holds by construction and cannot be violated. Or you can manufacture new evidence from old by applying the transformation and keeping the same answer, so that the system is simply shown the invariance many times and comes to respect it. Both encode the same belief. Neither is universally better.

Structure gives you a guarantee and costs you generality: the invariance is exact, it holds on inputs you never saw, and it reduces what has to be determined — but it is a hard constraint, so if the invariance is only approximately true you have forbidden something real. Evidence gives you flexibility and costs you certainty: the system will respect the invariance approximately, in proportion to how much manufactured evidence you supplied, and it can still deviate where genuine evidence pushes the other way — but nothing prevents it deviating where you did not want it to. The choice is essentially how confident you are: exact invariances belong in structure, approximate ones belong in evidence.

Manufacturing evidence has a second advantage worth stating separately, which is that it needs no cooperation from the machinery. The transformation is a function on inputs; you apply it before anything else runs. That means a small amount of domain knowledge can be injected into a system you did not build and cannot modify, which is often the actual situation — and it means the knowledge is expressed as data, where it can be inspected, versioned, and disagreed with, rather than buried in a structural decision that only the implementer can see.

The general framing to carry away is that "what we know about this domain" is a thing with a deployment target, and the target is a decision. Business rules, physical constraints, symmetries, known equivalences — for each, ask whether it belongs in the type system and the structure, where it will be enforced and cannot bend, or in the corpus of examples and test cases, where it will be respected but not guaranteed. Putting everything in one place by reflex is how systems end up either too rigid to fit reality or too loose to be relied on.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the dataset-augmentation section of the regularization chapter, which creates additional synthetic training examples by applying transformations or adding noise, uses the example of rotating a digit image a few degrees while keeping its label, and describes the process explicitly as a way of encoding additional domain knowledge — set against the convolutional chapter's alternative treatment of an invariance, where identical weights are imposed structurally across positions.
