---
type: work
title: "SIMULA - an ALGOL-Based Simulation Language"
figure: dahl
description: The first published introduction to Simula for a general programming-languages audience, written for Knuth's "Programming Languages" department in CACM. It motivates quasi-parallel processing (coroutines) and system-description-by-simulation as the design problems Simula answers, and gives a simplified account of the language's core concepts ahead of the full formal definition. Historically it predates the 1967 class/subclass mechanism, so it documents Simula I rather than the object-oriented Simula 67 that followed.
subdomains: [programming-environments-and-object-systems, programming-languages-and-semantics]
year: 1966
url: https://web.archive.org/web/20250123230819/https://dl.acm.org/doi/pdf/10.1145/365813.365819
access: public
host: institutional
tags: [work]
---

# SIMULA - an ALGOL-Based Simulation Language

**Author(s):** Ole-Johan Dahl, Kristen Nygaard
**Venue/year:** Communications of the ACM, Volume 9, Number 9 (September 1966), pp. 671-678.
**Source:** ACM has this article as free ("bronze" open access, confirmed via Unpaywall: `oa_status: bronze`, `is_oa: true`) at https://dl.acm.org/doi/pdf/10.1145/365813.365819, but the live dl.acm.org URL returns HTTP 403 to automated fetch tools (bot-blocking, not a paywall gate — Unpaywall's classification and the Wayback capture below both confirm the underlying PDF is genuinely free). Citing the Wayback Machine snapshot instead, which resolves directly: https://web.archive.org/web/20250123230819/https://dl.acm.org/doi/pdf/10.1145/365813.365819 (curl 200, application/pdf, 1.1MB; visually confirmed as the correct paper — title page reads "SIMULA — an ALGOL-Based Simulation Language, Ole-Johan Dahl and Kristen Nygaard, Norwegian Computing Center, Oslo, Norway," CACM Vol. 9/No. 9, p. 671). Not part of the Phase 1 top-10 list; added during Phase 3 verification as a clearly public, clearly central work (the first published Simula paper, with Dahl as lead author) surfaced while checking the softwarepreservation.org Simula bibliography page.

## Lessons
- [Give every entity its own place in its own text, so a life spread over time still reads as one story](../lessons/give-each-entity-its-own-sequence-control.md)
- [Separate the concurrency in your description from the concurrency in your execution, and make the scheduler an inspectable data structure](../lessons/concurrency-as-description-with-scheduling-as-data.md)
- [Choose the entity whose viewpoint already holds the information the behavior needs, and the program shrinks](../lessons/decompose-from-the-viewpoint-that-already-holds-the-information.md)
- [Let the machine's cost model set the grain of your abstractions, and refuse any mechanism whose expense is invisible to whoever uses it](../lessons/let-the-machines-cost-model-set-the-grain-of-your-abstractions.md)
- [Reach a new paradigm by lifting a restriction off an existing primitive, not by adding one](../lessons/an-object-is-a-block-instance-with-the-stack-discipline-removed.md)
- [Aim to be a middle layer: extend a base you refuse to replace, and become a base others need not replace](../lessons/build-a-middle-layer-language.md)
- [Build the vocabulary that forces a complete description, then make the description itself the program](../lessons/make-the-description-the-executable-artifact.md)
- [Give each component its own resumption point, and the state machine you would have hand-encoded disappears](../lessons/give-each-component-its-own-sequence-control.md)
- [Refuse expressive power whose cost is invisible at the point where it is used](../lessons/refuse-power-whose-cost-is-invisible.md)
- [To get a new kind of thing, take a construct you trust and delete one of its incidental restrictions](../lessons/objects-are-blocks-freed-from-the-stack.md)
