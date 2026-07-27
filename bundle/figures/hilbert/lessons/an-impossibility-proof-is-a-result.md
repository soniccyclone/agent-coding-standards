---
type: lesson
title: "When something resists being built, go prove it cannot be built under the assumptions you made"
figure: hilbert
works: [mathematische-probleme]
axes: [verifiability, primitive-count]
subdomains: [foundations-of-computation, distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# When something resists being built, go prove it cannot be built under the assumptions you made

**Lesson:** Repeated failure at a construction is data, and the disciplined response is to invert the question: show that no construction of that kind can exist given the stated premises. Hilbert treats this inversion as a first-class outcome rather than a consolation prize, and points at cases where it settled centuries of effort — the parallel postulate, squaring the circle, the general quintic by radicals — each of which got a fully satisfactory answer, though not the answer originally wanted. His most instructive example is from outside mathematics: after enough failed perpetual-motion machines, someone asked what relations among the forces of nature would have to hold for such a machine to be impossible, and the answer was conservation of energy. The impossibility proof did not merely close a dead end; it produced the law.

The reason this works is that an impossibility proof cannot be written without an exact inventory of the assumptions. To show no procedure of a given kind exists you must first say precisely what "of that kind" means, which forces the premises into the open where each one can be examined and, crucially, dropped. That is why such results are generative: the negative theorem always comes paired with a map of which assumption to relax to get something achievable. Hilbert pairs the inversion with the opposite conviction — that every well-posed problem admits a definite settlement, either an answer or a proof that none exists — and it is this pairing, not either half alone, that keeps the search honest. You are never permitted to shrug; you are only permitted to answer or to prove there is no answer.

For a working programmer this is the difference between grinding on a design that cannot work and extracting the constraint that explains why. The distributed-systems results everyone quotes have exactly this shape: consensus under asynchrony with one faulty process, or availability under partition, are not engineering shortfalls to be out-engineered but theorems whose premises tell you which knob to turn — bound the asynchrony, weaken the consistency, shrink the fault model. Someone who has internalized the move reaches for it early, at the whiteboard: state the assumptions, attempt the proof of impossibility, and let the attempt either kill the design or reveal the one assumption worth paying to remove.

**Source:** [Mathematische Probleme](../works/mathematische-probleme.md) — the methodological passage on proofs of impossibility, including the perpetual-motion inversion, and the immediately following declaration that mathematics admits no permanent ignorance.
