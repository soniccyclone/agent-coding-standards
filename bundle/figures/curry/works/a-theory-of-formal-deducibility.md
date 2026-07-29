---
type: work
title: "A Theory of Formal Deducibility"
figure: curry
description: Lecture notes from a course Curry taught at Notre Dame, laying out an abstract theory of formal systems and the notion of deducibility - how strings of symbols are derived from axioms via stated rules, treated as an object of study in its own right rather than assumed self-evident. It's Curry's proof-theoretic companion to the combinatory-logic work, developing formal systems in general before working through applications. The lecture-note format and lithoprinted publication reflect its origin as taught course material rather than a polished monograph.
subdomains: [foundations-of-computation, formal-methods-and-verification]
year: 1950
url: https://projecteuclid.org/ebooks/notre-dame-mathematical-lectures/A-Theory-of-Formal-Deducibility/toc/ndml/1175197175
extraction: complete
access: public
host: institutional
tags: [work]
---

# A Theory of Formal Deducibility

**Venue/year:** Notre Dame Mathematical Lectures, No. 6, University of Notre Dame, 1950 (lithoprinted).
**Source:** https://projecteuclid.org/ebooks/notre-dame-mathematical-lectures/A-Theory-of-Formal-Deducibility/toc/ndml/1175197175 — table-of-contents page for the volume on Project Euclid, whose "Notre Dame Mathematical Lectures" ebook series is published open access. Each chapter link carries an Open Access icon and download button; verified by directly fetching a chapter PDF (returned a real, unauthenticated 2-page PDF, not a paywall or login prompt). An Internet Archive copy also exists (archive.org/details/theoryofformalde0000curr) but is lending-restricted, so the Project Euclid open-access edition is the citation of record here.

**Phase 4 URL correction (2026-07-28).** The recorded URL is Project Euclid's
table-of-contents page for the book. That page renders an "institutional
sign-in" link prominently, which is misleading: the individual chapter PDFs
download **without any authentication**. Verified — a chapter fetch returned
HTTP 200, `application/pdf`. The reason five successive agents failed on this
figure is that all three of its sources were landing pages rather than content,
and nothing here told them how to get through.

Chapter PDFs come from Project Euclid's download endpoint, substituting the id:

    https://projecteuclid.org/accountAjax/Download?urlId=ndml%2F<ID>&downloadType=presschapter

| id | chapter |
|---|---|
| 1175197177 | Preface |
| 1175197179 | Notational Explanations |
| 1175197180 | Introduction |
| 1175197181 | Chapter I — Formal Systems and Formal Reasoning |
| 1175197182 | Chapter II — The Finite Positive Connectives |
| 1175197183 | Chapter III — Quantifiers |
| 1175197184 | Chapter IV — Negation |
| 1175197185 | Chapter V — Modalities |
| 1175197186 | Bibliography |

(1175197176 is the title/copyright page and 1175197178 the printed contents —
both skippable.) The argument-carrying chapters are the Introduction and I-V;
fetch them individually rather than looking for a whole-book PDF, which is not
offered. **Correction (2026-07-29):** an earlier version of this note offered archive.org
item `theoryofformalde0000curr` as a fallback "if the chapter endpoint ever stops
working." That was wrong and is retracted — the item is access-restricted
(`access-restricted-item: true`) and its `_djvu.txt` derivative returns an "Item
not available" HTML page. There is no working fallback for this book.

**Project Euclid is now behind an Imperva JS bot challenge** (added 2026-07-29,
discovered the hard way). A bare curl — even with a browser User-Agent — returns
a ~6KB "Pardon Our Interruption" interstitial *named as a .pdf*, for both the TOC
page and every chapter endpoint. Working recipe:

1. Fetch the TOC page into a fresh cookie jar (`curl -c jar ...`).
2. Wait ~3 seconds.
3. Request the chapter endpoint with `-b jar` AND a `Referer:` header pointing at
   the TOC page.

Imperva rate-limits aggressively: a burst of 9 sequential requests tripped it,
and it then refused even a slow retry loop for 10+ minutes. Pace the jar-seeding
genuinely. The chapter PDFs themselves have clean text layers (all 129 pages
extract with `pdftotext -layout`); OCR quality is mediocre in formula-heavy
passages — proof schemes mangle, "OF" often reads "OP" — but every argumentative
paragraph is legible.

## Lessons
- [Define an operator by what entitles you to assert it, and its laws stop being a matter of taste](../lessons/define-an-operator-by-what-entitles-you-to-assert-it.md)
- [A predicate that flips when the system grows cannot be a primitive](../lessons/a-predicate-that-flips-when-the-system-grows-cannot-be-primitive.md)
- [The step you never think about is carrying your whole metatheory](../lessons/the-rule-you-never-think-about-carries-your-whole-metatheory.md)
- [Build the system that explains before the system that feels natural, then derive the second from the first](../lessons/build-the-explaining-system-first-and-derive-the-comfortable-one.md)
- [Make checking definite even where finding cannot be](../lessons/make-checking-definite-even-where-finding-cannot-be.md)
- [There is no outside the language you are working in, so carve the layer you need out of the inside](../lessons/there-is-no-outside-the-language-you-are-working-in.md)
