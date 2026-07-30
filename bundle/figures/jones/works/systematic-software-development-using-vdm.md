---
type: work
title: "Systematic Software Development Using VDM"
figure: jones
description: The mature, textbook-form statement of VDM, refined from the 1980 book after a decade of teaching and industrial use. Covers specification in the VDM model-oriented style, data type invariants, and the reification/decomposition proof obligations needed to justify that an implementation meets its specification. Became the standard VDM reference through the 1980s-90s formal-methods period.
subdomains: [formal-methods-and-verification, software-engineering-and-architecture]
year: 1990
url: http://homepages.cs.ncl.ac.uk/cliff.jones/publications/Books/Jones1990.pdf
survey_pages: 345
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Systematic Software Development Using VDM

**Venue/year:** Prentice Hall International, 2nd edition, 1990 (1st edition 1986).
**Source:** http://homepages.cs.ncl.ac.uk/cliff.jones/publications/Books/Jones1990.pdf — self-archived on Jones's own Newcastle homepage, linked directly from his publications list (HTTP 200, confirmed live). Phase 1 had flagged this `paywalled` on the strength of a controlled-lending archive.org copy; that copy is DRM'd and was skipped, but this self-archived PDF of the 2nd edition is a genuine open copy. No equivalent open copy of the 1986 1st edition was found, so this file cites the 2nd edition specifically.

## Lessons
- [Work backwards from the goal, present forwards from what is known, and leave the gaps visible](../lessons/discover-backwards-present-forwards.md)
- [An informal argument is safe only if you know how the formal one would go](../lessons/an-informal-argument-is-safe-only-if-you-know-the-formal-one.md)
- [When values can be absent, weaken the logic rather than pretend, and definedness becomes visible](../lessons/weaken-the-logic-so-undefinedness-becomes-visible.md)
- [State is history divided by what still matters, and keeping the history instead is the lazy answer](../lessons/state-is-history-quotiented-by-what-still-matters.md)
- [You cannot prove a specification right, so probe it by deriving consequences and checking them against intent](../lessons/validate-a-specification-by-deriving-consequences.md)
- [Record a restriction the abstraction does not need if the implementation wants it, and make the user decide](../lessons/record-a-restriction-the-abstraction-does-not-need.md)
- [Build a theory of your data structure separately, so arguments about algorithms stay about algorithms](../lessons/build-a-theory-of-your-data-structure.md)
- [An invariant records where a clean structure meets a ragged reality, so treat its length as a warning](../lessons/an-invariant-records-a-mismatch-keep-it-short.md)
- [Check that what you are asking for is possible at all, and demote the check when it costs as much as building](../lessons/check-that-what-you-ask-for-is-possible-at-all.md)
- [Write down how a representation is to be read, then check every value you promised can be read out of it](../lessons/write-the-interpretation-and-check-it-covers-everything.md)
- [Read the architecture off the state, because whatever the state does not say gets scattered everywhere else](../lessons/read-the-architecture-off-the-state.md)
