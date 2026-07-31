---
type: lesson
title: "To prove something impossible, count what can be remembered against what must be distinguished"
figure: stearns
works: [on-the-computational-complexity-of-algorithms]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---
# To prove something impossible, count what can be remembered against what must be distinguished

**Lesson:** The reliable way to show a mechanism cannot meet a requirement is to compare two counts. On one side, the number of situations the mechanism is capable of telling apart within the resources it has left — a product of its internal states and the amount of storage its heads can physically reach in the remaining steps, which grows exponentially in those steps but with a modest base determined entirely by the mechanism's own parameters. On the other side, the number of situations the requirement forces it to treat differently: build a family of possible pasts such that any two of them demand different answers to some future question, and count the family. If the second count outgrows the first, no amount of ingenuity inside the mechanism matters, because the argument never mentioned how the mechanism works. The classic shape is a doubly exponential family of obligations against a singly exponential capacity, and the gap is so wide that the constants are irrelevant.

What makes the argument work is the construction of the obligation family, and this is where the real craft lives. You need a set of pasts, an inexpensive continuation that interrogates the past, and a proof that distinct members of the set demand distinct outputs for some continuation. Taking the pasts to be arbitrary subsets of something, rather than arbitrary members of it, is what buys the extra exponential — the mechanism must be prepared to answer a membership question about a set it was never allowed to store, and there are vastly more sets than elements. The counting then does the rest mechanically.

There is a strategic point wrapped around the technique. Impossibility is much easier to establish for a formulation in which you get to dictate what the mechanism is obliged to do than for one in which the mechanism merely has to produce some object. When your job is to construct a hard object, you are fighting for existence; when your job is to construct hard demands, you are choosing the battlefield, and the adversarial freedom is entirely yours. So when a lower bound resists, look for a reformulation of the same question as a recognition or response obligation — one where you specify the queries — and attack that instead. Reformulating to gain adversarial control over the requirement is often the whole difference between an open problem and a two-paragraph proof.

**Source:** [On the Computational Complexity of Algorithms](../works/on-the-computational-complexity-of-algorithms.md) — the impossibility example in the generalizations section, which bounds the number of past input histories a machine can distinguish in a given number of further steps by its states, bands and reachable squares, sets that against the number of subsets of words of a given length, and derives a contradiction; together with the following remark that recognition problems make impossibility results easier to obtain because the researcher controls what the machine is required to do.
