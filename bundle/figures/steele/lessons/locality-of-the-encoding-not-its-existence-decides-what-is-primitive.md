---
type: lesson
title: "Whether a feature is really derived is decided by how local its encoding is, never by whether an encoding exists"
figure: steele
works: [lambda-the-ultimate-imperative]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, foundations-of-computation]
tags: [lesson]
---
# Whether a feature is really derived is decided by how local its encoding is, never by whether an encoding exists

**Lesson:** Any universal language can encode any feature, so the existence of an encoding proves nothing about whether the feature is fundamental. This work makes that point about its own results and then supplies the test that does carry information: look at the translation. Is the rewrite a local rewrite, so that each construct maps to a corresponding piece of the target with the program's overall shape intact? Does the translated program remain recognizable as the same program? Does it stay roughly the same size? When all three hold, the feature was genuinely a notation over the target's mechanism, and the small primitive basis is not a trick — it is the honest account. Sequencing, loops, labeled jumps, and most variable assignment pass this test against procedure application and conditionals.

The test earns its keep by also failing. The same work reports that two of its constructs — an escape operator that abandons a pending computation, and assignable locations general enough to include components of data structures — cannot be given local translations. The rewrites for those are global and awkward, and the authors read that as evidence: these are probably not derived constructs at all, and if they are wanted they should be built in as primitives rather than simulated. That is a much stronger conclusion than "we could not find a nice encoding," because the locality criterion turns an aesthetic complaint into a structural claim about the primitive basis.

A programmer who adopts this criterion has a usable way to answer the recurring question of whether a capability belongs in the core of a system or in a library on top of it. Write the encoding and measure how far it spreads. If adding the capability forces changes threaded through unrelated parts of the program — every caller gains a parameter, every function's return convention changes, the control flow is turned inside out — the capability is not derived, it is a new primitive that you are paying for in diffuse complexity. The same reasoning explains why threading a context object through an entire codebase feels wrong: it is the visible cost of simulating something the substrate does not provide.

**Source:** [Lambda: The Ultimate Imperative](../works/lambda-the-ultimate-imperative.md) — the concluding section, which distinguishes the surprise of naturalness from the triviality of universality, and separates the locally-translatable constructs from escape operators and general assignable locations.
