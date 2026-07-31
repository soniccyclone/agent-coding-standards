---
type: lesson
title: "Consume the statistics into the structure so the runtime never needs them"
figure: sussman
works: [structure-and-interpretation-of-computer-programs]
axes: [hardware-affinity, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Consume the statistics into the structure so the runtime never needs them

**Lesson:** A Huffman tree carries a weight at every node, and the authors note in passing that those weights play no part whatsoever in encoding or decoding — they exist solely to drive the construction. The frequencies are consumed by the build and are afterwards inert. What survives into the operating structure is not the statistics but their consequence: rare symbols sit far from the root, common ones near it, and the walk down the tree is oblivious to why.

This is a pattern worth naming because it is easy to get wrong in the direction of keeping too much. Optimization inputs — measured frequencies, access patterns, cost estimates, profile data, a cardinality histogram — feel like they should stay available, since they are what justified the shape. But the moment they have been fully expressed in the shape, retaining them adds size, adds a thing that can go stale, and invites code to consult them at runtime and thereby take a second dependency on facts that were only ever true of the sample. The cleanest version of this kind of design ends with the evidence discarded and the decision embodied.

The test for whether you have actually done it is whether the runtime path ever reads the statistic. If decoding had to compare weights, the tree would not have absorbed the frequency information; it would merely be storing it near the point of use, and every query would be re-deriving a decision that should have been made once. Compilers do this properly with branch layout, databases with a chosen join order, allocators with size-class boundaries: the profile shapes the artifact and then goes away. Systems that get it wrong keep consulting the histogram on every operation and call the resulting variance "adaptivity."

The corresponding liability is the one that makes this a trade rather than a free win. A structure that has swallowed its statistics cannot tell you it has become wrong. Huffman's optimality holds for messages whose symbol frequencies match the ones the tree was built from; feed it a different distribution and it still decodes perfectly, just less well, with nothing in the artifact that notices. So the discipline is to strip the statistics from the operating structure but keep them somewhere outside it — in the build inputs, in the provenance — precisely so you can ask later whether the assumptions the artifact was compiled against still hold.

**Source:** [Structure and Interpretation of Computer Programs](../works/structure-and-interpretation-of-computer-programs.md) - chapter 2 section 2.3.4's description of Huffman encoding trees, which assigns each leaf a weight equal to its relative frequency and each internal node the sum of the weights below it, remarks that the weights are not used in the encoding or decoding process but only to help construct the tree, describes the repeated-merge construction that places lowest-frequency symbols farthest from the root, and notes that the resulting code is best for messages whose symbol frequencies match those the code was constructed from.
