---
type: lesson
title: "Carry identity in an opaque handle, then constrain the human names by whatever consumes them downstream"
figure: reenskaug
works: [working-with-objects-the-ooram-software-engineering-method]
axes: [expressiveness, verifiability]
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
tags: [lesson]
---
# Carry identity in an opaque handle, then constrain the human names by whatever consumes them downstream

**Lesson:** In this system's internal representation, every element of a model is identified by an opaque handle, and the names people assign exist to help those people understand what they are looking at — they carry no formal weight. That decoupling is what makes a model safely editable: renaming anything is a display change, cannot break a reference, and cannot collide. Systems that instead make the human-chosen name the identity acquire the familiar pathologies, where renaming is a refactor, two teams cannot both use the obvious word, and identity silently changes when someone fixes a typo.

The interesting part is the qualification, because pure decoupling is not the whole answer. When the model is used to generate code, those names become identifiers in the generated program — and at that point a name that was purely decorative starts determining whether anyone can trace the running system back to the design it came from. The advice given is to choose names that can be used unchanged as program identifiers, so the correspondence between model and program is as evident as possible. Not names that are legal after mangling; names that survive the translation untouched. Any transformation applied on the way out — case conversion, punctuation stripping, collision suffixing — is a place where a reader holding the model and a reader holding the code have to reconstruct the mapping in their heads, and that reconstruction is where they diverge.

The mechanism that makes this practical rather than an aspiration is tooling that warns while the name is being chosen: the analyst is told when a name does not conform to the syntax and pragmatics of the target language, and told when a name duplicates another in a way that would fail to compile downstream. That is the load-bearing design decision, because the constraint originates in a system the modeller is not looking at and may not know. Discovering it at generation time means a build error and a rename cascade; discovering it at authoring time costs one keystroke. The general principle is that a constraint imposed by a downstream consumer should be enforced at the upstream point of authorship, where it is cheap and where the person with the intent is present.

Both halves together give the working rule: never let a human-readable label be the thing that establishes identity, and never let it be arbitrary either — free to change, constrained in what it may be.

**Source:** [Working With Objects: The OOram Software Engineering Method](../works/working-with-objects-the-ooram-software-engineering-method.md) — appendix A3 on the scope of identifiers, which states that when a model is represented as a structure of objects the entities are identified by their object identifiers while user-assigned names help users understand the models but have no formal significance; that if the model is used to generate code the names become identifiers in the chosen programming language, so the wise analyst uses entity names usable unchanged as program identifiers to make the model-to-program relationship as evident as possible; and that the modeling tools support this by warning when a chosen name does not conform to the syntax and pragmatics of the chosen language and when duplicate names would cause compilation errors.
