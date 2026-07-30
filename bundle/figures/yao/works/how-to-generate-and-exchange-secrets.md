---
type: work
title: "How to Generate and Exchange Secrets"
figure: yao
description: The paper that introduces what's now called Yao's garbled circuits — a way to encrypt a boolean circuit so a second party can evaluate it on private inputs without learning anything beyond the output. Built to solve general two-party secure computation, generalizing the earlier Millionaires' Problem work. Became the basis for most practical secure multi-party computation systems built since.
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
year: 1986
url: https://mit6875.github.io/FA23HANDOUTS/yao-garbled-circuits.pdf
survey_pages: 6
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# How to Generate and Exchange Secrets

**Venue/year:** 27th Annual Symposium on Foundations of Computer Science (FOCS 1986), Toronto, pp. 162-167.
**Source:** https://mit6875.github.io/FA23HANDOUTS/yao-garbled-circuits.pdf — course handout page for MIT 6.875 (Cryptography), a standard rehost of foundational papers for the class. Verified via fetch: extracted text confirms title, author "Andrew Chi-Chih Yao," and FOCS 1986 venue.

## Lessons
- [Make abandonment a first-class correctness property, and specify it as a recovery procedure the injured party can run](../lessons/correctness-must-cover-the-party-who-walks-away.md)
- [Rest the whole edifice on one named assumption, stated before the first result](../lessons/rest-everything-on-one-named-assumption.md)
- [When two incomparable things must change hands, stop balancing the trade and build one gate that opens for both](../lessons/stop-balancing-the-trade-and-build-a-shared-gate.md)
- [When the protocol cannot be strengthened, strengthen what participants must arrive holding — and pick the arrival format that lets stages chain](../lessons/change-the-entry-contract-to-buy-a-stronger-guarantee.md)
