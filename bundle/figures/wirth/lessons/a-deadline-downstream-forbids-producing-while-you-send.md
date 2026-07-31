---
type: lesson
title: "A deadline downstream forbids producing while you send"
figure: wirth
works: [project-oberon]
axes: [hardware-affinity, verifiability, parallelizability]
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
tags: [lesson]
---
# A deadline downstream forbids producing while you send

**Lesson:** Overlapping generation with delivery is the default instinct and usually the right one: start emitting as soon as the first unit exists, and let the two activities share the elapsed time. That instinct silently assumes the consumer will wait if you are late. Once the consumer is a mechanism with its own clock — one that will take a unit every fixed interval whether or not you have produced it, and for which arriving late is not slow but wrong — the assumption is gone, and the pipeline you were counting on becomes a liability. Every unit you have not yet computed is now a deadline you might miss, and the failure is not a stall but a corrupted result.

The correct response is to stop overlapping. Compute the whole thing first, into a form from which delivery is a pure transfer requiring no thought, and only then begin. This looks like a regression — you have serialised two phases that could have run together and increased the latency to first output by the whole production time — but it converts a distributed timing property, which you would have had to establish for the worst case of every code path in the producer, into a local one: the delivery loop must sustain a fixed rate while doing nothing but moving bytes, which is a claim you can inspect by reading a short piece of code. Buying a much easier proof with some latency is a good trade, and refusing to make it explicitly is how systems acquire timing bugs that appear only under load, only sometimes, and only in the field.

The generalisation is that a hard rate on one side of an interface propagates backwards as a completeness requirement on the other. Whenever you find a consumer that cannot be made to wait, look immediately upstream and ask what work still remains to be done during the transfer; whatever you find there must either be moved earlier or proven to fit in the interval, and moving it earlier is nearly always cheaper than proving it. This is also the point at which to notice that the rate itself is a design parameter you may be able to negotiate. The reason the consumer cannot wait is usually that the two ends share no signal for pausing — and if the medium could carry such a signal, or the unit size could be reduced until re-establishing agreement is cheap, the whole constraint dissolves. Materialising everything in advance is the right answer given the constraint; asking whether the constraint was chosen is the better question to ask first.

**Source:** [Project Oberon](../works/project-oberon.md) — section 9.3's remark that, because the synchronous line's clock is fixed and one byte must be sent every fixed interval, computation of the byte sequence and transmission of the packet cannot be interleaved, so the data of an entire packet must be ready before transmission is initiated; together with the surrounding discussion of why the packet length is bounded by clock accuracy when the clock is not transmitted alongside the data.
