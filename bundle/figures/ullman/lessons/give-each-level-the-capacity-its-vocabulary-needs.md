---
type: lesson
title: "Give each level the capacity its vocabulary needs, not an equal share"
figure: ullman
works: [mining-of-massive-datasets]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [software-engineering-and-architecture, algorithms-and-complexity, programming-languages-and-semantics]
tags: [lesson]
---
# Give each level the capacity its vocabulary needs, not an equal share

**Lesson:** In a system built as a stack of levels, where each level describes its input in terms of things the level below it found, the amount of room each level needs is not the same. The bottom level has a short vocabulary. There are only so many distinct primitive features in any domain, and they are shared by everything: a handful of edge orientations, a handful of token classes, a handful of event types. Levels above compose those primitives, and the number of distinct compositions grows with every level, because composition multiplies. Allocating each level the same capacity therefore starves the top and wastes the bottom, and the waste is worse than it looks: capacity nobody needs at the bottom does not sit idle, it gets used to memorise particulars of whatever data was on hand.

The allocation rule that follows is to size each level by how many distinct things that level can be talking about, which is a question about the domain rather than about the machinery. It is answerable by argument before anything is built. How many primitive shapes are there really? How many combinations of two are meaningful? The answers are rough, but rough is enough to establish that the sequence should grow rather than stay flat, and roughly how fast. A geometric progression is the usual outcome, because each level composes a fixed-size neighbourhood of the level below.

There is a second quantity that has to grow along with capacity, and forgetting it produces a system that is wide but blind. Each level must also see a larger portion of the original input than the level below, or its extra capacity has nothing to express: the compositions it is supposed to be recognising are not visible in what reaches it. Extent and capacity have to be scaled together, and in a well-arranged stack the mechanism that widens the view is the same mechanism that discards detail, so the two are naturally coupled. If your architecture widens capacity without widening view, the extra room is spent re-describing the same small window in more ways.

Generalised, this is a claim about where the interesting design decisions live in any layered abstraction. The number of concepts a layer needs is set by the combinatorics of the layer beneath it, so a uniform budget across layers is almost always wrong, and the direction of the error is predictable. It applies to the size of intermediate representations in a compiler, the number of derived categories in a taxonomy, the number of distinct message types at each tier of a protocol stack. Ask at each level what could be being said there, and count it, before deciding how much room to provide.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — chapter 13's walkthrough of a convolutional architecture, in which the number of filters doubles at every convolutional layer, justified by the observation that the first layer recognises very simple structures such as edges and there are not too many different simple structures, while later layers recognise more complex features drawn from a larger region of the original image because of the pooling done in between.
