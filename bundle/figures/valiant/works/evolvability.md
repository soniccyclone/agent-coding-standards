---
type: work
title: "Evolvability"
figure: valiant
description: Valiant models Darwinian evolution as a restricted, resource-bounded form of machine learning, asking which target behaviors a population can converge toward using only aggregate mutation-and-selection feedback rather than the richer labeled-example feedback that PAC learning assumes. He shows evolvability under this model is strictly weaker than PAC learnability, giving a precise complexity-theoretic account of what natural selection can plausibly discover in a polynomial number of generations. It's an unusual case of turning a question from biology into an algorithmic complexity result with an actual proof.
subdomains: [algorithms-and-complexity]
year: 2009
url: https://people.seas.harvard.edu/~valiant/evolvability-2008.pdf
survey_pages: 19
survey_text_layer: full
survey_fetch_mb: 0
extraction: complete
access: public
host: self-archived
tags: [work]
---

# Evolvability

**Venue/year:** Journal of the ACM, 56(1), 2009, article 3.
**Source:** https://people.seas.harvard.edu/~valiant/evolvability-2008.pdf — self-archived PDF on Leslie Valiant's own Harvard faculty page.

## Lessons
- [Stop speculating about the shape of the search space and classify which objectives induce a navigable one](../lessons/ask-which-objectives-induce-a-navigable-space-not-what-spaces-look-like.md)
- [An optimizer that sees only a scalar score is strictly weaker than one that sees the cases, and the gap is provable](../lessons/a-scalar-score-is-a-weaker-signal-than-labelled-cases-and-provably-so.md)
- [Require convergence from any starting state, then close the back door that would let a single step fake a restart](../lessons/require-convergence-from-any-state-and-close-the-back-door-that-would-fake-it.md)
- [Place a new model inside an established one, and push the containment as tight as it will go](../lessons/place-a-new-model-inside-an-old-one-and-make-the-containment-as-tight-as-you-can.md)
- [Engineer progress to arrive in quanta bigger than your measurement error, and give the comparator a neutral band](../lessons/engineer-progress-into-quanta-larger-than-your-measurement-error.md)
- [The improving path may have to run through states holding pieces that belong nowhere in the answer](../lessons/the-improving-path-may-run-through-states-that-contain-nothing-of-the-answer.md)
- [Carry an inactive record alongside the active state, because which moves are reachable depends on what the state remembers](../lessons/carry-an-inactive-record-because-reachable-moves-depend-on-what-the-state-remembers.md)
- [No step may be justified by a later payoff, so complexity has to arrive as a ladder of targets each worth reaching on its own](../lessons/no-step-may-be-justified-by-a-later-payoff.md)
- [Name the resource your guarantee assumes but cannot control, then notice that starving it is itself a mechanism](../lessons/name-the-resource-your-guarantee-assumes-but-does-not-control.md)
- [Classify which kind of barrier you hit, because only some kinds can be engineered around](../lessons/classify-which-kind-of-barrier-you-hit-before-deciding-what-to-change.md)
- [Choose a vocabulary wide enough to say what you need and narrow enough to search, and accept the modularity that follows](../lessons/choose-a-vocabulary-wide-enough-to-say-it-and-narrow-enough-to-search.md)
