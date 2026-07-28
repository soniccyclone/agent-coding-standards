---
type: work
title: "How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs"
figure: lamport
description: Defines sequential consistency, the requirement that a multiprocessor's actual execution look like some valid interleaving of each individual processor's own sequential instruction order. Works out what that requirement demands of both hardware and compilers if it's to actually hold. Became the baseline correctness condition against which weaker, faster memory models are still measured today.
subdomains: [distributed-systems-and-concurrency, operating-systems-and-systems-programming]
year: 1979
url: https://lamport.azurewebsites.net/pubs/multi.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# How to Make a Multiprocessor Computer That Correctly Executes Multiprocess Programs

**Venue/year:** IEEE Transactions on Computers C-28(9), September 1979
**Source:** https://lamport.azurewebsites.net/pubs/multi.pdf — self-archived PDF on Lamport's own site, live and directly downloadable (HTTP 200).

## Lessons
- [Correct parts do not make a correct whole; name the composition condition and price it](../lessons/local-correctness-does-not-compose.md)
