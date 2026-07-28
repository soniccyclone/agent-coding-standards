---
type: lesson
title: "A foundation that supplies every mechanism is not yet a usable system, and no checklist of mechanisms can tell you whether it is adequate — only building its most demanding client can"
figure: lampson
works: [reflections-on-an-operating-system-design]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# A foundation that supplies every mechanism is not yet a usable system, and no checklist of mechanisms can tell you whether it is adequate — only building its most demanding client can

**Lesson:** There is a seductive way to plan a big system: specify a small privileged core containing the minimal facilities from which everything else can be constructed, build that core well, and treat the rest as straightforward application of it. The seduction lies in how measurable the core is. You can enumerate its object types and its calls, argue that each is necessary, watch it become reliable, and feel finished. What this accounting silently omits is that "everything else" is where the majority of the labor lives, and that its difficulty is not proportional to how many mechanisms the core withheld. A team can arrive at a genuinely excellent core, discover it is years from anything a working programmer can use, and run out of money in the gap.

The second half of the trap is subtler and more instructive. If the core's interface is designed and frozen before its hardest client has been designed, then the only evidence for its adequacy is the designers' imagination. And imagination systematically checks the wrong property: it verifies that each needed function is expressible, because expressibility is what a designer can reason about at a whiteboard. It does not surface the two failures that actually kill the layer — that a handful of operations which happen to be on the client's inner loop cost far more than the client can afford, and that one required construction is not merely awkward but impossible without breaking the core's central guarantee. Both of these are discovered by writing the client, and essentially only by writing the client. The functional review passes; the interface still fails.

What a builder does differently is refuse to treat the boundary as designable in isolation. Before fixing an interface, sketch its most demanding consumer far enough to know which of its calls will be hot and which of its constructions are the hardest, and price those specifically rather than pricing the interface as an average. Treat "we will find out when we build the layer above" as a schedule risk with unbounded tail, not as ordinary future work. And keep in mind that the reliability of the core is not evidence for the health of the whole: a core can be nearly crash-free while every failure users experience originates above it, which is exactly what you should expect, and exactly why core reliability is such a poor proxy for whether the project will succeed.

**Source:** [Reflections on an Operating System Design](../works/reflections-on-an-operating-system-design.md) — the history section's frank account of why the project ran out of funding, including the admission that a kernel had been mistaken for an operating system, together with the retrospective on extensibility where the kernel's functional adequacy is judged a success but its per-operation cost and its inability to support one crucial construction are not.
