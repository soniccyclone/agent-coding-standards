---
type: work
title: "The End of an Architectural Era (It's Time for a Complete Rewrite)"
figure: stonebraker
description: Argues that the 1970s-era RDBMS architecture — disk-oriented buffer pool, lock-based concurrency control, write-ahead logging — carries overhead that no longer matches modern OLTP workloads which fit largely in memory. The paper introduces H-Store, a distributed main-memory OLTP prototype built around single-threaded partition execution and lightweight or absent logging, and reports throughput over two orders of magnitude above a leading commercial RDBMS on TPC-C-style workloads. It became the direct intellectual precursor to VoltDB and the broader NewSQL/in-memory OLTP movement.
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
year: 2007
url: https://www.vldb.org/conf/2007/papers/industrial/p1150-stonebraker.pdf
extraction: complete
survey_pages: 11
survey_text_layer: full
survey_fetch_mb: 2
access: public
host: institutional
tags: [work]
---

# The End of an Architectural Era (It's Time for a Complete Rewrite)

**Author(s):** Michael Stonebraker, Samuel Madden, Daniel J. Abadi, Stavros Harizopoulos, Nabil Hachem, Pat Helland
**Venue/year:** Proceedings of the 33rd International Conference on Very Large Data Bases (VLDB), Vienna, 2007, pp. 1150-1160 (industrial track).
**Source:** https://www.vldb.org/conf/2007/papers/industrial/p1150-stonebraker.pdf — official VLDB conference archive (vldb.org), institutional host; resolves 200 via direct GET with a browser user agent (bare HEAD/curl default UA gets a 403 from vldb.org's front end — false negative on a naive check, confirmed live by both curl GET and WebFetch).

## Lessons
- [Measure useful work as a fraction of runtime](../lessons/measure-useful-work-as-a-fraction-of-runtime.md)
- [Name the workload property that lets a mechanism be deleted](../lessons/name-the-workload-property-that-lets-a-mechanism-be-deleted.md)
- [A closed set of programs turns runtime decisions into design-time ones](../lessons/a-closed-set-of-programs-turns-runtime-decisions-into-design-time-ones.md)
- [Escalate mechanism on measured failure, not on its possibility](../lessons/escalate-mechanism-on-measured-failure-not-on-its-possibility.md)
- [A live copy can replace a record of the past](../lessons/a-live-copy-can-replace-a-record-of-the-past.md)
- [The seam between two languages is where the cost collects](../lessons/the-seam-between-two-languages-is-where-the-cost-collects.md)
