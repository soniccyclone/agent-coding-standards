---
type: lesson
title: "The right layering absorbs the tools you would otherwise have to build alongside it"
figure: parnas
works: [designing-software-for-ease-of-extension-and-contraction]
axes: [primitive-count, expressiveness, cognitive-load]
subdomains: [software-engineering-and-architecture, programming-languages-and-semantics]
tags: [lesson]
---
# The right layering absorbs the tools you would otherwise have to build alongside it

A system that ships in configurations tends to grow a second system beside it whose only job is to produce those configurations — a generator, a build-time configurator, a bespoke language with its own translator. This support software is treated as inevitable overhead, and it is frequently larger than the thing it exists to produce, which is the tell that something has gone wrong. Parnas points out that a properly ordered structure gives you the same services for free, because each level already is a language extension available to whoever writes the level above. You never sit down to build a translator; you build the system, and the convenience features arrive as a side effect of having levels at all.

The configurator disappears by a different and slightly startling route. If the flexible, general facility sits above the specialized fixed one, then the general facility can be run to produce the fixed one's contents — a component that interprets descriptions at run time is also, at build time, exactly the thing that generates the static tables a run-time-free version needs. The upper levels can generate the lower-level versions of the system. So the generality you were worried about paying for at run time turns out to be the mechanism that lets you ship a configuration that does not pay for it, provided you got the ordering right and put the interpretive machinery above the thing it configures rather than beside it.

The transferable move is to stop treating tooling as a separate category of artifact. When you find yourself planning a program whose purpose is to assemble, specialize, or configure your system, read it as a report about the system's structure: either some capability that already exists internally has been placed where the build cannot reach it, or the layer that should have provided the language for expressing configurations was never built as a layer. Both are structural defects with structural fixes, and both are cheaper to fix than to staff. The alternative is paying twice — once for the system, once for the apparatus that makes it deliverable — and maintaining the apparatus forever.

**Source:** [Designing Software for Ease of Extension and Contraction](../works/designing-software-for-ease-of-extension-and-contraction.md) — the summation point that designing for subsets and extensions reduces the need for support software, its argument that each level provides a language extension for the next so no compiler need be built, and the earlier observation in the address-processing example that upper level programs can generate the tables used by the fixed-format lower level versions in place of a separate generation program.
