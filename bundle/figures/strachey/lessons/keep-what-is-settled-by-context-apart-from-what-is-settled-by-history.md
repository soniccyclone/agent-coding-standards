---
type: lesson
title: "Keep what is settled by context apart from what is settled by history"
figure: strachey
works: [the-varieties-of-programming-language]
axes: [verifiability, cognitive-load, parallelizability]
subdomains: [programming-languages-and-semantics, operating-systems-and-systems-programming]
tags: [lesson]
---
# Keep what is settled by context apart from what is settled by history

**Lesson:** Every system that computes carries two kinds of state, and they obey opposite laws. One kind is determined by where you are: it nests, several versions of it can be live at once, leaving one and returning to an outer one is routine, and nothing that happened earlier in time can change what it says. The other kind is determined by what has happened: there is only ever one of it, changes to it cannot be undone, and its content at any moment is a summary of the entire past. The first behaves the way ordinary mathematics behaves. The second is the reason programming is harder than ordinary mathematics.

Most of the persistent confusion in language design and in systems work comes from failing to keep these two apart, or from representing them with the same mechanism so that the properties of the weaker one contaminate the stronger. Once you see the split, a great many recurring arguments resolve into the same question: is this thing context or is it history? A binding of a name to a procedure is context. A file's contents are history. A variable in most languages is the awkward hybrid — a context-determined handle whose content is history-determined — and the whole L-value/R-value apparatus exists precisely to keep that hybrid from collapsing into mush.

What this changes in practice is that you stop treating "state" as one topic. You push as much as possible into the context-shaped kind, where reasoning is local and cheap and concurrency is unproblematic, and you take the irreducible remainder and make it explicit, singular, and visible as history — passed as a value, threaded through, or held behind a boundary that names it for what it is. The design mistake this guards against is the tempting one: making a nested, scoped, apparently mathematical facility that secretly reads or writes the single irreversible thing, so that two identical-looking uses of it disagree because of something that happened between them.

**Source:** [The Varieties of Programming Language](../works/the-varieties-of-programming-language.md) — the section on stored values, which contrasts the static nesting environment with the singular irreversible machine state and names that contrast as the source of confusion in both languages and operating systems.
