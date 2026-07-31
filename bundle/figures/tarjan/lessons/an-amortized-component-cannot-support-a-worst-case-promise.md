---
type: lesson
title: "Interchangeable at the interface is not interchangeable at the guarantee: an amortized component cannot hold up a per-operation promise"
figure: tarjan
works: [a-data-structure-for-dynamic-trees]
axes: [verifiability, cognitive-load]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Interchangeable at the interface is not interchangeable at the guarantee: an amortized component cannot hold up a per-operation promise

**Lesson:** Two variants of the same lower-layer structure appear in this paper. They expose identical operations, satisfy identical static shape properties, and differ only in the character of the bounds on their two restructuring operations: one variant's costs are amortized over a sequence, the other's hold for every individual call. The authors note in closing that the substitution is one-directional — the strong variant can stand in for the weak one anywhere, but the weak one cannot be used in the version of the structure that promises a bound on every single operation. Nothing about the interface reveals this. A type checker, a test suite, and a specification written in terms of results rather than costs would all accept the illegal substitution.

The reason the asymmetry exists is worth understanding rather than memorizing. An amortized bound is a claim about a sum, and it earns its cheap steps by having surplus banked from earlier expensive ones. An enclosing structure that promises a per-operation bound will call into the component at moments of its own choosing, including moments where no surplus has accumulated — so the component's average is irrelevant to the caller's worst case, and the accounting cannot be transported across the boundary. This makes the guarantee class a real part of a component's contract, on equal footing with its signature and its semantics. Averages compose with averages. A worst-case promise can only be built from worst-case parts, and every layer in a stack that wants one must be paid for in full.

The practical failure this predicts is the sort that surfaces only under load. Swap in a container whose lookup is constant on average, a memory allocator with amortized reclamation, a rate limiter with bursty smoothing, a hash map that occasionally rehashes — every one is a legal substitution in a system whose obligations are stated as throughput, and an illegal one in a system whose obligations are stated as tail latency or a hard deadline. The same object is correct or incorrect depending on a property of the *caller* that the object cannot see. So a component's documented cost should always say which kind of bound it is, a caller with a per-operation obligation should treat "amortized" as a rejection rather than a footnote, and a library offering both variants should expect that the more expensive one exists for a reason and not quietly default to the faster one.

**Source:** [A Data Structure for Dynamic Trees](../works/a-data-structure-for-dynamic-trees.md) — the closing remark that the globally biased variant of the underlying search tree works in both the amortized and worst-case versions of the structure while the locally biased variant works only in the amortized one, together with the two pairs of lemmas that state the concatenation and splitting costs of the locally biased variant as amortized and those of the globally biased variant as holding per operation, and the worst-case section's requirement that the globally biased variant replace the locally biased one.
