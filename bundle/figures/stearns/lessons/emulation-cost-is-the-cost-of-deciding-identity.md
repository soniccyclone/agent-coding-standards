---
type: lesson
title: "When you give up names, the whole emulation cost collapses into deciding identity"
figure: stearns
works: [on-the-computational-complexity-of-algorithms]
axes: [hardware-affinity, primitive-count]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# When you give up names, the whole emulation cost collapses into deciding identity

**Lesson:** Substituting a poorer storage structure for a richer one — a single band for several, a line for a plane — produces a strikingly uniform penalty across cases that look unrelated: the emulated cost is the square of the original. That uniformity is a clue, and following it up locates the single operation the whole penalty is buying. The poor structure has no way to name a location, so it keeps the entire history of accesses and, whenever the emulated machine reaches for a location, must decide whether some past entry refers to the same place. That decision is the cost. Everything else in the emulation is bookkeeping proportional to what is already there. The condition under which any generalized structure admits the same square penalty is exactly the condition that this identity test can be performed cheaply from the recorded history, which is why unrelated generalizations land on the same exchange rate — they are all paying for the same missing primitive.

That reframes what an addressing scheme is for. A name is a device for deciding identity in constant time, and its absence is not a mild inconvenience but a change in the complexity class of every access. Content-addressed and log-structured designs are exactly the trade being described: give up names, gain uniformity and history, pay in identity resolution. The characteristic engineering symptom is a system that behaves beautifully until the history it must search grows, at which point cost per operation rises with the age of the system rather than with its load — the signature of an identity test done by search.

The transferable habit has two parts. First, when comparing two designs, stop asking which is faster and ask what the exchange rate is, because exchange rates come in a small number of kinds: free up to a constant, or a fixed polynomial penalty, and knowing which one you are looking at determines whether the difference is an implementation detail or an architectural commitment. Second, when a penalty is uniform across superficially different substitutions, do not accept the uniformity as coincidence — find the single operation all of them are paying for. Reinstating that one operation as a primitive is usually the cheapest possible fix, and identifying it is more valuable than any amount of optimising around it.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the other-devices section, where several band-count and dimensionality reductions each cost a squaring, the planar-tape simulation is carried out by recording the access history and testing whether two recorded positions coincide by balancing the shift instructions between them, and the closing remark stating that any generalized structure whose return-to-a-square test can be done in real time yields the same square law; contrasted with the variants shown in the same section to cost nothing at all.
