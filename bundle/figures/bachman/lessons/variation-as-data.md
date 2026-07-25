---
type: lesson
title: "When the nth program is the first program again, express the difference as data"
figure: bachman
works: [oral-history-charles-bachman]
axes: [expressiveness, primitive-count]
subdomains: [databases-and-data-management, software-engineering-and-architecture]
tags: [lesson]
---
# When the nth program is the first program again, express the difference as data

**Lesson:** The formative episode Bachman keeps returning to in his oral history is the late-1950s report-generator work: a team noticed that every report program they wrote was, in generic outline, the same program — read the master file, match records, emit lines — differing only in a handful of specifics. Their response was not a library of shared subroutines but a category shift: capture the invariant machinery once, describe each report's particulars declaratively (what to print, where, and under what record conditions), feed in a separate declarative description of the file's own structure, and let a master program *generate* the disposable per-report program. End users could then specify reports by filling in forms rather than by programming.

The way of thinking: when you catch yourself writing the same program repeatedly, stop asking how to write it faster and ask what, precisely, varies between instances. Whatever varies is not code — it is data awaiting a notation. Splitting a program family into one generic engine plus per-case declarative descriptions shrinks the set of things that must be hand-built and trusted from N programs to one engine and one description language, and it relocates the act of specification to people who understand the requirement rather than the machine.

The same move recurs across Bachman's career at larger scales: files carrying metadata that describes their own record formats, schemas as machine-readable descriptions that other software consumes, translation programs generated from pairs of schema maps rather than written by hand. A programmer who thinks this way habitually looks for the family behind the individual program, and treats "a person is hand-writing the nth instance of this" as a signal that a description language is missing.

**Source:** [Oral History: Charles Bachman](../works/oral-history-charles-bachman.md) — the GE Hanford / SHARE 9PAC report-generator account in the early career section, including the packet decks, the metadata deck, and the generated one-use program.
