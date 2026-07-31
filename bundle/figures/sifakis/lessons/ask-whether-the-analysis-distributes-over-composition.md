---
type: lesson
title: "An analysis only scales if it distributes over the operator that builds the system, and that is a theorem with fine print"
figure: sifakis
works: [property-preserving-abstractions-1995]
axes: [parallelizability, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# An analysis only scales if it distributes over the operator that builds the system, and that is a theorem with fine print

**Lesson:** There are two routes to a simplified model of a system assembled from parts. Assemble first and simplify the result, or simplify each part and assemble the simplifications. The second route is the only one that scales, because the first requires materializing the combined behavior — the very object whose size drove you to simplify. So the question that decides whether an analysis survives contact with a large system is whether it commutes with the assembly operator. That is not a property you can assume; it is a theorem, and in this paper it arrives loaded with hypotheses about how the per-part simplifications line up with the parts' shared variables, and it comes out differently depending on whether the parts run in lockstep, run independently, or interleave under a declared synchronization set.

The second thing the paper insists on asking is which route yields the *more precise* model, not merely which is cheaper. The intuition that composing simplifications must be the lossier option turns out to be conditional: the comparison holds unrestricted in one direction only for some assembly operators, and the reverse comparison needs relatively strong side conditions for tightly coupled composition while being easy to satisfy for loosely coupled composition. Coupling is the variable. The more the parts constrain each other's steps, the more information lives in the assembly itself rather than in the parts, and the more the distribution law has to be paid for.

Two things to carry away. First, when you design any per-component analysis — a cost model, a type discipline, an availability calculation, a resource bound — establish early whether its results compose over your actual system-building mechanism, because an analysis that only works on the assembled whole has no path to large systems no matter how good it is. Second, when it does compose, do not assume the compositional answer is the degraded one; work out the direction of the comparison, since a route that is both cheaper and no less precise is common enough to be worth checking for, and the coupling in your architecture is the thing that predicts the answer.

**Source:** [Property Preserving Abstractions for the Verification of Concurrent Systems](../works/property-preserving-abstractions-1995.md) — section 9's two motivations for composing abstractions of components rather than abstracting the compound system, its explicit question of which route yields the better approximation, and the three theorems giving compositionality results for synchronous, asynchronous, and mixed parallel composition with their differing side conditions.
