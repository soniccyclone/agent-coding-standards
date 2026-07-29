---
type: lesson
title: "State an interface as classes separated by a margin, and error stops accumulating across the boundary"
figure: turing
works: [proposed-electronic-calculator-ace-report]
axes: [verifiability, hardware-affinity, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# State an interface as classes separated by a margin, and error stops accumulating across the boundary

**Lesson:** A contract that names exact values cannot be honoured by anything physical, and a designer who insists on exact values ends up either lying or paralyzed. The move that rescues the situation is to weaken every clause from a point to a class: not "this input produces this output" but "any input in this well-separated class produces an output in that well-separated class," with the classes required to stay a stated distance apart. The weakening looks like a concession and is actually the source of all the strength, because a signal that is merely inside its class can be pushed back to the centre of that class, and once you can do that at every hop, degradation stops compounding no matter how many hops there are.

That single property is what makes an unreliable, continuously-decaying medium usable as memory. If the states were merely distinguishable-in-principle you would only be able to bound the error over one pass; because they are separated by a margin you can restore at each pass and the number of passes drops out of the correctness argument entirely. The margin is therefore not slack to be trimmed but the thing being bought, and it should be sized from a stated tolerable failure rate, with every loss along the path tallied so you know exactly how much headroom remains rather than hoping.

The second payoff is organizational, and it is the one people underrate. Once the contract is stated in classes with margin, the people implementing the substrate and the people reasoning on top of it can each work at full speed without auditing the other's assumptions — one side owes "outputs land in the right class," the other side may assume nothing finer. Timing works the same way: rather than pretending propagation is instantaneous, accept the real delays and publish a schedule everyone designs against. A programmer who internalizes this stops writing interfaces in terms of exact observed behaviour, states tolerances and the normalization step that enforces them, and treats every layer boundary as a place to re-standardize rather than a place to pass imprecision along.

**Source:** [Proposed Electronic Calculator (Report on the ACE)](../works/proposed-electronic-calculator-ace-report.md) — the circuit-elements chapter, which replaces exact input/output claims with classes required to be a finite distance apart and calls this a division of labour between mathematicians and engineers, together with the storage chapter's account of reshaping each recirculating signal to the nearest ideal form and the delay-line chapter's margin computed from a target error probability.
