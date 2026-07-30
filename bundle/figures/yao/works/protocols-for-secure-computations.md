---
type: work
title: "Protocols for Secure Computations"
figure: yao
description: Introduces the general problem of secure multi-party computation through the "Millionaires' Problem" — two parties who want to compare their wealth without revealing the actual amounts — and gives protocols built from one-way functions. Establishes the framework later generalized into garbled-circuit-based two-party and multi-party computation. Also touches on mental poker and oblivious protocols as applications.
subdomains: [algorithms-and-complexity, distributed-systems-and-concurrency]
year: 1982
url: https://cdn.sanity.io/files/r000fwn3/production/0e0427aedfed65c8dd688c094b181feacf4eaab4.pdf
survey_pages: 5
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# Protocols for Secure Computations

**Venue/year:** 23rd Annual IEEE Symposium on Foundations of Computer Science (FOCS 1982), Chicago, pp. 160-164.
**Source:** https://cdn.sanity.io/files/r000fwn3/production/0e0427aedfed65c8dd688c094b181feacf4eaab4.pdf — PDF asset linked from Evervault's papers page (evervault.com/papers/yao), a company-run rehost of classic cryptography papers. Verified by rendering page 1: title, "Andrew C. Yao, University of California, Berkeley," and the Millionaires' Problem introduction are all visible.

## Lessons
- [State a privacy requirement as an equality with what the answer already implies, quantified over what an adversary can compute](../lessons/state-privacy-as-an-equality-with-what-the-answer-implies.md)
- [Concede the deviation you cannot prevent, then define correctness as that deviation being the only one available](../lessons/concede-the-attack-you-cannot-prevent-and-make-it-the-only-one.md)
- [An audit that requires opening the box destroys the property it was protecting; buy tunable doubt instead](../lessons/an-audit-that-opens-the-box-is-not-an-audit.md)
- [Price a new guarantee as a ratio to the unconstrained baseline, so you learn whether the cost belongs to the guarantee or to the problem](../lessons/price-a-guarantee-against-the-unconstrained-baseline.md)
- [A model earns its keep by making impossibility sayable, not by making solutions prettier](../lessons/a-model-earns-its-keep-by-making-impossibility-sayable.md)
- [When a goal is proved unreachable, vary the goal's shape rather than reaching for stronger tools](../lessons/when-a-goal-is-impossible-vary-the-goal-not-the-tools.md)
