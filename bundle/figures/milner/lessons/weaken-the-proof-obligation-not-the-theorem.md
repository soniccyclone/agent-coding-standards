---
type: lesson
title: "Weaken the proof obligation, not the theorem, when the obvious witness will not close"
figure: milner
works: [a-calculus-of-mobile-processes]
axes: [verifiability, cognitive-load]
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
tags: [lesson]
---
# Weaken the proof obligation, not the theorem, when the obvious witness will not close

**Lesson:** To show two systems interchangeable by the coinductive method you exhibit a relation containing them and closed under the systems' own steps. In a calculus where communication can manufacture a fresh scope boundary out of nothing, the obvious relation is not closed: take one step and the two sides differ by a boundary that the relation, written down by hand for the case at hand, does not mention. The tempting fix is to enlarge the relation until it absorbs everything the dynamics can produce — every layering of boundaries, every renaming — which makes each individual proof enormous and re-does the same closure work every time.

What is done instead is to weaken the closure requirement once and prove, separately and permanently, that the weaker requirement still suffices. Exhibiting a relation whose steps land not inside the relation but inside the relation modulo added boundaries is declared enough, and a lemma establishes that any such relation is contained in genuine interchangeability. The same treatment is applied to landing merely near an already-established equivalence rather than inside the relation, and the two relaxations are combined. Afterwards the actual proofs — commutativity and associativity of parallel composition, the expansion law, the preservation of equivalence by recursive definition — each exhibit a small, obvious relation, and the heavy lifting is amortized across all of them.

The general principle is that the shape of a proof obligation is itself a design artifact, tunable independently of the theorem. When you notice that the same tedious bookkeeping recurs in every proof, that bookkeeping is a candidate to be discharged once as a general lemma about your method rather than repeated. This is the same instinct as pulling a common preamble out of many functions, applied to arguments rather than code, and it changes what is feasible: the associativity proof requires case analysis over dozens of derivation shapes, and it is only tractable because each case has to establish something small.

The practical form for a programmer is to distrust the first invariant that looks right and fails to be preserved. Before strengthening the invariant into something unmaintainable, ask whether the failure is uniform — always off by the same kind of wrapping, always up to some equivalence you already trust. If so, prove the weakening once, name it, and use it everywhere. The theorem you wanted stays intact; only the price of establishing it drops.

**Source:** [A Calculus of Mobile Processes, I and II](../works/a-calculus-of-mobile-processes.md) — Part II's development of simulation up to restriction, up to bisimilarity, and their combination, each with a lemma showing containment in bisimilarity, and the subsequent use of those notions in the proofs of the composition laws and of preservation under recursive definition.
