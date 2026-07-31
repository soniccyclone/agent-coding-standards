---
type: lesson
title: "Build a special-purpose system so it reads as a fragment of a general one you already believe"
figure: scott
works: [a-type-theoretical-alternative-to-iswim-cuch-owhy]
axes: [expressiveness, verifiability, cognitive-load, primitive-count]
subdomains: [programming-languages-and-semantics, foundations-of-computation, formal-methods-and-verification]
tags: [lesson]
---
# Build a special-purpose system so it reads as a fragment of a general one you already believe

**Lesson:** A general framework can be perfectly adequate in principle and still be the wrong instrument, and the diagnosis has a recognizable form: it can express what you want but does not make the distinction you care about salient. Everything in computation can be phrased inside general set theory, yet most of set theory concerns the transfinite while computation concerns finite processes, and its axioms are built to capture arbitrary subsets while you care about algorithmically given ones. The concrete symptom is that a notion you need constantly — whether some function you just defined is effective — is not visible in the formalism and has to be re-established by hand each time. That is the signal to build something restricted and purpose-shaped, rather than to keep working in the universal thing.

The trap on the other side is inventing a free-standing formalism, because then its theorems are only true relative to itself. The move that gets both is to design your restricted system with its own primitives, axioms and rules — genuinely its own thing, tuned to the distinctions you need — while respecting the conventions of the general framework closely enough that the whole apparatus can be *read* as a fragment of it. Then each theorem you prove is recognizable as valid in a setting whose consistency you already accept, and you have inherited its credibility without inheriting its inconvenience. This is different from encoding your system inside the general one, which would give the credibility back at the price of the salience you built the system to gain.

The engineering analogue is exact. A special-purpose language, notation, or model earns its keep by making the distinctions of one domain immediate, and it stays trustworthy by remaining interpretable in terms of something more general whose semantics is already settled — so that anything you conclude in the small system is automatically a claim in the large one. A restricted system with no such reading is a set of rules to be taken on faith. A restricted system that is merely notation over the general one has not restricted anything. The valuable position is the narrow gap between them: independent in its axioms, embeddable in its meaning.

**Source:** [A Type-Theoretical Alternative to ISWIM, CUCH, OWHY](../works/a-type-theoretical-alternative-to-iswim-cuch-owhy.md) — the 1969 introduction, which argues set-theoretical formalism is unhelpful for computation because of its transfinite emphasis and its concern with arbitrary rather than algorithmically defined subsets, notes that it is not generally clear when a function defined there is recursive, and then presents the paper's system as independent in its axioms and rules yet obeying the canons of type theory so that it can and must be read as a fragment of set theory with its theorems recognizable as valid — the feature the introduction identifies as missing from the type-free calculus.
