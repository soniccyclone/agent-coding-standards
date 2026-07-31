---
type: lesson
title: "If no bounded observation can move a belief, the matter is already settled and you are only ignorant"
figure: kolmogorov
works: [grundbegriffe-der-wahrscheinlichkeitsrechnung]
axes: [verifiability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification]
tags: [lesson]
---
# If no bounded observation can move a belief, the matter is already settled and you are only ignorant

**Lesson:** Kolmogorov's closing theorem: take a property of an infinite sequence of variables such that, for every n, learning the first n variables leaves the property's probability exactly where it was. Then that probability is zero or one — no other value is available. He also identifies the natural class satisfying the hypothesis: independent variables together with a property whose truth is unaffected by changing any finite number of them.

Read as epistemics this is a sharp instrument. When no bounded amount of evidence can shift your estimate of a claim, the claim is not genuinely uncertain. It is determined, and whatever number you were carrying was measuring your own ignorance rather than any indeterminacy in the world. That kills a specific and very common move: reporting middling confidence about such a property as though middling confidence were the modest, honest answer. It is not one of the answers on offer. Either the property holds or it does not, and the intermediate figure is a statement about you.

The engineering content is a criterion for which questions testing can bear on at all. Does this process eventually converge, eventually stop retrying, eventually drain the queue, eventually release every lock — each of these is invariant under any finite prefix of behavior. Rewrite the first million steps however you like and the answer does not budge. It follows that no finite run gives evidence about it: not a soak test, not a week in staging, not a year in production. The answer is fixed by the structure of the rules, so it can only be established by argument about the rules, and when you cannot make that argument you do not possess a probably-fine system — you possess a system that either has the property or lacks it, and you do not know which. The skill worth building is the sorting: prefix-invariant properties go to proof, prefix-sensitive properties go to measurement, and confusing the two buys you both wasted test cycles and confidence you have not earned.

**Source:** [Grundbegriffe der Wahrscheinlichkeitsrechnung](../works/grundbegriffe-der-wahrscheinlichkeitsrechnung.md) — the appendix on the zero-or-one law, which proves that a property whose conditional probability given the first n variables equals its absolute probability for every n must have probability zero or one, and notes that the hypothesis is satisfied when the variables are mutually independent and the property is unchanged by altering finitely many of them.
