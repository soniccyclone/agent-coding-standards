---
type: lesson
title: "An equivalence proved at one resolution licenses nothing at a finer one"
figure: stearns
works: [on-the-computational-complexity-of-algorithms]
axes: [hardware-affinity, expressiveness, primitive-count]
subdomains: [foundations-of-computation, algorithms-and-complexity]
tags: [lesson]
---
# An equivalence proved at one resolution licenses nothing at a finer one

**Lesson:** It was long settled that enriching a machine — more storage bands, more symbols — adds nothing to the set of things it can compute. That settled fact is routinely misread as a licence to ignore the enrichments, and the misreading is the whole trap. An equivalence is always an equivalence with respect to some observation. Prove two designs indistinguishable under "what answers exist" and you have proved nothing about "how fast the answers arrive," and the second question is the one under which the enrichments turn out to be decisive. So the extra bands, provably inert for computability, become the reason to build the model with them, because the finer measure can see exactly what the coarser one was blind to.

The general habit is to attach the observation to every equivalence claim you accept or make, and to treat a change of question as invalidating the claim until re-proved. Two functions with the same input-output behaviour are interchangeable under testing and not under profiling. A refactoring is behaviour-preserving with respect to the properties someone bothered to observe, and silently arbitrary with respect to allocation counts, failure ordering, and everything else. A protocol change that preserves the set of reachable states can still destroy every latency property of the system. In each case the earlier proof is not wrong, it is simply about a coarser world, and inheriting it into a finer one is a category error that feels like rigour.

The constructive corollary matters as much as the warning. Because the axis of interest determines which refinements are inert and which are load-bearing, choosing a model is choosing which distinctions to keep alive, and that choice should be made against the question at hand rather than inherited from whoever asked the previous question. When the target of interest is real machines, a model whose shape resembles those machines is not a concession to engineering but a precondition for the results meaning anything — the resemblance is the justification. And when you discover that some feature everyone treats as an implementation detail is exactly the feature your measure can see, you have found where the interesting results are going to come from.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the model-selection argument in the introduction and the following section, which cites the known result that added storage bands and symbols do not enlarge the computable functions, then chooses the many-band model anyway on the grounds that it resembles a real computer and that, once speed rather than computability is the question, the extra bands make a difference.
