---
type: figure
title: Andrew Chi-Chih Yao
description: b. 1946, Tsinghua. Founded communication complexity; proved the Yao min-max principle.
status: accepted
layer: implementation-mapping
subdomains: [algorithms-and-complexity]
tags: [figure, accepted]
---

# Andrew Chi-Chih Yao

**Dates:** b. 1946. Chinese-American computer scientist; PhD physics (Harvard) then CS (Illinois); now at Tsinghua University.

## Why a candidate
Founded communication complexity as a formal subfield and proved the Yao min-max principle linking randomized worst-case and deterministic average-case complexity — rigorous, technique-driven complexity theory rather than "famous algorithm" work.

## Top 10 most influential works

Phase 3 status (verified against `works/`):
1. "A Journey Through Computer Science" (2021 Kyoto Prize lecture) — `public`, see `works/a-journey-through-computer-science.md`
2. "Some Complexity Questions Related to Distributive Computing" (1979, STOC, founding communication complexity paper) — unavailable, see access flag below
3. "Probabilistic Computations: Toward a Unified Measure of Complexity" (1977, FOCS, Yao's principle) — unavailable, see access flag below
4. "Theory and Applications of Trapdoor Functions" (1982, FOCS) — `public`, see `works/theory-and-applications-of-trapdoor-functions.md`
5. "Protocols for Secure Computations" (1982, FOCS) — `public`, see `works/protocols-for-secure-computations.md`
6. "How to Generate and Exchange Secrets" (1986, FOCS, garbled circuits) — `public`, see `works/how-to-generate-and-exchange-secrets.md`
7. "Should Tables Be Sorted?" (1981, JACM) — `public`, see `works/should-tables-be-sorted.md`

Five of seven works confirmed public via third-party academic rehosts (course pages, a company's papers page) or, for the Kyoto lecture, the Inamori Foundation's own site. The remaining two — both central to Yao's "why a candidate" case — are flagged below.

## Phase 3 access flag

Two works central to the "why a candidate" case have no confirmed public copy anywhere:

- **"Some Complexity Questions Related to Distributive Computing" (STOC 1979)** — the paper that founded communication complexity as a subfield. Checked: ACM Digital Library (403/paywalled), Yao's own Tsinghua IIIS faculty publication list (links only to the paywalled ACM DL entry, no self-archived copy), general web search, and a search for an archived scan of the STOC 1979 proceedings on archive.org (none found). No Wayback snapshot of an open copy exists because no open copy was ever found to snapshot.
- **"Probabilistic Computations: Toward a Unified Measure of Complexity" (FOCS 1977)** — the paper that introduces Yao's min-max principle, the other pillar of the "why a candidate" case. Checked: IEEE Xplore (closed access), oa.mg (closed access), Semantic Scholar (no PDF available), Yao's own faculty page (links only to the paywalled IEEE Xplore entry), and a search for an archived scan of the FOCS 1977 proceedings (none found).

Both papers predate routine self-archiving norms and were never picked up by course-page rehosts the way the 1981/1982/1986 papers were. The corpus's coverage of Yao's foundational communication-complexity and min-max-principle contributions therefore rests on secondary sources (lecture notes, textbooks, the Kyoto Prize retrospective) rather than the primary papers themselves.

## Lessons
Yao's characteristic move is to convert a question you cannot answer into one you can, usually by changing what is being quantified over. A guarantee that only switches on past every real input is not an answer, so invert it into a question about reach; a which-is-better comparison becomes a game between the two answers, from which the equivalence can be read off; a growing checklist of tests becomes one quantification over every test a checker could run. He treats hardness as a resource rather than an obstacle — a proof that something is impossible can be spent to buy a capability elsewhere, and every impossibility result is somebody's guarantee if you go find the field where it is good news. His discipline about foundations is strict: rest the edifice on one named assumption stated before the first result, build on the weakest interface that suffices rather than on an instance's incidental structure, and argue in the smallest model that makes the reasoning legible before widening it until every rival design sits inside. Where a guarantee cannot be obtained outright he assumes only a sliver of it and builds the amplifier that makes it total, or concedes the deviation he cannot prevent and defines correctness as that deviation being the only one available. Two lessons are pointed warnings for anyone specifying security: an audit requiring you to open the box destroys the property it protects, and permission to store a function of someone's data is a categorically different power from permission to store the data.
