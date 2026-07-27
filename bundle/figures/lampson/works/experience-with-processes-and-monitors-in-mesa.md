---
type: work
title: "Experience with Processes and Monitors in Mesa"
figure: lampson
description: Co-authored with David Redell, this reports on what happened when Hoare-style monitors met real, large concurrent programs written in Mesa at PARC. It works through the rough edges theory hadn't anticipated — nested monitor calls, competing definitions of what a wait should do, priority scheduling, timeouts, and abnormal exit from a monitored region — and proposes concrete fixes validated against working systems. The "Mesa semantics" for condition variables it settles on (signal as a hint rather than an immediate handoff) went on to become the dominant model in POSIX threads and most later concurrency libraries.
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
year: 1980
url: https://bwlampson.site/23-ProcessesInMesa/Acrobat.pdf
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
_(empty — lesson extraction is Phase 4)_
