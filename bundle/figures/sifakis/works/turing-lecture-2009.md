---
type: work
title: "Model Checking: Algorithmic Verification and Debugging"
figure: sifakis
description: The joint Turing Award lecture paper, co-written with Edmund Clarke and E. Allen Emerson, surveying model checking from its origins through symbolic, bounded, and partial-order techniques to counterexample-guided abstraction refinement. Written for a general CACM audience rather than specialists, it frames model checking's core value as algorithmic debugging of designs, not just yes/no verification. Serves as the field's own retrospective on why the technique succeeded in industrial hardware and software verification.
subdomains: [formal-methods-and-verification]
year: 2009
url: https://www-verimag.imag.fr/~sifakis/TuringAwardPaper-Apr14.pdf
survey_pages: 10
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
extraction: complete
tags: [work]
---

# Model Checking: Algorithmic Verification and Debugging

**Author(s):** Edmund M. Clarke, E. Allen Emerson, Joseph Sifakis

**Venue/year:** Communications of the ACM, 52(11), pp. 74-84, November 2009

**Source:** Self-archived by Sifakis on his Verimag/CNRS Grenoble faculty page (www-verimag.imag.fr/~sifakis/TuringAwardPaper-Apr14.pdf), linked from his publications list.

## Lessons
- [Ask whether this one structure satisfies the formula, not whether some structure does](../lessons/check-the-model-you-have-not-every-model.md)
- [Make the negative answer carry evidence: an analysis that only says no is half a tool](../lessons/a-failing-check-must-hand-back-a-witness.md)
- [A method that must be practiced while building competes with building; one that runs on the finished artifact does not](../lessons/separate-the-analysis-from-the-act-of-building.md)
- [Choose a specification notation by what it can state, then by how comfortably; efficiency is the last constraint](../lessons/pick-the-notation-by-what-must-be-sayable.md)
- [Prefer the algorithm that behaves well on the instances you get, not the one with the better bound](../lessons/worst-case-bounds-are-guarantees-not-forecasts.md)
- [When an exhaustive method stalls, attack the representation before the algorithm](../lessons/when-search-saturates-change-the-representation.md)
- [A one-directional guarantee plus a feedback loop beats waiting for a two-directional one](../lessons/let-the-false-alarm-refine-the-abstraction.md)
- [Everything you prove is about the model; the whole guarantee rests on how the model was derived](../lessons/a-model-is-worth-only-its-link-to-the-artifact.md)
- [Automation covers whether your requirements are consistent, never whether they are all there](../lessons/soundness-can-be-checked-completeness-cannot.md)
- [Give up on the general theory: specialize the argument to one property and one architecture](../lessons/narrow-the-guarantee-until-it-becomes-cheap.md)
- [Heavy reliance on after-the-fact checking is a symptom of a discipline that lacks construction rules](../lessons/put-the-guarantee-in-the-construction-rule.md)
- [Reasoning at the level where structure is still visible beats translating everything down to one composition primitive](../lessons/do-not-flatten-architecture-into-one-primitive.md)
