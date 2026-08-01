---
type: lesson
title: "An example small enough to follow is outside the regime it is teaching"
figure: ullman
works: [mining-of-massive-datasets]
axes: [cognitive-load, verifiability]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# An example small enough to follow is outside the regime it is teaching

**Lesson:** Techniques that exist because of scale can only be demonstrated at a size where they are pointless. A sparse encoding shown on a four-by-four matrix takes more space than writing the matrix out. A method justified by the infeasibility of exact solution is illustrated on an instance you can solve exactly by hand in a minute. A detector for a signal that emerges over billions of items is run on four items and reports nothing conclusive. This is not a flaw in the examples; there is no alternative, because an example whose behaviour you can verify by inspection is by definition one where the machinery has nothing to do. The flaw is leaving that unsaid, because a reader who is not told will calibrate on the demonstration and conclude that the technique is marginal.

Two distinct failures follow from the silence. The first is dismissal: someone measures the technique on the tractable case, finds it slower or larger or less accurate than the naive alternative, and reports honestly that it does not help. They are right about what they measured and wrong about the claim. The second, worse, failure is adoption of the wrong thing. Having seen only the small case, a reader keeps the parts that mattered there and drops the parts that were pure overhead at that size, which are usually the parts that were the whole point. The blocking scheme gets simplified away because it obviously cost more than it saved on the toy. The approximation gets replaced by the exact computation because on four nodes the exact computation is a quadratic you can solve on paper.

The fix is a single sentence attached to the demonstration, and it needs to do three things: say that the example is outside the regime, say what the regime actually is in numbers, and say which observable quantity crosses over. Something is being illustrated here that is not the technique's value, and naming what it is — the mechanical procedure, the shape of the encoding, the sequence of steps — separates it from the claim about payoff, which the example cannot support and should not be asked to. The number matters more than the qualitative hedge. "This helps once the fraction of nonzero entries drops below roughly one in ten" is a claim a reader can check against their own data; "this helps at scale" is a claim they can only take on faith or reject.

The habit generalises past documentation to any argument by demonstration: benchmarks, proofs of concept, spike branches, migration pilots. Each is chosen for tractability, and tractability is usually correlated with the absence of the condition that motivated the work. Before running a pilot, write down which parameter of the real setting the pilot has changed and by what factor, and which conclusions therefore do not transfer. Do it beforehand, because afterwards the pilot has produced numbers, and numbers are hard to argue with even when they measured the wrong regime.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the footnote in chapter 5 conceding that the four-node transition matrix used to illustrate the compact sparse representation is not itself sparse enough for the representation to be useful, and that the example only shows the process; reinforced by the same chapter's hand-solution of the hubs-and-authorities equations as a quadratic on a five-node graph after stating that only iteration is possible at Web scale, and by the spam-mass example whose four values are all closer to zero than to one and therefore conclude nothing.
