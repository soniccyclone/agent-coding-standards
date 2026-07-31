---
type: work
title: "Back to the Future: The Story of Squeak, A Practical Smalltalk Written in Itself"
figure: ingalls
description: The system paper for Squeak, describing how Ingalls and collaborators built a complete, portable Smalltalk-80 implementation almost entirely in Smalltalk itself, translating only a small kernel to C for each target platform. It covers the object memory, the BitBlt/WarpBlt graphics primitives, and the interpreter, plus measured performance against other Smalltalk implementations of the era. The paper is as much an argument for self-hosting as an engineering trick — proof that a live, introspectable system can also be fast and genuinely portable.
subdomains: [programming-environments-and-object-systems, software-engineering-and-architecture]
year: 1997
url: http://files.squeak.org/docs/OOPSLA.Squeak.html
survey_text_layer: full
access: public
host: institutional
tags: [work]
---

# Back to the Future: The Story of Squeak

**Author(s):** with Ted Kaehler, John Maloney, Scott Wallace, Alan Kay
**Venue/year:** OOPSLA '97: Proceedings of the 12th ACM SIGPLAN Conference on Object-Oriented Programming, Systems, Languages, and Applications, 1997.
**Source:** http://files.squeak.org/docs/OOPSLA.Squeak.html — full HTML text, hosted on files.squeak.org, the Squeak open-source project's own document server. Verified 200 OK on both http and https; confirmed complete (abstract through references, all sections and tables present).
**Reading copy:** full text is served as HTML, not PDF (~7,964 words). Fetch the URL and read the HTML directly; `pdftotext` on it returns nothing, which is what made earlier surveys record this as having no text layer.

## Lessons
- [Never write the low-level system in the low-level language: write it in a subset of your good language shaped like the target, and translate](../lessons/write-the-low-level-system-in-a-target-shaped-subset-and-translate.md)
- [Treat the order of a bootstrap as a design artifact: make every stage observable, and deliberately under-build whatever that stage cannot stress](../lessons/sequence-a-bootstrap-and-underbuild-what-cannot-be-stressed-yet.md)
- [Measure the cost your architecture exists to avoid — the avoidance machinery is often the more expensive half, and deleting it deletes a family of problems](../lessons/measure-the-cost-you-built-an-architecture-to-avoid.md)
- [Design representations so the cheap conversion is the correct one, quantize the parameter you cannot afford exactly, and perform each operation in the space where its algebra actually holds](../lessons/make-representations-nest-and-operate-where-the-algebra-holds.md)
