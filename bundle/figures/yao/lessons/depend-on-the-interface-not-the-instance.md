---
type: lesson
title: "Build on the weakest interface that suffices, not on an instance's incidental extra structure"
figure: yao
works: [protocols-for-secure-computations]
axes: [primitive-count, expressiveness]
subdomains: [algorithms-and-complexity, software-engineering-and-architecture]
tags: [lesson]
---
# Build on the weakest interface that suffices, not on an instance's incidental extra structure

**Lesson:** A construction that works because the component you happened to pick has an extra property — an operation that commutes, a representation you can inspect, a coincidence of the encoding — is a construction fused to that component. It cannot be re-implemented on a successor, it fails silently when the component is swapped for a supposedly equivalent one, and its correctness argument is really an argument about the component rather than about the design. Deriving the same capability from only the generic interface every member of the family offers costs more thought up front and buys three things at once: the design survives its component being retired or broken, the family of usable components is the whole family rather than one member, and the proof obligation shrinks to properties that are stated in the interface instead of properties someone has to remember are being relied on.

The subtle part is that reliance on incidental structure rarely announces itself. It appears as a step that seemed natural because the concrete component made it natural — reordering two operations, comparing intermediate values, reusing a value in a second role. Locating those steps means re-deriving the design against the abstract interface and watching where the derivation stalls, which is also, usually, where the design gets better: the generic replacement for a structure-dependent trick tends to be leaner than the trick, because the trick was carrying assumptions the problem never needed. Cost can improve rather than degrade in the process, so the trade is not automatically generality-for-efficiency.

The instinct to formalize is: when a design depends on a component, write down the smallest interface that makes the design work, then check whether your chosen component is the only member of that interface you have actually tested against. If it is, you have an untested coupling, not an abstraction. This applies as much to a storage engine's ordering guarantees or a scheduler's fairness accident as it does to a cryptographic assumption; in every case the question is whether the property you lean on is one the contract promises or one this implementation merely exhibits.

**Source:** [Protocols for Secure Computations](../works/protocols-for-secure-computations.md) — the contrast drawn between the paper's own protocols, which require only a general public-key mechanism, and earlier constructions for the same problems that depended on the specific one-way functions used having a commutativity property, plus the accompanying note that the generic version also transmits far fewer bits as the problem grows.
