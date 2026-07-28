---
type: work
title: "How to Build a Highly Available System Using Consensus"
figure: lampson
description: A tutorial-style distillation of Lamport's Paxos algorithm, framing it as the go-to way to get consensus among unreliable processes without relying on real-time guarantees. Lampson's practical contribution is the observation that full consensus is too expensive to run on every operation, so real systems should use it sparingly — to elect and renew leases — and let the lease-holder handle routine work unilaterally. Widely credited with making Paxos legible to systems builders who found Lamport's original presentation opaque.
subdomains: [distributed-systems-and-concurrency]
year: 1996
url: https://bwlampson.site/58-Consensus/Acrobat.pdf
survey_pages: 17
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# How to Build a Highly Available System Using Consensus

**Author(s):** Butler Lampson

**Venue/year:** Distributed Algorithms (WDAG '96), Lecture Notes in Computer Science 1151, Springer, 1996.

**Source:** https://bwlampson.site/58-Consensus/Acrobat.pdf — hosted on Lampson's own personal publications page (bwlampson.site), self-archived.

## Lessons
- [Redundancy only helps if the redundant parts are functions: force determinism first, and the whole reliability problem collapses into agreeing on one sequence of inputs](../lessons/make-the-component-a-function-then-agreement-is-the-only-hard-part.md)
- [Spend the expensive agreement on who is allowed to decide, not on each decision — and notice that the cheap path then rests on a physical assumption, not a logical one](../lessons/spend-agreement-on-who-decides-not-on-what-is-decided.md)
- [A specification's state is a useful fiction nobody has to be able to compute, and every bit of nondeterminism you leave in it is room for an implementation you haven't thought of yet](../lessons/a-specification-state-is-a-fiction-and-nondeterminism-is-the-room-you-leave.md)
- [Act only on facts that can never become false again, and keep strengthening the invariant until it is something each participant can maintain alone — the algorithm is what is left over](../lessons/act-only-on-facts-that-cannot-be-retracted.md)
