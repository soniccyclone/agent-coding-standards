---
type: lesson
title: "Judge a tool by which of the hard parts it removes, not by the list of things it can express"
figure: hoare
works: [hints-on-programming-language-design]
axes: [cognitive-load, expressiveness]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Judge a tool by which of the hard parts it removes, not by the list of things it can express

**Lesson:** Before evaluating a language, a library, or a framework, name the activities that actually consume the practitioner's effort, then ask which of them the tool touches. The genuinely hard parts of programming are deciding what the program should do and stating that precisely, deciding how to decompose it and fixing the interfaces between the pieces, explaining the result to whoever inherits it, and hunting the errors that survive all of that. A tool that adds expressive range without shortening any of those four is not helping with the job; it is helping with a job nobody was struggling at. This reframing is the whole content of the position, and it cuts against the criteria that usually decide tool adoption in practice — familiarity of notation, size of library, existing popularity, institutional sponsorship — none of which are claims about difficulty removed.

Two consequences follow that are easy to state and rarely honored. First, readability outranks writeability, and by a large margin, because a program's text is read by its author again, by reviewers, and by whoever adapts it years later, whereas it is written once. Abbreviation schemes, implicit defaults, and elided declarations trade a permanent cost for a momentary saving. The tempting rebuttal is that a tool can expand the abbreviations and print the explicit form on demand, but machine-expanded output is essentially never more readable than well-written input; the only reliable win in that direction is mechanical layout. Second, documentation cannot be a phase that follows commissioning. Treated as an add-on, it records what the code turned out to be rather than what it was supposed to be, which is the information that was actually scarce; treated as part of design and coding, the same act that explains the intent also constrains the construction. So the language's job includes letting the programmer express what a program is *for*, at every level from strategy down to representation, not merely what it does.

The design test this yields is unglamorous and useful: for each proposed feature, identify which of the four difficulties it reduces and what it costs the other three. Features that reduce none of them are decoration, however clever, and features that reduce one by aggravating another need the trade stated out loud rather than assumed away.

**Source:** [Hints on Programming Language Design](../works/hints-on-programming-language-design.md) — the Principles section, which isolates program design, documentation, and debugging as the difficulties a language should attack, and its arguments about readability over writeability and documentation as integral rather than appended.
