---
type: work
title: "Consensus in the Presence of Partial Synchrony"
figure: lynch
description: Introduces partial synchrony as a middle ground between the fully synchronous and fully asynchronous system models, formalizing several variants (unknown fixed timing bounds, or bounds that only hold eventually). Shows which of these variants admit consensus protocols that tolerate faulty processes and which don't, sidestepping the FLP impossibility result by weakening the asynchrony assumption rather than the fault model. The partial-synchrony framing it introduces underlies how later protocols like Paxos and PBFT reason about liveness under realistic network conditions.
subdomains: [distributed-systems-and-concurrency, algorithms-and-complexity]
year: 1988
url: https://groups.csail.mit.edu/tds/papers/Lynch/jacm88.pdf
survey_pages: 36
survey_text_layer: full
survey_fetch_mb: 3
access: public
host: institutional
tags: [work]
---

# Consensus in the Presence of Partial Synchrony

**Author(s):** with Cynthia Dwork, Larry Stockmeyer
**Venue/year:** Journal of the ACM 35(2), April 1988
**Source:** https://groups.csail.mit.edu/tds/papers/Lynch/jacm88.pdf — hosted on MIT CSAIL's Theory of Distributed Systems group publications page (university-hosted), live and directly downloadable (HTTP 200).

## Lessons
- [Let timing assumptions buy you progress and nothing else, so safety never depends on the clock](../lessons/keep-timing-assumptions-out-of-safety.md)
- [Refusing to call a slow participant broken is what makes a fault budget mean anything](../lessons/a-slow-participant-is-not-a-broken-one.md)
- [Solve the problem in the model you wish you had, then pay for that model once, in a layer you can swap](../lessons/build-the-model-you-wish-you-had-then-pay-for-it-once.md)
