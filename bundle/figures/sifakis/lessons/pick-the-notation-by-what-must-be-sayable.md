---
type: lesson
title: "Choose a specification notation by what it can state, then by how comfortably; efficiency is the last constraint"
figure: sifakis
works: [turing-lecture-2009]
axes: [expressiveness, cognitive-load]
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# Choose a specification notation by what it can state, then by how comfortably; efficiency is the last constraint

**Lesson:** When selecting a formalism for describing correct behavior, the binding constraint is what the formalism can say at all. If the property that matters to you falls outside its expressive range, every other virtue is irrelevant, because you will end up checking something adjacent to what you cared about and calling it done. Only after that requirement is met do the softer criteria come into play: how compactly a given property can be written, and how naturally an engineer arrives at the right formula. Compactness and comfort usually move together but not always, and comfort resists formalization entirely — which is exactly why it gets neglected in academic comparisons and dominates in industrial ones.

The trade is real in both directions. More expressive notations generally cost more to decide; more compact ones can cost more still, since a short formula may unfold into an exponentially larger equivalent in a weaker system. Two formalisms can also be incomparable rather than ordered: one distinguishes what happens along every future from what happens along some future and pays in conceptual overhead; the other keeps a single linear picture of time, is easier to learn, and simply cannot state certain claims about possibility. Picking between them is not a matter of finding the stronger one but of knowing which claims your domain actually needs to make.

The practical consequence is to resist the instinct that the informal criterion is the unimportant one. That significant industrial effort has gone into building specification languages whose main advantage over their academic ancestors is that working engineers can write them correctly is a measurement, not a compromise. A notation nobody can wield produces specifications that are subtly wrong, and a check against a wrong specification is worse than no check, because it converts an open question into false confidence.

**Source:** [Model Checking: Algorithmic Verification and Debugging](../works/turing-lecture-2009.md) — Emerson's sections on expressiveness and efficiency, including the succinctness/convenience distinction, the linear-versus-branching-time debate, and the industrial temporal logics built for usability.
