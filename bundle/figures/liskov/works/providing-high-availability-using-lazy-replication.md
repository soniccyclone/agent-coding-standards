---
type: work
title: "Providing High Availability Using Lazy Replication"
figure: liskov
description: Proposes replicating data across sites using causal rather than total operation ordering, which is cheaper to enforce than strict consistency while still being strong enough for services like shared mail or bulletin boards where users mainly need to see a causally coherent view of updates. Lets a client read from and write to whichever replica is nearest or available, with updates propagated lazily in the background instead of synchronously agreed on before any operation returns. An early, practical argument for weakening consistency deliberately in exchange for availability, well ahead of the CAP-theorem-era vocabulary that would later formalize the same trade-off.
subdomains: [distributed-systems-and-concurrency, databases-and-data-management]
year: 1992
url: https://www.cs.princeton.edu/courses/archive/spr24/cos418/papers/lazy.pdf
survey_pages: 32
survey_text_layer: full
survey_fetch_mb: 2
access: public
host: third-party-rehost
tags: [work]
---

# Providing High Availability Using Lazy Replication

**Author(s):** with Rivka Ladin, Liuba Shrira, Sanjay Ghemawat
**Venue/year:** ACM Transactions on Computer Systems 10(4), November 1992
**Source:** https://www.cs.princeton.edu/courses/archive/spr24/cos418/papers/lazy.pdf — course-reading mirror hosted by Princeton's COS 418 (Distributed Systems) archive, not the authors' own site; content-verified (PDF metadata title "Providing high availability using lazy replication", author "Ladin").

## Lessons
- [Consistency strength belongs to the operation, not to the system](../lessons/consistency-strength-is-a-per-operation-choice.md)
- [If you can name the dependency, you do not need the coordination](../lessons/if-you-can-name-the-dependency-you-do-not-need-the-coordination.md)
- [A consistency guarantee ends where information flow leaves your interface](../lessons/your-guarantee-ends-where-information-flow-leaves-your-api.md)
- [Never show anyone an effect that is less durable than the promise you made about it](../lessons/never-show-anyone-an-effect-less-durable-than-your-promise.md)
