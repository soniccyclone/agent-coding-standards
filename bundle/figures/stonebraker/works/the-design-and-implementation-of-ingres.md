---
type: work
title: "The Design and Implementation of INGRES"
figure: stonebraker
description: Describes the operational 1976 INGRES system — one of the first working relational DBMSs — as a set of cooperating UNIX processes on PDP-11 hardware, covering its query language (QUEL), storage structures, and query decomposition strategy. It is the primary evidence that the relational model, published by Codd as theory in 1970, could be built and run at reasonable performance on commodity hardware rather than remaining an abstract proposal. The paper's process-per-query, OS-hosted architecture also set an early template for building a DBMS on top of a general-purpose operating system rather than bare metal.
subdomains: [databases-and-data-management, operating-systems-and-systems-programming]
year: 1976
url: https://www2.eecs.berkeley.edu/Pubs/TechRpts/1976/Archive/ERL-m-577.pdf
extraction: complete
survey_pages: 36
survey_text_layer: full
survey_fetch_mb: 6
access: public
host: institutional
tags: [work]
---

# The Design and Implementation of INGRES

**Author(s):** Michael Stonebraker, Eugene Wong, Peter Kreps, Gerald Held
**Venue/year:** ACM Transactions on Database Systems 1(3), 1976, pp. 189-222 (also circulated as UC Berkeley ERL technical report M577/M-577).
**Source:** https://www2.eecs.berkeley.edu/Pubs/TechRpts/1976/Archive/ERL-m-577.pdf — UC Berkeley EECS Technical Reports archive (institutional), linked directly from the department's own tech-report index page at https://www2.eecs.berkeley.edu/Pubs/TechRpts/1976/29338.html; PDF confirmed live (200) and its extracted text shows the matching 1976 copyright notice.

## Lessons
- [Three features that rewrite the same tree are one feature](../lessons/three-features-that-rewrite-the-same-tree-are-one-feature.md)
- [A system that describes itself in its own terms inherits its own tooling](../lessons/a-system-that-describes-itself-in-its-own-terms-inherits-its-own-tooling.md)
- [Solve one case completely and make everything else reduce to it](../lessons/solve-one-case-completely-and-make-everything-else-reduce-to-it.md)
- [An atomic unit can only be as large as what you can undo](../lessons/an-atomic-unit-can-only-be-as-large-as-what-you-can-undo.md)
