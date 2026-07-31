---
type: lesson
title: "When the motivation for an approach collapses, its machinery is usually still the valuable part"
figure: scott
works: [a-type-theoretical-alternative-to-iswim-cuch-owhy]
axes: [verifiability, expressiveness, cognitive-load]
subdomains: [foundations-of-computation, programming-languages-and-semantics, formal-methods-and-verification]
tags: [lesson]
---
# When the motivation for an approach collapses, its machinery is usually still the valuable part

**Lesson:** A piece of work usually bundles two separable things: a reason for doing it that way, and the apparatus built to carry it out. When the reason dies — a rival approach turns out to work after all, the obstacle you were routing around gets removed, the premise is refuted — the reflex is to discard the whole bundle, because the argument that justified it no longer holds. That reflex throws away the wrong half. A proof rule, a set of axioms, an interface, a decomposition of a problem was justified by the motivation but does not depend on it; it can be lifted out and attached to whatever framework replaced the original. What has actually expired is the claim that this was the *only* way, which was never the useful part of the contribution.

Scott shelved this manuscript for twenty-four years because its foundational argument had been overtaken by his own subsequent discovery, and the argument was indeed dead. The axiomatics were not. Circulated privately, they became one of the direct motivations for building machine-checked proofs about recursively defined functions, and that project led to the design of ML — a lineage entirely indifferent to whether the type-free calculus turned out to have models. The judgment "outmoded" was correct about the framing and badly wrong about the content, and the twenty-four-year delay is what that misjudgment cost.

The practical form of this is a habit when abandoning a direction: before you drop it, separate the parts that were arguments from the parts that were constructions, and ask of each construction whether anything in it referred to the premise you just lost. Usually most of it does not. The same reading applies to other people's superseded work, which is where the cheap finds are — a rejected approach that was rejected for its motivation still contains whatever it invented in order to function, and nobody is looking there because the headline verdict was negative.

**Source:** [A Type-Theoretical Alternative to ISWIM, CUCH, OWHY](../works/a-type-theoretical-alternative-to-iswim-cuch-owhy.md) — the 1993 preface's account of why the paper went unpublished, that the advocated foundational program had been outmoded by the discovery of lattice-theoretic models, alongside its note that the proof system laid out here was continued and extended by others and motivated the automated-proof work that led to ML. The closing 1993 afterthought makes the same point about the paper's definitions and open problems still holding up.
