---
type: work
title: "Towards a Theory of Type Structure"
figure: reynolds
description: Independently arrives at what Girard had already found in a different guise — a lambda calculus, later called System F, in which functions can take types as arguments, so a single term can carry a whole family of types rather than one fixed type. Works out the basic proof theory of these polymorphic functions and lays the groundwork for what would later be formalized as parametric polymorphism. Now treated, alongside Girard's independent discovery, as foundational to the type systems behind ML, Haskell, and their descendants.
subdomains: [programming-languages-and-semantics, foundations-of-computation]
year: 1974
url: https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/theotypestr.pdf
survey_pages: 18
survey_text_layer: ocr
survey_fetch_mb: 0
access: public
host: self-archived
extraction: complete
tags: [work]
---

# Towards a Theory of Type Structure

**Venue/year:** Programming Symposium (Colloque sur la Programmation), Paris, LNCS vol. 19, Springer-Verlag, 1974, pp. 408-425.
**Source:** https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/theotypestr.pdf — live PDF (HTTP 200), a scanned copy self-archived by Reynolds in his own CMU FTP directory (filename `theotypestr.pdf`, under his `jcr` account). Also independently mirrored by CMU (`~crary/819-f09/Reynolds74.pdf`) and Northeastern's PRL group, both live, confirming this is the correct paper.
**Reading copy:** `scratchpad/ocr-text/reynolds__towards-a-theory-of-type-structure.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [Judge a discipline by an invariance it guarantees, not by the mistakes it happens to catch](../lessons/judge-a-discipline-by-the-invariance-it-guarantees.md)
- [Duplication that refuses to factor means you are missing a kind of parameter, not a clever trick](../lessons/duplication-that-will-not-factor-means-a-missing-kind-of-parameter.md)
- [A theorem you cannot even state is telling you some construct's meaning is too thin](../lessons/an-unstateable-theorem-means-a-meaning-is-too-thin.md)
- [A feature added for convenience can change what is computable, so measure its power instead of assuming](../lessons/a-convenience-feature-can-change-what-is-computable.md)
