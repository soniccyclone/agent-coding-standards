---
type: figure
title: Jeffrey D. Ullman
description: b. 1942, Stanford. Turned relational and Datalog theory into the standard graduate curriculum. Turing Award 2020.
status: accepted
layer: design-thought
subdomains: [databases-and-data-management]
tags: [figure, accepted]
---

# Jeffrey D. Ullman

**Dates:** b. 1942. Stanford (Ascherman Professor Emeritus); co-founded the Stanford InfoLab.

## Why a candidate
Turned relational and Datalog theory into the standard graduate curriculum — his textbooks are the mechanism by which "reason from the algebra/logic, not the engine" became the field's default teaching.

## Top 10 most influential works
1. Datalog and recursive-query papers (various, 1980s, self-archived on Stanford InfoLab) — `public`
2. *Principles of Database Systems* (1980, textbook) — `paywalled` (1st ed. borrowable on Internet Archive)
3. *Principles of Database and Knowledge-Base Systems, Vols I & II* (1988/1989) — `paywalled`
4. "The Theory of Joins in Relational Databases" (1979, with Aho, Beeri) — `paywalled`
5. "Universality of Data Retrieval Languages" (1979, with Aho) — `paywalled`
6. *Database Systems: The Complete Book* (2000+, with Garcia-Molina, Widom) — `paywalled`

## Phase 3 access flag

Verified public works (`bundle/figures/ullman/works/`): two self-archived Datalog/deductive-database
papers — "Assigning an Appropriate Meaning to Database Logic with Negation" (1994) and "A Comparison
Between Deductive and Object-Oriented Database Systems" (1991), both live on Ullman's own Stanford
InfoLab page — plus one addition beyond the original top-10, *Mining of Massive Datasets*
(Leskovec/Rajaraman/Ullman), a full free textbook self-archived at the same site.

Everything else on the original top-10 remains genuinely inaccessible, and this cuts at the heart of the
"why a candidate" claim, which rests on his **textbooks** having become the standard vehicle for teaching
relational/Datalog theory:

- *Principles of Database Systems* (1980) and *Principles of Database and Knowledge-Base Systems* (Vols
  I/II, 1988/89) — checked Internet Archive: both are `access-restricted-item: true`, controlled-digital-
  lending only (DRM'd Adobe Digital Editions loan, not a public copy). No self-archived PDF/PS found on
  Ullman's InfoLab page or elsewhere.
- *Database Systems: The Complete Book* — still in print, no free copy found; the book's own page
  (`ullman-books.html` → `dscb.html`) links only to course slides/errata, not the text.
- "The Theory of Joins in Relational Databases" (1979, with Aho, Beeri) and "Universality of Data
  Retrieval Languages" (1979, with Aho) — both sit behind ACM's Digital Library. Third-party metadata
  (Unpaywall, OpenAlex) tags them "bronze"/"gold" OA with a `dl.acm.org/doi/pdf/...` link, but ACM DL
  fronts every page — OA or not — with Cloudflare bot-blocking that returned 403 to both `curl` (with a
  real browser User-Agent) and WebFetch; I could not independently confirm actual public accessibility
  per the verification rule. No self-archived copy found on Ullman's site or Alfred Aho's Columbia page.

Net effect: the specific database-theory textbooks and 1979 relational-theory papers named in the
original pass are not independently verifiable as public through this process, though the broader
"textbook as curriculum mechanism" claim is still evidenced by *Mining of Massive Datasets* and by the
self-archived Datalog papers above.
