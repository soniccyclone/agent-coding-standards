---
type: work
title: "Authentication in Distributed Systems: Theory and Practice"
figure: lampson
description: Lays out a theory of authentication built around "principals" and a speaks-for relation that lets a system reason about delegated and role-based authority, not just raw identity. Co-authored with Martin Abadi, Michael Burrows, and Edward Wobber, it pairs the theory with a working implementation covering key distribution, naming, program loading, delegation, access control, and revocation. Underpins much later work on distributed authorization, including the design of Kerberos-adjacent and capability-delegation systems.
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
year: 1992
url: https://bwlampson.site/45-AuthenticationTheoryAndPractice/Acrobat.pdf
survey_pages: 46
survey_text_layer: full
survey_fetch_mb: 0
access: public
host: self-archived
tags: [work]
---

# Authentication in Distributed Systems: Theory and Practice

**Author(s):** Butler Lampson, Martin Abadi, Michael Burrows, Edward Wobber

**Venue/year:** ACM Transactions on Computer Systems 10(4), November 1992, pp. 265-310.

**Source:** https://bwlampson.site/45-AuthenticationTheoryAndPractice/Acrobat.pdf — hosted on Lampson's own personal publications page (bwlampson.site), self-archived.

## Lessons
- [Treat the source of a request as a composed expression rather than an atomic name, and give the composition operators algebraic laws so authority can be computed instead of guessed](../lessons/make-identity-an-expression-not-an-atom.md)
- [Split every decision into an expensive search you do not have to trust and a cheap check you do, then let the untrusted half fail only in the safe direction](../lessons/let-the-untrusted-part-search-and-the-trusted-part-only-check.md)
- [Withdrawing a fact by notifying everyone who holds it is a distributed problem you cannot win; give the fact an expiry and make withdrawal a refusal to renew](../lessons/give-every-belief-an-expiry-instead-of-a-notification-list.md)
- [When authority has to cross a boundary, do not hand it over — mint a weaker one that records both parties and requires both to opt in](../lessons/do-not-transfer-authority-manufacture-a-weaker-one-that-names-both-parties.md)
