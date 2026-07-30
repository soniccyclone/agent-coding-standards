---
type: work
title: "Types, Abstraction, and Parametric Polymorphism"
figure: reynolds
description: Formalizes what it means for a polymorphic function to behave "the same way" at every type it's instantiated at, a property Reynolds names parametricity, and gives it a precise relational semantics. This paper is the origin of the idea later popularized by Wadler as "theorems for free" — that a polymorphic function's type alone, without inspecting its implementation, can constrain and sometimes fully pin down its behavior.
subdomains: [programming-languages-and-semantics, formal-methods-and-verification]
year: 1983
url: https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/typesabpara.pdf
survey_pages: 11
survey_text_layer: ocr
survey_fetch_mb: 0
access: public
host: self-archived
extraction: complete
tags: [work]
---

# Types, Abstraction, and Parametric Polymorphism

**Venue/year:** Information Processing 83, Proceedings of the IFIP 9th World Computer Congress, Paris, September 1983, North-Holland, pp. 513-523.
**Source:** https://www.cs.cmu.edu/afs/cs/user/jcr/ftp/typesabpara.pdf — live PDF (HTTP 200), a scanned copy self-archived by Reynolds in his own CMU FTP directory (filename `typesabpara.pdf`, under his `jcr` account).
**Reading copy:** `scratchpad/ocr-text/reynolds__types-abstraction-and-parametric-polymorphism.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [A type is a restriction on what you are allowed to say, not a description of which values exist](../lessons/a-type-restricts-what-you-may-say-not-what-values-exist.md)
- [When your notion of correspondence stops working at higher order, weaken the notion rather than shrink the language](../lessons/weaken-the-notion-of-correspondence-until-it-crosses-higher-order.md)
- [Withhold the ability to inspect, and the interface starts telling you what the implementation must do](../lessons/withhold-inspection-so-the-interface-becomes-informative.md)
- [Every expressive power you add is paid for out of a reasoning principle, so find out which one before you spend it](../lessons/every-added-power-is-paid-for-out-of-a-reasoning-principle.md)
- [When a definition resists you, derive it from the theorems it has to support and prove your results parametric in it](../lessons/let-the-theorems-you-must-keep-determine-the-definition.md)
