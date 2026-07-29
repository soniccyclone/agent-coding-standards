---
type: work
title: "The Use of Name Spaces in Plan 9"
figure: thompson
description: Explains Plan 9's central organizing idea — that every resource, local or remote, is represented as a file, and each process assembles its own private view of the world by mounting and binding those files into a per-process name space rather than sharing one global hierarchy. This lets unrelated processes, or the same process at different times, see entirely different arrangements of the same underlying services without any of them being aware of the others' view. It generalizes and extends the file-centric philosophy of Unix into an explicit mechanism for building distributed systems.
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
year: 1993
url: https://9p.io/sys/doc/names.pdf
extraction: complete
survey_pages: 7
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: institutional
tags: [work]
---

# The Use of Name Spaces in Plan 9

**Author(s):** Rob Pike, Dave Presotto, Ken Thompson, Howard Trickey, Phil Winterbottom
**Venue/year:** Operating Systems Review 27(2), April 1993, pp. 72-76.
**Source:** https://9p.io/sys/doc/names.pdf — live PDF, hosted on 9p.io, the official Plan 9 from Bell Labs documentation site maintained as the project's own archive. Content verified 2026-07-24 (decoded PDF text stream shows title, authors, and Bell Laboratories affiliation).

## Lessons
- [Make the naming context a per-process parameter, not a property of the machine](../lessons/make-the-naming-context-a-per-process-parameter.md)
- [A component that consumes the same interface it provides can be interposed anywhere](../lessons/a-component-that-consumes-the-interface-it-provides-can-be-interposed.md)
- [An abstraction's limit is what it implies, not what it can be made to encode](../lessons/an-abstractions-limit-is-what-it-implies-not-what-it-can-encode.md)
