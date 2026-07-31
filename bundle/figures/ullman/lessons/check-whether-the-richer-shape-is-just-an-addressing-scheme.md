---
type: lesson
title: "Check whether the richer shape is just an addressing scheme"
figure: ullman
works: [mining-of-massive-datasets]
axes: [primitive-count, cognitive-load]
subdomains: [programming-languages-and-semantics, algorithms-and-complexity]
tags: [lesson]
---
# Check whether the richer shape is just an addressing scheme

**Lesson:** When data arrives in a shape your machinery does not handle — nested where you expected flat, multi-dimensional where you expected one — there are two very different situations that look alike from the outside. Either the shape carries structure the computation depends on, in which case the machinery genuinely has to be extended, or the shape is only a convenient way of naming positions, in which case there is a reversible relabelling onto the shape you already handle and nothing needs to be built. Distinguishing these before writing code is worth real effort, because the second case is common and the cost of guessing wrong is an entire parallel implementation that turns out to have been unnecessary.

The test is whether you can exhibit the correspondence and show that the computation is indifferent to it. Merge the extra dimensions into one, check that every element of the original has exactly one image and vice versa, and check that the operations you actually perform give the same answers on either side. If they do, the elaborate shape is documentation — it records which index means what, which is genuinely valuable to a reader — layered over a structure your existing code already accepts. Convert at the boundary, run the machinery you have, convert back.

Getting this right has a compounding effect on the size of a system. Every primitive that has to grow a case for the new shape grows a case for every future shape too, and the cases interact. Keeping the core defined over one flat representation and pushing every richer view out to a conversion at the edge means the core stays a fixed size regardless of how many presentations accumulate around it. It also means the correctness argument for the core is made once, rather than once per shape.

A related caution comes free with this one. Rich shapes usually arrive carrying a name borrowed from somewhere the same word denotes an object with substantial mathematical structure and laws attached. Borrowing the name does not import the laws. If your version supports only relabelling and nothing else, say so plainly, because a reader who knows the original word will otherwise assume properties your implementation has never provided and will write code that depends on them.

**Source:** [Mining of Massive Datasets](../works/mining-of-massive-datasets.md) — the tensors section of the neural-nets chapter, which handles a four-dimensional weight array over a two-dimensional image and a two-dimensional hidden layer by flattening pairs of dimensions into single ones, exhibits the one-to-one mapping between hidden nodes in the two arrangements, concludes that the multi-dimensional notation is only a convenient grouping of vectors so the existing vector-based training algorithm applies unchanged, and warns explicitly that these arrays have little in common with the tensors of physics.
