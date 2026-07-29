---
type: lesson
title: "Your cost model is the style guide people actually obey; make the good structure the cheap one"
figure: ungar
works: [programming-as-an-experience]
axes: [hardware-affinity, expressiveness, cognitive-load]
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
tags: [lesson]
---
# Your cost model is the style guide people actually obey; make the good structure the cheap one

Everyone advises pulling shared logic out into its own named piece, and building abstractions for control rather than repeating the same shape of loop. Then people don't, and the usual explanation is discipline. It is not discipline. If extracting a small piece of common logic adds a measurable cost every time it runs, the advice is asking programmers to pay for tidiness in the currency their users notice, and they correctly decline. If a user-written control abstraction is inherently slower than the one built into the language, then control abstraction is a luxury for code that isn't hot, which in practice means the code most worth structuring well is the code structured worst.

This makes the implementation's cost model a policy instrument, and one far stronger than documentation, because it operates on every decision without anyone deliberating. Whatever your system makes free is what will be common in code written on it. So the useful question for an implementer is not only "how fast is this" but "which structures am I taxing, and are they the ones I want less of." Removing the penalty on fine-grained decomposition does not merely permit good factoring; it produces it, and what shows up is code decomposed further than a person would dare in a system that charged for it — layers of small pieces resolving down to primitives, because nothing punished the layering.

The trap to avoid is the escape hatch that looks like a solution: let the programmer request the optimization explicitly at each site. That converts a systemic property into a per-decision burden and usually comes bundled with a semantic sacrifice — you get the speed by giving up the dynamic behavior that made the abstraction worth having. Now every extraction requires a judgment call about whether it deserves special treatment, which is exactly the deliberation you were trying to remove, and the honest answer at most sites is unknowable in advance. Doing it automatically from observed behavior costs the implementer much more and costs each user nothing.

The transferable habit reaches beyond compilers. Any platform, framework, or API sets prices: a query pattern that is expensive, a module boundary that costs a round trip, a validation that is slow enough to skip. Those prices are read by everyone who builds on it and obeyed silently. If you find yourself writing guidelines urging people toward a structure your system makes expensive, stop writing guidelines and go make it cheap — that is the only version of the advice that gets followed.

**Source:** [Programming as an Experience: The Inspiration for Self](../works/programming-as-an-experience.md) — the section on factoring and extensible control, which argues that per-call overhead is a standing disincentive against decomposition and that erasing it automatically, rather than by explicit programmer request, is what changes how programs get written.
