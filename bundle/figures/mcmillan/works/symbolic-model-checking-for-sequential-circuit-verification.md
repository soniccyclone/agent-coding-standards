---
type: work
title: "Symbolic Model Checking for Sequential Circuit Verification"
figure: mcmillan
description: The journal version of McMillan's thesis work, showing symbolic model checking applied to real industrial hardware designs rather than toy examples. Burch, Clarke, Long, McMillan, and Dill verify sequential circuits directly against CTL specifications by combining BDD-based state-space representation with a technique for handling the interaction between control logic and data paths. The paper demonstrated the approach was not just theoretically sound but practical on circuits far too large for explicit-state tools of the era.
subdomains: [formal-methods-and-verification]
year: 1994
url: https://mcmil.net/pubs/TCAD94.pdf
extraction: complete
survey_pages: 24
survey_text_layer: full
survey_fetch_mb: 2
access: public
host: self-archived
tags: [work]
---

# Symbolic Model Checking for Sequential Circuit Verification

**Author(s):** Jerry R. Burch, Edmund M. Clarke, David E. Long, Kenneth L. McMillan, David L. Dill
**Venue/year:** IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 13, no. 4, April 1994.
**Source:** https://mcmil.net/pubs/TCAD94.pdf — self-archived PDF on McMillan's own site, live and directly downloadable (HTTP 200, first page confirmed: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, Vol. 13, No. 4, April 1994," title and full author list match). Note: originally flagged `paywalled` in the Phase 1/2 pass with a co-author list of "Clarke, Grumberg" — that was incorrect on both counts; the actual authors are Burch, Clarke, Long, McMillan, Dill, and a self-archived copy exists on McMillan's site.

## Lessons
- [Let cost track the description's structure, not the population it describes](../lessons/let-cost-track-structure-not-size.md)
- [Never assemble the object you only need to interrogate; the peak intermediate is your real limit](../lessons/the-peak-intermediate-is-the-real-limit.md)
- [Measure the exponent of a parameterised family, not the runtime of a benchmark](../lessons/measure-the-exponent-not-the-benchmark.md)
- [Spend human judgement where search is expensive and machine effort where it is cheap](../lessons/spend-human-judgement-where-search-is-expensive.md)
