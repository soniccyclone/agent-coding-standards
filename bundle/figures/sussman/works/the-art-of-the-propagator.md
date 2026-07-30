---
type: work
title: "The Art of the Propagator"
figure: sussman
description: Proposes a programming model where computation is a network of small autonomous machines ("propagators") linked by shared cells that accumulate partial information, with each machine continuously watching the cells it cares about and adding whatever new facts it can deduce. Because propagators only ever add information to a cell (never overwrite it) and run independently of any global schedule, the model sidesteps a lot of the ordering and mutation headaches that come with conventional imperative or even standard dataflow programming. It reads as Sussman revisiting constraint-propagation ideas from decades earlier with a more disciplined formal foundation.
subdomains: [programming-languages-and-semantics, distributed-systems-and-concurrency]
year: 2009
url: https://groups.csail.mit.edu/mac/users/gjs/6.945/readings/art.pdf
survey_pages: 50
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# The Art of the Propagator

**Author(s):** Alexey Radul and Gerald Jay Sussman
**Venue/year:** MIT CSAIL Technical Report MIT-CSAIL-TR-2009-002, January 26, 2009 (draft dated December 13, 2008).
**Source:** https://groups.csail.mit.edu/mac/users/gjs/6.945/readings/art.pdf — live PDF self-archived in Sussman's own MIT CSAIL directory, served as a reading for his 6.945 course.

## Lessons
- [Find the assumption too basic to be stated, negate it, and follow the consequences — that is where new models come from](../lessons/negate-the-assumption-nobody-writes-down.md)
- [Put the combining rule in the shared place rather than in the producers, and directions of flow you never enumerated become available](../lessons/put-the-combining-rule-in-the-shared-place.md)
- [If updates only ever add information, order stops mattering — and the single operation that takes information away costs you that freedom everywhere](../lessons/one-retraction-costs-you-the-whole-schedule-freedom.md)
- [Carry each conclusion's grounds with it, and inconsistency stops being fatal because consistency becomes local](../lessons/carry-the-grounds-and-inconsistency-stops-being-fatal.md)
- [Put failure in the infrastructure and make it name its causes; a dead end that knows why it failed eliminates a region instead of a point](../lessons/make-failure-informative-instead-of-encoding-around-it.md)
- [Bookkeeping attached to an aggregate can never be finer than the aggregate, and its errors are silent because the answers stay right](../lessons/metadata-is-only-as-precise-as-the-unit-it-is-attached-to.md)
