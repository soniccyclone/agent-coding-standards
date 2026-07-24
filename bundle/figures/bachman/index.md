---
type: figure
title: Charles W. Bachman
description: 1924-2017, GE/Honeywell. Designed IDS and led CODASYL's network data model - the navigational alternative Codd's algebra displaced. Turing Award 1973.
status: accepted
layer: implementation-mapping
subdomains: [databases-and-data-management]
tags: [figure, accepted]
---

# Charles W. Bachman

**Dates:** 1924-2017. Engineer at General Electric, later Honeywell/Cullinane.

## Why a candidate (contrast case, weighted lower per brief)
Represents the navigational/pointer-chasing alternative to the relational model — including him sharpens why Codd's algebraic approach was the epistemic break, not an incremental improvement on the CODASYL convention. Mechanism-first reasoning, deliberately weighted lower than Codd/Fagin/Abiteboul/Ullman.

## Top 10 most influential works
Impact runs through one system (IDS) and one standards effort (CODASYL) more than a broad publication record:
1. "The Programmer as Navigator" (1973 Turing lecture) — `public` (amturing.acm.org)
2. CODASYL Data Base Task Group (DBTG) Report (1971, principal architect) — `public` (widely archived by university libraries)
3. "Data Structure Diagrams" (1969) — `uncertain`
4. Integrated Data Store (IDS) system design (GE, 1963-64) — largely unpublished internal design — `uncertain`
5. "The Origin of the Integrated Data Store (IDS)" (2009, retrospective oral history) — `paywalled`

## Phase 3 access flag

Verified 2026-07-24. Of the original top-10, only item 1 ("The Programmer as
Navigator") turned out to have a working free copy on first pass; item 5's
gap is filled by a public substitute. Items 2-4 are genuinely unavailable
despite being central to the "why a candidate" case:

- **#2, CODASYL DBTG Report (1971)** — the report Bachman principally
  architected, and the concrete artifact behind "led CODASYL's network data
  model" in this figure's own description. No public full text found. The
  ACM SIGMOD Anthology page that search results point to
  (sigmod.org/publications/anthology/vol6/codasyl.htm) is a *listing* of
  what was distributed on a physical anthology DVD - every PDF link on it
  resolves to a permanent `pdfMissing.htm` placeholder, confirmed both live
  and in Wayback (2024 snapshot, same placeholders), so it was likely never
  actually served from the website. Sold via the ACM Digital Library
  (paywalled, confirmed 403). An academia.edu upload exists but 403'd on
  direct fetch and academia.edu requires signup to read even when it
  resolves, so it doesn't qualify as a public source here. No Wayback,
  HathiTrust, Google Books, or DTIC copy of the report itself located
  (DTIC has secondary reports *about* CODASYL implementations, not the DBTG
  report).
- **#3, "Data Structure Diagrams" (1969)** — the paper "Bachman diagram" is
  named after. Only found behind the ACM Digital Library paywall
  (dl.acm.org/doi/pdf/10.1145/1017466.1017467, confirmed 403). Checked the
  usual rehost patterns that worked for other figures in this corpus
  (course mirrors, esp.org, fsmwarden.com's personal database-theory
  archive - which mirrors Codd extensively but has no Bachman directory) and
  found nothing. Semantic Scholar and SciSpace both catalog it but link back
  to the same paywalled ACM copy rather than hosting an independent PDF.
- **#4, IDS system design (GE, 1963-64)** — as Phase 1 already noted, this
  was internal GE engineering documentation, not a publication; there's no
  expectation a public artifact exists, so this isn't really a discovery
  gap so much as confirmation the "work" is a system rather than a citable
  document. The closest public window into it is the oral-history
  substitute added below.
- **#5, 2009 IEEE Annals retrospective** — confirmed paywalled at both the
  ACM Digital Library and IEEE Xplore (the latter returned HTTP 418 to
  automated fetches; Project MUSE lists only a summary). Filled by a public
  substitute instead: a 2011 IEEE History Center oral-history interview
  (`works/oral-history-charles-bachman.md`) in which Bachman gives essentially
  the same IDS-origin account in his own words, hosted on ETHW
  (ieee-run institutional archive, verified live).

Net: 2 of 5 original top-10 items converted to public `work` files (#1 as
listed, plus a substitute for #5); #2 and #3 - arguably the two most
load-bearing items on the list - remain inaccessible anywhere public that
could be found. Flagging per standing procedure rather than blocking; Phase
4 lesson extraction for Bachman will have a thinner public-primary-source
base than the other pilot figures as a result.
