---
type: lesson
title: "When an ideal is unbuildable, keep its interface and make the gap a parameter"
figure: schneider
works: [byzantine-generals-in-action-implementing-fail-stop-processors]
axes: [cognitive-load, verifiability, hardware-affinity]
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# When an ideal is unbuildable, keep its interface and make the gap a parameter

Some abstractions are strictly unachievable rather than merely hard. A component guaranteed never to expose corrupted state, and guaranteed to advertise its own death, cannot be built from a finite amount of hardware: enough failures will take out the very machinery that does the detecting, and after that nothing constrains the behavior. The tempting responses are both bad. Abandoning the abstraction throws away the reasoning leverage it gave every design above it. Claiming it anyway makes every design above it wrong in a way that surfaces only in the field, under exactly the conditions where being wrong matters most.

The third option is to keep the interface exactly as the ideal specified it and attach a single number: this component behaves as the ideal describes unless more than *k* of its internal parts fail, and outside that budget makes no promise at all. Users above the boundary continue to reason in the clean model, unchanged, because within budget the clean model is literally true. Everything that leaks is compressed into one parameter they can see, argue about, and trade against cost. Turn the parameter up and the implementation converges toward the ideal; turn it down and it gets cheap. The abstraction stops being a binary claim and becomes a dial.

What makes this work, rather than being a euphemism for "it mostly works," is that the escape clause is stated in terms of a *countable* event inside the implementation, not in terms of vague reliability. The consumer of the abstraction can compose these numbers, reason about whether the budget is plausible for their deployment, and know precisely which conclusions to stop drawing when it is exceeded. Compare that with the usual situation, where an implementation approximates an ideal by an unstated margin and every user silently assumes the margin is zero.

The transferable move: when you find yourself about to weaken an interface because the strong version cannot be implemented, try instead to hold the interface fixed and find the parameter that measures how far the implementation may be pushed before the interface's promises evaporate. Publish that parameter as part of the contract. It is a far more useful thing to hand a caller than a hedged interface, because it preserves their ability to reason simply while telling them exactly where simple reasoning ends.

**Source:** [Byzantine Generals in Action: Implementing Fail-Stop Processors](../works/byzantine-generals-in-action-implementing-fail-stop-processors.md) — the introduction's impossibility argument about finite hardware and error-detection facilities, and the resulting definition of a parameterized family of approximations that converges on the ideal as the parameter grows.
