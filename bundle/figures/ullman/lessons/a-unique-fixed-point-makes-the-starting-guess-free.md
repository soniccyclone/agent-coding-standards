---
type: lesson
title: "A unique fixed point makes the starting guess free"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# A unique fixed point makes the starting guess free

**Lesson:** Most heuristics have to be validated before they are trusted, because a wrong heuristic produces a wrong answer. There is one class where this is not true, and it is underexploited: when a computation is defined as the limit of an iteration with a unique fixed point, the initial value cannot affect the result. It can only affect how many iterations you spend getting there. That turns initialisation into a pure performance knob with no correctness surface, which means you can pour in any guess you have — a stale result from last week, an output from a cruder model, a hand-written prior, the answer to a similar question — without owing anyone an argument that the guess is good.

The asymmetry in the payoff is what makes this worth deliberately looking for. A guess that is close saves a meaningful fraction of the iterations, and on a computation whose whole cost is fifty passes over a matrix that does not fit in memory, a fraction is real money. A guess that is bad costs a few extra passes at worst. Nothing else in a numerical pipeline offers that shape, and the reason people leave it on the floor is that initialisation is conventionally written once, as a uniform vector or all zeros, in the same commit as the loop, and then never revisited because it is not where the interesting mathematics lives.

Two things have to be true, and both are checkable rather than matters of judgement. The fixed point must actually be unique, which usually rests on the same conditions that made the iteration converge at all, and is exactly the thing to re-examine if your problem has a symmetry or a free scaling that leaves a family of solutions rather than one. And the stopping rule must be a test on the answer, not a fixed iteration count: a loop hardcoded to fifty passes gains nothing from a better start, and worse, hides the gain, so nobody discovers that ten would have done. Warm starting and convergence-based termination are a package; either alone is close to useless.

The generalisation reaches well past matrix iterations. Any computation whose specification is "the value satisfying this equation" rather than "the value produced by this procedure" has this property, and specifying things that way on purpose is a design move with this as one of its returns. Constraint solvers, layout engines, distributed reconciliation loops, and equilibrium simulations all admit warm starts for the same reason, and all of them typically run in contexts where a nearly-correct previous answer is sitting right there. Recognising the shape is the whole trick: the question to ask of any expensive loop is whether its answer is defined by where it ends up or by what it did, because only the first kind lets you cheat at the beginning.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 5's topic-sensitive PageRank example, where the iteration is started with the surfers already concentrated on the teleport set and the text remarks that although the initial distribution has no effect on the limit it may help the computation converge faster; together with the chapter's repeated framing of PageRank as the limit of multiplying any nonzero starting vector, stopped when the vector changes little between rounds.
