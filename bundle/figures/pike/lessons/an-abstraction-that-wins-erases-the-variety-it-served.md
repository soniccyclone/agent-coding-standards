---
type: lesson
title: "An abstraction that wins erases the variety it served"
figure: pike
works: [systems-software-research-is-irrelevant]
axes: [hardware-affinity, expressiveness, primitive-count]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# An abstraction that wins erases the variety it served

**Lesson:** A layer built to absorb differences between many underlying things makes those things interchangeable, and once they are interchangeable the cheapest one takes the whole market. The variety the layer existed to manage then disappears — not because anyone decided it should, but because the layer removed the reason to maintain it. The abstraction ends up sitting on a single implementation, and the property it was praised for becomes untestable and eventually vestigial: nobody exercises the other paths, so nobody knows whether they still work, so they don't.

This is worth internalizing because it reverses the usual intuition about how portability layers and their kin fail. The failure mode is not that the abstraction proves too leaky to cover the cases; it is that it covers them so well that only one case survives. And the loss is real, because underlying diversity was also the supply of problems that produced new ideas in the first place. When there was one machine architecture per vendor, making things work across them was where the interesting questions lived; when there is effectively one, that whole source of questions is gone, and with it a source of designs nobody thought to want.

The practical reading is not "avoid abstracting" — the layer usually earned its keep at the time. It is that you should know which kind of abstraction you have. If it exists to hide variation, its own success is a clock running against it: expect the day when the second implementation is hypothetical, and decide then whether to keep paying for generality nobody uses or to collapse it deliberately and honestly. Carrying a variation-hiding layer that has only ever seen one variant is a cost with no benefit, and pretending otherwise misleads everyone who reads the code. A programmer who believes this asks, of every compatibility layer, how many live implementations sit under it today — and treats "one" as a decision to make rather than a fact to leave alone.

**Source:** [Systems Software Research is Irrelevant](../works/systems-software-research-is-irrelevant.md) — the PC and Unix slides, which argue that portability led to ubiquity, that ubiquity made architecture stop mattering, and that a major source of interesting problems vanished as a result.
