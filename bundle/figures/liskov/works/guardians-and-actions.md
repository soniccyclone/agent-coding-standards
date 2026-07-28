---
type: work
title: "Guardians and Actions: Linguistic Support for Robust, Distributed Programs"
figure: liskov
description: Introduces Argus, a language built around two constructs for distributed programming: guardians, which are modules that own and protect long-lived data at a single node, and atomic actions (transactions), which give programmers a way to group operations across guardians so that node crashes and network partitions can't leave shared state in an inconsistent half-updated condition. Makes the case that failure handling has to be a language-level concern, not something bolted on by convention in application code. Direct ancestor of the transactional and replication ideas Liskov's group extended in Argus's later implementation papers and in PBFT.
subdomains: [distributed-systems-and-concurrency, programming-languages-and-semantics]
year: 1983
url: https://courses.mpi-sws.org/ds-ws18/papers/liskov-argus.pdf
extraction: complete
survey_pages: 24
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
tags: [work]
---

# Guardians and Actions: Linguistic Support for Robust, Distributed Programs

**Author(s):** with Robert Scheifler
**Venue/year:** ACM Transactions on Programming Languages and Systems (TOPLAS) 5(3), July 1983
**Source:** https://courses.mpi-sws.org/ds-ws18/papers/liskov-argus.pdf — course-reading mirror hosted by MPI-SWS (Max Planck Institute for Software Systems) for a distributed-systems seminar, not the author's own site; content-verified (title, both author names, and abstract text present in the PDF). Note: a separate MIT OpenCourseWare link surfaced during the search hosts a discussion outline about this paper, not the paper itself — not used here.

## Lessons
- [Funnel every failure into the one outcome your program already knows how to handle](../lessons/funnel-every-failure-into-the-one-outcome-you-already-handle.md)
- [Hide the mechanism and the location; never hide the possibility of failure or the cost](../lessons/hide-the-mechanism-never-the-possibility-of-failure.md)
- [Make the unit of failure nestable and failure handling becomes composable](../lessons/make-the-unit-of-failure-nestable.md)
- [Your representation choice sets the concurrency ceiling, not your concurrency constructs](../lessons/your-representation-choice-sets-the-concurrency-ceiling.md)
