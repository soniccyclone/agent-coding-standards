---
type: lesson
title: "Bill the unavoidable blowup to the input dimension that stays small in practice"
figure: pnueli
works: [on-the-synthesis-of-a-reactive-module]
axes: [verifiability]
subdomains: [algorithms-and-complexity, formal-methods-and-verification]
tags: [lesson]
---

# Bill the unavoidable blowup to the input dimension that stays small in practice

**Lesson:** Cost is normally quoted against one lumped measure of how big the input is, and that convention hides a design decision. Most real inputs have several independent dimensions, and when they do, the same problem admits several incomparable cost profiles that no single-number bound can rank. The profile you want is the one that is cheap in the dimension your actual instances grow along and expensive only in a dimension that stays bounded for structural reasons. Nothing about the underlying hardness is being evaded; the hardness is simply being charged to a different account, and which account it lands in decides whether the method is usable.

Concretely in this work, the objects being tested carry two independent sizes: how many internal configurations they have, and how many acceptance conditions govern their infinite behavior. Earlier methods paid against the two combined, so growth in either was equally punishing. The replacement pays polynomially in configurations and exponentially in acceptance conditions. That is only an improvement because of a fact about provenance rather than a fact about the problem: the objects that arise from translating a written requirement have a great many configurations and very few acceptance conditions, since one grows with the exponential unfolding of the formula and the other tracks its handful of eventualities. Knowing where your instances come from is what makes the reallocation a win instead of a wash.

The same paper carries a companion lesson about how to read a bad bound. Its overall procedure is doubly exponential in the length of the requirement, and it says so plainly while still arguing the framework is worth adopting. Both halves are correct. A worst-case bound describes the adversarial instance, not the instances you will hand it, and it says nothing about the value of the conceptual frame the procedure sits inside. A frame whose full automation is out of reach can still be the right way to organize the work, because it fixes what counts as a correct derivation and lets machinery take over pieces of the job incrementally as it improves.

The transferable habit has two parts. Before optimizing anything, decompose the input's size into the dimensions that can vary independently, then measure which of them your real workload actually grows in — the answer is frequently not the one the standard bound is stated against. And when a complexity result looks disqualifying, ask which dimension it is exponential in and whether your instances are constrained in that dimension by how they are generated. Refusing to accept a one-parameter cost claim as a verdict on feasibility is not optimism, it is a demand for the measurement that would settle the matter.

**Source:** [On the Synthesis of a Reactive Module](../works/on-the-synthesis-of-a-reactive-module.md) — the introduction's contrast between prior emptiness-checking costs and the new bound, with its explicit note about why separating the two size parameters matters for the automata that specifications produce; the emptiness section's restatement of that reasoning; and the frank statement of the overall doubly exponential cost alongside the argument that the derivation framework earns its place regardless.
