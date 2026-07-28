---
type: work
title: "The Byzantine Generals Problem"
figure: lamport
description: Formalizes what it means for a set of distributed processes to reach reliable agreement when some of them may fail in arbitrary, even adversarial, ways rather than simply crashing. Proves that agreement is only achievable if fewer than a third of the components are faulty, and gives protocols that reach it under that bound. Became the standard framing for fault tolerance whenever failures can't be assumed to be honest or well-behaved.
subdomains: [distributed-systems-and-concurrency]
year: 1982
url: https://lamport.azurewebsites.net/pubs/byz.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# The Byzantine Generals Problem

**Author(s):** with Robert Shostak and Marshall Pease
**Venue/year:** ACM Transactions on Programming Languages and Systems 4(3), July 1982
**Source:** https://lamport.azurewebsites.net/pubs/byz.pdf — self-archived PDF on Lamport's own site, live and directly downloadable (HTTP 200).

## Lessons
- [Every reliability guarantee is relative to a failure model; state it, and know what weakening it costs](../lessons/make-the-failure-model-explicit.md)
