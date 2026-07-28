---
type: lesson
title: "Know whether your confidence comes from proof or from survival, and distrust your reading of the result aimed at your own work"
figure: church
works: [a-set-of-postulates-for-the-foundation-of-logic]
axes: [verifiability, cognitive-load]
subdomains: [foundations-of-computation, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Know whether your confidence comes from proof or from survival, and distrust your reading of the result aimed at your own work

Church states his working plan with unusual candor. He will push the consequences of his postulates until either a contradiction appears or the development has run far enough that no contradiction seems likely — and he adds that this kind of evidence, which he calls empirical and admittedly inconclusive, is the only evidence of consistency anyone actually has for any logic worth using. That is an accurate and useful description of an epistemic position most people occupy without admitting it. Extended use without failure is genuine evidence; it is not a proof; and confusing the two is the mistake, not relying on the weaker kind when the stronger is unavailable.

Immediately after, the same page shows what pressure does to that clarity. Gödel had recently shown that a consistency proof of the sort Church hoped for is unavailable for Principia Mathematica. Church acknowledges the result, observes that its argument uses implication between propositions in a way his own system does not permit, notes that no obvious modification carries it over, and concludes that a consistency proof for his system remains conceivable. Every step there is defensible in isolation. The conclusion was still wrong: the system was inconsistent, and Kleene and Rosser proved it within a few years.

The mechanism is worth naming, because it is not ignorance and it is not carelessness. The technical gap Church identifies is real, and searching for it is exactly what a careful reader should do. The bias sits in what happens after the gap is found: a difference that merely blocks one particular proof gets treated as grounds for hope, when all it establishes is that this specific argument does not transfer. Nobody applies that generosity to a limitation result aimed at someone else's design. The asymmetry is the tell.

A programmer who takes both halves of this seriously keeps an honest register of which invariants are proved, which are tested, and which have merely never been observed to fail, and does not let time in production silently promote the third category into the first. And when a result, a benchmark, or a review says something unwelcome about their own design, they force the argument to be evaluated by the standard they would apply if it targeted a colleague's — since the instinct to locate the one respect in which the criticism does not quite apply is strongest exactly when the criticism is correct.

**Source:** [A Set of Postulates for the Foundation of Logic](../works/a-set-of-postulates-for-the-foundation-of-logic.md) — the section on the possibility of a consistency proof, where Church characterizes accumulated contradiction-free development as inconclusive empirical evidence and then argues that Gödel's incompleteness result may not transfer to his own system.
