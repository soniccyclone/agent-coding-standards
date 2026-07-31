---
type: lesson
title: "The search method you commit to gets a veto over every component"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# The search method you commit to gets a veto over every component

**Lesson:** Choosing how you will search for a good configuration is usually treated as a decision made after the system is designed, applied to whatever design you ended up with. It runs the other way. A search procedure works by exploiting some property of the space it moves through, and every component of the system must possess that property or the search cannot see past it. Commit to a method that follows local slope, and every piece must have a slope — which immediately disqualifies the piece that expresses the behaviour you actually wanted, if that behaviour is a clean yes-or-no decision. The decision function is flat everywhere except at one point where it is vertical, so the search learns nothing from it anywhere, and cannot pass through it to reach the parts behind.

So the component gets replaced with a smoothed approximation of itself: something that behaves nearly like the decision you wanted at the extremes, but transitions gradually rather than abruptly, and therefore reports a usable direction everywhere. This is a genuine concession — the smoothed version is not what you meant, its outputs are neither of the two answers you wanted, and downstream reasoning now has to accommodate values in between. You accept it because the alternative is a system that cannot be fitted at all, which is worse than one that has been fitted approximately.

Having accepted the concession, notice that the requirements it imposes are specific enough to be checked, not vague preferences. The property the search reads must exist everywhere the search will go, must not shrink toward nothing over the range of values the component will actually see, and must not blow up. The middle requirement is the one that catches people, because a component can be perfectly well behaved on paper and still starve the search: if its response flattens out over most of its operating range, every step the search takes there is negligible, and the process appears to be stuck for reasons nothing in the code suggests. That failure is silent, it is a property of the component's shape rather than a bug, and it can only be diagnosed by someone who knows the search's requirement and thought to check it.

Generalised: whenever you pick an automated procedure to explore a space of designs — a solver, an optimiser, a search over configurations, a scheduler — write down what that procedure needs from the things it manipulates, and treat that list as a design constraint on every part of the system, not as a compatibility problem to sort out later. The parts that violate it will not announce themselves; they will just make the procedure quietly ineffective.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the activation-functions section of the neural-nets chapter, which explains that gradient descent forces the choice of node output function, lists the three properties such a function must have (differentiable almost everywhere, derivative that does not saturate over the expected input range, derivative that does not explode), and rules out the step function on the grounds that its derivative is zero everywhere except at the origin, replacing it with the S-shaped logistic function.
