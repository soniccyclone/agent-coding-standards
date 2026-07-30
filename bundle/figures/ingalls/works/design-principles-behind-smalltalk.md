---
type: work
title: "Design Principles Behind Smalltalk"
figure: ingalls
description: Ingalls' own statement of the goals driving Smalltalk's design — personal mastery, uniform metaphor (everything is an object sending and receiving messages), and a system built to be extended and inspected from within itself rather than treated as a closed black box. It lays out design maxims later cited throughout object-oriented programming literature, such as making the reach of a language equal to the reach of the whole system. Written for a general Byte Magazine audience rather than a specialist one, so it reads as an accessible manifesto more than a technical spec.
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
year: 1981
url: https://worrydream.com/refs/Ingalls_1981_-_Design_Principles_Behind_Smalltalk.pdf
survey_pages: 8
survey_text_layer: ocr
survey_fetch_mb: 5
access: public
host: third-party-rehost
extraction: complete
tags: [work]
---

# Design Principles Behind Smalltalk

**Venue/year:** Byte Magazine, Vol. 6, No. 8, August 1981, pp. 286-298.
**Source:** https://worrydream.com/refs/Ingalls_1981_-_Design_Principles_Behind_Smalltalk.pdf — live PDF, rehosted on Bret Victor's worrydream.com reference archive. Verified 200 OK, application/pdf, 8 pages. Also mirrored at gwern.net/doc/cs/1981-ingalls.pdf (verified 200 OK) if the worrydream copy ever goes down.
**Reading copy:** `scratchpad/ocr-text/ingalls__design-principles-behind-smalltalk.txt` — OCR of the scanned original by tesseract at 300dpi. Running prose is reliable; **mathematical and logical notation is not** — turnstiles, implication arrows, subscripts and small-caps headings come through mangled. Ground every lesson in the prose argument and do not transcribe or rely on a formula from this text. Page markers `=== page N ===` correspond to PDF pages.

## Lessons
- [Design a language by building real applications in the version you already have, then redesigning from the scar tissue](../lessons/design-the-language-by-being-its-user-first.md)
- [Set the size of the whole system by what one person can master, and pay for it by deleting special cases](../lessons/one-person-must-be-able-to-hold-the-whole-system.md)
- [Read your own programs for bookkeeping: text that is not about the problem is an indictment of the language](../lessons/programs-should-visibly-be-about-their-problem.md)
- [State what you want, never how it is done, because dependencies grow quadratically and only the request is safe to share](../lessons/ask-for-intent-and-let-the-receiver-choose-the-method.md)
- [Pick one metaphor and make it hold at every scale, so the vocabulary learned at the bottom still works at the top](../lessons/one-metaphor-applied-at-every-scale.md)
- [Give user-defined things exactly the standing of built-in ones, or people will model their domain in primitives](../lessons/give-user-defined-things-the-same-standing-as-built-ins.md)
- [Put each capability at the one place where the most things inherit it, and let protocol rather than type set the reach](../lessons/put-each-capability-where-it-is-amplified.md)
- [Concentrate the whole system's contact with hardware into a few primitives, then spend all your optimization there](../lessons/concentrate-contact-with-technology-into-few-primitives.md)
- [Treat everything that does not fit your framework as a defect in the framework's reach, not as a separate layer to live with](../lessons/anything-outside-the-framework-is-a-defect-in-its-reach.md)
- [Treat human cognition as the fixed constraint and the machine as the adjustable side, then design to the whole span between them](../lessons/treat-the-human-side-as-the-fixed-point.md)
- [Make reference uniform, so a variable can hold anything and no caller has to plan for what it holds](../lessons/make-reference-uniform-so-generality-costs-nothing-per-use.md)
