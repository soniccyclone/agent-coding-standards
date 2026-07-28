---
type: lesson
title: "Count the conformance work before promising novelty"
figure: pike
works: [systems-software-research-is-irrelevant]
axes: [primitive-count, cognitive-load, expressiveness]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Count the conformance work before promising novelty

**Lesson:** Anything that has to survive in a real environment must speak the protocols, formats, and interfaces that environment already assumes, and that obligation is not a footnote on the schedule — on a genuinely novel system it can consume nearly all of it, leaving only a sliver for the idea that motivated the project. The obligation also grows without your consent: each standard is externally owned, changes on someone else's cadence, and sometimes is made deliberately awkward to implement by whoever benefits from incompatibility. Treat the conformance surface as the primary budget line, estimated up front, rather than as integration work to be discovered late.

The consequence is structural, not merely tiring. When the great majority of effort is spent honoring imposed structure, the remaining slop is where all novelty has to fit, and a design whose novel part must fit in the slop will end up making the conservative choice everywhere it touches the outside world. The extreme case is a system whose architecture is genuinely new and whose first construction task is an emulation layer for the thing it replaces: the compatibility layer will define what the rest can assume, and the new architecture becomes a substrate for old semantics. The obligation you accepted for adoption has quietly become the specification.

A programmer who believes this does two things differently. First, they price conformance explicitly and early, and let that number decide the scope of the ambition — a small idea that fits the remaining slop and ships beats a large one that gets ground down to nothing. Second, they choose which compatibility to accept as a design decision rather than a default, because each one purchased buys reach and spends exactly the freedom the project existed to use. Sometimes the right answer is to abandon a standard and accept the narrower audience, and that trade should be made deliberately, with the cost of the alternative counted.

**Source:** [Systems Software Research is Irrelevant](../works/systems-software-research-is-irrelevant.md) — the Standards slide, with its estimate of what fraction of a full operating system's effort went to externally imposed conformance, and the Unix slide's observation about emulation layers being built first.
