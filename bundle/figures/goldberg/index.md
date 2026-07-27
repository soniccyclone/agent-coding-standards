---
type: figure
title: Adele Goldberg
description: b. 1945, Xerox PARC/ParcPlace. Co-authored the definitive Smalltalk-80 reference works; wrote on environment design as pedagogical/architectural stance.
status: accepted
layer: implementation-mapping
subdomains: [programming-environments-and-object-systems]
tags: [figure, accepted]
---

# Adele Goldberg

**Dates:** b. 1945. Member of Xerox PARC's Learning Research Group, co-developer of Smalltalk-80, later CEO of ParcPlace Systems, ACM President 1984-86.

## Why a candidate
Co-authored the definitive Smalltalk-80 reference works and wrote directly about environment design (the system as something you browse and modify while it runs) as a pedagogical and architectural stance, not just a shipped product.

## Top 10 most influential works
Fewer than 10 works under her sole/lead authorship — most co-authored with Kay/Ingalls/Robson or book-length:
1. "Personal Dynamic Media" (1977, with Kay) — `public` (see Kay entry)
2. *Smalltalk-80: The Language and Its Implementation* (1983, with Robson) — `paywalled` (Internet Archive lending copy)
3. *Smalltalk-80: The Interactive Programming Environment* (1984) — `paywalled`
4. "The Influence of an Object-Oriented Language on the Programming Environment" (1984, book chapter) — `paywalled`
5. "Programmer as Reader" (1987, IEEE Software) — `paywalled`

## Phase 3 access flag
Two works central to the "why a candidate" case — the ones that carry her
argument for environment design as a pedagogical/architectural stance, as
opposed to the Smalltalk-80 reference works, which are just specification —
turn out genuinely unavailable as public sources, confirmed unavailable
rather than just re-flagged:

- **"The Influence of an Object-Oriented Language on the Programming
  Environment"** — corrected venue: ACM Conference on Computer Science
  (CSC-83), 1983, pp. 35-54, not "1984 book chapter" as the Phase 1 stub had
  it (DOI 10.1145/800172.809678). Semantic Scholar lists it as closed access
  with no open PDF on file; ACM Digital Library returns 403 to
  unauthenticated fetches; no self-archived or third-party copy turned up
  via search-engine scraping (WebSearch budget was exhausted mid-task,
  DuckDuckGo/Bing HTML scraping returned nothing usable), CiteSeerX, or
  Internet Archive full-text/proceedings search.
- **"Programmer as Reader"** — IEEE Software 4(5), 1987, pp. 62-70 (DOI
  10.1109/MS.1987.231775), with an earlier "Invited Paper" appearance at
  IFIP Congress 1986, pp. 379-386. Same result: Semantic Scholar closed
  access/no open PDF, IEEE Xplore is subscription-gated, no public mirror
  found by any method tried above.

Both checked directly plus Wayback Machine (no snapshot of an open copy
exists to fall back to, since none was ever found). Flagging per standing
procedure rather than blocking — reviewed in batch later. If either
surfaces later (e.g. a paper copy gets scanned to an institutional archive),
promote to a `work` file at that point.

## Lessons
Goldberg's through-line is that a system's expressive substrate and the
environment you inhabit while working on it are one design problem, and that
the right response to not knowing what will be built is to invest in the
substrate and hand specification to whoever has the problem — a stance whose
success criterion is what users make that the designers never imagined, and
whose implied unit of design is vocabulary, since fixing what may be asked of
a thing is language design at every scale from one class to a whole framework.
Uniformity is the price paid for that: one mechanism for everything with no
privileged tier for arithmetic, control, type definitions, or running
computations, on the explicit bet that the resulting cost is an implementation
cost that technique will retire while structural exceptions never amortize —
and where the machine must be reached, the escape hatch is built to stay
inside the model, invisible in the semantics and visible only in the
specification. She pairs this with unusually disciplined engineering habits:
promise and mechanism written as separate documents, deliberate incompleteness
declared as runnable behavior rather than commentary, a family's whole meaning
derived from a handful of operations with specializations licensed for speed
alone, concepts reified the moment they start living only in explanations, and
a specification complete enough that a stranger can rebuild the machine while
being told plainly that only behavior — never code shape — is being fixed.
Her distinct contribution is to extend all of that to the act of programming
itself: response time and channel quality treated as properties of what can be
thought rather than numbers to tune, the environment treated as material you
reshape from within rather than a pipeline you feed, structural relations
turned into first-class queries because most work is finding out what already
exists, failures delivered as ordinary requests so a halted computation stays
alive to be questioned and resumed, history kept as re-executable actions in
whichever representations the questions demand, and performance settled by a
measuring instrument made of the same material as the thing measured.
