---
type: work
title: "Project Oberon: The Design of an Operating System and Compiler"
figure: wirth
description: A full workstation environment — operating system, compiler, and user interface for the Oberon language and its Ceres hardware — documented top to bottom, including source code, as a demonstration that a complete, usable system could be built and understood by a tiny team instead of a large organization. Written with Jurg Gutknecht, it operationalizes Wirth's stepwise-refinement and lean-software convictions at the scale of a whole system rather than a single program. The book doubles as an extended case study in single-author-comprehensible systems design, later re-issued with updated editions targeting FPGA-based RISC hardware.
subdomains: [operating-systems-and-systems-programming, programming-environments-and-object-systems]
year: 1992
url: https://people.inf.ethz.ch/wirth/ProjectOberon1992.pdf
survey_pages: 441
survey_text_layer: full
survey_fetch_mb: 4
access: public
host: self-archived
tags: [work]
---

# Project Oberon: The Design of an Operating System and Compiler

**Author(s):** Niklaus Wirth and Jurg Gutknecht
**Venue/year:** Addison-Wesley / ACM Press, 1992.
**Source:** https://people.inf.ethz.ch/wirth/ProjectOberon1992.pdf — live PDF, self-archived on Niklaus Wirth's ETH Zurich personal page.

## Lessons
- [Separate the unit of action from the unit of packaging](../lessons/separate-the-unit-of-action-from-the-unit-of-compilation.md)
- [Pick the switching granularity first; the protection machinery follows from it](../lessons/pick-the-switching-granularity-first-the-protection-follows-from-it.md)
- [Root a tree of requests instead of fixing a set of operations](../lessons/root-a-tree-of-requests-instead-of-fixing-a-set-of-methods.md)
- [Prefer the state that is already visible as the interface between steps](../lessons/prefer-the-state-that-is-already-visible-as-the-interface.md)
- [A participant that can fail should be removed before it runs, not after](../lessons/a-repeatedly-failing-participant-should-eject-itself.md)
- [Price a metaphor by the actions it actually produces](../lessons/price-a-metaphor-by-the-actions-it-actually-produces.md)
- [Bind at the latest moment, so each part exists exactly once](../lessons/bind-at-the-latest-moment-so-each-part-exists-once.md)
- [Choose the arrangement whose undo is simple, not the one whose forward move is free](../lessons/choose-the-arrangement-whose-undo-is-simple.md)
- [Ask the population instead of maintaining a registry](../lessons/ask-the-population-instead-of-maintaining-a-registry.md)
- [Make the container and the contained the same kind of thing, and global policy becomes a local default](../lessons/make-the-container-and-the-contained-the-same-kind-of-thing.md)
- [A self-inverse operation needs no saved copy and no precondition](../lessons/a-self-inverse-operation-needs-no-saved-copy.md)
- [Let each level transform requests for the level below it, and never reach past a child](../lessons/let-each-level-transform-requests-for-the-level-below-it.md)
