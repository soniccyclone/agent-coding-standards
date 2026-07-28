---
type: work
title: "Reflections on an Operating System Design"
figure: lampson
description: A retrospective on the CAL time-sharing system built for the CDC 6400 at Berkeley, candidly assessing what worked and what didn't. The system used capabilities for protection and a strictly layered structure meant to isolate each layer from failures above it; Lampson walks through how that isolation broke down once levels got added to the memory hierarchy, and what a better structure would have looked like. An early example of a builder writing up a system's failure modes as carefully as its successes.
subdomains: [operating-systems-and-systems-programming]
year: 1976
url: https://bwlampson.site/15-ReflectionsOnOS/Acrobat.pdf
survey_pages: 29
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Reflections on an Operating System Design

**Author(s):** Butler Lampson

**Venue/year:** Communications of the ACM 19(5), May 1976, pp. 251-265.

**Source:** https://bwlampson.site/15-ReflectionsOnOS/Acrobat.pdf — hosted on Lampson's own personal publications page (bwlampson.site), self-archived.

## Lessons
- [A foundation that supplies every mechanism is not yet a usable system, and no checklist of mechanisms can tell you whether it is adequate — only building its most demanding client can](../lessons/a-kernel-is-not-a-system-and-only-its-hardest-client-can-tell-you.md)
- [An indirection is only real if absence is representable and detectable; without a fault on 'not here yet' you must materialize everything in advance, and that eagerness spreads into layers with no business knowing](../lessons/indirection-you-cannot-fault-on-is-not-indirection.md)
- [When an outer layer's job is to construct the inner layer's objects, self-defense cannot mean withholding the dangerous power — give it the power over a bounded territory instead](../lessons/bound-the-dangerous-power-instead-of-refusing-it.md)
- [A rule about how costs must be attributed is an architectural constraint in disguise: decide what it forbids before you adopt it, and make sure every exhaustible resource is inside the model rather than beside it](../lessons/an-accounting-rule-is-an-architectural-constraint-in-disguise.md)
