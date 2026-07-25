---
type: work
title: "Recent Investigations in Relational Data Base Systems"
figure: boyce
description: A solo-authored Codd survey paper reviewing progress on several fronts of relational database theory at once — normalization, query sublanguages for programmers and casual users, reconciling multiple views over one model, and data exchange across distributed sites. Its normalization section is the earliest public record of what later got named Boyce-Codd Normal Form, Codd crediting Boyce by name for jointly developing a cleaner definition of third normal form that drops the somewhat arbitrary prime/non-prime attribute distinction used in the original 2NF/3NF definitions. Solely authored by Codd, but it is the actual paper trail behind the figure's namesake result, and it corrects the earlier assumption on file that the definition traces only to an unpublished internal memo.
subdomains: [databases-and-data-management]
year: 1974
url: https://www.fsmwarden.com/Codd/rec-1975.pdf
access: public
host: third-party-rehost
tags: [work]
---

# Recent Investigations in Relational Data Base Systems

**Author(s):** E. F. Codd (paper credits R. F. Boyce by name within the text for co-developing the normal-form definition discussed below)
**Venue/year:** Proceedings of the 1974 IFIP Congress, Stockholm, Sweden, pp. 1017-1021 (North-Holland); also circulated as IBM Research Report RJ1385, San Jose, California, April 1974.
**Source:** https://www.fsmwarden.com/Codd/rec-1975.pdf — live page, HTTP 200 verified directly with curl (application/pdf, 6 pages), and content-checked by extracting the text: it opens "RECENT INVESTIGATIONS IN RELATIONAL DATA BASE SYSTEMS / E. F. Codd / IBM Research Laboratory," and its normalization section reads "More recently, Boyce and Codd developed the following definition..." followed by the revised third-normal-form definition now called BCNF. The filename's "1975" is the host's own naming quirk; the paper's content, references, and every secondary citation (dblp, SIGMOD's Codd bibliography) place it at IFIP 1974.
**Host:** third-party-rehost — fsmwarden.com, a personal site hosting scanned copies of several Codd IBM Research Reports (the same host already used for Codd's "Further Normalization" work file in this corpus), not Codd's or IBM's own site.

## Correction to Phase 1/2 stub
The figure stub described BCNF's origin as "an unpublished IBM internal memo with Codd, 1974, later formalized in secondary literature." That's superseded by this find: the Boyce-Codd definition was presented in this public, citable 1974 paper, not left in an internal memo. No `## Phase 3 access flag` is needed — nothing here turned out to be unavailable.

## Lessons
- [Of two equivalent definitions, the one needing fewer auxiliary concepts is the right one](../lessons/prefer-the-definition-with-fewer-concepts.md)
- [Component-wise invariants don't certify the composition](../lessons/local-normal-forms-dont-certify-the-whole.md)
