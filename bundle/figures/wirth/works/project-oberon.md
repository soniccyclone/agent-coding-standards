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

## Coverage note (partial extraction — NOT exhausted)

Read against `pdftotext -layout` output of the 2005 edition PDF (441 pages → 22864 lines
of extracted text). Identity verified: title page and preface name N. Wirth and J.
Gutknecht, Project Oberon, ETH Zurich, February 1992.

**Read and mined:** front matter and table of contents; chapter 5 sections 5.1 and 5.2
(text as abstract data type; text management and the piece-chain representation, through
the auxiliary FindPiece/SplitPiece procedures at line 3991); chapter 1 (Historical Background
and Motivation); chapter 2 in full (Basic Concepts and Structure of the System — viewers,
commands, tasks, tool texts, extensibility, dynamic loading, module hierarchy, chapter
tour); chapter 3 in full (The Tasking System — interactive and background tasks, the
scheduler, the concept of command, generic facilities, toolboxes, and the complete
listings of modules Oberon and System); chapter 4 through section 4.6 (The Display System
— screen layout model and the tiling comparison, viewers as objects, frames, display
management including viewer management, menu viewers and cursor management, raster
operations, standard display configurations). Extraction stops mid-way through the
literature list at the end of chapter 4.

**Not read:** the remainder of chapter 5 from line 3991 on — the rest of the piece-chain
implementation, section 5.3 (text frames), 5.4 (the font machinery), 5.5 (the edit
toolbox) — and everything after it: chapter 6 (The Module
Loader); chapter 7 (The File System); chapter 8 (Storage Layout and Management); chapter 9
(Device Drivers); chapter 10 (The Network); chapter 11 (the dedicated server); chapter 12
(The Compiler); chapter 13 (A Graphics Editor); chapter 14 (Building and Maintenance
Tools); and appendix A (Ten Years After: From Objects to Components).

**Resume at line 3532** of the extracted text — the `5. The Text System` heading.
Everything above that line has been read, including the complete listings of modules
Viewers, MenuViewers and the display section of System at lines 2917–3504, which are
source code and yielded no lesson beyond what the chapter-4 prose already gave.
Regenerate the text with: `pdftotext -layout ProjectOberon1992.pdf PO.txt`.

Chapter start lines in the extracted text, for planning a resumed pass: ch. 5 at 3532,
ch. 6 at 7049, ch. 7 at 7696, ch. 8 at 9747, ch. 14 at 22341 (chapters 9–13 fall between
9747 and 22341 and their headings did not extract as clean line starts).

Note that a large fraction of the remaining lines are complete Oberon source listings
rather than prose; the prose sections at the head of each chapter and each numbered
section are where the extractable lessons are.

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
- [Edit the description, not the contents](../lessons/edit-the-description-not-the-contents.md)
