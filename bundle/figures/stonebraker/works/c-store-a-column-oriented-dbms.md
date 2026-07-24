---
type: work
title: "C-Store: A Column-oriented DBMS"
figure: stonebraker
description: Proposes a relational database engine built around column-wise rather than row-wise physical storage, aimed at read-heavy analytical workloads where classic row stores waste I/O reading unneeded fields. The paper lays out storage as overlapping sorted column projections, compression tuned to sort order, and a write-optimized staging area reconciled into the read-optimized store, plus a redesigned transaction model to match. C-Store's design directly seeded the commercial column-store wave (Vertica among others) and reframed "one size fits all" RDBMS assumptions.
subdomains: [databases-and-data-management]
year: 2005
url: https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf
access: public
host: institutional
tags: [work]
---

# C-Store: A Column-oriented DBMS

**Author(s):** Michael Stonebraker, Daniel J. Abadi, Adam Batkin, Xuedong Chen, Mitch Cherniack, Miguel Ferreira, Edmond Lau, Amerson Lin, Sam Madden, Elizabeth O'Neil, Pat O'Neil, Alex Rasin, Nga Tran, Stan Zdonik
**Venue/year:** Proceedings of the 31st International Conference on Very Large Data Bases (VLDB), Trondheim, 2005, pp. 553-564.
**Source:** https://www.vldb.org/archives/website/2005/program/paper/thu/p553-stonebraker.pdf — official VLDB conference archive (vldb.org), institutional host; resolves 200 via direct GET (blocks bare HEAD requests, hence the browser-UA check).

## Lessons
_(empty — lesson extraction is Phase 4)_
