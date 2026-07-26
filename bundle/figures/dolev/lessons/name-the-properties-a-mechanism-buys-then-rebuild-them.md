---
type: lesson
title: "A mechanism you depend on is a bundle of properties; name them and you may not need the mechanism"
figure: dolev
works: [polynomial-algorithms-for-multiple-processor-agreement]
axes: [primitive-count, verifiability, cognitive-load]
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
tags: [lesson]
---
# A mechanism you depend on is a bundle of properties; name them and you may not need the mechanism

**Lesson:** When a component appears indispensable, that appearance is usually an artifact of never having asked what the surrounding correctness argument actually consumes from it. Unforgeable signatures looked like the thing that made fault-tolerant agreement tractable, and every protocol that used them inherited the assumption wholesale. The productive move is to interrogate the dependency: write down, as separate propositions, each guarantee the proof leans on. Here the list came out at two items. Nobody can put into circulation a value the originator never emitted. And a value arriving at a given point in the exchange carries evidence that it already travelled through some number of distinct, independent parties over prior steps.

Once the second guarantee is stated in that form, it stops looking cryptographic. It is a claim about corroboration counts, and corroboration counts can be manufactured out of nothing but message passing and arithmetic on the fault budget: require that enough distinct parties vouch for a claim before it is treated as established, and require a chain of distinct vouchers before it is treated as settled. What the signature scheme provided as a physical impossibility, thresholds provide as a counting impossibility. The payoff is not aesthetic. It removes a whole trust assumption and a whole implementation layer from the system while keeping the cost polynomial, which the previous generation of unauthenticated protocols could not do.

The habit worth stealing is the audit itself, and it cuts both ways. Before treating a dependency as a primitive, enumerate the properties your argument uses; the list is nearly always shorter and weaker than the component, and the slack is where cheaper or more portable implementations live. Conversely, a team that imports a heavy mechanism without ever writing that list down cannot say what breaks when the mechanism is misconfigured, cannot substitute anything for it, and cannot tell whether a proposed replacement is adequate. Unexamined dependency is not just cost; it is an unbounded liability, because nobody knows the shape of what would have to be replaced.

**Source:** [Polynomial Algorithms for Multiple Processor Agreement](../works/polynomial-algorithms-for-multiple-processor-agreement.md) — the pivot into the unauthenticated construction, where the paper first factors authentication into the two jobs it performs for the earlier proofs and then supplies substitutes for both via the two corroboration thresholds and the chain-of-relayers condition.
