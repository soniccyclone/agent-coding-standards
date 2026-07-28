---
type: work
title: "Sacrificing Serializability to Attain High Availability of Data in an Unreliable Network"
figure: fischer
description: Presents a replicated-dictionary algorithm that stays available and keeps processing updates through node and network failures (including lost or duplicated messages) by giving up full serializability in exchange for a weaker, best-effort consistency guarantee relative to whatever communication actually succeeded. Needs no transaction log or synchronized clocks, and targets applications like calendars and mail where eventual, approximate consistency is good enough. An early, concrete data point for the availability-versus-consistency tradeoff that the CAP theorem would later formalize.
subdomains: [distributed-systems-and-concurrency, databases-and-data-management]
year: 1982
url: https://sites.cs.ucsb.edu/~agrawal/spring2011/ugrad/p70-fischer.pdf
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# Sacrificing Serializability to Attain High Availability of Data in an Unreliable Network

**Author(s):** with Alan Michael
**Venue/year:** Proceedings of the 1st ACM SIGACT-SIGMOD Symposium on Principles of Database Systems (PODS '82), pages 70-75, March 1982
**Source:** https://sites.cs.ucsb.edu/~agrawal/spring2011/ugrad/p70-fischer.pdf — third-party rehost, a UCSB course reading page (Divyakant Agrawal's Spring 2011 course materials), live and directly downloadable (HTTP 200). Text extracted from the PDF confirms title, authors, and abstract match. The ACM Digital Library and a DTIC technical-report mirror (ADA111261) both exist but are paywalled/access-blocked respectively; this course mirror is the confirmed-public copy.

## Lessons
- [A weaker guarantee still deserves an exact one: specify degraded operation, do not merely apologize for it](../lessons/give-degraded-mode-an-exact-specification.md)
- [Whether a replicated thing can be weakened is decided by its operations, not by its protocol](../lessons/choose-the-operation-set-that-can-be-reconciled.md)
