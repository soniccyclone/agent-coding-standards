---
type: work
title: "On the Semantics of Updates in Databases"
figure: vardi
description: Tackles the view-update problem — when a user requests a change to a view or to a database known only incompletely, what changes to the underlying data actually satisfy that request, and which of several candidate translations should count as correct. Fagin, Ullman, and Vardi formalize criteria for judging update translations sound, giving one of the first rigorous accounts of update semantics under incomplete information rather than treating updates as an afterthought to query semantics.
subdomains: [databases-and-data-management]
year: 1983
url: http://www.cs.rice.edu/~vardi/papers/pods83.pdf
survey_pages: 15
survey_text_layer: ocr
survey_fetch_mb: 0
access: public
host: self-archived
extraction: complete
tags: [work]
---

# On the Semantics of Updates in Databases

**Author(s):** Ronald Fagin, Jeffrey D. Ullman, Moshe Y. Vardi
**Venue/year:** PODS 1983 (2nd ACM SIGACT-SIGMOD Symposium on Principles of Database Systems).
**Source:** http://www.cs.rice.edu/~vardi/papers/pods83.pdf — verified live (HTTP 200, application/pdf, ~865KB), self-archived on Vardi's own Rice University papers page.
**Reading copy:** `scratchpad/ocr-text/vardi__on-the-semantics-of-updates-in-databases.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.
**Host:** self-archived — author's own site.

## Lessons
- [Decide whether your state is closed under its own consequences, because that decides what deletion means](../lessons/decide-whether-your-state-is-closed-under-consequence.md)
- [Paired operations are rarely duals: check which direction your invariant survives](../lessons/paired-operations-are-rarely-duals-check-which-way-the-invariant-survives.md)
- [An ambiguous outcome should widen what you record, not reject the request](../lessons/an-ambiguous-answer-should-widen-the-state-not-reject-the-request.md)
- [Rank your invariants explicitly, or automatic repair will sacrifice whichever one is cheapest to drop](../lessons/rank-your-invariants-or-repair-will-sacrifice-the-wrong-one.md)
- [What you chose to record explicitly decides what a change means, not the change operator](../lessons/what-you-record-explicitly-decides-what-a-change-means.md)
- [Read a request as evidence in the caller's vocabulary, not as a description of the end state](../lessons/read-a-request-as-evidence-not-as-a-description-of-the-end-state.md)
- [To state a constraint that spans two structures, build the single structure that contains both](../lessons/to-constrain-a-relation-between-two-structures-build-the-one-containing-both.md)
