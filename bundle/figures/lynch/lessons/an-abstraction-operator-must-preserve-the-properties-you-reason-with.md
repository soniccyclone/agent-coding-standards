---
type: lesson
title: "Judge a composition operator by whether your reasoning survives it in both directions"
figure: lynch
works: [an-introduction-to-input-output-automata]
axes: [cognitive-load, parallelizability, verifiability]
subdomains: [distributed-systems-and-concurrency, formal-methods-and-verification, software-engineering-and-architecture]
tags: [lesson]
---
# Judge a composition operator by whether your reasoning survives it in both directions

**Lesson:** Most of the technical content in this model is not the automaton definition; it is a run of results establishing that assembling components does not disturb the facts you wanted to use. Whatever the assembled system can be observed doing projects down onto something each part could have done alone, and conversely, individually possible behaviors that agree on their shared actions can be pasted back up into a behavior of the whole. Scheduling guarantees survive too: the notion of giving each primitive part its turn is defined so that a part's turn-taking obligations remain intact after it is embedded in something larger. None of this is automatic — the paper is explicit that the analogous facts fail in other formalisms — and it is the entire reason a proof about a big system can be assembled from proofs about small ones.

The design principle worth extracting is that a composition operator's value lies in what it preserves, not in what it expresses. An operator that can build any topology you like but under which a component's established properties may evaporate has bought you nothing: every claim has to be re-established at every level, and the cost of understanding the system grows with the system rather than with its largest component. The projection direction gives you decomposition of any obligation into per-part obligations. The pasting direction gives you the ability to construct system behaviors from component behaviors, which is what you need to show something is possible rather than merely permitted. You want both, and demanding both restricts which operators you are allowed to define — which is why the model imposes compatibility conditions on what may be combined at all rather than allowing arbitrary wiring.

The sharpest illustration is the decision not to conceal inter-component communication automatically when components are combined. Hiding is available, but only as a separate operation you invoke deliberately. The reason is that automatic hiding would make the result depend on the order in which you grouped the parts: an action shared by three components is a broadcast to all of them, but concealing it while combining the first two would silently demote it to a private matter and change the meaning of adding the third. Convenience would have cost associativity, and associativity is precisely what lets you reason about a subsystem first and then extend the argument.

The transferable habit is to treat every "and then we wrap it" boundary in a system with suspicion until you can state what crosses it and what is preserved across it. Layers that quietly erase information — a wrapper that swallows an error class, a facade that serializes what was concurrent, a module system that renames what was shared — do not merely lose fidelity. They invalidate whatever you had established underneath, and force the reasoning to start over at the new level.

**Source:** [An Introduction to Input/Output Automata](../works/an-introduction-to-input-output-automata.md) — the composition section's paired projection and pasting propositions, their fairness-preserving counterparts, and the accompanying justification for making the hiding of shared actions a separate explicit operator.
