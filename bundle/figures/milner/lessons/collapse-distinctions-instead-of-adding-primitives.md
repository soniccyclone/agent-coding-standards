---
type: lesson
title: "When a new capability threatens to multiply your primitives, collapse a distinction instead"
figure: milner
works: [a-calculus-of-mobile-processes]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# When a new capability threatens to multiply your primitives, collapse a distinction instead

**Lesson:** Adding a capability to a formalism usually means adding machinery, and the machinery multiplies. Here the capability is letting a running system rearrange who can talk to whom, which naively requires variables ranging over channel identifiers on top of the variables already ranging over data, on top of the channels themselves — three categories of thing where there were two, with binding rules and substitution behavior needed for each. The move taken instead is subtraction: erase the distinction between channel, variable, and datum entirely. There is one sort of atom, and the only content a message can carry is one of these atoms. What remains is two classes of entity — atoms and processes — and a calculus whose grammar fits on one line.

The reason this is more than aesthetic economy is that the collapse makes the model more expressive, not less. Because the thing received can be used as a channel, a process's set of possible interlocutors is genuinely dynamic; because there is no separate category of value, the interesting question of what computation over structured data even means gets answered inside the calculus rather than assumed alongside it, with compound data represented as processes that hand out their pieces on request. A design that had kept the categories apart would have had to build data in as a second, parallel theory.

The collapse is not free, and the honest part of the design is that it charges the bill openly rather than hiding it. Once atoms are all one kind of thing, the notion of two processes being interchangeable stops being stable under renaming — two behaviors that agree while a pair of atoms are distinct can diverge when those atoms turn out to be the same. That is a real cost, paid in a more delicate theory of equality, and it is accepted because the alternative was a permanently bifurcated calculus.

A designer who works this way, on being handed a requirement that seems to demand a third kind of thing, first looks for the two existing kinds that could be identified. Unification often makes the hard case visible instead of leaving it distributed across special forms — and a hard case you can see is one you can develop a theory for.

**Source:** [A Calculus of Mobile Processes, I and II](../works/a-calculus-of-mobile-processes.md) — Part I's introduction and the discussion following the grammar, where the anticipated over-richness of primitives is named and then avoided by identifying links, variables and values; the consequence for equality surfaces in Part I's algebraic section.
