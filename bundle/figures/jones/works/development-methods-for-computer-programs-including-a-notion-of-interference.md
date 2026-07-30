---
type: work
title: "Development Methods for Computer Programs including a Notion of Interference"
figure: jones
description: Jones's Oxford DPhil thesis (under Hoare), the original source of the interference/rely-guarantee idea later published as the 1983 TOPLAS paper. Works out, at greater length than the journal version, how to extend a VDM-style specify-and-refine development method to programs that share mutable state with a concurrently running environment. Not in the Phase 1 top-10 list but surfaced while verifying the 1983 papers as the clearly central, clearly public antecedent to both.
subdomains: [formal-methods-and-verification, distributed-systems-and-concurrency]
year: 1981
url: http://www.cs.ox.ac.uk/files/9025/PRG-25.pdf
survey_pages: 265
survey_text_layer: ocr
survey_fetch_mb: 10
access: public
host: institutional
extraction: complete
tags: [work]
---

# Development Methods for Computer Programs including a Notion of Interference

**Venue/year:** PhD thesis, Oxford University, June 1981. Printed as Programming Research Group Technical Monograph PRG-25.

**Source:** http://www.cs.ox.ac.uk/files/9025/PRG-25.pdf — hosted on Oxford's own Computer Science department file server, linked directly from Jones's Newcastle publications list (HTTP 200, confirmed live).
**Reading copy:** `scratchpad/ocr-text/jones__development-methods-for-computer-programs-including-a-notion-of-interference.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [Never add state to the artifact for the sake of the argument about it](../lessons/never-add-state-to-the-artifact-for-the-argument.md)
- [Model a type with exactly the distinctions its operations can observe, and no more](../lessons/build-the-model-your-operations-can-distinguish.md)
- [Keep the definition of meaning separate from the tools for reasoning, and then keep several tools](../lessons/keep-meaning-separate-from-the-tools-for-reasoning.md)
- [Record order-independence at the moment you know it, because it cannot be recovered later](../lessons/record-order-independence-while-you-still-know-it.md)
- [Build a theory of your data structure separately, so arguments about algorithms stay about algorithms](../lessons/build-a-theory-of-your-data-structure.md)
- [Each level of a design must be readable without the levels above it](../lessons/each-level-must-be-readable-without-the-ones-above.md)
- [Two fragments with the same effect in isolation are not interchangeable once anything else can watch](../lessons/sequential-equivalence-is-not-equivalence-under-interference.md)
- [Describe an algorithm by the condition it maintains, not by its sequence of steps](../lessons/describe-an-algorithm-by-its-invariant.md)
- [Replace a blanket restriction with an obligation you can discharge case by case](../lessons/replace-blanket-restrictions-with-dischargeable-obligations.md)
- [When participants cannot coexist, weaken each assumption until the promises can supply it](../lessons/weaken-the-assumption-until-the-promises-can-supply-it.md)
- [Specify a fault-tolerant component as ideal behaviour plus the substrate misbehaviour it survives](../lessons/specify-reliability-as-ideal-behaviour-plus-tolerated-misbehaviour.md)
- [Choose between describing a thing by a model and by its visible behaviour according to who is reading](../lessons/hidden-state-is-not-a-vice-in-a-description.md)
- [A specification you can run stops being a specification](../lessons/a-specification-you-can-run-stops-being-a-specification.md)
- [Keep the example that killed each simplification, and count before generalizing](../lessons/keep-the-example-that-killed-each-simplification.md)
- [Keep the tree of alternative designs, not just the branch you shipped](../lessons/keep-the-tree-of-alternative-designs.md)
- [A method is only usable at scale if no completed design step can be invalidated by a later check](../lessons/no-design-step-may-be-invalidated-by-a-later-check.md)
- [Expect refinement to resurrect obligations the abstraction had no vocabulary to state](../lessons/refinement-resurrects-obligations-the-abstraction-could-not-state.md)
- [A component whose only job is to make things faster has a vacuous functional specification](../lessons/a-component-that-only-optimizes-has-a-vacuous-functional-spec.md)
