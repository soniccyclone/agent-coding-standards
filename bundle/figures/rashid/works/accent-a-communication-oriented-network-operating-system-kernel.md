---
type: work
title: "Accent: A Communication Oriented Network Operating System Kernel"
figure: rashid
description: Describes Accent, the CMU kernel that preceded Mach, built around a single abstraction - typed messages sent between processes over location-independent ports - through which every kernel service, including virtual memory and device access, is exposed. Covers Accent's copy-on-write large-message IPC and its integration of virtual memory with the communication system so that network transparency falls out of the messaging model rather than being bolted on. Direct architectural predecessor of Mach's IPC and VM design.
subdomains: [operating-systems-and-systems-programming, distributed-systems-and-concurrency]
year: 1981
url: http://web.archive.org/web/20170810225453/http://cseweb.ucsd.edu/classes/wi08/cse221/papers/rashid81.pdf
extraction: complete
survey_pages: 12
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# Accent: A Communication Oriented Network Operating System Kernel

**Author(s):** Richard Rashid, George Robertson
**Venue/year:** 8th ACM Symposium on Operating Systems Principles (SOSP), Pacific Grove, CA, December 1981, pp. 64-75.
**Source:** http://web.archive.org/web/20170810225453/http://cseweb.ucsd.edu/classes/wi08/cse221/papers/rashid81.pdf — Wayback Machine snapshot (Aug 2017) of a UCSD graduate-OS-course reading mirror; the original cseweb.ucsd.edu copy now 403s live and CMU's own institutional repository copy (kilthub.cmu.edu, article 6602927) sits behind bot-challenge middleware that blocks non-interactive fetches, so the course-mirror snapshot is the resolvable public copy. Confirmed a genuine 12-page PDF (verified via `file`), not a challenge/error page.

## Lessons
- [Choose the semantics you can reason about, then buy the cost back underneath where nobody has to know](../lessons/choose-the-semantics-you-can-reason-about-and-buy-the-cost-back-underneath.md)
- [Name the role, never the thing currently filling it, and design so a stranger can stand in the middle](../lessons/name-the-role-not-whatever-currently-implements-it.md)
- [State a request's real requirements as data, because the code that could exploit them has not been written yet](../lessons/state-requirements-as-data-so-parties-you-never-anticipated-can-act-on-them.md)
- [An abstraction everyone knows is slow is usually just the one the hardware was never tuned for](../lessons/an-abstraction-known-to-be-slow-is-usually-just-the-one-the-hardware-was-not-tuned-for.md)
- also carries [A system that grows a new access mechanism per resource kind is losing the argument it started by winning](../lessons/one-kind-of-reference-for-every-kind-of-resource.md) and [Put mechanism in the privileged core and push every decision out of it](../lessons/the-privileged-core-should-hold-mechanism-and-refuse-to-hold-decisions.md)
