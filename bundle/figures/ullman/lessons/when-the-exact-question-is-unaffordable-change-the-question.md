---
type: lesson
title: "When the exact question is provably unaffordable, change the question"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, primitive-count]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# When the exact question is provably unaffordable, change the question

**Lesson:** Before optimising a computation, establish whether the exact answer is achievable at all within your budget — and this is often decidable by counting rather than by experiment. If answering a family of queries exactly requires distinguishing more input states than your storage can encode, then two distinguishable inputs must share a representation, and a query exists on which one of them gets the wrong answer. That is a proof, not a difficulty, and it converts an open-ended engineering effort into a settled question. Knowing the exact answer is impossible is genuinely liberating: it moves the discussion from "how do we make this fit" to "what weaker guarantee do we want, and how do we bound it."

Once you are approximating, two disciplines separate the useful from the merely plausible. The first is to bound the error structurally rather than measure it empirically. Force the representation into a shape where the worst case is computable — components whose sizes grow geometrically, only the boundary component ever uncertain, so the uncertainty is provably a bounded fraction of what has already been accounted for. Then a single tunable parameter, how many components of each size you permit, moves that bound to any tolerance you name, at a stated cost in space. The second discipline is to distrust the portability of the guarantee. The same construction applied to values that can be negative loses its bound entirely, because relative error is meaningless when the true answer can be near zero while its constituents are large. An error guarantee is a theorem about a specific setting; carrying the technique to a new setting means redoing the theorem, and sometimes discovering there isn't one.

The most radical version of this move is to change the question rather than approximate the answer. A sharply bounded window is expensive to maintain precisely because something must fall out of it, which means remembering enough to know what falls out. Replace it with a smoothly weighted aggregate over all history and the maintenance collapses to two arithmetic operations per arrival, with no history retained — and if the reason you wanted a window was to emphasise the recent, the weighted aggregate serves the actual purpose better than the sharp cutoff ever did. The lesson is to interrogate the specification, not only the implementation. The sharp boundary was frequently an arbitrary formalisation of a vague intent, and a different formalisation of the same intent can be cheap where the first was provably not.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the stream-mining chapter's window-counting sections: the pigeonhole argument that exact counts require the whole window, the geometric bucket structure with its tunable relative-error bound, the observation that signed values break that bound, and the exponentially decaying window offered as a reformulation rather than an approximation.
