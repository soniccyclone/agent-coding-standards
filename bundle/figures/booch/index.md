---
type: figure
title: Grady Booch
description: b. 1955, Rational Software/IBM. Codified widely-used notations for describing large-system structure; co-created UML.
status: accepted
layer: implementation-mapping
subdomains: [software-engineering-and-architecture]
tags: [figure, accepted]
---

# Grady Booch

**Dates:** b. 1955. Co-founder of Rational Software (later IBM), IBM Fellow.

## Why a candidate, with a caveat
Codified widely-used notations for describing large-system structure, but this leans more toward methodology/notation convention than the rigorous compositional reasoning the vetting philosophy prioritizes — weaker candidate than Parnas or Lehman, included for historical coverage of OO-era architecture practice.

## Top 10 most influential works
Sparse beyond two flagship books:
1. *Object-Oriented Analysis and Design with Applications* (1991/1994, book) — `paywalled`, confirmed genuinely unavailable, see Phase 3 access flag
2. *The Unified Modeling Language User Guide* (1998, with Rumbaugh, Jacobson) — `paywalled`, confirmed genuinely unavailable, see Phase 3 access flag
3. "Object-Oriented Development" (1986, IEEE Transactions on Software Engineering — corrected title/venue, Phase 1 stub had "Object Oriented Design"/"IEEE Software") — `uncertain`, resolved to genuinely unavailable, see Phase 3 access flag
4. *Handbook of Software Architecture* (ongoing) — `public` (Booch self-publishes at handbookofsoftwarearchitecture.com), but see Phase 3 access flag: the handbook proper turned out to be a content-free shell; the four public works actually captured in `works/` come from its Presentations page, not the handbook text itself

## Phase 3 access flag
Verified 2026-07-24. All three of Booch's flagship written works — both books and the
1986 paper — turned out genuinely unavailable through any public channel:

- **OOAD book**: Internet Archive holds it (`archive.org/details/objectorientedan0000booc`) but
  as controlled digital lending (`Access-restricted-item: true` — borrow/checkout with a
  login, not a free download). A GitHub-hosted PDF dump and an epdf.pub scan turned up in
  search but are unambiguous piracy hosts, not the kind of legitimate third-party rehost
  (course mirror, preservation nonprofit) the pilot's policy covers — excluded per the
  public-sources-only rule.
- **UML User Guide**: same situation — Internet Archive lending copy only
  (`archive.org/details/unifiedmodelingl00booc`). A promising-looking direct PDF link
  (patologia.com.mx/informatica/uug.pdf) turned out to be a dead link resolving to an
  expired web host's placeholder page, not the book.
- **"Object-Oriented Development" (1986)**: confirmed closed access via Unpaywall/DOI
  lookup (10.1109/TSE.1986.6312937, IEEE Transactions on Software Engineering) — no OA
  location, `is_oa: false`. No self-archived preprint or technical-report precursor found
  (unlike Codd's IBM Research Reports in the pilot batch, Rational doesn't appear to have
  circulated this one as a public tech report before journal publication).

This leaves Booch's case resting on secondary/tertiary material rather than his primary
texts — a real gap, but the underlying "why a candidate" claim (codifying OO-era
architecture notation and practice) is corroborated well enough by that secondary material
that it doesn't change the accept/caveat call above.

On the **Handbook of Software Architecture** itself: the Phase 1 stub marked the whole site
`public`, which is true but overstates what's there. As of 2026-07-24, the
Concepts/Patterns/Systems/Books sections (i.e., the actual codified handbook the site is
named for) are empty WordPress navigation stubs — bio and menu only, no essays, patterns,
or case studies. The two sections with real content are Papers (an index of one-line
blurbs for Booch's ~40-installment "On Architecture" IEEE Software column, each blurb
linking out to a paywalled full column — the blurbs themselves are public but too thin to
extract lessons from) and Presentations (four embedded, freely-watchable YouTube keynotes).
Those four keynotes are captured as individual `work` files in `works/` since they're the
only substantive public Booch-authored material this pass turned up; the handbook page
itself isn't citable as a standalone work because it has no content of its own to cite.
