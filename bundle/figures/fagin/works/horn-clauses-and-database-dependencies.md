---
type: work
title: "Horn Clauses and Database Dependencies"
figure: fagin
description: Defines "implicational dependencies" and "embedded implicational dependencies," a broad class of first-order sentences that subsumes essentially every previously studied database dependency (functional, multivalued, join, embedded multivalued, and more) as a special case. Introduces "faithfulness with respect to direct product" as the key technical property, proves this whole dependency class is faithful, and uses it to establish that Armstrong relations (relations realizing exactly the dependencies implied by a given set) exist even for these very general dependencies — a result earlier techniques couldn't reach. Also proves that projections of dependency classes are again dependency classes of the same kind, closing a gap left open by prior functional-dependency-only results.
subdomains: [databases-and-data-management, foundations-of-computation]
year: 1982
url: https://web.archive.org/web/20210806201654/https://researcher.watson.ibm.com/researcher/files/us-fagin/jacm82.pdf
extraction: complete
access: public
host: self-archived
tags: [work]
---

# Horn Clauses and Database Dependencies

**Venue/year:** Journal of the ACM 29(4), October 1982, pp. 952-985 (extended abstract at STOC 1980).
**Source:** Wayback Machine snapshot (2021-08-06) of Fagin's self-archived PDF, formerly at researcher.watson.ibm.com/researcher/files/us-fagin/jacm82.pdf. HTTP 200 verified via curl; PDF content confirmed by direct read (34-page paper, title/abstract/body all match).

## Lessons
- [Define a class by the property your results need, not by listing its members](../lessons/define-a-class-by-the-property-your-results-need.md)
- [Build the most permissive instance your spec allows, then read the missing rules off it](../lessons/build-the-most-permissive-legal-instance-and-read-the-gaps-off-it.md)
- [Separate the criterion from the witness that satisfies it](../lessons/separate-the-criterion-from-the-witness-that-satisfies-it.md)
- [A guarantee proved without a finiteness assumption may not survive one](../lessons/a-guarantee-proved-without-finiteness-may-not-survive-finiteness.md)
- [The shape of your proof is feedback on your definitions](../lessons/the-shape-of-your-proof-is-feedback-on-your-definitions.md)
- [Check how a property behaves under the operations you plan to apply to it](../lessons/a-property-of-the-whole-need-not-be-a-property-of-the-part.md)
