---
type: lesson
title: "Introduce a destructive operation as the twin of a pure one, specified by the equation it still satisfies and the equation it breaks"
figure: mccarthy
works: [lisp-1.5-programmers-manual]
axes: [expressiveness, verifiability]
subdomains: [programming-languages-and-semantics, software-engineering-and-architecture]
tags: [lesson]
---
# Introduce a destructive operation as the twin of a pure one, specified by the equation it still satisfies and the equation it breaks

**Lesson:** The manual admits something a purist would rather not: the constructive core cannot change anything. Its only builder makes fresh structure, so every apparent modification is a copy, and a system that must work on large shared structure in a small memory cannot afford that. The mutating operators are introduced for exactly this reason, and the way they are introduced is the lesson. Each is defined by an equation to its pure counterpart — as a *value*, replacing a field is indistinguishable from building a new pair from the new field and the old remainder — and then the text states plainly that the effect is not the same, because no new cell is made and the old one now reads differently to everyone holding a link to it. The specification is deliberately two-part: here is what is preserved, and here is precisely what is not.

This is a better discipline than either of the tempting alternatives. Presenting the mutating operator on its own terms forces every reader to derive its meaning from scratch. Presenting it as merely an optimization of the pure one hides the thing that will actually bite. Naming the shared equation buys transferable intuition; naming the broken one tells you which reasoning you must stop doing. The manual pairs the operators up systematically — a concatenation that copies its first argument alongside one that does not, a value-yielding function alongside a version rewritten to reuse the cells it was handed — so the reader sees the pattern rather than a scattering of exceptions.

The broken equation is not local, which is why it deserves the prominence. Once two structures can share cells and cells can be rewritten, the consequences show up in code that never mentions the mutating operators at all: a definition can be altered from underneath, a structure can be made to point back into itself, and the functions that walk structure looking for equality or performing substitution can be sent into an unterminating walk on input that used to be finite. The mutation's cost is paid by the readers, not the writer, and the specification has to say so or the readers will not know to worry.

A programmer who works this way, when adding an in-place variant to any pure interface, writes down both halves before writing the implementation: the invariant that still holds — usually about the returned value — and the precise class of assumption that other code must now abandon, usually about whether previously-obtained references remain stable. That written delta becomes the review checklist for every caller. The habit generalizes to caches that can be invalidated, to buffers reused across calls, to objects handed out and later mutated, and to any API that starts returning a view where it used to return a copy: the change is defensible only when you can state what it preserves, and honest only when you state what it destroys.

**Source:** [LISP 1.5 Programmer's Manual](../works/lisp-1.5-programmers-manual.md) — the list-structure-operators subsection, which motivates mutation by the copying cost of the pure core, gives the value-equivalence equation for field replacement, and warns about damaged definitions and self-referential structure defeating the searching functions.
