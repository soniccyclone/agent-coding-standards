---
type: lesson
title: "Find out which assumptions a result actually rests on, because inherited machinery narrows where it applies"
figure: kolmogorov
works: [three-approaches-to-the-quantitative-definition-of-information]
axes: [primitive-count, verifiability]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Find out which assumptions a result actually rests on, because inherited machinery narrows where it applies

**Lesson:** Results arrive wrapped in the framework that first produced them, and the wrapping is usually mistaken for part of the result. A quantity discovered inside probability theory gets treated as inherently probabilistic, so people believe they need a distribution before they may use it — when in fact the same quantity can be obtained by pure counting over a set of possibilities, with no distribution anywhere. The counting version is not a lesser sibling; it is the version that still works when there is nothing to be probabilistic about. Every assumption you carry along unnecessarily is a case you have excluded yourself from for no gain.

The habit is to audit derivations for load-bearing assumptions instead of accepting the whole apparatus a result came packaged in. Strip an assumption, see whether the argument still closes. Often it does, and the stripped result covers strictly more situations. Often it does not, and now you know precisely which situations were relying on it, which is worth as much. What you must not do is skip the audit, because the default is accumulation: frameworks grow by inheriting each other's premises, and nobody notices that the whole tower is being required for a conclusion that needed two floors of it.

The counter-discipline is equally important. Being able to state the weaker version does not mean the richer framework was waste — the probabilistic setting genuinely buys concepts and relationships the combinatorial one has no way to express, and it is the right tool where its assumptions actually hold. The point is to know which one you are standing on and why, rather than defaulting to the most elaborate framework available because it is the one you learned. Minimal-assumption formulations travel; maximal-assumption formulations say more where they apply. Both facts have to be held at once, and the mistake is having only the elaborate version and thinking its scope is universal.

**Source:** [Three Approaches to the Quantitative Definition of Information](../works/three-approaches-to-the-quantitative-definition-of-information.md) — §1's insistence that the combinatorial definition of entropy and information is logically independent of any probabilistic assumption and that its mathematical problems are not trivialities, set against §2's account of the additional concepts and relationships that only become available once distributions are assumed.
