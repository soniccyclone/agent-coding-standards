---
type: work
title: "MapReduce and Parallel DBMSs: Friends or Foes?"
figure: stonebraker
description: A response to the early-2010s claim that MapReduce would make parallel relational databases obsolete for large-scale data processing. The authors argue the two are complementary rather than competing: MapReduce excels at ETL-style, schema-on-read processing of messy or unstructured data, while parallel DBMSs remain far more efficient once data is structured and repeatedly queried, citing benchmark comparisons showing large performance gaps in the DBMS's favor on relational-style workloads. It's a direct rebuttal piece, written partly against the trajectory that produced Hadoop, and one of the earlier attempts to intellectually separate the "big data" and "database" communities' claims from their evidence.
subdomains: [databases-and-data-management, distributed-systems-and-concurrency]
year: 2010
url: https://cs.stanford.edu/people/chrismre/cs345/rl/PDBMSvsMR.pdf
extraction: complete
survey_pages: 8
survey_text_layer: full
survey_fetch_mb: 3
access: public
host: third-party-rehost
tags: [work]
---

# MapReduce and Parallel DBMSs: Friends or Foes?

**Author(s):** Michael Stonebraker, Daniel Abadi, David J. DeWitt, Sam Madden, Erik Paulson, Andrew Pavlo, Alexander Rasin
**Venue/year:** Communications of the ACM 53(1), January 2010, pp. 64-71.
**Source:** https://cs.stanford.edu/people/chrismre/cs345/rl/PDBMSvsMR.pdf — course-materials mirror on a Stanford faculty course page (Chris Ré, not an author), third-party rehost; PDF confirmed live (200) and its extracted text opens with the matching "Communications of the ACM | January 2010 | vol. 53 | no. 1" masthead.

## Lessons
- [Separate the model from the implementation before you blame either](../lessons/separate-the-model-from-the-implementation-before-you-blame-either.md)
- [Decide where in a data set's life you pay the cost](../lessons/decide-where-in-a-data-set-s-life-you-pay-the-cost.md)
- [The cost of reaching a system's advertised speed is part of its speed](../lessons/the-cost-of-reaching-a-system-s-advertised-speed-is-part-of-its-speed.md)
