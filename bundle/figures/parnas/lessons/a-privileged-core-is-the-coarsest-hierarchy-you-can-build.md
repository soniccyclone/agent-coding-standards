---
type: lesson
title: "A privileged core is the coarsest hierarchy you can build, and it freezes whatever you put inside"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A privileged core is the coarsest hierarchy you can build, and it freezes whatever you put inside

The standard move for taming a large system is to designate a core — kernel, nucleus, runtime, platform, framework — hold the essential services in it, and let everything else be optional around the edge. Parnas points out that this is not an alternative to a layered ordering; it is a layered ordering with exactly one boundary in it, and the coarseness is the whole problem. Everything inside the line is mutually entangled by default and present in every configuration you will ever ship. Anything you got wrong about what belongs there cannot be corrected by omission, only by surgery.

The failure is symmetric and both halves show up in practice. Facilities that end up in the core cannot be removed, so configurations that would be perfectly viable without them are unobtainable. And once two capabilities are fused inside the core, a client who needs one of them without the other has no legitimate route, so it goes around the core entirely and reimplements what it needs — which is how a privileged inner layer ends up with a population of clients bypassing it, the exact opposite of the discipline it was supposed to impose. The same pattern appears in a checking mechanism welded so tightly into an invocation path that programs which have already established the property statically cannot decline to pay for it.

Underneath is a sharp claim about the premise. The core exists because someone believed a set of services is always needed, and Parnas reports never having found a feature for which that is true. What people mean is that a feature is almost always needed, and for the purpose of deciding structure, almost-always is simply not-always: it names a real configuration that your architecture has now made impossible. The remedy is not a smaller core, it is a finer ordering — many levels, each earned, each providing a subset you could stop at — because a structure built from small increments can always be truncated wherever a customer's line happens to fall, while a two-part partition can only be truncated in the one place you guessed at up front.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the section comparing the layered approach with kernel and nucleus approaches to operating system design, its examples of users bypassing a core to reach a fused capability and of type checking too intrinsic to disable, and its remark on the word "almost."
