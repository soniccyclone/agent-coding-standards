---
type: lesson
title: "A deliberately simple model at the user's level is what allows sophistication to be stacked above it"
figure: wilkes
works: [computers-then-and-now]
axes: [cognitive-load, verifiability, parallelizability]
subdomains: [operating-systems-and-systems-programming, programming-languages-and-semantics]
tags: [lesson]
---
# A deliberately simple model at the user's level is what allows sophistication to be stacked above it

**Lesson:** The single most consequential decision in a general-purpose system may be a restriction rather than a capability: settling that, as far as the person writing programs is concerned, one thing happens at a time. The hardware need not honour that literally, and by and large it does not. What matters is that the model presented upward is sequential, because every layer of sophistication built afterwards — languages, libraries, operating systems, tooling — rests on being able to say what the state of the computation is at a given point. Remove that and each layer must carry the combinatorics of concurrent effects into everything above it, and the layers stop composing.

The evidence for how much this is worth is what happens without it. Attempts to program machines whose operations genuinely overlapped from the programmer's point of view were vastly harder than the difference in mechanism suggests, and the difficulty is not a matter of familiarity: it is that the simple model is the precondition for building anything on top, so its absence does not make one task harder, it makes the whole tower impossible. A simplification with that property is not a concession to weak programmers. It is load-bearing structure, and it is worth defending against locally-attractive features that would compromise it.

The general principle is that the interface a system offers upward should be chosen for what can be built on it, not for how much of the machine it exposes. Fidelity to the mechanism and capacity to support layers are usually in tension, and the second one compounds while the first one does not. A model simple enough to reason about at every point invites decades of construction above it; a model that faithfully reports everything the substrate does invites each of its users to rediscover the same complexity independently.

**Source:** [Computers Then and Now](../works/computers-then-and-now.md) — the next-breakthrough section's assessment that accepting one operation at a time as the programmer sees it made programming conceptually simple and paved the way for successive layers of sophistication, supported by the author's observation of attempts to program early machines whose operations proceeded in parallel.
