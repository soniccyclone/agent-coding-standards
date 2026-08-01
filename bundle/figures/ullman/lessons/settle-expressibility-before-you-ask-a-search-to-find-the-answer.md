---
type: lesson
title: "Settle expressibility by hand before you ask a search to find the answer"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture, foundations-of-computation]
tags: [lesson]
---
# Settle expressibility by hand before you ask a search to find the answer

**Lesson:** Whenever an automatic procedure is going to pick the contents of some structure, two independent questions are in play, and they get conflated constantly. The first is whether the structure is even capable of holding an acceptable answer. The second is whether the procedure will find one. A disappointing result is consistent with either, and the two call for opposite responses: enlarge the structure, or fix the search. Left conflated, this becomes an expensive loop in which the search is retuned over and over against a space that never contained what was wanted.

The way to separate them is to construct one acceptable answer by hand, before any search is run, and check that the structure holds it. This is not a proposal to hand-build the real system. It is an existence proof plus a yardstick: the space is now known to be adequate, so any subsequent failure belongs to the search; and the constructed answer's quality becomes the number the search has to beat before anyone claims it has done something. Doing this well requires an instance small enough to reason about completely, which is why the exercise is worth doing on a toy instance rather than the real one. The instance is a probe of the representation, not a demonstration of the application.

The matching move on the other side is a lower bound: show that the obvious smaller structure cannot hold any acceptable answer. Together these bracket the design. You know the weakest machinery that could work and you know one thing that does work, so the remaining argument is about cost and about search, not about possibility. Without the lower bound you will over-build by reflex, since a bigger structure is always safer and its excess is invisible until it starts fitting noise or costing money.

The habit generalises to anything configured by an optimiser or a generator rather than by hand, which now covers a great deal: query planners, schedulers, autotuned parameters, layouts chosen by a fitting procedure, policies produced from examples. Before handing the decision over, write down one setting you believe is good and check that the configuration language can express it. If it cannot, the search was never going to reach it either, and the fix is at the level of the language rather than the level of the search. One caution comes with the practice: the hand-built answer is a diagnostic, not a template. Its structure will usually be legible and modular in a way the found answer is not, and expecting the found answer to look like it is a mistake, since nothing in the search was ever asked to produce something a person could read.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 13's opening, which exhibits a small hand-built network with explicit weights and thresholds that solves a bit-vector recognition problem exactly, presents it as an example of what one would like to achieve while stating that designing such a net from training examples is the actual subject, poses as an exercise a proof that no single perceptron can solve the same problem, and later attaches a footnote to a hand-design exercise on recurrent nets warning that such networks are to be learned from data rather than designed the way the exercise asks.
