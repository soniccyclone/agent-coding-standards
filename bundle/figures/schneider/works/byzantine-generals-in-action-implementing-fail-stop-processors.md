---
type: work
title: "Byzantine Generals in Action: Implementing Fail-Stop Processors"
figure: schneider
description: Shows how to approximate an idealized "fail-stop processor" — one that halts cleanly instead of producing corrupted output, and whose failure is reliably detectable by others — out of ordinary processors that can fail in arbitrary (Byzantine) ways, using replication and a Byzantine-agreement protocol among the replicas. Connects this construction back to the state-machine approach: fail-stop processors are the clean abstraction that lets higher-level fault-tolerant services be designed without reasoning about arbitrary failure modes directly. Originally flagged `paywalled`, but a self-archived copy lives alongside Schneider's other papers on his own Cornell page.
subdomains: [distributed-systems-and-concurrency]
year: 1984
url: https://www.cs.cornell.edu/fbs/publications/ByzGensInAction.pdf
extraction: complete
survey_pages: 10
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Byzantine Generals in Action: Implementing Fail-Stop Processors

**Venue/year:** ACM Transactions on Computer Systems 2(2), May 1984.
**Source:** https://www.cs.cornell.edu/fbs/publications/ByzGensInAction.pdf — self-archived PDF on Schneider's own Cornell publications page (`cs.cornell.edu/fbs/publications/`), live and directly downloadable (HTTP 200, `application/pdf`, ~650KB). Phase 1 pass had flagged this `paywalled` (it does sit behind ACM DL at dl.acm.org/doi/10.1145/190.357399); the author's self-archived copy resolves that.

## Lessons
- [An assumption is a debt: you don't know what a design costs until someone builds the thing it assumes](../lessons/price-the-assumption-you-build-on.md)
- [When an ideal is unbuildable, keep its interface and make the gap a parameter](../lessons/index-an-unreachable-abstraction-by-its-breaking-point.md)
- [Noticing a fault is cheaper than surviving one, so buy redundancy per layer instead of uniformly](../lessons/detect-cheaply-mask-expensively.md)
- [Compare two architectures by which event fires their expensive operation, not by how expensive the operation is](../lessons/compare-designs-by-what-triggers-the-expensive-operation.md)
