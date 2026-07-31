---
type: lesson
title: "Build under randomized loss so nothing can depend on any one part"
figure: ullman
works: [mining-of-massive-datasets]
axes: [verifiability, parallelizability]
subdomains: [software-engineering-and-architecture, distributed-systems-and-concurrency]
tags: [lesson]
---
# Build under randomized loss so nothing can depend on any one part

**Lesson:** A system assembled under ideal conditions will develop dependencies on the presence of every part, because there is nothing to stop it. Some of those dependencies are load-bearing and some are accidents of assembly, and from the outside they are indistinguishable — until a part goes missing and you find out which kind you had. The intervention that prevents this is to remove parts, at random, continuously, throughout construction. Anything that was relying on a specific part being present cannot survive the process, so what you are left with is what works without any particular part. The resilience is not tested in afterwards; it is a property the construction procedure could not have produced without.

The randomisation is doing something more than stress testing. Because a different subset is missing each round, the system is effectively being assembled many times over in many configurations, and the final artefact behaves like a consensus over all of them rather than like any one. That is the same benefit you would get from building many independent variants and combining their outputs, obtained without paying for many variants — one of the better deals available, and worth reaching for whenever the alternative is maintaining several near-duplicate systems in order to average them.

The catch is at the boundary between construction and use, and it is easy to miss. If you build under conditions where some fraction of the parts are absent and then deploy with all of them present, the deployed system is not the one you built — every downstream consumer now receives more contribution than it ever did during assembly. Something has to be scaled to compensate, and the correction factor is determined by the removal rate you chose. Generally: any deliberate distortion applied during construction creates an obligation to state the inverse adjustment for the deployed configuration, and forgetting it produces a system that is subtly miscalibrated everywhere rather than broken anywhere.

The pattern transfers to operations directly. Killing instances on purpose, injecting latency and errors into internal calls, and rotating credentials aggressively are all the same move: make the failure ordinary during construction so that no accidental dependence on its absence can form. And the same caveat applies — a system operated permanently under injected fault is not the same system as one running clean, so the difference between the two conditions has to be accounted for rather than assumed away.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the dropout section of the regularization chapter, which deletes a random fraction of hidden nodes and their edges for each minibatch, restores them and deletes a different subset for the next, explains the benefit as making a single network behave like a collection of networks that would otherwise have to be trained separately and combined by voting, and notes that the weights on outgoing edges must be scaled by the dropout rate once the full network is used, since it has more nodes than any network used during training.
