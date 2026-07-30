---
type: lesson
title: "Two systems are related only at some level of description, and refining either one destroys the relation"
figure: kolmogorov
works: [three-approaches-to-the-quantitative-definition-of-information]
axes: [cognitive-load, expressiveness]
subdomains: [foundations-of-computation, software-engineering-and-architecture]
tags: [lesson]
---
# Two systems are related only at some level of description, and refining either one destroys the relation

**Lesson:** Real things are unboundedly detailed, and the correspondence between two of them lives at a particular grain and nowhere else. A map tells you a great deal about a stretch of terrain, but the fibers of the paper and the spread of the ink correspond to nothing on the ground. Push the description of either side past the level at which the two were coupled and the shared content does not diminish gradually, it disappears. The mutual information is a property of the pair of *descriptions*, not of the pair of objects.

This is why "more detail is more faithful" is wrong as a design principle. Every model, schema, log, or mirror of an external system is a description chosen at some resolution, and adding resolution below the coupling grain adds only content that the other side does not constrain — which means content that can drift arbitrarily without ever being wrong, and therefore content nothing can validate. That is where representations rot: not in the parts that disagree with reality but in the parts reality has no opinion about. Fidelity is achieved by choosing the level at which two things genuinely track each other and describing exactly that.

Practically, the question to ask about any interface or data model is where the correspondence actually stops. Two services agree about order identities and amounts; they do not agree about row layouts, retry timings, or object graphs, and any coupling that reaches into those is coupling to noise. The same test settles arguments about how much to expose: detail above the coupling grain is contract, detail below it is implementation, and the boundary is discovered by asking which distinctions the other side could, even in principle, be sensitive to. Simplify each side toward that grain and the relationship becomes both stable and cheap to state.

**Source:** [Three Approaches to the Quantitative Definition of Information](../works/three-approaches-to-the-quantitative-definition-of-information.md) — the opening argument of §3 that real objects are infinitely complex while the relations between two of them survive only as the describing schemes are simplified, illustrated by the map that carries much information about a region while the microstructure of its paper and ink carries none.
