---
type: work
title: "A Simple Technique for Handling Multiple Polymorphism"
figure: ingalls
description: Addresses the double-dispatch problem — how to pick the right method when an operation's behavior depends on the runtime types of two objects, not just the one receiving the message (the classic case being arithmetic between mixed numeric types). Ingalls proposes a lightweight convention using ordinary single-dispatch message sends to resolve this without extending the language, keeping to idiomatic Smalltalk-80 style. Originally flagged as paywalled in the earlier pass; a legitimate open copy exists via a university course's public bibliography mirror.
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
year: 1986
url: https://algoritmos-iii.github.io/assets/bibliografia/simple-technique-for-handling-multiple-polymorphism.pdf
survey_pages: 3
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: third-party-rehost
tags: [work]
---

# A Simple Technique for Handling Multiple Polymorphism

**Venue/year:** OOPSLA '86 / ACM SIGPLAN Notices, Vol. 21, No. 11, November 1986.
**Source:** https://algoritmos-iii.github.io/assets/bibliografia/simple-technique-for-handling-multiple-polymorphism.pdf — live PDF, rehosted as a course bibliography mirror (Algoritmos III). Verified 200 OK, application/pdf, 3 pages.

## Lessons
- [Treat a dispatch as one degree of type-uncertainty removed, and chain as many as the problem has variable terms](../lessons/each-dispatch-removes-one-degree-of-polymorphism.md)
