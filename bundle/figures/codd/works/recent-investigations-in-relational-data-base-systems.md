---
type: work
title: "Recent Investigations in Relational Data Base Systems"
figure: codd
description: A solo-authored survey paper reviewing progress on several fronts of relational database theory at once — normalization, query sublanguages for programmers and casual users, reconciling multiple views over one model, and data exchange across distributed sites. Its normalization section is the earliest public record of what later got named Boyce-Codd Normal Form: Codd credits Boyce by name for jointly developing a cleaner definition of third normal form that drops the somewhat arbitrary prime/non-prime attribute distinction used in the original 2NF/3NF definitions.
subdomains: [databases-and-data-management]
year: 1974
url: https://www.fsmwarden.com/Codd/rec-1975.pdf
extraction: complete
access: public
host: third-party-rehost
tags: [work]
---

# Recent Investigations in Relational Data Base Systems

**Venue/year:** Proceedings of the 1974 IFIP Congress, Stockholm, Sweden, pp. 1017-1021 (North-Holland); also circulated as IBM Research Report RJ1385, San Jose, California, April 1974.
**Source:** https://www.fsmwarden.com/Codd/rec-1975.pdf — live page, HTTP 200 verified via curl (application/pdf, 6 pages), content-checked by extracting the text: opens "RECENT INVESTIGATIONS IN RELATIONAL DATA BASE SYSTEMS / E. F. Codd / IBM Research Laboratory," and its normalization section reads "More recently, Boyce and Codd developed the following definition..." followed by the revised third-normal-form definition now called BCNF. The filename's "1975" is the host's own naming quirk; the paper's content, references, and every secondary citation (dblp, SIGMOD's Codd bibliography) place it at IFIP 1974.
**Host:** third-party-rehost — fsmwarden.com, a personal site hosting scanned copies of several Codd IBM Research Reports (the same host used for Codd's "Further Normalization" work file in this corpus), not Codd's or IBM's own site.

## Correction to Phase 1/2 stub
This resolves item 8's `uncertain` flag to public, and separately corrects the earlier assumption that BCNF's origin traces only to an unpublished internal memo — the Boyce-Codd definition was presented in this public, citable 1974 paper. Found during the Boyce (co-author) Phase 3 pass rather than Codd's own pilot pass; backfilled here for consistency.

## Lessons
- [Refine a definition until its arbitrary distinctions vanish](../lessons/refine-definitions-until-arbitrary-distinctions-vanish.md) — the BCNF passage is the primary source
- Also cited on [Bind programs to information, never to its arrangement](../lessons/bind-programs-to-information-not-arrangement.md) (the fourth data-exchange policy) and [State the properties of the result; let the system choose the procedure](../lessons/state-properties-let-the-system-choose-the-procedure.md) (the sublanguage survey)
