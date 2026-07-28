---
type: work
title: "Impossibility of Distributed Consensus with One Faulty Process"
figure: lynch
description: Proves that in an asynchronous message-passing system, no deterministic protocol can guarantee consensus among processes if even a single process might fail (by simply stopping) — the classic "FLP" result. The argument works by showing an adversary can always find some execution that delays a decision indefinitely, without ever explicitly crashing any process. Became the reference impossibility bound the whole distributed-consensus literature (Paxos, Raft, partial-synchrony models) is defined in reaction to.
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
year: 1985
url: http://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf
survey_pages: 9
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: institutional
tags: [work]
---

# Impossibility of Distributed Consensus with One Faulty Process

**Author(s):** with Michael J. Fischer, Michael S. Paterson
**Venue/year:** Journal of the ACM 32(2), April 1985
**Source:** http://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf — hosted on MIT CSAIL's Theory of Distributed Systems group publications page (Lynch's own research group, university-hosted), live and directly downloadable (HTTP 200). Note: this is the JACM journal version; a separate 1983 PODS preliminary version also lives on the same page as pods83-flp.pdf.

## Lessons
- [A distributed algorithm can only depend on what its participants can actually tell apart](../lessons/correctness-can-only-rest-on-what-a-process-can-distinguish.md)
- [Reason about a concurrent system by the set of outcomes still reachable, not by the history that produced the current state](../lessons/track-what-outcomes-are-still-open-not-what-has-happened.md)
- [A fault-tolerance claim is meaningless until you say when the faults are allowed to happen](../lessons/impossibility-is-a-statement-about-when-the-adversary-may-act.md)
- [When you cannot agree on an answer, try agreeing on who counts and derive the answer](../lessons/reduce-agreement-on-data-to-agreement-on-membership.md)
