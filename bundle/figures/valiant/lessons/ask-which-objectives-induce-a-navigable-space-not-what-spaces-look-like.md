---
type: lesson
title: "Stop speculating about the shape of the search space and classify which objectives induce a navigable one"
figure: valiant
works: [evolvability]
axes: [cognitive-load, verifiability]
subdomains: [algorithms-and-complexity, foundations-of-computation]
tags: [lesson]
---
# Stop speculating about the shape of the search space and classify which objectives induce a navigable one

**Lesson:** Arguments about whether incremental improvement can reach a complicated goal usually stall on an empirical question nobody can settle: what does the space of candidates actually look like, how rugged is it, how many dead ends does it have. That question is unanswerable in general and the answers people offer are assumptions dressed as observations. The reframing that makes progress is to notice that the space is not an independent object. It is induced — jointly by the objective you are measuring against and by the distribution of situations the measurement is taken over. So instead of asking what such spaces are like, ask which objectives give rise to spaces that a bounded incremental process can traverse. That is a classification problem with provable answers, and it replaces speculation with theorems.

The reversal has real consequences for how you argue. A claim that some goal cannot be reached incrementally now has to be a claim about the goal, not a hand-wave about the terrain, and it can be proved or refuted. A claim that a goal *is* reachable becomes a construction: exhibit the candidate space, the local moves, and the argument that improving moves are always available until you are close. And the results come out asymmetric in an informative way — some goals with substantial internal structure turn out to be reachable, while others that look no more complicated are provably out of reach — which means the intuition that complexity of the goal predicts reachability is simply wrong. Reachability is its own property.

The habit worth taking away is to treat "can this be found by local improvement" as a question with a domain, and to make the domain explicit before answering. Two systems doing hill-climbing against different objectives are not doing the same thing at different difficulty; they may be on opposite sides of a hard boundary. And when a target is on the wrong side, no amount of tuning the local moves rescues it, so the effort belongs in choosing or decomposing the target instead. There is a second payoff, easy to miss: a theory that classifies targets makes predictions about which targets will be found in the wild. If a class is provably unreachable, then a process that reached its goals this way was not aiming at anything in that class, and that is a falsifiable statement about the systems you observe rather than a fact about your model.

**Source:** [Evolvability](../works/evolvability.md) — the remark in section 2 following the definition of performance, which declines to speculate about the fitness landscapes found in the world and instead asks which ideal functions give rise to landscapes that permit convergence, together with section 4's contrasting results for parity functions and section 5's for monotone conjunctions, and the observation that the unreachability of a class is exactly the theory's prediction that nothing was aiming at it.
