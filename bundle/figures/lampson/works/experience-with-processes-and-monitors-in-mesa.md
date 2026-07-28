---
type: work
title: "Experience with Processes and Monitors in Mesa"
figure: lampson
description: Co-authored with David Redell, this reports on what happened when Hoare-style monitors met real, large concurrent programs written in Mesa at PARC. It works through the rough edges theory hadn't anticipated — nested monitor calls, competing definitions of what a wait should do, priority scheduling, timeouts, and abnormal exit from a monitored region — and proposes concrete fixes validated against working systems. The "Mesa semantics" for condition variables it settles on (signal as a hint rather than an immediate handoff) went on to become the dominant model in POSIX threads and most later concurrency libraries.
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
year: 1980
url: https://bwlampson.site/23-ProcessesInMesa/Acrobat.pdf
extraction: complete
survey_pages: 23
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Experience with Processes and Monitors in Mesa

**Author(s):** Butler Lampson, David Redell

**Venue/year:** Communications of the ACM 23(2), February 1980, pp. 106-117.

**Source:** https://bwlampson.site/23-ProcessesInMesa/Acrobat.pdf — hosted on Lampson's own personal publications page (bwlampson.site), self-archived.

## Lessons
- [Deliberately weaken what a synchronization event promises, because a weaker guarantee makes every proof local and every later extension free](../lessons/weaken-the-promise-to-localize-the-proof.md)
- [Mutual exclusion between participants of very different speeds destroys the fast one's worst-case guarantee, so a speed boundary is where a coordination model has to change](../lessons/never-share-exclusion-across-a-speed-boundary.md)
- [The measured price of a primitive decides which program structures are available to you, so publish the price and treat granularity as a consequence of it](../lessons/the-price-of-a-primitive-decides-which-structures-you-can-think-in.md)
