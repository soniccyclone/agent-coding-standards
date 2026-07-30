---
type: lesson
title: "Know which machine your claim needs, and don't let a convenience strengthen the assumption"
figure: tarjan
works: [fibonacci-heaps-and-their-uses-in-improved-network-optimization-algorithms]
axes: [hardware-affinity, primitive-count]
subdomains: [algorithms-and-complexity]
tags: [lesson]
---
# Know which machine your claim needs, and don't let a convenience strengthen the assumption

**Lesson:** Deep in the description of the structure sits an indexed array, used for the mundane job of finding two trees whose roots have the same number of children so they can be joined. Nothing about the design needs indexed access; the array was simply the obvious way to write it. But an indexed array assumes a machine that can compute an address and jump to it, which is a strictly stronger assumption than one that can only follow links it already holds. Fredman and Tarjan notice this and remove it: a linked chain of rank markers, each node holding a pointer to the marker for its own rank, does the same job with no arithmetic on addresses, since a rank only ever moves by one and the pointer can be walked along with it. The stated conclusion is that the whole structure runs on the weaker machine at no asymptotic cost. The same paragraph does the analogous thing for space, naming how many pointers per node the implementation uses and how far that can be reduced by more elaborate representations at the price of a constant factor.

The lesson is about hygiene in what a result depends on. Every performance claim is relative to a model of what operations are free, and that model is usually inherited unexamined from whatever language you wrote the code in. A convenience — an array, a hash table, a sort, unbounded integers, an atomic instruction — silently widens the set of assumptions the claim rests on, and the widening is invisible because the convenience wasn't the point. It matters when the assumption stops holding: an algorithm whose bound needed random access degrades on a linked or distributed representation, one whose bound needed unit-cost arithmetic on machine words degrades when the keys grow, one that needed a cheap atomic operation degrades across a network. The discipline is to ask, of each such use, whether the result actually needs it or merely used it, and to spend the effort removing it when the answer is the second.

The payoff is not purism, it is portability of the reasoning. A claim proved under weaker assumptions survives more re-implementations, and knowing exactly which capabilities are load-bearing tells you in advance which environments will break the claim rather than finding out by measurement. It also separates two kinds of improvement that get conflated: reducing the assumed capabilities of the machine, and reducing the constant factors on a given machine. The paper keeps them separate, quantifying the space trade as a constant factor and the model reduction as free, which is exactly the information a reader needs to decide whether either applies to them.

**Source:** [Fibonacci Heaps and Their Uses in Improved Network Optimization Algorithms](../works/fibonacci-heaps-and-their-uses-in-improved-network-optimization-algorithms.md) — the closing remarks of the section defining the structure, which observe that the array used to pair equal-rank roots is not essential, replace it with a linked list of rank nodes so the structure runs on a pointer machine with no asymptotic loss, and separately state the per-node pointer count and how much it can be reduced at a constant-factor cost in running time.
