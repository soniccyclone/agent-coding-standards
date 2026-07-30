---
type: work
title: "Introduction to Mathematical Logic"
figure: church
description: Church's graduate textbook synthesizing three decades of his own and others' work on the propositional and predicate calculus, formalized languages, and the theory of effective calculability, into a single systematic reference. It's dense and notation-heavy even by the standards of the field, but it's the volume where the lambda-calculus-era results of the 1930s got assembled into a teachable, self-contained logical foundation. Long treated as the standard entry point for formal logic as it bears on computability.
subdomains: [foundations-of-computation]
year: 1956
url: https://archive.org/details/dli.ernet.449121
survey_text_layer: ocr
survey_pages: 378
access: public
host: third-party-rehost
tags: [work]
---

# Introduction to Mathematical Logic

**Venue/year:** Princeton Mathematical Series no. 17, Princeton University Press, 1956 (Volume I; no further volumes were published).
**Source:** https://archive.org/details/dli.ernet.449121 — full freely-downloadable scan (PDF/EPUB/full text, no lending restriction) hosted by the Internet Archive under the Digital Library of India collection.
**Reading copy:** `scratchpad/ocr-text/church__introduction-to-mathematical-logic.txt` — the Internet Archive's own OCR of this scan (167,804 words, high quality: 37% of tokens are common English function words). Read that file rather than the 181MB PDF. This is a full-length textbook, so read it in sequential chunks. As with any OCR, the prose is reliable but the logical notation is not — Church's formalism will not have survived, so ground every lesson in his prose argument about method, not in a formula.

## Lessons
- [Choosing a notation is choosing a theory of the domain, and surface similarity is no evidence of shared structure](../lessons/choosing-a-notation-is-choosing-a-theory.md)
- [Denoting the same thing does not make two expressions interchangeable; substitution has a scope and you must know where it ends](../lessons/same-value-does-not-mean-interchangeable.md)
- [Make checking decidable even when finding is not, or the check itself will need checking forever](../lessons/checking-must-be-decidable-even-when-finding-is-not.md)
- [Whatever stays in the scaffolding was never really formalized, and the finished thing must stand without it](../lessons/whatever-stays-in-the-scaffolding-was-never-formalized.md)

_Coverage note: extraction is PARTIAL and `extraction: complete` is deliberately withheld. The Internet Archive text derivative for this volume runs ~1.16 MB (roughly 360k tokens), which exceeds a single agent's context. Read in full for these lessons: front matter and preface, Introduction sections 00 (logic), 01 (names), 02 (constants and variables), and 07 (the logistic method). Not yet read: Introduction sections 03 (functions), 04 (propositions and propositional functions), 05 (improper symbols, connectives), 06 (operators, quantifiers), 08 (syntax), 09 (semantics), and Chapters I-V with their appendices. A follow-up pass should resume at section 03 and at section 08 in the `_djvu.txt` derivative._
