---
type: lesson
title: "A compact description says nothing about the cost of running it"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# A compact description says nothing about the cost of running it

**Lesson:** Two numbers get conflated constantly: how much it takes to write down what a system is, and how much it takes to run it once. They are independent quantities, and a design that dramatically shrinks the first can leave the second entirely untouched or even raise it. The confusion is easy to fall into because the same design decision often reduces both — and easy to be badly hurt by when it does not, because the reasoning that justified the design ("far fewer parameters, therefore far less work") was never actually about work.

The clean example of the split is any construct that describes one rule and applies it at every position of a large input. Its description is a single small rule; its execution is that rule evaluated once per position, which can be many thousands of evaluations. The description shrank because you shared; the execution did not shrink at all, because sharing a rule does not mean applying it fewer times. So the design's benefit is entirely on the side of what has to be determined and stored — which is a real benefit, since it is the one that governs how much evidence you need and how much you can hold in memory — and it should be claimed as that benefit only.

Getting this right matters most in planning, where the two numbers answer different questions. Description size tells you about the cost of building, transmitting, storing, and versioning the thing, and about how much data you need to pin it down. Execution cost tells you what the service will cost per request, what hardware it needs, and what its latency will be. A conversation that mixes them produces the familiar surprise of a compact artefact that is expensive to serve, which nobody predicted because everyone had been quoting the compact number.

The general discipline is to state both figures whenever describing a system, and to name which one any claimed improvement moved. "Far fewer parameters" and "far less computation" are different sentences. So are "small binary" and "fast startup", "concise query" and "cheap query", "short specification" and "efficient implementation" — in each pair, the first is a property of the text and the second of the process, and only measurement connects them.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the "how many nodes in a convolutional layer?" aside in the convolutional-networks chapter, which contrasts the small number of nodes whose weights are determined during training with the fact that at application time each filter is evaluated at every one of tens of thousands of pixel positions, and states as the key point that a compact representation does not imply cheap application.
