---
type: lesson
title: "Two programs can share a deep structure that neither one exhibits"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture]
tags: [lesson]
---
# Two programs can share a deep structure that neither one exhibits

**Lesson:** Two procedures are set side by side that look nothing alike -- one walks a tree summing selected squares, the other builds a list of selected numbers from a generated series. Described abstractly, both turn out to be the same four-stage pipeline: produce a stream of items, discard some, transform each, combine the survivors. The stages differ in their contents and the order of two of them; the shape is identical.

The observation the authors then make is the one worth extracting. That shared shape is nowhere to be found in either procedure. There are no distinct parts corresponding to the stages: the production of items is implemented partly by the base-case tests and partly by the recursive structure, and the combining is spread between those same tests and an operator buried in the recursion. The programs do not merely fail to *highlight* the common structure -- they decompose the computation along entirely different lines, mingling all four stages together.

So there is a real structure that the artifact does not exhibit, and this is a distinct failure mode from having no structure at all. It cannot be found by reading the code, because reading the code shows you the decomposition the author happened to use. It is found by describing what the computation *does* at a level above the text and noticing that two descriptions match. The remedy is then to reorganize so that the stages become separately nameable parts, and that reorganization is the actual design act -- not a tidying pass afterwards.

The habit generalizes to any codebase where people sense that two components are "kind of similar" but cannot say how. That intuition is usually detecting a shared abstract shape that neither implementation manifests. Write the abstract description of each, in stages, without looking at the code; if the descriptions align, you have found a structure worth making explicit, and you will usually find that neither program's existing decomposition can be nudged into it -- both need rewriting against the shape rather than toward each other.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.2.3, which sets a tree-summing procedure beside a Fibonacci-filtering one, describes both as enumerate-filter-map-accumulate pipelines and draws them as signal-flow diagrams, then observes that the two definitions fail to exhibit that structure: the enumeration is implemented partly by the null and pair tests and partly by the tree-recursive structure, the accumulation partly by the tests and partly by the addition in the recursion, and in general no distinct parts of either procedure correspond to the elements of the signal-flow description.
