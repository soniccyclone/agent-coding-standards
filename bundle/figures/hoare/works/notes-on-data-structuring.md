---
type: work
title: "Notes on Data Structuring"
figure: hoare
description: A long expository chapter working through how to reason formally about data types and their representations, covering enumerations, arrays, records, discriminated unions, and pointer-based structures, and building toward the correctness-of-representation ideas Hoare formalized separately the same year. Written as a companion to Dijkstra's and Dahl's essays in the same volume, aimed at showing that data structuring deserves the same disciplined treatment as control-flow structuring. Its terminology and worked examples influenced how type systems and abstract data types were later taught.
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
year: 1972
url: https://www.cs.cornell.edu/courses/cs4860/2018fa/lectures/Notes-on-Data-Structuring_Hoare.pdf
survey_pages: 92
survey_text_layer: full
survey_fetch_mb: 4
access: public
host: third-party-rehost
tags: [work]
---

# Notes on Data Structuring

**Author(s):** C. A. R. Hoare
**Venue/year:** Chapter II in O.-J. Dahl, E. W. Dijkstra, and C. A. R. Hoare, *Structured Programming* (Academic Press, 1972), pp. 83-174.
**Source:** https://www.cs.cornell.edu/courses/cs4860/2018fa/lectures/Notes-on-Data-Structuring_Hoare.pdf — course-reading mirror hosted by Cornell University (CS4860, Fall 2018). Content verified directly by decompressing the PDF's text streams: opening text reads "II. Notes on Data Structuring".

## Lessons
- [Keep the notation you design in deliberately unimplemented, so its expensive conveniences must be spent rather than tolerated](../lessons/keep-the-design-notation-deliberately-unimplemented.md)
- [An operation belongs in the primitive set exactly when its efficiency depends on the representation](../lessons/an-operation-is-primitive-when-its-cost-depends-on-the-representation.md)
