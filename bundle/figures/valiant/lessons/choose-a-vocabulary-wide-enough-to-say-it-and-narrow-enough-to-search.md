---
type: lesson
title: "Choose a vocabulary wide enough to say what you need and narrow enough to search, and accept the modularity that follows"
figure: valiant
works: [evolvability]
axes: [expressiveness, cognitive-load, primitive-count]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity]
tags: [lesson]
---
# Choose a vocabulary wide enough to say what you need and narrow enough to search, and accept the modularity that follows

**Lesson:** The set of descriptions an adaptive process is allowed to consider is a design decision with two opposing failure modes, and there is no setting that avoids both. Too restrictive, and the behaviors you actually need cannot be expressed at all, so no amount of successful searching helps. Too permissive, and the process cannot navigate: the space is large enough that improving moves stop being findable, and a shifting environment leaves it stranded. Expressiveness and navigability trade against each other directly, and the good choice is not the maximum of either. It is the narrowest vocabulary that still covers the behaviors you must reach — a bound from below by requirements, from above by searchability.

A related decision is usually made unconsciously: the space of descriptions the process searches need not coincide with the space of behaviors you are aiming at. Widening it can help, by supplying stepping stones — intermediate descriptions that no one wants as answers but that make a path exist. Narrowing it can also help, if a cruder family yields adequate approximations while being far easier to traverse. So there are two separate knobs, the family of targets you hold yourself responsible for and the family of candidates you are willing to consider, and holding them equal by default forfeits both moves.

The structural consequence of accepting a narrow vocabulary is the part usually presented as a virtue on its own terms. If each stage of construction can only acquire a member of a limited family, then anything elaborate must be assembled from many small pieces, each individually within that family, each with an identifiable job — which is to say the result is modular whether or not anyone valued modularity. Modularity is what a bounded acquisition mechanism forces, not an aesthetic imposed on top of it. That reframing is worth having when arguing about architecture, because it replaces taste with a constraint: the question is not whether modular decomposition is nicer, but whether the process building the system can acquire anything larger than a module at a time. When it cannot, the decomposition is compulsory, and effort spent debating it is better spent choosing the vocabulary each module is written in.

**Source:** [Evolvability](../works/evolvability.md) — section 6's discussion of the choice of the class of functions a genome's mechanism can acquire, which fails if too restrictive because the complex functions needed are then inexpressible and fails if too extensive because navigating among its members becomes infeasible as conditions change; the observation in section 3 that the representation class may differ from the class of ideal functions, with a richer representation possibly helping and a weaker one possibly giving adequate approximations with better properties for convergence; and section 6's argument that if what can be acquired is severely constrained then evolved systems are thereby constrained to consist of many identifiable small modules, making modularity a consequence of the limitation.
