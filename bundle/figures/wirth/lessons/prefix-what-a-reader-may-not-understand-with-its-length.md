---
type: lesson
title: "Prefix what a reader may not understand with its length"
figure: wirth
works: [project-oberon]
axes: [expressiveness, verifiability, cognitive-load]
subdomains: [software-engineering-and-architecture, operating-systems-and-systems-programming]
tags: [lesson]
---
# Prefix what a reader may not understand with its length

**Lesson:** A format that admits extensions defined elsewhere has to answer a question its designer would rather not think about: what happens when a reader meets a component whose definition it does not have? The naive answer — refuse the whole artifact — makes every extension a compatibility break, which defeats the point of having extensions. The workable answer costs one field. Precede each extension-defined region with the number of units it occupies, so that a reader lacking the definition can advance past it and keep going. It understands nothing about the region and does not have to; it only needs to know where the part it *does* understand resumes. The general principle is that a self-describing structure must let a reader skip what it cannot interpret, and skipping requires knowing the size in advance, which means the size travels ahead of the content.

Notice what this makes possible beyond mere survival. A reader that can skip unknown regions can process an artifact partially and correctly rather than partially and wrongly: it can present or transform everything within its competence and leave the rest untouched and intact, which is what allows an artifact to pass through a tool that predates half of its content. That property has to be designed in from the first version of the format, because it is the *first* version's readers that will encounter the future extensions, and no later change can retrofit a skip length into a stream those readers are already parsing.

The obligation this creates is on the writing side and should be stated plainly to whoever defines an extension: they must emit a correct count, and nothing else in the system can check it for them. A wrong count does not corrupt the extension's own region — its own reader consumes it correctly — it desynchronizes every subsequent element for the readers who skipped. That is a defect that appears only in the population that lacks the extension, which is exactly the population the author never tests against. Where the format allows it, prefer a framing whose length can be derived or validated independently, and where it does not, make the count a required, documented part of the extension's contract rather than a convention.

**Source:** [Project Oberon](../works/project-oberon.md) — section 13.8.3's description of the graphics file format, in which each element is headed by a class number, index/name pairs preceding first use establish the class and its allocator, the base type's data are read generically, and the extension's data — read by the extension's own `read` method — must always be headed by a byte giving the number of bytes that follow, information used in the case where the requested module is not present to indicate how many bytes to skip in order to continue reading further elements.
