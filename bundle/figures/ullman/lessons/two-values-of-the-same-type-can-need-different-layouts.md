---
type: lesson
title: "Two values of the same type can need different layouts"
figure: ullman
works: [mining-of-massive-datasets]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, operating-systems-and-systems-programming]
tags: [lesson]
---
# Two values of the same type can need different layouts

**Lesson:** Physical representation is usually chosen per type: this is a vector, so vectors are stored like this. That is one decision too coarse. Two values that are the same type in the model can have completely different occupancy in practice, and the right storage for one is badly wrong for the other. An input record drawn from an enormous vocabulary touches a handful of positions and should be stored as the list of positions it touches. A running accumulator over the same vocabulary starts empty and fills in almost immediately, so storing it as a list of touched positions costs more than storing it densely and gets worse every step. Same type, opposite layouts, and the choice should be made per role.

The way to tell them apart is not to look at the declared type but at how occupancy evolves. Values that arrive from outside and describe one observation are typically sparse and stay sparse, because one observation touches a small part of the world. Values that accumulate across many observations become dense quickly, because the union of many small sets is not small. Asking "does this fill up?" of each value in the design is a short exercise and decides the representation.

There is a second decision that goes with it: the vocabulary itself should be a mapping from names to positions built as you encounter them, rather than a fixed enumeration allocated up front. Nothing needs to know the full extent in advance, entries never seen cost nothing, and every value in the system indexes the same way. This is what makes the sparse side genuinely cheap rather than merely notionally cheap, and it is also where filtering pays off — dropping components that carry no information shrinks every sparse value that would have referenced them, compounding across the whole dataset.

The general habit is to separate the logical type from the storage strategy and to let each value's access and occupancy pattern pick the latter. This is the same reasoning behind choosing a different structure for a read-mostly table than for a write-heavy one of identical shape, or laying out a struct differently when it is iterated in bulk than when it is accessed one field at a time. The model says what a thing is; the usage says how to store it, and they are separate questions.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the box on the pragmatics of training on emails in the perceptron chapter, which assigns integers to words as they appear rather than materialising a component per vocabulary word, stores each document as the list of components in which it has a one, notes that removing uninformative words compresses the data further, and observes that only the weight vector needs all its components listed because it will not be sparse after a small number of examples.
