---
type: lesson
title: "A definition that lets you certify an artifact does not tell you how to build one or how to take one apart"
figure: floyd
works: [the-syntax-of-programming-languages-a-survey]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# A definition that lets you certify an artifact does not tell you how to build one or how to take one apart

**Lesson:** A formal definition of a class of artifacts reads like a stack of axioms, and it is easy to mistake possessing one for possessing the ability to work with the artifacts. It is not the same thing. Given a finished object and an account of its structure, the definition lets you certify that the object belongs to the class and lets you show someone else why. It does not tell you how to produce a member of the class to order, and it does not tell you how to recover the structure of an object handed to you without one. Those are two further problems, and they are the ones that actually cost money.

The gap is visible the moment you re-read the definition as a set of permissions rather than a set of truths. Each rule licenses a substitution, and repeatedly exercising those permissions manufactures members of the class, with the sequence of exercises standing as an abbreviated proof that what you produced belongs. Read this way the definition becomes a generator, and although the validating and generating readings carry the same content, the generating one is far more tractable to study, because it makes the process of construction explicit instead of leaving it implicit in a claim. Even then, something is missing: nothing in the definition says which permission to exercise when. Choosing among the alternatives is governed by whatever intent the author has, and that mechanism is not part of the formalism at all.

Recovery — taking a finished object and reconstructing why it qualifies — is the harder direction and the one that must be mechanized if the definition is to earn its keep. The definition constrains the answer without providing a procedure, so procedures have to be invented on top of it, each one working only for definitions of a restricted shape. This is why a field can possess a clean formalism for years and still argue about tooling: the formalism settled membership, and every remaining question is about the two directions of travel it left open.

A programmer who holds this distinction stops treating a schema, a type system, a grammar, or a specification as though writing it down finished the job. The useful questions after a definition exists are: can this generate valid instances, can it recover structure from instances it did not generate, and what shape must it be restricted to before either becomes cheap? Answering "the spec is written" to any of those is a category error, and one that shows up as a project discovering after the fact that its beautiful definition supports nothing it needs.

**Source:** [The Syntax of Programming Languages — A Survey](../works/the-syntax-of-programming-languages-a-survey.md) — the section on phrase structure grammars, which notes that a grammar analogous to an axiom set lets someone who already understands a program's structure prove it well formed while telling us neither how to synthesize a particular program nor how to analyze a given one, followed by the reinterpretation of each rule as a permit to substitute and the observation that the mechanism of choice among alternatives lies outside the formalism.
