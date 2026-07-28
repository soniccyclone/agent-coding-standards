---
type: work
title: "Programming with Abstract Data Types"
figure: liskov
description: Introduces abstract data types as a language-level construct — a type defined entirely by the operations that can be performed on it, with its internal representation hidden from callers. Argues that this hiding is what actually enables independent, modular program development, since client code can never come to depend on implementation details it cannot see. The ideas here became the basis of CLU, the language Liskov and her students built to test them directly.
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
year: 1974
url: https://dl.acm.org/doi/pdf/10.1145/800233.807045
access: public
host: institutional
tags: [work]
---

# Programming with Abstract Data Types

**Author(s):** with Stephen N. Zilles
**Venue/year:** Proceedings of the ACM SIGPLAN Symposium on Very High Level Languages (SIGPLAN Notices 9(4)), 1974
**Source:** https://dl.acm.org/doi/pdf/10.1145/800233.807045 — ACM Digital Library, gold open access (independently confirmed via Unpaywall, is_oa: true, host_type: publisher). Direct automated fetch is blocked by ACM's Cloudflare bot check (returns a JS challenge page to scripted requests), but the DOI resolves to a freely downloadable PDF for ordinary browser access.

## Lessons
- [Build the machinery for inventing vocabulary, not a guess at the vocabulary itself](../lessons/build-the-vocabulary-maker-not-the-vocabulary.md)
- [A type is exactly its operations, and nothing about how it is stored](../lessons/a-type-is-exactly-its-operations.md)
- [Hiding a detail is worthless unless the language makes it unreachable](../lessons/hiding-a-detail-is-worthless-unless-it-cannot-be-reached.md)
- [Let logical structure and physical structure diverge, and make the compiler own the gap](../lessons/logical-structure-and-physical-structure-are-allowed-to-diverge.md)
