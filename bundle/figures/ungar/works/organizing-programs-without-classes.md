---
type: work
title: "Organizing Programs Without Classes"
figure: ungar
description: Argues that everything classes are normally used for in an object-oriented language — sharing behavior, swapping representations, encapsulation, namespacing — can be done with plain object inheritance in a classless language, given a prototypes/traits split. It works through several idioms (dynamic inheritance for behavioral modes, structured namespaces for well-known objects) to show these aren't special cases requiring extra machinery, just recognizable uses of the same one mechanism. A direct follow-on to the original Self paper, making the case that dropping classes doesn't cost expressiveness.
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
year: 1991
url: https://bibliography.selflanguage.org/_static/organizing-programs.pdf
extraction: complete
survey_pages: 20
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: institutional
tags: [work]
---

# Organizing Programs Without Classes

**Author(s):** David Ungar, Craig Chambers, Bay-Wei Chang, Urs Hölzle
**Venue/year:** Lisp and Symbolic Computation 4(3), Kluwer Academic Publishers, June 1991
**Source:** https://bibliography.selflanguage.org/_static/organizing-programs.pdf — hosted directly on the Self language project's official bibliography site, the project's own archive. Verified reachable (HTTP 200, application/pdf) and content-matched against the page's abstract/author listing. The Phase 1/2 stub flagged this as paywalled with unstable public mirrors; the official project site turns out to host it directly and reliably.

## Lessons
- [A construct that silently bundles two decisions makes every case that wants them apart into a fight](../lessons/one-construct-two-decisions-is-where-designs-get-stuck.md)
- [Code that hand-simulates a mechanism the system already has is evidence the mechanism is too rigid, not that the code is sloppy](../lessons/hand-simulated-dispatch-means-the-real-one-is-too-rigid.md)
- [Names derived from structure cannot disagree with it; names kept beside it always eventually do](../lessons/derive-names-from-structure-so-they-cannot-go-stale.md)
