---
type: lesson
title: "Record order-independence at the moment you know it, because it cannot be recovered later"
figure: jones
works: [development-methods-for-computer-programs-including-a-notion-of-interference]
axes: [parallelizability, expressiveness]
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
tags: [lesson]
---
# Record order-independence at the moment you know it, because it cannot be recovered later

**Lesson:** When a design calls for every member of a collection to be processed, the designer usually knows whether the order matters. The notation then throws that knowledge away: the available construct walks an index upward, so a sequence is committed to, and nothing in the resulting text distinguishes an order that the problem demanded from an order the language insisted on. Recovering the distinction afterwards is disproportionately hard — it requires proving that no iteration's effect can be observed by another, over code that has had every opportunity to develop accidental dependencies in the meantime. The information was free at design time and expensive forever after.

The remedy is to have a way of saying "these, in any order" and to reach for it whenever it is true, before writing anything that could quietly rely on the sequence. The obligation is different in kind from the ordered case and worth understanding on its own terms: instead of a relation carried forward from step to step, what you must establish is that processing the remainder of the collection in any order, after any one member has been handled, yields the same overall effect. That obligation is what a compiler, a scheduler, or a later maintainer needs and cannot infer.

The general point is larger than iteration. Any time a notation forces a decision the problem did not require, the resulting artifact contains a commitment nobody made, and downstream anyone who wants the freedom back has to reconstruct which commitments were real. Freedom, once discarded, does not survive in the text. This is a good reason to judge notation by what it lets you leave unsaid, and a good reason to prefer, at every design step, the construct that decides the least.

**Source:** [Development Methods for Computer Programs including a Notion of Interference](../works/development-methods-for-computer-programs-including-a-notion-of-interference.md) — the arbitrary-order iteration rule introduced in the proof-rules chapter, with its stated motivation that recording such freedom matters because potential reordering or parallelism is very hard to detect afterwards in programs where the commitment to order was forced by the language rather than by the problem; and its worked use on the set-difference example.
