---
type: work
title: "Implementing Fault-Tolerant Services Using the State Machine Approach: A Tutorial"
figure: schneider
description: Lays out the state-machine-replication method as a general recipe for building fault-tolerant services — replicate a deterministic state machine across independent processors and use an agreement protocol to make every replica process the same client requests in the same order. Walks through what's required for correctness under both crash failures and Byzantine (arbitrary) failures, and how the technique specializes to different failure and synchrony assumptions. Became the standard reference tutorial that later systems (Paxos-based replication, virtual synchrony, Byzantine fault tolerance) all cite as the unifying model they instantiate.
subdomains: [distributed-systems-and-concurrency]
year: 1990
url: https://www.cs.cornell.edu/fbs/publications/SMSurvey.pdf
extraction: complete
survey_pages: 21
survey_text_layer: full
survey_fetch_mb: 2
access: public
host: self-archived
tags: [work]
---

# Implementing Fault-Tolerant Services Using the State Machine Approach: A Tutorial

**Venue/year:** ACM Computing Surveys 22(4), December 1990.
**Source:** https://www.cs.cornell.edu/fbs/publications/SMSurvey.pdf — self-archived PDF on Schneider's own Cornell publications page (`cs.cornell.edu/fbs/publications/`), live and directly downloadable (HTTP 200, `application/pdf`, ~2.1MB).

## Lessons
- [Redundancy is only available to components whose behavior depends on nothing but their input history](../lessons/push-nondeterminism-outside-the-replicated-core.md)
- [Split a guarantee into independently weakenable parts, then let the application's semantics pay for less of each](../lessons/decompose-a-guarantee-so-semantics-can-pay-for-it.md)
- [Express robustness as the exact assumption your design needs, not as a probability that hides it](../lessons/state-robustness-as-a-bounded-assumption.md)
- [Redundancy is unfinished until you can name who does the final combining, and shared fate can make a component free](../lessons/follow-the-single-failure-argument-past-the-system-edge.md)
- [The cheapest message is the one nobody sends: elapsed time can carry information if you have paid for synchrony](../lessons/silence-as-a-channel.md)
