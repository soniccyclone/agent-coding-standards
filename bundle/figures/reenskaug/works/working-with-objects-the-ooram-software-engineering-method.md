---
type: work
title: "Working with Objects: The OOram Software Engineering Method"
figure: reenskaug
description: A book-length treatment of OOram, Reenskaug's role-modeling method for object-oriented analysis and design, built around the idea of describing a system as a set of collaborating roles before ever committing to classes. The book works through the method across the full lifecycle — analysis, design, and synthesis of roles into concrete classes — with worked examples throughout. Now out of print; the authors put the final pre-publication draft online themselves once it went out of circulation, noting it lacks only the copy editor's final pass.
subdomains: [software-engineering-and-architecture, programming-environments-and-object-systems]
year: 1996
url: https://folk.universitetetioslo.no/trygver/1996/book/WorkingWithObjects.pdf
survey_pages: 497
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: self-archived
tags: [work]
---

# Working with Objects: The OOram Software Engineering Method

**Author(s):** Trygve Reenskaug, with Per Wold and Odd Arild Lehne
**Venue/year:** Prentice Hall, 1996 (this self-archived copy is the final pre-publication draft, dated 2001).
**Source:** https://folk.universitetetioslo.no/trygver/1996/book/WorkingWithObjects.pdf — self-archived by Reenskaug on his University of Oslo homepage after the printed book went out of print; the PDF's own title page states it's made freely available for that reason. Verified live (HTTP 200, direct PDF, ~2MB) and confirmed by extracting the text of the first pages.

## Lessons
- [Without the question, there is nothing in a model to judge](../lessons/a-model-answers-a-question-or-cannot-be-judged.md)
- [Hierarchy is an artifact of thought, not a property of the world](../lessons/hierarchy-is-an-artifact-of-thought-not-a-property-of-the-world.md)
- [Composition is reuse only when it preserves what you already checked](../lessons/composition-is-reuse-only-if-it-preserves-what-you-already-checked.md)
- [Extending one part alone is meaningless; extend the arrangement](../lessons/extend-the-arrangement-not-the-part.md)
- [Permission belongs to the relationship, not to the interface](../lessons/permission-belongs-to-the-relationship-not-the-interface.md)
- [The rigidity that makes an organization inhuman is exactly right for machines](../lessons/rigidity-that-is-inhuman-is-correct-for-machines.md)
- [Many views, one model — never let a view become the model](../lessons/many-views-one-model-never-let-a-view-become-the-model.md)

- [Sort your correctness claims by who can check them, because a tool's silence is not approval](../lessons/classify-your-correctness-claims-by-who-can-check-them.md)
- [Start where the risk is, not at the top of the abstraction ladder](../lessons/start-where-the-risk-is-not-where-the-abstraction-is.md)
- [When the ugly requirement arrives, describe it somewhere else and compose, rather than spoiling the clean description](../lessons/model-the-mess-separately-and-compose-it-in.md)
- [When you borrow a mechanism, permit it less than its source did](../lessons/deliberately-narrow-a-borrowed-mechanism.md)
- [Size each description to what a reader can hold at once, and exempt the pieces that get reused everywhere](../lessons/size-a-description-to-working-memory-with-a-reuse-exception.md)
- [Reuse costs you the fresh look, and the person advocating it should be the one to say so](../lessons/name-reuses-own-cost.md)

- [Of the programs that work, confine yourself to the ones you can understand — the machine will accept far worse](../lessons/restrict-yourself-to-the-programs-you-can-understand.md)
- [Building it is the experiment that tells you whether your separation of concerns was real](../lessons/implementation-is-the-test-of-whether-your-decomposition-was-real.md)
- [A description complete enough to generate the system has become the system, and needs its own abstraction](../lessons/a-description-detailed-enough-to-generate-code-is-code.md)

_PARTIAL EXTRACTION — updated 2026-07-29. Read in full so far: preface, chapter 1
(The main ideas), all of chapter 2 (Role Modeling), and **all of chapter 3 (Role
model synthesis, lines 4483-6286 — synthesis operation, aggregation kinds,
attributes and message parameters, safe vs unsafe synthesis, and the notation
across all seven views)**. Stopping point is now chapter 4 section 4.2 (line 7237), book page ~165
of 497 — chapter 4 sections 4.1.x are read in full, the rest of chapter 4 is not of the `pdftotext -layout` extraction held at
`scratchpad/reenskaug/ooram-slim.txt`.

NOT yet read: chapter 4 (bridge to implementation, Smalltalk and C++), chapter 5
(creating reusable components), chapter 6 (additional views and notation),
chapters 7-9 and 12 (the four case studies), chapter 10 (organizing for software
productivity, value chains), chapter 11 (instance-based reuse), and appendix A
(the OOram language). Chapter boundaries in that extraction: ch4 6287, ch5 8121,
ch6 9436, ch7 10525, ch8 12342, ch9 13620, ch10 15667, ch11 16756, ch12 18172,
end 21176.

Chapter 10 remains the highest-value unread target — organizational value chains
for software production is a subject no lesson in this corpus touches yet.
`extraction: complete` still deliberately withheld._
