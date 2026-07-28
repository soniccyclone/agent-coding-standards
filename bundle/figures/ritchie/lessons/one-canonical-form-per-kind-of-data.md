---
type: lesson
title: "One canonical form per kind of data is what makes independent programs combinable"
figure: ritchie
works: [unix-time-sharing-system-a-retrospective]
axes: [expressiveness, primitive-count, cognitive-load]
subdomains: [operating-systems-and-systems-programming, software-engineering-and-architecture]
tags: [lesson]
---
# One canonical form per kind of data is what makes independent programs combinable

**Lesson:** Ritchie ranks the properties of the file abstraction and puts one above all the others: not that files are efficient, not that they are randomly addressable, but that there is exactly one way text is stored. His reasoning is about the space of possible collaborations. When a kind of information has k competing encodings, any two programs that ought to work together have a real chance of disagreeing, and the cost of reconciling them is paid again for every pair. When it has one, every program that reads that kind of information can consume every program that writes it, and the useful combinations show up without anyone planning them. He offers a diagnostic for whether a system has achieved this, credited to McIlroy: have a program in some language emit a copy of itself, then try to feed that output to the language's own compiler. Systems that need an expert and a conversion step to close that loop have more encodings than they admit.

The subtlety is that this is not an argument against structured data. Ritchie is explicit that a program or a cooperating family of programs is entitled to any internal representation it finds useful, and points at a relational database running on top of the same unstructured files with several organizations of its own. The rule is scoped to information that crosses boundaries between independently written programs. Inside a boundary, pick whatever fits; across one, variety is pure cost. Note also that he concedes a related point about reading rather than storage — a way to ask for at most one line regardless of source would be welcome — and distinguishes it carefully, because changing how bytes are delivered does not multiply how they are stored.

A programmer who believes this treats format proliferation as a structural defect rather than a matter of convenience, and fights it hardest at interfaces rather than inside modules. When tempted to add a second encoding for the same information, they count the integrations that will now need a translator, and they look for the round-trip test that would expose the split. They also accept that canonicalizing costs somebody something — usually the program with the most specialized needs — and pay it deliberately, because the alternative charge falls on every future combination instead.

**Source:** [UNIX Time-Sharing System: A Retrospective](../works/unix-time-sharing-system-a-retrospective.md) — the discussion of file structure that dismisses the record concept and then singles out single-representation-of-text as the most important consequence, together with the recommendations to system designers at the end.
