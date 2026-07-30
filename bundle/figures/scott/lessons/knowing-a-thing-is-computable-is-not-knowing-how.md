---
type: lesson
title: "Knowing something can be computed is a different state of knowledge from knowing how"
figure: scott
works: [outline-of-a-mathematical-theory-of-computation]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# Knowing something can be computed is a different state of knowledge from knowing how

**Lesson:** A definition can determine an object completely and still leave you no closer to producing it. This is familiar from analysis, where a series can be proved convergent by an argument that gives no handle at all on its sum, and it holds in exactly the same way for functions: an abstract characterization can be enough to fix which function is meant and enough to establish that it is computable, while the question of how to compute it remains entirely open. The two facts are separately acquired and separately valuable, and conflating them is how a project ends up believing a problem is solved because it has been classified. Until the procedure is exhibited, what you possess is a description and an existence claim, not the thing.

The point sharpens once realizability is defined as the existence of some effective approximating sequence converging to the object. Many different sequences converge to the same limit, so establishing that at least one exists tells you nothing about which of them you should use, or whether any of them is remotely practical. The classification is a genuine result — it separates what can be reached from what cannot, and that boundary is worth knowing — but it is silent by construction on the questions engineering cares about: which approach, at what cost, converging how fast. Treating a positive computability verdict as an answer to those questions is reading a result for more than it says.

What follows for practice is a habit of keeping two ledgers. In one, what has been shown to exist or to be possible; in the other, what has actually been constructed and can be run. Work that moves an item from the first ledger to the second is real work, not write-up, and estimating it as write-up is a common way for a schedule to fail. The same split explains why an adequate theory of computation has to deliver both halves — the abstractions that say what is computable, and the realizations that say how — and why a theory that delivers only the first is incomplete rather than merely abstract. The corresponding discipline for your own claims: when you say something is possible, say plainly whether you mean you have done it, or that you have an argument that it can be done, because those two statements support very different decisions downstream.

**Source:** [Outline of a Mathematical Theory of Computation](../works/outline-of-a-mathematical-theory-of-computation.md) — the introduction's observation that a mathematically defined function can be known computable without it being obvious how to compute it, with the analogy to a series known to converge without its sum being known, and the conclusion that an adequate theory must supply both the abstractions and their physical realizations; together with the computability section's remark that many sequences converge to the same element, so knowing an element is computable does not tell you the best way to compute it.
