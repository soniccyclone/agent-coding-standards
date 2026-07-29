---
type: lesson
title: "The count of interacting parts caps which behaviours are reachable at all, whatever you tune"
figure: turing
works: [the-chemical-basis-of-morphogenesis]
axes: [primitive-count, expressiveness]
subdomains: [foundations-of-computation, distributed-systems-and-concurrency]
tags: [lesson]
---
# The count of interacting parts caps which behaviours are reachable at all, whatever you tune

**Lesson:** Before tuning a system, enumerate the qualitatively distinct behaviours its structure permits — and check that the behaviour you want is on the list. Some behaviours are unreachable not because the parameters are wrong but because there are too few interacting components for that behaviour to exist. A two-part interaction can be made to grow, to shrink, to oscillate in unison, or to settle into a fixed spatial pattern; it cannot be made to produce a travelling wave, and no search through its parameter space will ever find one. Add a third interacting component and the travelling wave becomes available. The count is a hard ceiling on the repertoire, sitting underneath every parameter you could turn.

The exhaustive classification is what makes this visible, and it is worth the effort for a second reason: it tells you what to go look for in the world. Once the list of possible behaviours is complete you can ask which entries you have actually observed, and the empty entries are either evidence your model is the wrong model or a prediction of something not yet found. A classification of the whole behaviour space is a stronger scientific object than any number of interesting examples, because the examples cannot tell you what is missing.

The practical consequence is a reordering of debugging and design work. When a system stubbornly refuses to do what you want, the first question is structural — is this behaviour in the reachable set for a system with this many interacting parts and this coupling topology? — and only after that a question of tuning. Endless parameter search for a behaviour that the structure forbids is the most expensive way to discover you needed one more component. Conversely, when you are about to add a component, the honest justification is naming the behaviour it unlocks that was previously unreachable, which is a much sharper argument than "more flexibility."

**Source:** [The Chemical Basis of Morphogenesis](../works/the-chemical-basis-of-morphogenesis.md) — the classification of asymptotic behaviour on a ring into six exhaustive cases, with the explicit note that two of them cannot be realized without a third morphogen, plus the later summary listing which cases have observed counterparts and which do not.
