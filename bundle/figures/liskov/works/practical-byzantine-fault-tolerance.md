---
type: work
title: "Practical Byzantine Fault Tolerance"
figure: liskov
description: Presents PBFT, the first Byzantine-fault-tolerant replication protocol shown to run efficiently enough for real asynchronous network deployments rather than just theoretical models. Tolerates up to one-third of replicas behaving arbitrarily — including maliciously — while still guaranteeing safety and liveness, using a three-phase agreement protocol with cryptographic message authentication instead of expensive digital signatures on every message. Its performance results are what moved Byzantine fault tolerance from a theoretical curiosity to something systems builders would actually consider using.
subdomains: [distributed-systems-and-concurrency]
year: 1999
url: http://web.archive.org/web/20251211170759/http://pmg.csail.mit.edu/papers/osdi99.pdf
survey_pages: 14
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Practical Byzantine Fault Tolerance

**Author(s):** with Miguel Castro
**Venue/year:** Proceedings of the Third Symposium on Operating Systems Design and Implementation (OSDI '99), February 1999
**Source:** Originally self-archived at http://pmg.csail.mit.edu/papers/osdi99.pdf (MIT Programming Methodology Group). The live pmg.csail.mit.edu host is currently unreachable (connection refused / 403 as of this check), so citing the Wayback Machine snapshot instead: http://web.archive.org/web/20251211170759/http://pmg.csail.mit.edu/papers/osdi99.pdf — content-verified (contains "Byzantine", "Castro", "castro,liskov" running header).

## Lessons
- [Never let a timing guess be load-bearing for correctness; spend it on progress instead](../lessons/never-let-a-timing-guess-be-load-bearing-for-correctness.md)
- [Design so that no irreversible step rests on a judgment you cannot make reliably](../lessons/no-irreversible-step-on-an-unreliable-judgment.md)
- [When a primitive is too expensive, find out which of its powers you actually use](../lessons/when-a-primitive-is-too-expensive-ask-which-of-its-powers-you-use.md)
- [Independence of failure is something you build, not a number you pick](../lessons/independence-of-failure-is-built-not-assumed.md)
