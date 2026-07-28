---
type: work
title: "Data Abstraction and Hierarchy"
figure: liskov
description: An OOPSLA keynote arguing that data abstraction, not inheritance, is the more fundamental organizing idea in program design, and that hierarchy is only useful insofar as it stays consistent with the abstractions it's built on. Works through when subclassing an abstraction actually preserves its meaning versus when it just reuses code while quietly violating the supertype's contract. This is the talk usually credited as the informal origin of what later became the Liskov Substitution Principle.
subdomains: [programming-languages-and-semantics, programming-environments-and-object-systems]
year: 1987
url: https://www.cs.tufts.edu/~nr/cs257/archive/barbara-liskov/data-abstraction-and-hierarchy.pdf
extraction: complete
survey_pages: 18
survey_text_layer: full
survey_fetch_mb: 1
access: public
host: third-party-rehost
tags: [work]
---

# Data Abstraction and Hierarchy

**Venue/year:** OOPSLA '87 Addendum to the Proceedings (keynote address), October 1987
**Source:** https://www.cs.tufts.edu/~nr/cs257/archive/barbara-liskov/data-abstraction-and-hierarchy.pdf — course-archive mirror on Tufts CS department pages (Nate Robins' cs257 archive), not the author's own site but a legitimate academic host; content extracted and confirmed to match (title, author, abstract text, October 1987 OOPSLA byline).

## Lessons
- [Inheritance is code assembly; it says nothing about what a type means](../lessons/inheritance-is-code-assembly-not-a-statement-of-meaning.md)
- [Any mechanism that creates insiders owes them a second contract](../lessons/a-mechanism-that-creates-insiders-owes-them-a-second-contract.md)
- [Keep the distinctions your implementation collapses](../lessons/keep-design-distinctions-the-implementation-collapses.md)
- [When you noticed the commonality decides how you should express it](../lessons/when-you-noticed-the-commonality-decides-how-to-express-it.md)
